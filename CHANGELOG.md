# Changelog

## 0.1.6

- The tile's mark on the Plugins page is the signed drawing.

## 0.1.5

- Each of the five templates' body is its Try it sentence in English, its own `description` word for word, followed by the seller's words (`$@`): typing `/claims-audit` asks cx the sentence the row shows, not a longer body.
- The skills state four facts from Amazon's *FBA Reports* page, each beside its place and the day it was read (2026-11-23): how often Amazon generates a near-real-time and a daily FBA report, and that a report already made within that period holds the newest content, with which reports the page marks daily or near real-time (new position SU61); the FBA returns and reimbursements reports' columns as Amazon documents them; and the fee preview's refresh, start offset and request limit.
- The Try it sentences themselves are unchanged.

## 0.1.4

- The five templates' Try it sentences say both halves of what each asks, in Chinese (`comchatx.prompts`) and English (each template's `description`).
- The `/claims-audit` template also asks where to claim what Amazon has not paid.

## 0.1.3

- The README no longer names another plugin; what the playbook builds on is its `comchatx.builds`, each with its reason, as signed on 2026-11-18. The sentence "To read stock states and money lines in depth, also install [Amazon Stock Playbook](…) and [Amazon Finance Playbook](…)." and its Chinese are gone; the two optional entries carry the reasons 「用于看清库存压着要花多少钱、什么时候该补货。」 / "Shows stock costs and when to restock." (`@comchatx/cx-amazon-stock-playbook`) and 「用于算出每个商品扣掉费用后赚了多少。」 / "Works out what each product earns after fees." (`@comchatx/cx-amazon-finance-playbook`).
- "What it uses" names the account, not the plugin: 「**你的亚马逊卖家账户**：cx 在这里读取库存流水、赔偿、退货、移除、货件和费用。」 / "**Your Amazon seller account:** cx reads your inventory ledger, reimbursements, returns, removals, shipments and fees there." Its Amazon Seller Profile line is gone.
- `cx-amazon-seller` is optional where it was required, with the reason 「用于让 cx 从第一条消息起就知道你在亚马逊开店。」 / "Tells cx from the start that you sell on Amazon."
- The five templates stay as they were.

## 0.1.2

- Four templates are named for the skill each asks: `/shipment-claims`, `/return-claims`, `/fee-claims` and `/claim-value`; `/claims-audit` asks all six.
- The `claim-filing` and `claim-value` skills' English lines carry no Chinese or Japanese characters, so the Plugins page lists all six skills.

## 0.1.1

- Nothing in the package changed: this is its first version published from GitHub, under npm's trusted publisher, with provenance.

## 0.1.0

- The first version: six skills on what Amazon owes an FBA seller, over `cx-amazon-sp-api`:
  - `warehouse-claims`
  - `shipment-claims`
  - `return-claims`
  - `fee-claims`
  - `claim-value`
  - `claim-filing`
- Five templates: `/claims-audit`, `/inbound-shortfall`, `/returns-check`, `/fee-check` and `/reimbursement-value`.
- Every line of the skills cites one of the standing positions in `research/`.
