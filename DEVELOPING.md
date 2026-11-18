# Developing cx-amazon-claims-playbook

The README is written for a seller, in English (`README.md`) and Chinese (`README.zh-CN.md`), and the Plugins page draws it. This file is for whoever works on the package. The README's words, the card's name and line and the templates' and skills' lines are the copy seat's, and wait on Jack's signature; `test/words.ts` holds them.

This is a [pi](https://pi.dev) package that tells cx what Amazon owes an FBA seller and when each claim closes, read through SP-API. It is written for the assistant in a [ComChatX](https://comchatx.com) seller's box. It reads the seller's account through the box's `cx` command and the [`cx-amazon-sp-api`](https://github.com/comchatx/cx-amazon-sp-api) package. `cx-amazon-seller` tells cx the seller sells on Amazon.

It is text only: no script, no extension and no dependency. Its changes are in [CHANGELOG.md](CHANGELOG.md).

Every line of the skills ends with the position it rests on, such as `(FC9)` or `(IN7, RM2)`. The positions live in the nine files under [`research/`](research/README.md), and `research/README.md` is their index. A line without a position only points to another file. The research stays in the repository and does not ship. `research/zh/` holds a Chinese reading of every position, numbered as the originals.

## What it holds

| | What the model reads | Positions |
|---|---|---|
| `skills/warehouse-claims` | Units lost or damaged in Amazon's hands after receipt. Covers what Amazon pays without a claim in each store (each forum post's store, and the UK contradiction), the window and where it is read, the IDR portal, the ledger's codes and pitfalls, transfers, AWD, cross-border moves, MCF, Vine and exclusions. | FC |
| `skills/shipment-claims` | Shipments in and out. Inbound shortfalls and receiving discrepancies, partnered and own carrier, prep and labels, the end of commingling, AWD and AGL, and the first mile. Removals and disposals: lost, short or damaged removals, grading, liquidation, dangerous-goods disposals and stranded removals. | IN, RM |
| `skills/return-claims` | Customer orders: refunded and not returned, wrong item, Amazon-fault dispositions, replacements, outbound loss before delivery, wrong-FNSKU returns and cross-border returns. | RT |
| `skills/fee-claims` | A fee charged on a basis Amazon's own rule did not support, in fifteen kinds. Covers the two fee windows as rules, remeasurement and the EU certification regime. | FE |
| `skills/claim-value` | What a reimbursement is worth and when it is taken back: sourcing cost, Manage Your Sourcing Cost, the dispute, the cap by store, under-valued lines, reversals, Japan, currency and Chinese cost proofs. | VR |
| `skills/claim-filing` | Where each kind is filed and with what evidence, limits, conduct and the automated-agent duties. Also every claims read with its role (`references/reads.md`), the steps no operation can do (`references/no-door.md`), where each window is stated, and the recovery market with the seller's choices. | FL, SU, EC |
| `prompts/*.md` | `/claims-audit`, `/inbound-shortfall`, `/returns-check`, `/fee-check` and `/reimbursement-value`. Each hands the seller's words to cx. | |

How a call is made, and how a report is asked for and landed, is the `amazon-sp-api` skill's (`references/door.md`), never this package's.

A value that differs by store or by year appears in no skill line. That covers a claim window, a cap, a fee, a band and a date of the year. The line states the rule, the store and the day it was read, and where cx reads the seller's own value today.

Some lines never enter a skill:
- the seat's own lines (research README § 10);
- the withdrawn positions;
- the positions that came, wholly or in part, through the help hub's content call, which the office closed on 2026-11-10 (research README § 11).

Every step of a claim that no SP-API operation can do is stated as the seller's step in Seller Central: opening a case, attaching evidence, answering or reopening one, entering a sourcing cost, asking for a remeasure and disputing a value. Nothing is built on the Support API, which needs a restricted role outside the application's five.

Two other packages own facts beside these:
- `@comchatx/cx-amazon-stock-playbook` owns the ledger's grammar and a shipment's state;
- `@comchatx/cx-amazon-finance-playbook` owns fee rates, money lines and how a reimbursement posts.

Their skills are named where a line needs them, and nothing of theirs is written here.

## What it needs

pi, and in the box the `cx` command with the Amazon SP-API source. It reaches no network itself.

## Install

```bash
pi install npm:@comchatx/cx-amazon-claims-playbook
```

On ComChatX, a seller installs it from the Plugins page.

## Develop

```bash
npm ci
npm run typecheck
npm test               # pi at the pin loads the package and its tarball and expands every template;
                       # every line of the skills cites a standing position, none withdrawn or held,
                       # each standing position is cited, and none restates the seat's own; each SKILL.md
                       # body is at most 371 words; no line of a skill file carries a fee amount, rate,
                       # share, band, capacity limit, claim window or date of the year; no tracked file
                       # names a path on a machine
```

The skills were measured with Anthropic's `skill-creator`. The cases, the fixture and the stand-in `cx` are in [`evals/`](evals/README.md), and nothing there ships.

## Release

A tag `v<version>` on `main` runs `.github/workflows/release.yml`, which publishes through npm trusted publishing. The tag's version must match the one in `package.json`. "Shipping it" in WRITING-A-PACKAGE.md gives the steps before the first release.
