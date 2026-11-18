# inbound-shortfalls.md 中文阅读（IN 立场）

**IN1** 亚马逊的 FBA 赔偿政策覆盖"at a facility or by a carrier operated by Amazon or on behalf of Amazon"（在亚马逊运营或代亚马逊运营的设施或承运人处）丢失或损坏的商品。条件之一是：卖家发出的是"the exact items and quantities stated in your shipping plan"（与货件计划完全一致的商品和数量）。来源：美国政策 PDF（2024-12-18）；德国政策 PDF（2025-02-24）。[官方文档]

**IN2** 被归为"distributor damaged"或"damaged by inbound carrier"的到货，是在亚马逊接收前就已损坏的。这些货不可售，会被移除。亚马逊指明的赔偿途径是卖家自己的承运人。来源：NR_Amazon，美国帖子 `0d6e8a48-…`（帖子 2025-03-19，回复 2025-04-11）。[官方文档] 读取位置：库存台账的处置状态，`GET_LEDGER_DETAIL_VIEW_DATA`（Amazon Fulfillment）。

**IN3** 对于亚马逊合作承运人造成的丢失，亚马逊员工让卖家按 Shipment to Amazon 政策向亚马逊提交索赔，并附所有权证明和交货证明。来源：TaylorR_Amazon，美国帖子 `10816b8f-…`（帖子 2024-11-12，回复 2024-11-29）[官方文档]。"亚马逊是托运人、卖家不能向合作承运人索赔"这一说法，来自同一帖子里卖家的陈述，以及帖子 `0fc75622-…` 中卖家转述的 UPS 回答；已读的亚马逊页面都没有这样说 [从业者观点]。

**IN4** 承运人的交货证明只能证明箱子到了，不能证明箱里有什么。2023-08-07 一封亚马逊卖家支持邮件，以此为由"at this time"拒绝了一次合作承运人的丢失索赔（"Amazon has no evidence the units were received"）。卖家后来转述说退款正在处理中。来源：该邮件，引于美国帖子 `0fc75622-…`。[官方文档，经卖家转述；后来的结果：从业者观点]

**IN5** 小包裹货件如果用卖家自己的承运人，货件上必须有追踪编号，亚马逊才会赔付。来源：SCP 的 *Shipment to Amazon claims*（supplychain.amazon.com/support/reimbursements），以及 Hopted 转载的无日期 FBA 页面。[官方文档（MCF）；经第三方转述（FBA）] 对 FBA，已读的亚马逊自己的页面说得更少：Indy_Amazon（2026-08-13）把"Tracking IDs and proof of delivery for inbound shipments"列为需准备的材料；gs.amazon.cn article-250807-3（2025-08）说亚马逊要求小包裹货件每箱有唯一追踪码，并说非合作承运人货件在录入有效追踪后显示为 Shipped。两者都没有用文字把赔付与追踪编号挂钩 [官方文档]。读取位置：`getShipment` → `trackingDetails.spdTrackingDetail`（Amazon Fulfillment）；用 `updateShipmentTrackingDetails` 写入。

**IN6** 在 v2024-03-20 模型中，每个 SPD 追踪编号都带 `trackingNumberValidationStatus`（`VALIDATED`、`NOT_VALIDATED`、`NOT_SUPPORTED` = 亚马逊找不到该编号的追踪信息）。模型说：24 小时后仍未验证的编号，要核对并更新。来源：`fulfillmentInbound_2024-03-20.json`，提交 `db2936aa`。[命令核实]

**IN7** 入库货件缺件的索赔期限按站点而定，从货件经核实送达运营中心之日起算；索赔要在货件关闭后提交。读取位置：卖家所在站点的帮助页 *FBA inventory reimbursement policy: Shipment to Amazon claims*（`GEYPWTSQRTXXXMVB`）（只返回脚本外壳；本文件未读到正文），以及该站点论坛的 News。没有任何 API 操作给出这个期限。美国站的证据：Indy_Amazon 的帖子（2026-08-13）、gs.amazon.cn article-250305-3（2025-03，"*美国适用"）和 article-250807-3（2025-08，"（美国站）"），以及一位卖家引用 `GEYPWTSQRTXXXMVB` 的帖子（2024-09-26，帖子站点为美国）；均于 2026-11-13 读取；数值见 *Values that move*。本条扩展了存货包的 I21。[官方文档]

