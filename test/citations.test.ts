import { existsSync, readFileSync, readdirSync } from "node:fs";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { expect, it } from "vitest";
import { body } from "./pi.js";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));

/** The nine research files and the prefix of the positions each numbers. */
const FILES = {
  "areas/fc-lost-damaged.md": "FC",
  "areas/inbound-shortfalls.md": "IN",
  "areas/customer-returns.md": "RT",
  "areas/removals-disposals.md": "RM",
  "areas/fee-overcharges.md": "FE",
  "areas/value-and-reversals.md": "VR",
  "method/sp-api-claims-surface.md": "SU",
  "method/filing-and-conduct.md": "FL",
  "beyond/recovery-economics.md": "EC",
} as const;
const PREFIX = "(?:FC|IN|RT|RM|FE|VR|SU|FL|EC)";
const ID = new RegExp(`${PREFIX}\\d+`, "g");
const GROUP = new RegExp(`\\((${PREFIX}\\d+(?:\\s*[,;]\\s*${PREFIX}\\d+)*)\\)`, "g");

type Position = { id: string; withdrawn: boolean; text: string };

/** A file's numbered positions, as its Positions section opens each: `FC1.`, `**IN1.**` or `- **RM1.**` at the head of a line; the first entry of an id is the position. */
const numbered = (file: string, prefix: string): Position[] => {
  const lines = readFileSync(join(ROOT, "research", file), "utf8").split("\n");
  const start = lines.findIndex((line) => /^#{2,3} (?:\d+\. )?Positions\b/.test(line));
  const end = lines.findIndex((line, n) => n > start && /^## /.test(line));
  const head = new RegExp(`^(?:- )?(?:\\*\\*)?(${prefix}\\d+)\\.(?:\\*\\*)?\\s*(.*)$`);
  const seen = new Map<string, Position>();
  for (const line of lines.slice(start + 1, end === -1 ? undefined : end)) {
    const match = line.match(head);
    if (match && !seen.has(match[1]!)) seen.set(match[1]!, { id: match[1]!, withdrawn: /^\*?\(withdrawn/.test(match[2]!), text: match[2]! });
  }
  return [...seen.values()];
};

const all = Object.entries(FILES).flatMap(([file, prefix]) => numbered(file, prefix));

/**
 * README § 11 holds what was read only through the help hub's content call, which the office closed on 2026-11-10, one row a position:
 * `(whole` is held entire and withdrawn in its file; `(part`, `(parts` or `(second statement` has a held part, and no line cites it at all;
 * `(clause` has one held clause, marked `[held` where it stands, and its other clauses may be cited.
 */
const heldRows = (() => {
  const readme = readFileSync(join(ROOT, "research", "README.md"), "utf8");
  const section = readme.slice(readme.indexOf("## 11."));
  return [...section.matchAll(new RegExp(`^\\| (${PREFIX}\\d+) \\((whole|parts?|second statement|clause)`, "gm"))].map((row) => ({ id: row[1]!, kind: row[2]! }));
})();
const HELD = heldRows.filter((row) => row.kind === "whole").map((row) => row.id);
const PARTLY_HELD = heldRows.filter((row) => /^part|^second/.test(row.kind)).map((row) => row.id);
const CLAUSE_HELD = heldRows.filter((row) => row.kind === "clause").map((row) => row.id);

const standing = new Set(all.filter((position) => !position.withdrawn && !(PARTLY_HELD as readonly string[]).includes(position.id)).map((position) => position.id));
const excluded = new Set(all.filter((position) => !standing.has(position.id)).map((position) => position.id));

/** The seat's own lines (README § 10): no source, so no skill rests on them; each with words that would restate its claim. */
const SEAT_CLAIMS = [
  /files nothing|only observes/i,
  /ordinary (?:fulfil\w* )?(?:centre|center|FC) loss/i,
  /not yet a claim|no claim route left/i,
  /`?approval-date`?[^.]*\b(?:places?|decides?) (?:a|the) line/i,
  /defines? an? under-valued|an under-valued line is/i,
  /\btwo skills\b|too (?:small|automated) to earn/i,
  /premature[^.]*before[^.]*window opens/i,
  /normal status[^.]*`?NORMAL`?|`NORMAL`[^.]*normal status/i,
  /`?caseId`?[^.]*`?case-id`?|`?case-id`?[^.]*`?caseId`?/,
  /older than the Reports API's keep/i,
  /(?:may be|are) (?:one|the same) flow/i,
] as const;

const markdown = (directory: string): string[] =>
  readdirSync(directory, { recursive: true, encoding: "utf8" }).filter((file) => file.endsWith(".md")).map((file) => join(directory, file));

/** A line that only points: to a reference, another skill of this package, the door's skill, one of the two other playbooks, or the research. */
const pointer = (line: string) =>
  /references\/[\w-]+\.md|\.\.\/[\w-]+\/SKILL\.md|research\/|amazon-sp-api skill|@comchatx\/cx-amazon-(?:stock|finance)-playbook/.test(line);

/** The package files a line points to: `references/<x>.md` in its own skill (the door's own references excepted) and `../<skill>/SKILL.md`. */
const targets = (file: string, line: string): string[] => {
  const skill = file.split("/").slice(0, 2).join("/");
  const own = /amazon-sp-api skill/.test(line) ? [] : [...line.matchAll(/(?<![\w/.-])references\/([\w-]+\.md)/g)].map((match) => `${skill}/references/${match[1]}`);
  const other = [...line.matchAll(/\.\.\/([\w-]+)\/SKILL\.md/g)].map((match) => `skills/${match[1]}/SKILL.md`);
  return [...own, ...other];
};

const lines = markdown(join(ROOT, "skills")).flatMap((file) =>
  body(readFileSync(file, "utf8"))
    .split("\n")
    .map((line) => line.trim())
    .filter((line) => line !== "" && !line.startsWith("#") && !/^\|?[-:| ]+\|?$/.test(line))
    .map((line) => ({ file: file.slice(ROOT.length + 1), line, ids: [...line.matchAll(GROUP)].flatMap((group) => group[1]!.match(ID) ?? []) })),
);

it("the research numbers 423 positions, 30 withdrawn, and README § 11's held rows agree with the files", () => {
  expect(all).toHaveLength(423);
  expect(all.filter((position) => position.withdrawn)).toHaveLength(30);
  expect(HELD).toEqual(["RT10", "RT12", "RT14", "RT15", "RT22", "RT23", "RT25", "RT26", "RT27", "RT28", "RT42", "RT45", "FC56"]);
  expect(PARTLY_HELD).toEqual(["RT3", "RT6", "RT8", "RT16", "RT19", "RT21", "RT36", "RT37", "FL4"]);
  expect(CLAUSE_HELD).toEqual(["FC54"]);
  const position = (id: string) => all.find((candidate) => candidate.id === id);
  for (const id of HELD) expect(position(id)?.withdrawn, id).toBe(true);
  for (const id of [...PARTLY_HELD, ...CLAUSE_HELD]) expect(position(id)?.withdrawn, id).toBe(false);
  for (const id of CLAUSE_HELD) expect(position(id)?.text, id).toContain("[held");
  expect(standing.size).toBe(423 - 30 - PARTLY_HELD.length);
});

it("every line of the skills and their references cites a standing position, except a line that only points", () => {
  expect(lines.length).toBeGreaterThan(0);
  for (const { file, line, ids } of lines) {
    if (ids.length === 0) expect(pointer(line), `${file}: ${line}`).toBe(true);
    for (const id of ids) {
      expect(excluded.has(id), `${file}: ${id} is withdrawn or held`).toBe(false);
      expect(standing.has(id), `${file}: ${id} does not exist`).toBe(true);
    }
  }
});

it("every file a line points to is in the package", () => {
  const pointed = lines.flatMap(({ file, line }) => targets(file, line).map((target) => ({ file, target })));
  expect(pointed.length).toBeGreaterThan(0);
  for (const { file, target } of pointed) expect(existsSync(join(ROOT, target)), `${file}: ${target}`).toBe(true);
  expect(targets("skills/warehouse-claims/SKILL.md", "[scope.md](references/does-not-exist.md): exclusions.")).toEqual(["skills/warehouse-claims/references/does-not-exist.md"]);
  expect(existsSync(join(ROOT, "skills/warehouse-claims/references/does-not-exist.md"))).toBe(false);
  expect(targets("skills/claim-filing/SKILL.md", "How a call is made: the amazon-sp-api skill's references/door.md.")).toEqual([]);
});

it("each standing position is cited somewhere in the skills", () => {
  const cited = new Set(lines.flatMap(({ ids }) => ids));
  expect([...standing].filter((id) => !cited.has(id))).toEqual([]);
});

it("no line of the skills restates a claim of the seat's own", () => {
  for (const { file, line } of lines) for (const claim of SEAT_CLAIMS) expect(claim.test(line), `${file}: ${line}`).toBe(false);
});

it("the citation check fails a line citing a withdrawn, a held or a missing position, and one citing nothing", () => {
  const check = (line: string) => {
    const ids = [...line.matchAll(GROUP)].flatMap((group) => group[1]!.match(ID) ?? []);
    return ids.length === 0 ? pointer(line) : ids.every((id) => standing.has(id));
  };
  expect(check("Removal claims are filed by hand (RM2).")).toBe(true);
  expect(check("Removal claims are filed by hand (RM2, FC3).")).toBe(true);
  expect(check("The cap is homed elsewhere (FC33).")).toBe(false);
  expect(check("Late-accepted returns are reimbursed (RT26).")).toBe(false);
  expect(check("Other stores' not-returned days differ (RT8).")).toBe(false);
  expect(check("An opt-out of the ownership evaluation keeps the units (FC56).")).toBe(false);
  expect(check("Expired stock damaged at a centre is eligible for a manual claim (FC54).")).toBe(true);
  expect(check("Removal claims are filed by hand (RM999).")).toBe(false);
  expect(check("Removal claims are filed by hand.")).toBe(false);
  expect(check("[windows.md](references/windows.md): the windows by store.")).toBe(true);
});

it("the seat's-own check catches a restated claim", () => {
  for (const line of ["A shortage on an open shipment is not yet a claim (IN13).", "Two skills cover the pack (EC19).", "Match the Support API's `caseId` to the report's `case-id` (SU9)."])
    expect(SEAT_CLAIMS.some((claim) => claim.test(line)), line).toBe(true);
});
