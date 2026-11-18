# fc-lost-damaged.md 的中文读本（Positions 部分，FC1–FC56）

**FC1** 运营中心运营索赔，覆盖符合条件的单位："lost or damaged by an Amazon fulfillment center or a facility operated on behalf of Amazon, after Amazon receives them from you"。这类损失 "are reported in your Inventory Ledger report"。Amazon 自己的政策 PDF（US 和 UK，创建于 2025-02-24）载有总条款：物品若 "lost or damaged at a facility or by a carrier operated by Amazon or on behalf of Amazon"，会换成同一 FNSKU 的新品，或予以赔偿。来源：Amazon 帮助文章 "FBA inventory reimbursement policy" 旧版，经 hopted.com 镜像（运营中心运营的措辞）；m.media-amazon.com 上的 Redlined_FBA_Reimbursement_policy_US.pdf 和 _UK.pdf（总条款）。[官方文档；运营中心运营的措辞经第三方镜像]

**FC2** US 站的 Amazon 员工（2026-08-13）把按采购成本（sourcing cost）估值扩展到 "lost and damage claims during inventory replenishment handled by Amazon or on behalf of Amazon to fulfillment centers or non-Amazon buildings in marketplaces where we provide the service"。2025-02-24 的 US 和 UK 政策 PDF 载有同一句话（value-and-reversals VR4）。来源：Indy_Amazon，0e07abc1（站点 US，§ 2a）。[官方文档，员工帖]

**FC3** News_Amazon 于 2024-07-24 在站点为 US 的帖子（81c3235d，`ATVPDKIKX0DER`）中发布：从某个指定日期起，Amazon 会 "proactively reimburse you for … items that are lost in our fulfillment centers … as soon as an item is reported as lost"。帖子说，"almost all" 仓库丢失、仓库损坏和客户退货的案例都将主动赔偿；没有得到赔偿的，仍可手动索赔；所有移除索赔仍须手动提交。来源：81c3235d。[官方文档；站点为命令核实，§ 2a] 这一条用 US 帖补充了 finance pack 的 P-ref-13。

**FC4** Amazon 是逐个站点宣布主动赔偿运营中心丢失单位的，每个站点一个 News 帖，各有自己的起始日期：2024-07-24 的 US 帖（81c3235d）和 Canada 帖（6605eede），以及 2024-10-10 的 UK 帖（d0fc997e）。2024-12-18 的 US、UK、Canada 估值帖（68864b6f、a941ac02、da761b17）各自重述了 "We now offer automatic reimbursements for items lost in our fulfil(l)ment cent(re|er)s"。其他站点没有找到这类公告；Sweden、中东各站和 Australia 的帖子只改了索赔时限。一个站点的日期，要从 `marketplaceId` 为该站点的帖子读（§ 2a）；日期本身在 Values that move。来源：上述各帖；AMZ123 wW7n3WJP 把 2025 年的日期归给 "欧洲站点" [从业者观点]，按帖子字段应收窄为 UK。[官方文档；站点按帖子字段为命令核实，§ 2a；其他站点"没有"是检索结果]

**FC5** UK 的矛盾：一则 UK 员工帖（Jameson_Amazon，2f44617d，2026-04-06，站点 UK）说，UK 仓库丢失库存 "Currently requires manual claim submission (automatic reimbursement disabled since August 2022)"，时限从 "the event" 起算；又说可售单位的仓库损坏会在一个指定期限内自动赔偿。Amazon 的 UK News 帖则说丢失会自动赔偿（d0fc997e，2024-10-10，附起始日期；a941ac02，2024-12-18，"We now offer"），并给出更短的手动时限（d0fc997e；9a92846d，2025-01-15）。两边都列出，不选其一。两边的数值在 Values that move。来源：2f44617d；d0fc997e；a941ac02；9a92846d（按 `marketplaceId` 均为站点 UK）。[官方文档]

**FC6** Amazon 2021 年的文字说：对 2021-03-19 之后的调整，Amazon 会替卖家处理 30 天的调查期（researching），卖家不必等 30 天再提交。来源：已收作 P-stock-states-51（论坛帖 5b46fd45，2021-04-07，按字段为站点 UK，经卖家转述的官方文字）。[官方文档，转述] 属于历史；这是引用别处已有的条目（held），未重做。