**IN8** 亚马逊的帖子 *Update on reimbursement claim window eligibility on FBA*（2024-08-06；"Starting September 5, 2024"）规定了"发往亚马逊的货件缺件"从货件送达日起算的最短和最长自然日数。这篇帖子以三个帖子发布，分别面向阿联酋、沙特阿拉伯和埃及站，不是面向美国或英国。来源：`96a05f4a-…`、`c6da88ce-…`、`e62a8ace-…` 帖子级的 `marketplaceId`（全包的帖子-站点对照表归 fc-lost-damaged）；天数见 *Values that move*。[官方文档；站点为命令核实] 读取位置：各站点论坛的 News。

**IN9** 亚马逊关于索赔期限的 News 帖子——美国（2024-07-24）、加拿大（2024-07-24）、英国（2024-10-10、2025-01-15）、瑞典（2025-01-15）、澳大利亚（2025-08-14）——都没有写发往亚马逊货件的期限。没有读到亚马逊关于欧盟、英国或日本入库期限长度的说法（亚马逊修订稿说了什么，见 IN35、IN36）。来源：各帖子的站点在此处经命令核实；内容同财务包 P-ref-16。[官方文档]

**IN10** Fulfillment Inbound 的任何操作（v0 或 v2024-03-20）都不返回送达、签入、接收或关闭日期。期限的起算日（"verified delivery date"）无法从 API 读取。来源：两个模型在 `db2936aa` 中的全部 `date-time` 字段。[命令核实] 读取位置：只有替代值：`GET_LEDGER_DETAIL_VIEW_DATA` 中第一条 `Receipts` 事件、所选的送货时间窗或承运人预约（`getShipment`、`listTransportationOptions`），以及承运人的追踪信息。

**IN11** 卖家平台按货件显示它是否可以申请调查，以及预计可申请的日期。亚马逊员工说这个日期是标准流程，并说差异"can auto-correct during the receiving process, but it's not guaranteed"（可能在接收过程中自动更正，但不保证）。来源：gs.amazon.cn article-250305-3（2025-03）；Angie_Amazon，美国帖子 `ecbb2ef1-…`（帖子 2026-04-03，回复 2026-04-09）。[官方文档] 读取位置：只在卖家平台（Contents 标签页；*Missing inbound FBA inventory* 工具，`G201214140`）。

**IN12** "Investigation completed – shipment contents counted and confirmed"表示亚马逊已把箱子与计划对上，并实际清点了件数。此后这些件不再可以申请调查。Selling Partner Support 找到的件会补入库存；找不到的，亚马逊视为少发，不赔付。来源：Julia_Amzn，英国帖子 `25ab2e15-…`（帖子 2024-08-16，回复 2024-08-20）；gs.amazon.cn article-250305-3。[官方文档] 读取位置：只在卖家平台。

**IN13** 提交调查申请会创建一个 Selling Partner Support 案例，案例号显示在 Contents 标签页上。亚马逊员工给出的调查时长是一个范围，不是规定；并说不是所有差异都会得到赔偿（审核时长见 filing-and-conduct FL30；数字见 *Values that move*）。来源：sell.amazon.com *How to track FBA shipments*（修改于 2025-10-03）；TaylorR_Amazon 2023-10-10；Christine_Amazon，美国帖子 `83caf79b-…`，2025-11-14；Bryce_Amazon，美国帖子 `e0a6f096-…`，2024-09-05。[官方文档] 读取位置：通过 Support API 读取案例，需要五个角色之外的受限角色（见 sp-api-claims-surface SU8）。

