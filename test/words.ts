/** The copy seat's words, with Jack for his signature: the card's name in each language and its line, each template's and each skill's words, the Overview. */
export const NAME = "Amazon Claims Playbook";
export const NAME_ZH = "亚马逊索赔分析手册";
export const LINE = { en: "Checks what Amazon may owe you, and says where to claim.", zh: "核对亚马逊可能该赔的货和钱，说明每类去哪索赔。" } as const;
export const SKILL_WORDS = {
  "warehouse-claims": { zh: "查出亚马逊仓库里丢失或损坏、还没赔的货。", en: "Units lost or damaged in Amazon's warehouses, not yet paid." },
  "shipment-claims": { zh: "核对入库少收，以及移除没送到的货。", en: "Shipments received short, and removals that never came back." },
  "return-claims": { zh: "找出退款了却没退回、或退回不对的订单。", en: "Refunds whose item never came back, or came back wrong." },
  "fee-claims": { zh: "查出按错尺寸、重量或类目多收的费用。", en: "Fees charged on the wrong size, weight or category." },
  "claim-value": { zh: "看清赔偿按什么价算，哪些又被撤回。", en: "What a reimbursement was worth, and when it was taken back." },
  "claim-filing": { zh: "说明索赔在哪提交、要什么证据、期限在哪查。", en: "Where each claim is filed, its evidence, and where its window is stated." },
} as const;
export const PROMPT_WORDS = {
  "claims-audit": { zh: "查一遍亚马逊可能该赔我的货和钱：哪些已经赔了，没赔的去哪里索赔。", en: "Find what Amazon may owe me, what it has already paid, and where to claim the rest.", body: "Find what Amazon may owe me: units lost, damaged or received short, removals that never came back, refunds whose item was never returned, and fees charged wrongly. For each, say what it rests on in my own reports, whether Amazon already paid it, where to claim it if not, and where the window for my store is stated." },
  "shipment-claims": { zh: "查我最近几批入库有没有少收：差多少，现在能不能索赔，要交什么证据。", en: "Check my recent shipments for units received short: how many, whether each can be claimed yet, and what Amazon asks to see.", body: "Check my recent shipments to Amazon for units received short: how many on which shipments, whether each can be claimed yet, and what Amazon asks to see." },
  "return-claims": { zh: "找出已经退款、货却没退回或退回不对的订单，看亚马逊赔了没有。", en: "Find refunds whose item never came back or came back wrong, and whether Amazon has paid for each.", body: "Find refunds where the item never came back to Amazon, or came back as something else or damaged by Amazon, and whether Amazon has already paid for each." },
  "fee-claims": { zh: "查亚马逊有没有按错尺寸、重量或类目收费，哪些费用还能申诉。", en: "Check whether Amazon charged my fees on the wrong size, weight or category, and which can still be disputed.", body: "Check whether Amazon charged my fees on the wrong size, weight or category: which products, since when, and which charges can still be disputed for my store." },
  "claim-value": { zh: "看亚马逊给我的赔偿各按什么价算，哪些比我的成本低，哪些后来又撤回了。", en: "See what Amazon's reimbursements to me were valued at, which fall below my cost, and which were taken back.", body: "Look at what Amazon has reimbursed me: what each payment was valued at, which look low against my own cost, and which were later taken back." },
} as const;
/** The Overview, each README whole. */
export const OVERVIEW = {
  "README.md": "cx reads your Amazon reports to check what Amazon may owe you: units lost or damaged in its warehouses, shipments received short, removals and returns that never came back, fees charged wrongly, and reimbursements paid low. For each, it says whether Amazon already paid and where your store's window is stated. You file claims in Seller Central: cx cannot open a case or send evidence.\n\nSome things you can ask:\n\n- Did every unit from last month's removal orders come back?\n- Does Amazon pay for units lost in its warehouse without a claim?\n- Can filing many claims put my account at risk?\n\n## What it uses\n\n- **Your Amazon seller account:** cx reads your inventory ledger, reimbursements, returns, removals, shipments and fees there.\n",
  "README.zh-CN.md": "cx 读你的亚马逊报告，核对亚马逊可能该赔你的货和钱：仓库里丢失或损坏的货、入库少收、移除后没送回、退款后没退回，以及多收的费用和赔少了的赔偿。每一项都说明亚马逊赔过没有、索赔期限写在哪。索赔由你在卖家后台提交，cx 不能开案件，也不能上传证据。\n\n你可以这样问：\n\n- 上个月的移除订单，货都送回来了吗？\n- 仓库里丢的货，亚马逊会自己赔吗？\n- 索赔提得多，会不会影响店铺？\n\n## 用到的数据\n\n- **你的亚马逊卖家账户**：cx 在这里读取库存流水、赔偿、退货、移除、货件和费用。\n",
} as const;
