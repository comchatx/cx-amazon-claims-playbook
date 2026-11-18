import { readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { expect, it } from "vitest";
import { body } from "./pi.js";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));

const markdown = (directory: string): string[] =>
  readdirSync(directory, { recursive: true, encoding: "utf8" }).filter((file) => file.endsWith(".md")).map((file) => join(directory, file));

/** Every skill file whole, its frontmatter and headings included. */
const files = markdown(join(ROOT, "skills")).map((file) => ({ file, text: readFileSync(file, "utf8") }));

/** A money amount: a currency sign or code beside a number. */
const MONEY = /[$€£¥₹]\s?\d|\b\d[\d,.]*\s?(?:USD|EUR|GBP|JPY|CAD|AUD|MXN|BRL|INR|AED|SAR|SEK|PLN|SGD|cents?)\b|\b(?:USD|EUR|GBP|JPY|CAD|AUD|INR)\s?\d/;
/** A share: a percentage. */
const SHARE = /\d\s?%|\bper ?cent\b/i;
/** A rate by volume or by unit. */
const RATE = /\d[\d.,]*\s*(?:per|\/)\s*(?:cubic|cu\.?\s?ft|ft3|m3|unit)\b/i;
/** A band: a range of days or months, or an open band past a number of days. */
const BAND = /\b\d{1,3}\s?(?:–|-|to)\s?\d{1,3}\s?(?:days?|months?)\b|\b\d{1,3}\+\s?(?:days?|months?)\b|\b(?:over|more than|past|beyond|under|less than|fewer than)\s\d{1,3}\s(?:days?|months?)\b/i;
/** A capacity limit's size: a volume or a unit count beside a limit. */
const LIMIT = /\b(?:limit|capacity|cap)\b[^.]*\b\d[\d,.]*\s?(?:cubic|cu\.?\s?ft|units)\b|\b\d[\d,.]*\s?(?:cubic feet|cubic metres|cubic meters)\b/i;
/** A claim window: a number of days or months beside a claim, reimbursement, dispute, investigation, filing or window. */
const WINDOW = /\b(?:claims?|reimburs\w*|disput\w*|investigat\w*|appeal\w*|filed|window|re-?evaluat\w*)\b[^.]*\b\d{1,3}\s(?:calendar |business )?(?:days?|months?)\b|\b\d{1,3}\s(?:calendar |business )?(?:days?|months?)\b[^.]*\b(?:claims?|reimburs\w*|disput\w*|investigat\w*|appeal\w*|filed|window|re-?evaluat\w*)\b/i;
/** A date of the year: a month with its day, a month by name, or an ISO date beside a cut-off, peak or event. */
const MONTH = /\b(?:January|February|March|April|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept?|Oct|Nov|Dec)\b|\bMay\s\d/;
const EVENT_DATE = /\b(?:cut-?off|deadline|peak|Prime Day|Prime Big Deal Days|Black Friday|Cyber Monday|holiday|arrive by)\b[^.]*\b20\d{2}-\d{2}-\d{2}\b|\b20\d{2}-\d{2}-\d{2}\b[^.]*\b(?:cut-?off|deadline|Prime Day|Prime Big Deal Days|Black Friday|Cyber Monday|arrive by)\b/i;

const CHECKS = { MONEY, SHARE, RATE, BAND, LIMIT, WINDOW, MONTH, EVENT_DATE } as const;
const carried = (line: string): string[] => Object.entries(CHECKS).filter(([, check]) => check.test(line)).map(([name]) => name);

it("no line of any skill file, frontmatter and headings included, carries a fee amount, a rate, a share, a band, a capacity limit, a claim window or a date of the year", () => {
  expect(files.length).toBeGreaterThan(0);
  const found = files.flatMap(({ file, text }) => text.split("\n").flatMap((line) => carried(line).map((name) => `${file.slice(ROOT.length + 1)}: ${name}: ${line}`)));
  expect(found).toEqual([]);
});

it("the value check catches each kind of carried value and passes the rule stated with where it is read", () => {
  const caught: Record<keyof typeof CHECKS, string> = {
    MONEY: "The monthly storage fee is $0.87 per cubic foot for standard size",
    SHARE: "AWD waives the fees when 70% of supply is replenished",
    RATE: "Storage costs 2.40 per cubic foot from October",
    BAND: "Customer-return claims open 60-120 days after the refund",
    LIMIT: "The capacity limit was 30,000 cubic feet",
    WINDOW: "A lost-inventory claim is filed within 60 days",
    MONTH: "Peak storage runs October to December",
    EVENT_DATE: "The Prime Day cut-off was 2026-05-27",
  };
  for (const [name, line] of Object.entries(caught)) expect(carried(line), line).toContain(name);
  for (const line of [
    "The applied rate is the storage fee report's `storage_rate` column (C1).",
    "Amazon announced the 2027 US change on 2026-11-05; from 2027-02-01 storage is priced by age (C21).",
    "A claim's window is on the help page, which this research could not read (I12).",
    "Units may be bought now when fulfillable (W1).",
  ]) expect(carried(line), line).toEqual([]);
});


it("each SKILL.md body is at most 371 words", () => {
  for (const name of readdirSync(join(ROOT, "skills"))) {
    const words = body(readFileSync(join(ROOT, "skills", name, "SKILL.md"), "utf8")).split(/\s+/).filter(Boolean).length;
    expect(words, name).toBeLessThanOrEqual(371);
  }
});

it("the value check catches a claim window, a cap and a dispute window stated as a value", () => {
  for (const line of ["Lost and damaged claims must be filed within 60 days of the loss report", "The per-unit cap is $5,000", "A valuation can be disputed for 90 days after the reimbursement", "Removals lost in transit: 15-75 days from creation"])
    expect(carried(line), line).not.toEqual([]);
  for (const line of ["The window is the store's own, read from its latest News post on claim windows (FC9).", "Amazon reimburses at sourcing cost from 2025-03-31 in the US (VR2)."])
    expect(carried(line), line).toEqual([]);
});