**IN14** 亚马逊的页面把 `CLOSED` 定义为所有件已接收；或者在两者不一致时，从货件创建起算的一个超时，各页面写的超时长度不同。v0 模型没有给出超时（"arrived at the fulfillment center and all items have been marked as received"）。读取位置：站点的货件状态帮助页和 sell.amazon.com 的追踪指南。证据：sell.amazon.com（修改于 2025-10-03）；gs.amazon.cn article-250807-3（2025-08）；TaylorR_Amazon（2023-10-10）；v0 `ShipmentStatus`；各自写的超时见 *Values that move*。这些超时的日期归存货包 I9，此处未重读。[官方文档；模型部分为命令核实]

**IN15** 对入库货件的丢件索赔，亚马逊要求：
- 货件编号；
- 所有权证明（供应商发票、其他卖家的收据，或制造商签字的装箱单），写明购买日期、商品名称和数量，并写明出具方和买方；
- 交货证明：LTL/FTL 要有亚马逊盖章的文件，写明提货时的箱数和总重量；小包裹要有有效的追踪编号。

丢失的件在货件的 Contents 标签页提交；损坏的件通过支持案例提交。来源：SCP 页面；Indy_Amazon 2026-08-13；KJ_Amazon 回复 2025-02-13；gs.amazon.cn 2025-03 和 2025-08。[官方文档]（filing-and-conduct FL24 为提交重述了这份清单；中文措辞见 IN41。）

**IN16** 亚马逊只接受不可编辑格式的所有权文件（PDF、JPG、JPEG、PNG、TIFF）。它不接受形式发票和合同，并允许卖家遮盖进货价格。来源：gs.amazon.cn article-250305-3（2025-03）。[官方文档]

**IN17** 每个货件只允许一次索赔；同一货件的后续索赔会被拒绝（见 filing-and-conduct FL7，该限制归它）。本文件补充的证据：AWD 条款（2026-01-14）对 AWD 也同样适用——每个货件一次货件索赔，每箱一次设施索赔。[官方文档]

**IN18** 亚马逊建议在货件的商品页面提交申请，而不是找卖家支持，因为卖家支持很可能会把卖家指回那里。亚马逊还说，调查不会改变卖家现有的库存。来源：gs.amazon.cn article-250807-3（2025-08）。[官方文档]

**IN19** 多收的件也通过同一个 Action required 菜单申请调查（"Extra units shipped"；缺件在员工帖子里是"Units not shipped"或"Research missing units"）。已读的亚马逊页面都没有说多收可以抵消缺件。来源：Christine_Amazon 2025-11-14；gs.amazon.cn 2025-08 [官方文档]；2018 年帖子中转述的"leader"说法及其反驳 [从业者观点]。

**IN20** 亚马逊的 Contents 标签页和 v0 的商品列表按 SKU 列出发货数与接收数，所以一个 SKU 的多收和另一个 SKU 的缺件是两行。已读的亚马逊页面没有写抵消规则。从业者计算短缺有两种做法：按货件和 SKU 计算（PrepVia，2026-08-25；优麦云的索赔助手，2024-06-05），或跨货件计算——卖家说运营中心是这样做的（帖子 `111de1ae…`，摘要；2018 年帖子转述的"leader"）。已读的从业者都没有建议索赔时做抵消。[按 SKU 分行：在 v0 模型中命令核实；这些做法：从业者观点] 读取位置：按 SKU 比较 `QuantityShipped` 与 `QuantityReceived`（v0，Amazon Fulfillment）。

**IN21** 亚马逊政策把发往亚马逊货件的索赔，以及由亚马逊或代亚马逊处理的补货途中的丢失，归入"预订单"类别，按制造或采购成本赔偿。对同一批 PDF 做文本提取时能看到一句关于发往亚马逊货件索赔按"estimated proceeds"估值的话，但在渲染后的页面上它是被划掉的（美国 2024-12-18、美国 2025-02-24、日本 2025-02-19）；那是 2025 年以前的依据。估值本身归 value-and-reversals（见 VR1、VR2、VR4、VR28）。来源：这些 PDF，2026-11-13 渲染后阅读。[官方文档；命令核实] 读取位置：卖家所在站点的 *FBA inventory reimbursement policy*（`G200213130`）；赔付记录在 `GET_FBA_REIMBURSEMENTS_DATA`。