**FC7** 2024 年变化之前，Amazon 政策文字规定的运营中心运营索赔时限，从 "the date the item was reported lost or damaged in your Inventory Ledger report" 起算（数值在 Values that move）。US 站一位卖家转述了 Amazon 文字："Starting October 23, 2024, the FBA inventory reimbursement policy for the eligibility claim windows, except for shipment to Amazon claims, will be updated from 18 months to 60 days." 来源：hopted.com 镜像；2de1ef2f（2024-10-16，站点 US；本文件早先称其为 EU 论坛帖）。[官方文档，经镜像和转述]

**FC8** 中文从业者来源把 2024 年前的时限说成 180 天（mjzj 上的招单猫；知无不言 50256，2021），而 Amazon 的是 18 个月。180 天这个数字，在读过的任何 Amazon 文字里都没有依据。来源：如上所列。[从业者观点]

**FC9** 运营中心丢失或损坏的索赔时限按站点设定，并通过公告变更。某站点的时限长度，运行时从该站点域名下显示的 G200213130 读取，并从 `marketplaceId` 为该站点的最新索赔时限 News 帖读取（§ 2a）；没有任何 SP-API 操作返回它。读过的帖子载有以下站点的时限：US（81c3235d；员工帖 0e07abc1）、CA（6605eede）、UK（d0fc997e、9a92846d；员工帖 2f44617d 与之不一致，见 FC5）、SE（1101821c）、SA、EG 和 AE（c6da88ce、e62a8ace、96a05f4a），以及 AU（d8f9a56c）。DE、FR、IT、ES、NL、PL、BE、IE、JP、IN、MX、BR、TR、SG 均未找到。数值：见 Values that move。[官方文档；站点为命令核实，§ 2a]

**FC10** 运营中心索赔时限从 Amazon 报告事件之日起算（"after the item was reported lost or damaged"；"the date the loss or damage event appears in your reports"；"the date the unit is marked as … 'Misplaced'"），不是从卖家发现之日起算。来源：81c3235d；0e07abc1；c6da88ce。[官方文档]

**FC11** 2024-08-06 的那套时限（2024-09-05 生效；"calendar days"；从 "Inventory Adjustment report" 起算）是为 Saudi Arabia（c6da88ce）、Egypt（e62a8ace）和 UAE（96a05f4a）站点发布的，不是为 US、UK 或 EU 发布的。各份副本不同：只有 Egypt 帖列出了承运人损坏的退货和丢失的客户退货。它链接到 "Summary of FBA reimbursement policies and requirements for lost and damaged inventory"（GVTRADRKAA3XXUJ3，未读到）。来源：这三个帖子，`marketplaceId` 读于 2026-11-13。[官方文档；站点为命令核实，§ 2a]

**FC12** 陷阱：Amazon 2026-08-13 的员工帖让卖家去 "Reports > Fulfillment > Inventory Adjustments"；Saudi Arabia、Egypt 和 UAE 站 2024-09-05 的 News 帖以及 Supply Chain Portal 政策，都从 "Inventory Adjustment report" 起算时限。而 Amazon 已在 2023-01-31 停用这份报告，改用 Inventory Ledger。来源：0e07abc1；c6da88ce；supplychain.amazon.com/support/reimbursements；P-stock-states-28。[官方文档；"ledger 是其继任者"这一对应为推断]

**FC13** IDR portal 由 News_Amazon 于 2025-01-21 在站点为 US 的帖子中宣布（b175b700）；没有找到其他站点的上线帖。它的范围和排除项，就提交而言由 filing-and-conduct FL5 收存（见 filing-and-conduct FL5）。来源：b175b700（datePublished 2025-01-21，原始页面读取）。[官方文档] 这一条给 finance pack 的 P-ref-13 / § E3 补上日期和站点。

**FC14** SP-API 模型克隆里，没有任何操作或 schema 返回 IDR portal 的 Eligible-for-Claim 列表、它的状态或它的处理理由。来源：对模型和 schema grep "misplaced"、"reimburs"、"defect"（db2936aa）；"defect" 的命中是账户健康、物流追踪，以及 Finances 发票模型的 `defectTypes`（发票差异，如 `PRODUCT_COST_NOT_ACTIVE`），都不是 IDR。上游 main 在 b13d1d1（2026-11-10）只多了一处 Analytics Economics schema 改动，没有相关字段。[模型部分为命令核实；报告类型部分为推断，依据是 finance pack 读到的 FBA Reports 页面]

