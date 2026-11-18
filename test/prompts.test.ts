import { readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { expect, it } from "vitest";
import { PROMPT_WORDS } from "./words.js";
import { typed } from "./pi.js";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const manifest = () => JSON.parse(readFileSync(join(ROOT, "package.json"), "utf8")) as { comchatx: { prompts: Record<string, { zh: string }> } };

it("each template expands in a pi session: its arguments and the seller's own words reach the model, no placeholder does", async () => {
  const expected: Record<string, [string, string]> = {
    "claims-audit": ["/claims-audit 只看英国站", `${PROMPT_WORDS["claims-audit"].body} 只看英国站`],
    "shipment-claims": ["/shipment-claims FBA19ABCDEF", `${PROMPT_WORDS["shipment-claims"].body} FBA19ABCDEF`],
    "return-claims": ["/return-claims", `${PROMPT_WORDS["return-claims"].body}`],
    "fee-claims": ["/fee-claims SKU-1,SKU-2", `${PROMPT_WORDS["fee-claims"].body} SKU-1,SKU-2`],
    "claim-value": ["/claim-value 2026-01-01..2026-10-31", `${PROMPT_WORDS["claim-value"].body} 2026-01-01..2026-10-31`],
  };
  expect(Object.keys(expected).sort()).toEqual(Object.keys(manifest().comchatx.prompts).sort());
  for (const [name, [input, text]] of Object.entries(expected)) {
    const received = await typed(ROOT, input);
    expect(received.trim(), name).toBe(text);
    expect(received, name).not.toMatch(/\$\{?[@0-9A]/);
  }
}, 120_000);