**IN22** 已撤回。原因：每件赔付上限归 value-and-reversals（见 VR29）；Supply Chain Portal 页面自己的上限和兜底规则归 filing-and-conduct（FL27）和 fc-lost-damaged（FC40）。本文件读到的数值保留在 *Values that move*。

**IN23** 对于 2026-01-01 当天或之后创建的美国货件，到货时没有正确预处理和商品贴标的件，如果损坏或"untraceable"（无法追踪），不予赔偿。在该日期之前创建的货件，即使晚到，也保留亚马逊的预处理服务。这适用于通过 AWD、AGL、Amazon SEND 和 Supply Chain Portal 进入美国 FBA 的库存。来源：Jameson_Amazon，美国帖子 `5c63f045-…`（帖子 2025-11-25，回复 2025-12-01）；回复原文是"created before January 1"和"created after January 1"，"当天或之后"是本岗位的解读。[官方文档；边界日为推断] 读取位置：计划的 `createdAt`（`getInboundPlan`/`listInboundPlans`，Amazon Fulfillment）；每个商品的 `prepOwner`/`labelOwner`。

**IN24** 亚马逊于 2025-12-08（英国和加拿大论坛帖子）宣布：2026-03-31 当天或之后发出的库存，结束混合库存（commingling）。持有制造商条码的品牌代表不需要亚马逊标签；转售者和没有制造商条码的商品必须使用亚马逊标签。公告没有提到赔偿。来源：帖子 `06778c12-…`（英国）、`cd352647-…`（加拿大）。[官方文档；站点为命令核实]

**IN25** 一位从业者称，2026-03-31 之后，没有所需条码的到货会被标为残次，不予赔偿。来源：PPC Land，2026-03-24。[从业者观点]

**IN26** AWD 货件索赔使用 MCF 库存赔偿政策的索赔期限，从经核实送达 AWD 站点之日起算；每个货件一次索赔，每箱一次 AWD 设施索赔，通过支持案例提交。从 AWD 运往 FBA 中心途中丢失的件按 MCF 政策赔偿，AWD 索赔按 MCF 政策的方法估值。MCF 政策就是 Supply Chain Portal 的赔偿页面（IN34），所以 AWD 索赔适用的期限、上限和估值要在那里读，而不是在 FBA 政策里读。来源：AWD 服务条款，日期 2026-01-14，2026-11-13 读取；期限数值见 *Values that move*。[官方文档] 本条细化了存货包 I21（见更正部分）。

**IN27** AWD 模型对一个 AWD 入库货件按 SKU 返回预期数量和接收数量（`getInboundShipment`，带 `skuQuantities=SHOW`），单位为 `PRODUCT_UNITS`、`CASES` 或 `PALLETS`。亚马逊的教程说 API 中没有 AWD 报告。来源：`db2936aa` 中的 AWD 模型 [命令核实]；*Track an inbound shipment with expected and received SKU details*（2026-09-09）[官方文档]。角色：Amazon Warehousing and Distribution，在五个角色之外。

**IN28** AWD → FBA 补货货件使用 FBA 货件编号。对这类货件的缺件，亚马逊员工开了案例，要求的是所有权证明，不是交货证明。来源：KJ_Amazon，美国帖子 `2c97b436-…`，回复 2025-02-13。[官方文档]