**FC15** 从业者描述的 IDR 页面有 Overview、Eligible for Claim、In Progress、Resolved 和 Defect Status Trend，处理结果有 Reimbursed、Reconcile 和 Ineligible，数据来自 ledger、客户退货报告和政策。来源：eComEngine（2025-02-13）；My Amazon Guy（2025-01-24）。[从业者观点]

**FC16** 已撤回。原因：按索赔类型的入口归 filing-and-conduct 收存，见 filing-and-conduct FL4。本文件只保留 UK 员工对丢失路径的措辞（§ 7）。

**FC17** Amazon 说 Transaction Item ID 在 Inventory Ledger 里找。从业者把 ledger 的 `Reference ID` 粘进损坏状态查询工具，所以调整行的 Reference ID 就当作 Transaction Item ID 用。来源：2f44617d；旧版政策文字；Spaghetti，Sellers Ask Sellers（2024-10-14）[从业者观点]。[推断]

**FC18** Amazon 为运营中心索赔点名的证据有：损失的日期或地点（例如 FC ID）、Transaction Item ID 或 FNSKU、所有权证明。对于丢失时已不可售的单位，Amazon "may request additional information or documentation"，用来定一个降低后的价值。来源：旧版政策文字（镜像）；2f44617d；0e07abc1。[官方文档]

**FC19** 按 Amazon UK 员工的说法，可售单位的仓库损坏会在一个指定期限内自动赔偿（见 Values that move）；来源处置状态为 customer damaged、inbound carrier damaged、expired 或 distributor damaged 的损坏，属于 "Eligible for manual claims"。来源：2f44617d（站点 UK）。[官方文档，员工帖，仅限 UK]

**FC20** Amazon 旧版政策文字列出三项索赔前检查：在 Manage FBA Inventory 中确认该单位没有被找到或恢复；在 Inventory Ledger 中确认日期和调整代码；在 Reimbursements report 中 "by FNSKU and date" 确认尚未赔偿。来源：该政策的 hopted.com 镜像。[官方文档，经镜像]

**FC21** 已撤回。原因：过早提交和重复提交作为行为规范，归 filing-and-conduct 收存，见 filing-and-conduct FL7 和 FL11。US 员工帖的 "Don't file prematurely" 和 "Don't submit duplicate claims" 仍在 § 6 中引用，作为 Amazon 的索赔前规矩。

**FC22** 标记运营中心丢失的 ledger 代码是 M 和 5（misplaced）。运营中心损坏是 6、7、E、H、K 和 U，每个后面跟一行 P。找回是 F 和 N，更正是 O，处置是 D。N 和 O 也会因为赔偿而移动单位。来源：已收作 P-stock-states-34 和 -35（Openbridge 和 Reason Automation 对 Amazon ledger 帮助文字的转载）。[官方文档，经第三方] 这是引用别处已有的条目（held），未重做。

**FC23** 从业者筛选未结丢失的方法各不相同，这里并列为几种选择，都不是 Amazon 的，也不选其一：Spaghetti（2024-10-14）在 ledger 明细视图的 Adjustments 中，按原因代码 M 和 5、未对账数量至少为一来筛；知无不言 50256（2021-12-15）在旧的对账报告中去掉未对账为空和为零的行，再看 M 行；Seller Labs（2026-03-18）标出原因为 misplaced、damaged 和 disposed 的负数行。[从业者观点]

**FC24** 用找回抵消丢失的从业者，做法也不同，并列为选择，不选其一：按成对的行，M −1 再 F +1，净额为 0（ZonGuru，2021-10-11）；按 FNSKU，(E + M) 对 (F + N)，差额为负就读作缺货（连连，2021-11-16）。FC25 和 FC26 是这两种做法各自会遇到的陷阱。[从业者观点]

**FC25** 陷阱：N 和 O 也记录因赔偿而发生的移动，所以把 N 算作找回的净额，可能把一笔赔偿当成找回的单位。来源：P-stock-states-35；连连的方法。[推断]

**FC26** 陷阱：找回的单位可能出现在与丢失时不同的运营中心、不同的日期，或不同的 FNSKU 下（代码 3 和 4）。在汇总视图上按国家算净额会把这些掩盖掉，而明细视图每行都带 `Fulfillment Center`。来源：P-stock-states-29、-30、-35。[推断]

**FC27** 从业者按 FNSKU 加日期范围，把 ledger 的丢失行和 Reimbursements report 的行对上，不只按 FNSKU，因为两者之间没有任何标识符相连。来源：Seller Labs（2026-03-18）[从业者观点]；finance pack P-ref-36。[从业者观点]

