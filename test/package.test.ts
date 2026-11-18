import { execFileSync } from "node:child_process";
import { mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { DefaultResourceLoader, SettingsManager } from "@earendil-works/pi-coding-agent";
import { afterEach, expect, it } from "vitest";
import { LINE, NAME, NAME_ZH, OVERVIEW, PROMPT_WORDS, SKILL_WORDS } from "./words.js";

const ROOT = resolve(fileURLToPath(new URL("..", import.meta.url)));
const manifest = JSON.parse(readFileSync(join(ROOT, "package.json"), "utf8")) as { pi: unknown; files: unknown; comchatx: { skills: Record<string, unknown>; prompts: Record<string, unknown> } };
const scratches: string[] = [];
afterEach(() => { for (const scratch of scratches.splice(0)) rmSync(scratch, { recursive: true, force: true }); });

const walk = (directory: string): string[] => readdirSync(directory, { withFileTypes: true }).flatMap((entry) => (entry.isDirectory() ? walk(join(directory, entry.name)) : [join(directory, entry.name)]));

it("the pinned pi lists the package's skills as its manifest names them, with nothing it could not read", async () => {
  const home = mkdtempSync(join(tmpdir(), "pi-package-"));
  scratches.push(home);
  const agentDir = join(home, "agent");
  const cwd = join(home, "project");
  for (const directory of [agentDir, cwd]) mkdirSync(directory);
  writeFileSync(join(agentDir, "settings.json"), JSON.stringify({ defaultProjectTrust: "always", packages: [ROOT] }));
  const loader = new DefaultResourceLoader({ cwd, agentDir, settingsManager: SettingsManager.create(cwd, agentDir) });
  await loader.reload();
  const { skills, diagnostics } = loader.getSkills();
  expect(diagnostics).toEqual([]);
  expect(manifest.pi).toEqual({ skills: ["./skills"], prompts: ["./prompts"] });
  const prompts = loader.getPrompts();
  expect(prompts.diagnostics).toEqual([]);
  expect(prompts.prompts.map((prompt) => prompt.name).sort()).toEqual(Object.keys(manifest.comchatx.prompts).sort());
  expect(skills.map((skill) => skill.name).sort()).toEqual(Object.keys(manifest.comchatx.skills).sort());
  for (const skill of skills) expect(skill.description.trim(), skill.name).not.toBe("");
  // The Plugins page lists a skill by what pi lists, its description as the English line, and drops a skill whose English line holds a Chinese character.
  for (const skill of skills) expect(skill.description, skill.name).not.toMatch(/[一-鿿]/);
  // A seller types one set of names: each template that asks one skill is named for it, and /claims-audit asks them all.
  expect(prompts.prompts.map((prompt) => prompt.name).filter((name) => name !== "claims-audit" && !skills.some((skill) => skill.name === name))).toEqual([]);
});

it("ships its skills, its templates, its README in English and in Chinese and its license, and nothing else", () => {
  // npm 12 keys its answer by the package's name; earlier ones answer a list.
  const answer = JSON.parse(execFileSync("npm", ["pack", "--dry-run", "--json", "--ignore-scripts"], { cwd: ROOT, encoding: "utf8" })) as { files: { path: string }[] }[] | Record<string, { files: { path: string }[] }>;
  const packed = Array.isArray(answer) ? answer : Object.values(answer);
  const shipped = ["skills", "prompts"].flatMap((directory) => walk(join(ROOT, directory)).map((path) => relative(ROOT, path)));
  expect(packed[0]!.files.map((file) => file.path).sort()).toEqual(["LICENSE", "README.md", "README.zh-CN.md", "package.json", ...shipped].sort());
  expect(manifest.files).toEqual(["skills", "prompts", "README.zh-CN.md"]);
});

type Field = { name: string; nameZh: string; about: string; skills: Record<string, unknown>; prompts: Record<string, unknown>; builds: unknown };
const field = () => (manifest as unknown as { description: string; comchatx: Field });

it("the card's name and line are the copy seat's: comchatx.name in English and comchatx.nameZh in Chinese, npm's description in English, comchatx.about in Chinese", () => {
  const pkg = field();
  expect(pkg.comchatx.name).toBe(NAME);
  expect(pkg.comchatx.nameZh).toBe(NAME_ZH);
  expect(pkg.description).toBe(LINE.en);
  expect(pkg.comchatx.about).toBe(LINE.zh);
});

it("each template's English description, Chinese words and seller's message are the drafted ones", () => {
  const { comchatx } = field();
  expect(Object.keys(comchatx.prompts).sort()).toEqual(Object.keys(PROMPT_WORDS).sort());
  for (const [name, words] of Object.entries(PROMPT_WORDS)) {
    expect(comchatx.prompts[name], name).toEqual({ zh: words.zh });
    const text = readFileSync(join(ROOT, "prompts", `${name}.md`), "utf8");
    expect(JSON.parse(text.match(/^description: (".*")$/m)![1]!), name).toBe(words.en);
    expect(text.split("\n---\n")[1], name).toBe(`${words.body} $@\n`);
  }
});

it("the Plugins page's field gives every skill its drafted words in both languages, and builds on the door and the seller profile, naming the two playbooks it points to as optional", () => {
  const { comchatx } = field();
  expect(Object.keys(comchatx.skills).sort()).toEqual(Object.keys(SKILL_WORDS).sort());
  for (const [name, words] of Object.entries(SKILL_WORDS)) expect(comchatx.skills[name], name).toEqual(words);
  expect(comchatx.builds).toEqual([{ on: "cx-amazon-sp-api", need: "required" }, { on: "cx-amazon-seller", need: "required" }, { on: "@comchatx/cx-amazon-stock-playbook", need: "optional" }, { on: "@comchatx/cx-amazon-finance-playbook", need: "optional" }]);
});

it("each README is the drafted Overview, whole", () => {
  for (const [file, text] of Object.entries(OVERVIEW)) expect(readFileSync(join(ROOT, file), "utf8"), file).toBe(text);
});