**IN29** 没有任何 SP-API 操作提供入库货件的调查资格或可调查日期、"Investigation completed"这一行、货件的对账结果、索赔期限，或亚马逊核实的送达日期。这些都是卖家平台里的视图（Shipping Queue → Contents/Reconcile）。"没有操作能提交或答复索赔"以及 Support API 能读到案例的哪些内容，归 sp-api-claims-surface（SU8–SU12）。来源：`db2936aa` 中的 Fulfillment Inbound、AWD 和报告模型（之后的上游提交都没有改动它们）。[命令核实]

**IN30** 已撤回。原因：已移除的对账报告和接收报告归 sp-api-claims-surface；见 SU42。

**IN31** 从业者给出的入库期限，在已读的亚马逊页面中都找不到依据：60–90 天（Refunzo，2026-01-18）；Receiving 状态的索赔从创建起 90 天（百运网，2026-05-27）；欧盟 6 个月（Helium 10 FAQ 和 SELLERLOGIC，摘要）。[从业者观点]（AMZ123 / 深圳美辰物流，2023-10-27，说的 18 个月是运营中心操作类索赔，不是入库。）AMZ123（问答 1KqAXyXG，2025-05-19）说索赔期为 180 天；已读的亚马逊页面都不支持。[从业者观点]

**IN32** 货件可能显示 Delivered 若干天后才变成 Checked-in，旺季更久；这个滞后是亚马逊写明的上限，且亚马逊可能更改（gs.amazon.cn article-250807-3，2025-08，2026-11-13 读取；数值见 *Values that move*）。用合作承运人时，货件在提货时显示 Shipped；用卖家自己的承运人时，在录入有效追踪后显示 Shipped。[官方文档]

**IN33** AWD 条款规定了按箱子尺寸收费的费用索赔的提交期限，从收费日起算（第 4.2 节）。来源：AWD 条款，日期 2026-01-14，2026-11-13 读取；数值见 *Values that move*。[官方文档] 截至 2026-11-13，fee-overcharges 还没有收录这一条；在它收录之前，本条留在这里。

**IN34** AWD 服务条款提到的"MCF inventory reimbursement policy"，就是页面 https://supplychain.amazon.com/support/reimbursements，标题为 *Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS)*：条款中的五处提及都链接到这个页面。该页面的资格要求 MCF 账户"in Active state"，它的期限、上限和估值是它自己的，不是 FBA 政策的（与 filing-and-conduct FL27 所述一致）。来源：AWD 条款，日期 2026-01-14（链接目标于 2026-11-13 从页面 HTML 读取）；SCP 页面，2026-11-13 读取。[官方文档；链接为命令核实]

**IN35** 亚马逊 2024-12-11 的英国政策修订稿写明，从 2025-01-09 起索赔期限改变，"except for shipment to Amazon claims"（发往亚马逊货件的索赔除外）。英国的发往亚马逊货件期限不在那次改动之内，该页面也没有写它的长度。来源：`_PC__Kiwi_Comms_redlined_policy_UK_clean_version.pdf`（m.media-amazon.com，创建于 2024-12-11），2026-11-13 读取。[官方文档] 读取位置：英国站域名下的 `GEYPWTSQRTXXXMVB`（只返回脚本外壳；本文件未读到正文）。

**IN36** 亚马逊 2024-08-20 的欧盟修订稿改动了客户退货、运营中心操作和移除这几页，没有 Shipment to Amazon 这一页；亚马逊 2025-02-19 的日本政策提到了 Shipment to Amazon claims，但没有写期限。通过允许的途径读到的亚马逊页面，都没有写欧盟站点、英国或日本入库期限的长度。一篇 2025-06-06 的英国员工帖子说丢失或损坏库存"File within 60 days"，但没有说是哪类索赔，也没有说从何时起算；一位英国卖家转述说，卖家平台以"over 6 months since arrived"为由拒绝了他（2025-01-08）。来源：`EU_Policy_Redline.pdf`（创建于 2024-08-20）；`redline_FBA_reimbursement_policy__EN_version.pdf`（G/09，创建于 2025-02-19）；Spencer_Amazon，帖子 `e236599d-…`（站点英国）；帖子 `c3831651-…`（站点英国）；均于 2026-11-13 读取。[官方文档；卖家的转述：从业者观点] 读取位置：所在站点域名下的 `GEYPWTSQRTXXXMVB`，以及该站点论坛的 News。