**FC28** 找回的单位可能在赔偿几个月后回来，赔偿被冲回，单位有时已过期，还被收取移除或处置费。来源：My Amazon Guy（Noah Wickham，2025-10-31），转述卖家报告。0e07abc1 上一位卖家的回复（"Then a year later their inventor was 'found' and they were billed for storage and disposal fees"）讲的是一笔从未赔付的入库短少，不是冲回，只能支持"晚找回"和"收费"两点。[从业者观点] 冲回机制见 finance pack P-ref-18。

**FC29** 从业者 Spaghetti 报告：一个账户 2023 年获赔 $10,000，其中被冲回 $870。来源：Sellers Ask Sellers 4875（2024-10-16 的帖子，datePublished 2024-10-16T14:02Z；已从 2024-10-17 更正）。[从业者观点；单一账户]

**FC30** `getInventorySummaries` 返回 `researchingQuantity`，即 "the misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers"。它是唯一提到 misplaced 单位的 SP-API 字段。来源：fbaInventory.json（db2936aa），grep。[命令核实] 这一条补充 P-stock-states-12。

**FC31** Finances v0 模型对 `FBAInventoryReimbursement` 的描述是 "if a seller's inventory is damaged" 时发生。`LostOrDamagedReimbursement` 是 Easy Ship 的类型，不是 FBA。来源：financesV0.json（db2936aa）。[命令核实]

**FC32** AWD API 模型、Data Kiosk schema 和通知 schema 里，都没有关于丢失、损坏或已赔偿单位的字段。来源：对模型克隆的 grep（db2936aa）。[命令核实]

**FC33** 已撤回。原因：每单位上限归 value-and-reversals 收存，见 value-and-reversals VR29。"£2,000" 员工帖 9d4ff2a6 的站点是 UK（§ 2a）。

**FC34** 已撤回。原因：估值申诉时限归 value-and-reversals 收存，见 value-and-reversals VR20。它的证据帖是 UK 员工帖 9d4ff2a6 和 Australia 帖 d8f9a56c（§ 2a）。

**FC35** UK 在估值上的矛盾：UK 员工（2f44617d，2026-04-06）说赔偿依据是 "estimated proceeds - your item's value minus applicable fees"；而 Amazon 的 UK News 帖 a941ac02（2024-12-18，站点 UK，本文件早先读作 EU 帖）及其延期帖 0252e05d（2025-02-28，站点 UK）把下单前的丢失改为按采购成本估值，2025-02-24 的 UK 政策 PDF 也是如此（value-and-reversals VR2）。UK 员工帖下一位卖家报告：一件 Amazon 卖 £75、制造商卖 £46 的商品，被估为 "£8.86 Amazon estimated"（发票金额未给出）。来源：2f44617d；a941ac02；0252e05d；R-UK。[官方文档；卖家报告为从业者观点]

**FC36** 在读过的 Amazon 页面里，运营中心之间调拨时丢失的单位没有单独的索赔类型。ledger 把它们显示为调整，在途单位记在 "In Transit Between Warehouses"。来源：P-stock-states-31；0e07abc1；知无不言 50256 [从业者观点]。[推断]

**FC37** Amazon 的 AWD 条款（日期 2026-01-14）对在 AWD 设施内或由 Amazon 运营的承运人丢失或损坏的单位，予以更换或赔偿。设施索赔时限从 "on the date that the Unit was identified by Amazon as lost or damaged" 起算，估值按 MCF 赔偿方法。来源：supplychain.amazon.com/legal/service-terms/warehouse-and-distribution。[官方文档]

**FC38** 一位卖家在 2024-09-17 引用的 Amazon AWD 帮助文字承诺：AWD "during facility audit or replenishment of boxes to the FBA network" 发现箱数少于已收货数时，按 "fair value" 赔偿，需向 Selling Partner Support 开案例。来源：10da82b7，引用 GHV89YC29VWN6SBM。[官方文档，转述]

**FC39** AWD 到 FBA 的补货货件带有 FBA 货件 ID 和补货订单 ID，其短少按入库短少处理。卖家报告 Amazon 向他们要卖家无法持有的承运人追踪号。来源：1d0a23e7（2025-11-26）；b738f397（2025-08-21）[从业者观点]；索赔归 inbound-shortfalls。[从业者观点]