**IN37** 按 *Amazon Global Logistics Freight Service Terms*（日期 2026-01-14），亚马逊承担丢失风险"only from receipt at Origin until delivery at Destination"（只从在起运地接收起，到在目的地交付止），而 Destination"means an Amazon facility"（指亚马逊设施）。从中国起运的海运，签约方是 Beijing Century Joyo Courier Co., Limited（BCJ），索赔"exclusively against the Amazon Contracting Party (not the carrier)"（只能向亚马逊签约方提出，不能向承运人提出）。对于亚马逊无法清点、交付时封条完好的密封集装箱，亚马逊"not liable for shortages or any damage … unless proximately caused by our independent action"（不对短缺或任何损坏负责，除非直接由亚马逊自身行为造成）；对包装不当造成的损失，亚马逊也不负责。来源：该条款的序言及 §§ 1.4、3.5、5.5、10.3、19，2026-11-13 读取。[官方文档] 读取位置：supplychain.amazon.com 上标明日期的条款，以及该订舱的提单。

**IN38** AGL Freight 的丢失或损坏索赔，是在一定期限内向亚马逊发出的书面通知；期限从交付日起算，货物丢失则从计划交付日起算。提起诉讼另有期限，从亚马逊书面拒赔起算。亚马逊记入的金额，卖家在规定期限内没有书面异议的，即为全部和解。赔偿额有限制：发往美国的海运提单按每票货件限额，除非订舱时书面约定了更高责任；否则按适用公约或报关价值，取较低者；另有每 12 个月的累计上限。卖家必须证明亚马逊、其分包商或实际承运人有过失，并且必须自己为货物投保。来源：AGL Freight Service Terms §§ 7.7、8、10.1、10.6、10.8、11.1、11.3，2026-11-13 读取；期限和限额见 *Values that move*。[官方文档] 计费条款归财务包（P-ful-29 至 P-ful-31）。

**IN39** 亚马逊的 FBA 政策覆盖"at a facility or by a carrier operated by Amazon or on behalf of Amazon"的丢失；货物在卖家委托的承运人或货代手中、交付前发生的丢失，不在这句话的范围内，要按卖家与该承运人的合同索赔。亚马逊的中文文章把货代、仓库和清关时的点数错误，以及运输中纸箱破损，列为箱内短缺的原因，并告诉卖家在申请调查前先与发货人员和承运人确认。来源：美国政策 PDF（2024-12-18）；gs.amazon.cn article-250807-3（2025-08），2026-11-13 读取。[官方文档；范围的解读为推断]

**IN40** 从业者把头程追偿描述为按合同向货代或航空公司索赔：收货时在交付单据上注明异常；隐藏损坏要在短期内书面通知；除非货物投了保，否则按公约以重量计算限额；材料包括 AWB 或提单、商业发票、装箱单和照片（百运网，2026-11-09）。深圳美辰物流（AMZ123，2023-10-27）通过追踪信息区分是承运人的问题还是仓库的问题，前者与货代协商。[从业者观点]

**IN41** 亚马逊的中文页面把入库证据称为库存所有权证明（供应商发票、其他卖家的收据，或制造商签字的装箱单，写明日期、货件号或 PO 号、商品名称、发货数量，并有签字或盖章）；对 LTL/FTL，交货证明是承运人的提货单，"须经亚马逊盖章"。中国从业者则把货代盖公司章的签收单当作 POD（百运网，2026-05-27），并说亚马逊仓库收货时常常不盖章（AMZ123，2024-05-12）。仅有货代盖章的签收单是否满足亚马逊对 LTL/FTL 的要求，尚未读到。来源：gs.amazon.cn article-250305-3（2025-03）、article-250807-3（2025-08）[官方文档]；从业者 [从业者观点]。