**FC40** Supply Chain Portal 的赔偿政策（从 Inventory Adjustment report 起算；有它自己的上限，以及按零售价或预估售价的兜底百分比，数值在 Values that move）是一个不同于 Seller Central FBA 的项目，适用于活跃的 MCF 账户（filing-and-conduct FL27），它的数字不是 FBA 的。来源：supplychain.amazon.com/support/reimbursements。[官方文档]

**FC41** 对 finance pack 的更正：2024-07-24 两个载有 2024-11-01 自动赔偿的 News 帖，是两个站点各自的帖子：81c3235d 是 US 站的（客户退货索赔 "between 60-120 days"）；6605eede 是 Canada 的（"between 45-105 days"），P-ref-13、P-ref-16 和 § F 引的是它。来源：两页均为原始页面读取，`marketplaceId` 读于 2026-11-13。[官方文档；站点为命令核实，§ 2a]

**FC42** 2025-10-15 的索赔时限帖（d8f9a56c，英式拼写，95 次浏览，0 回复）是 Australia 站的（`A39IBJ37TRP1C6`）。把它当作 US 规则（早先的调研笔记如此），或当作不分站点（value-and-reversals VR20 如此），页面本身都不支持。来源：d8f9a56c 原始页面读取。[官方文档；站点为命令核实，§ 2a]

**FC43** 从业者报告 2024 年以前就有仓库损坏的自动赔偿：同时显示 "Damaged at Amazon" 和 "Transfer to holding" 的行已经赔过了。来源：雨果网（王璧辉，2019-06-12）。[从业者观点，历史]

**FC44** Amazon 的中文 FBA 常见问题说，仓库损坏的单位不能移除，会自动赔偿并核销。来源：已收作 finance pack P-ref-37。[官方文档] 这是引用别处已有的条目（held），未重做。

**FC45** Seller Forums 帖子的站点，是它自己帖子对象里的 `marketplaceId`（在 `contentMetadata` 之后、`pinnedToCategory` 之前），在每个论坛域名上都不变；而 `selectedMarketplaceId` 跟随域名。在四个站点由自身内容确定的帖子上（UK 标题和 £ 金额；只发往 Germany 的德文帖；£ 赔偿；£ 上限），这个字段都指向该站点。来源：从四个域名对 2f44617d 的普通 GET、2b01db4c、092c0c0b、9d4ff2a6；Amazon 的 *Marketplace IDs* 页面。[命令核实；"该字段指明规则所管辖的站点"在这四帖上做过检查，Amazon 没有文档说明]

**FC46** Amazon 会把同一段 News 文字按站点分成多个帖子发布，各份副本的数值不同（2024-07-24 的 US 和 Canada 帖相隔 0.66 秒，客户退货时限不同；2024-08-06 的 Saudi Arabia 和 Egypt 帖有两行不同）。在一个帖子里读到的数值，只是那个站点的数值。来源：81c3235d、6605eede、c6da88ce、e62a8ace（§ 2a）。[命令核实]

**FC47** 卖家帖子的这个字段，是卖家发帖时所在的站点，可能与帖子讨论的站点不同（c0d6d3da 讲的是在 IT、ES、FR 的 Pan-EU 销售，字段却是 UK）。来源：c0d6d3da 原始页面读取。[字段值为命令核实；这一解读为推断]

**FC48** 读过的 Amazon 页面里，没有一页为 Amazon 跨境调拨（Pan-EU、UK–EU）途中丢失的单位或 EFN 库存，点名索赔类型、时限、路径或赔付站点；ledger 把这种丢失记为某个运营中心的调整，每行带 `Country` 和 `Store`，调拨本身记为 `WhseTransfers`。Amazon 的协议允许它 "move Units among facilities"，并按 FBA Guidelines 赔偿 "while they are being stored" 期间的损失（AU 协议 F-4）。来源：2025-02-24 的政策 PDF；§ 2a 的 News 帖；stock pack § F3；AU 协议 PDF（2024-06-12）。[官方文档；ledger 的解读为推断] 把跨境调拨丢失当作普通运营中心丢失，是本席自己的推断（见 Seat's own）。

**FC49** 一笔赔偿记入哪个站点、用哪种货币，要从 Reimbursements report 的 `currency-unit`、Finances v0 的 `AdjustmentEvent.StoreName` 和 `AdjustmentAmount.CurrencyCode`，以及 Finances v2024-06-19 的 `marketplaceDetails.marketplaceId` 读取；对存放在一国、在另一国销售或报告的单位，读过的 Amazon 页面没有说明规则。来源：financesV0.json 和 finances_2024-06-19.json（db2936aa）；value-and-reversals 关于 `currency-unit` 的内容。[字段为命令核实；规则未定]

**FC50** 在 NA Remote Fulfillment 下，单位留在 US 运营中心，商品在 Amazon.ca、Amazon.com.mx 和 Amazon.com.br 上销售；这类单位在下单前丢失，属于 US 运营中心丢失，读过的页面没有说明其赔偿的站点或货币。来源：sell.amazon.com/fulfillment-by-amazon/remote-fulfillment（读于 2026-11-13）。[官方文档；"属于 US 运营中心"的解读为推断] 这一解读是本席自己的（见 Seat's own）。

**FC51** MCF 订单在送往买家途中丢失或损坏，按 Amazon 的 MCF 条款索赔，不按运营中心运营索赔：Amazon 的 MCF 页面排除 "marked as delivered by the carrier" 的订单，排除 MCF 费用，排除用 MCF 履行 Amazon 订单或移除库存的情况（India 页面），并设有自己的时限、估值依据和上限（数值在 Values that move）。某站点的 MCF 政策是哪一页，归 inbound-shortfalls（见 inbound-shortfalls IN26）。来源：supplychain.amazon.com/support/reimbursements（"MCF order related claims"）；smartcommerce.amazon.in MCF 赔偿页面（2023-01-24）；卖家帖 868caeba、a8d3c233（US）、63437a69（UK）[从业者观点]。[官方文档]

**FC52** 读过的 Amazon 页面里，没有一页讲 Vine 单位在到达 Vine Voice 之前丢失或损坏怎么办。Vine 单位是 FBA 库存（"FBA inventory must be sent to Amazon fulfillment centers for products to be shipped to Vine Voices"）。来源：sell.amazon.com/tools/vine（读于 2026-11-13）。[官方文档；"没有"是检索结果] 把发出前丢失的 Vine 单位当作普通运营中心丢失，是本席自己的推断（见 Seat's own）。

**FC53** ledger 明细能回溯 18 个月；读过的每一个运营中心运营时限都不超过这个范围，且都从丢失报告起算；读过的 Amazon 页面都没有说，一条超出回溯范围仍未对账的丢失行会怎样。来源：*FBA Reports*（见 sp-api-claims-surface SU15）；§ 3；Values that move。[官方文档；这一比较是我们做的，该行的结局未定] 这一比较是本席自己的算术（见 Seat's own）。

**FC54** Amazon 的资格清单排除：待处置或已处置的单位、有缺陷或被客户损坏的单位、不符合 FBA 产品限制的单位，以及（US）货件已取消或删除的单位；清单没有点名过期、召回或不可抗力的排除。关于在运营中心损坏的过期库存，UK 员工帖把它列为 "Eligible for manual claims"。［保留，见 README § 11：Amazon 的损坏库存归属页面把 "expired" 归为卖家过错这一句，只经 customer-returns RT10 通过已关闭的途径读取 G9MAM9ELJTSSNYS5 得来，不进任何技能。］来源：R-US 和 R-UK（2025-02-24）；2f44617d。[官方文档]

**FC55** Amazon 的协议对 "by reasons, events or other matters beyond our reasonable control" 导致的不履行免责（AU 协议，General Terms 12），并让卖家承担召回费用（S-3.1）；读过的赔偿页面或帖子，没有一个把这两条用到在运营中心丢失或毁损的单位上。来源：AmazonServicesBusinessSolutionsAgreement_2024edits1.pdf（AU，创建于 2024-06-12），m.media-amazon.com。[官方文档；AU 文本，US 协议的相应条款未通过开放途径重读]

**FC56** （撤回：保留，见 README § 11；它唯一的来源是 customer-returns 通过一条现已关闭的途径读取的 G9MAM9ELJTSSNYS5。经允许途径能确立的内容见 customer-returns RT11。）原文为：卖家对某个 ASIN 退出损坏库存归属（damaged-inventory ownership）后，其符合条件的损坏单位会被标为 "defective"，且 "will not be eligible for damage reimbursements"；加入则覆盖 Amazon 过错的仓库损坏库存。来源：customer-returns § 3（G9MAM9ELJTSSNYS5 v4，US），以指引方式引用。[官方文档，由另一文件通过一条现已关闭的途径读取]
