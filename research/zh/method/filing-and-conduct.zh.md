# filing-and-conduct.md 的中文读本（FL 各条立场）

**FL1**　没有任何 SP-API 操作能开启 FBA case 或索赔、附上证据、回复 case 或重开 case。这些都在 Seller Central 里完成，由卖家本人或卖家授权的用户来做。Support API 的读取操作和那一个承运商索赔操作，见 sp-api-claims-surface SU8、SU10、SU12、SU13。〔命令核实，在该处核实〕

**FL2**　Amazon 的政策把两件事定为条件：按索赔类型走对应流程，并提供所有要求的信息。原话："We may decline your claim if you do not."。Supply Chain Portal 政策对它自己的项目也这样规定。来源：FBA inventory reimbursement policy PDF（US，创建于 2025-02-24）；April 2021 UK 路径下的 PDF；SCP 页面（2026-11-13 读取）。〔官方文档〕

**FL3**　只有 Amazon 尚未赔付过的商品才能索赔。版主的指示是：手动提交前先查 Reimbursements 报告。来源：US PDF 2025-02-24；Indy_Amazon，US，2026-08-13。〔官方文档〕

**FL4**　不同索赔类型的入口不同。Amazon 的 US 版主在 2026-08-13 给出的入口如下：
- warehouse damaged：政策页上的 "Check warehouse damaged reimbursement status" 工具，按 Transaction Item ID；
- warehouse lost：一个 Get Support case（"FBA Issue > Inventory Lost in Warehouse"），按 FNSKU 或 Transaction Item ID；
- missing from inbound：该货件的 Reconcile 标签页；
- damaged inbound：一个 Get Support case（Canada 站点 2022-07-25 的一封 Amazon 拒绝信写的是："open a claim through the Contact Us page"）；
- customer returns：政策页上的 "Check FBA order reimbursement status" 工具，按订单号；
- removals："Resolve a removal order issue" 工具，按 removal order ID。

customer returns 还有 Amazon 的第二种说法：帮助页 *Customer return claims*（G9N934L7Y4SFWPJ4，US v14，CA v5；GB 为 G84Z6B8BTKVNV53S）让索赔工具从 IDR portal 的 "Eligible for claim" 标签页上的订单号开始，并允许在那里对 "Resolved" 决定提出异议。这是 customer-returns RT41 的读法，2026-11-13 经由 help hub 的 content call 读取，而办公室已在 2026-11-10 关闭了这条途径。两种说法都连同日期列出，不选其一；两页都没说它们是不是同一个流程。（"两者可能是同一流程"是本文件自己的读法，未定。）来源：Indy_Amazon，thread 0e07abc1，US，2026-08-13〔官方文档，员工帖〕；thread 481080e4，Canada，2022-07-25〔官方文档，转述〕；customer-returns RT41〔官方文档，经由已关闭的途径〕。

**FL5**　IDR portal 于 2025-01-21 在 US 站点宣布上线。它覆盖 warehouse lost、warehouse damage 和 customer returns，并且"doesn't include defects under missing from inbound, removals or warehouse disposals"。入口是 FBA dashboard 的 Inventory 菜单，或 Reimbursements 报告。它的帮助页（G66ZLS453YSE2Y4R）未读。来源：News_Amazon，thread b175b700（`createdAt` 2025-01-21；`marketplaceId` 为 US）。〔官方文档〕（财务包 E3；portal 显示什么见 fc-lost-damaged FC13–FC15。）

**FL6**　陷阱：Amazon 2026 年的员工指引提到 "Inventory Adjustments" 报告和 "Transaction Item ID"，并链接了一个 Seller Central 报告页 `reportcentral/INVENTORY_ADJUSTMENT/0`。该报告的 API 类型（`GET_FBA_FULFILLMENT_INVENTORY_ADJUSTMENTS_DATA`）已于 2023-01-31 移除，由 Inventory Ledger 取代；Amazon 的 FBA 报告类型页也不再列出它。那个 Seller Central 页面是否还提供这份报告，需要登录，未读。Amazon 没有说 ledger 的 `Reference ID` 就是 Transaction Item ID。来源：Indy_Amazon 2026-08-13〔官方文档〕；Amazon 的弃用通知（只见搜索文本；developer-docs changelog 页面对普通 GET 不返回通知正文）和库存包 P-stock-states-28〔官方文档，经由搜索文本和库存包〕；Amazon 的 FBA 报告类型页（`GET_LEDGER_DETAIL_VIEW_DATA` 的 `Reference ID` 列，2026-11-13 读取）〔官方文档〕；一份中文 ERP 指南〔从业者观点〕。

**FL7**　同一个入库货件的第二次索赔会被 Amazon 拒绝。原话："you may file only one claim per shipment. Additional claims for the same shipment will be declined."。2026 年 US 版主的说法是：每个货件或每个事件只能索赔一次。来源：转述的 Amazon Services 拒绝文本（Canada 站点，2022-07-25，thread 481080e4）；SCP 页面（其自身项目）；Indy_Amazon，US，2026-08-13。〔官方文档〕（inbound-shortfalls IN17 在它的领域里持有同一规则。）

**FL8**　Amazon 的支持规则是：一个 case 只谈一个问题；同一问题已有 case 开着时，不再开新 case。来源：Connor_Amazon，US，2025-01-31（thread 460319ae）。〔官方文档〕

**FL9**　读过的 Amazon 页面都没有规定每个 case 的商品上限或每天的 case 上限。数量只作为行为问题出现（FL11）。来源：§ B 中的页面。〔推断，基于所读页面〕

**FL10**　从业者给出的每 case 和每天的数字互相矛盾，也都没有引用 Amazon 页面：
- 每个 case 5 个 FNSKU（较早的指南）；
- 每个 case 10 个 SKU（AMZ123 2022，Jungle Scout China 2022）；
- 每个 case 1 个 FNSKU，每个店铺-站点每天最多 10 个（SellerSpace 2025）；
- 一天开了"30+个case"后被停用（看点资讯 2021）。

〔从业者观点〕

**FL11**　Amazon 禁止妨碍它帮助其他卖家的行为。它举的例子是 "submitting insufficiently researched or premature requests" 和 "submitting a large number of requests in a short time"（April 2021 政策 PDF 中为 "high volumes"）。反复这样做的卖家 "may receive delayed support on their cases or be subject to monitoring, investigation, and account action"。这一段出现在 April 2021 UK 路径政策 PDF 和 2025-02-24 US PDF 中，Amazon 自己的消息也引用过：Canada 站点的一封拒绝信（2022-07-25），和一条 Selling Partner Support 消息（US，2024-08-22）。Supply Chain Portal 政策对 MCF 账户有它自己的版本（"delayed support or … further account monitoring and action"）。来源：上述 PDF；thread 481080e4 和 6833e3db〔官方文档，转述〕；SCP 页面〔官方文档〕；Buy with Prime reimbursement policy〔只见搜索文本；普通 GET 返回 403〕。

**FL12**　Selling Partner Support 的重述："we decline requests that are not consistent with our policies"。在 "no further action" 之后，卖家不应 "by reopening the case or raising it again in other cases" 来寻求不同结果；"Amazon may close cases or limit support if you don't follow these guidelines."。这条消息发给了一位正在为丢失货物追讨部分赔付的卖家，并链接了 *Guidelines for contacting Selling Partner Support*（GK3V2JYCN2P28BFX，未读）。来源：时间为 08/22/2024 的支持消息，在 2024-08-25 的回帖中贴出，thread 6833e3db，US。〔官方文档，转述〕

**FL13**　有日期的变化：账户状态条件放宽了适用范围。April 2021（UK 路径）要求 "when you file a claim" 时账户为正常状态。2025-02-24 的 US 文本要求 "When a lost or damaged item claim is filed, under review, and during any appeals" 时都为正常状态。2026 年 US 版主排除了 "blocked, terminated, or fraud status" 的账户。SCP 政策要求 MCF 账户 "in Active state and not under review or suspension"。来源：两份 PDF；Indy_Amazon 2026-08-13；SCP 页面。〔官方文档〕

**FL14**　如果文件 "forged, tampered with, or illegible"，或账户被怀疑有欺诈或严重违规，Amazon 可以拒绝提交的 sourcing cost。来源：US PDF 2025-02-24。〔官方文档〕（政策中对同一商品重复提交的规则归 value-and-reversals VR22。）

**FL15**　Seller Code of Conduct 要求卖家 "Provide accurate information to Amazon … at all times"，并 "Act fairly and not misuse Amazon's features or services"。这些话来自转述：Amazon 的页面（G1801）对普通 GET 只返回脚本空壳，也没找到许可范围内的原始副本（m.media-amazon.com 上的 BSA PDF、gs.amazon.cn 搜索）；它们是一位 Amazon 员工对该页的引用。来源：Emet_Amazon，US，2024-11-23（thread a3c0c769）。〔官方文档，员工对未读页面的转述〕

**FL16**　卖家贴出的因索赔被停用的通知中，提到了 BSA 第 3 条（只有 807fb6a2）、Seller Code of Conduct、"FBA credit reimbursement abuse"（807fb6a2、e885be1d）、"repeatedly submitted improper claims for FBA reimbursement"，以及（中文，2021）"短时间内提交了不适当或者大量的重复请求，滥用了亚马逊的销售合作伙伴支持服务"。来源：thread 807fb6a2（US，2024-07-01）、e885be1d（US，2023-03-27）、22eecf9e（US，2021-05-04）；看点资讯 2021-04-16。〔从业者观点：卖家贴出的 Amazon 原话〕

**FL17**　因索赔被停用的卖家称自己用过第三方索赔服务（807fb6a2，2024；22eecf9e，2021）。一条卖家回帖说，对这类合作方 "Amazon holds YOU responsible"。一位被停用的卖家发现，账户停用期间该服务仍在提交 case；帖中没有结果。DAM Law Firm 写道，从 2026-03-04 起卖家要为账户上的每个 Agent 负责。读过的 Amazon 页面都没有说卖家要为服务商提交的索赔负责。来源：thread 807fb6a2、22eecf9e；DAM Law Firm 2026-09-03。〔从业者观点〕

**FL18**　从业者报告过一例停用：入库短缺已获赔付，之后"找到"的货品被证明不是该卖家的。来源：敏哥跨境记，跨境知道，2024-09-24。〔从业者观点〕

**FL19**　读过的 Amazon 页面既没有禁止、也没有认可第三方索赔服务。来源：§ D 中的页面。〔推断，基于所读页面〕

**FL20**　SP-API AUP 2.11 要求代卖家行事的应用 "ensure all submissions and communications are accurate, policy-compliant, and do not result in frivolous or non-compliant contacts or degradation of Amazon support systems"。AUP 1.1 把它限制在卖家授权过的活动内。来源：Acceptable Use Policy（页面无日期）。〔官方文档〕

**FL21**　需要 Amazon Portal 访问权的 SP-API 开发者，应请卖家通过 secondary user permissions 授予，且不得索要或共享 Amazon Portal 的用户名或密码。来源：AUP 3.3、3.7〔官方文档〕。该处没有说 SP-API 之外的第三方也受同样约束〔推断〕。

**FL22**　有日期的变化：从 2026-03-04 起，BSA 要求任何访问 Amazon Services 的自动化软件或 AI agent 表明自己是自动化系统、遵守 Agent Policy、并在 Amazon 要求时停止访问；Amazon 可以限制它的访问。该日期后继续使用即视为接受。来源：News_Amazon，US thread 84e3f6b1（2026-02-17）和 Canada thread 8a2dfc1c（2026-02-19）〔官方文档〕。Agent Policy 本身的文本（GS83KH2MA7HM69PH）未读：对普通 GET 只返回脚本空壳，也没找到许可范围内的原始副本。公告三项义务之外的规则全都来自转述："Agent/[agent name]" user-agent 字符串、不模仿人类击键、如实回答，均出自 ecomsellertool（2026-09-25，2026-11-04 更新）〔从业者观点：转述，未与 Amazon 页面核对〕。

**FL23**　（已收窄：该 skill 的 SP-API 与建 case 行为归 sp-api-claims-surface，见 sp-api-claims-surface SU14。）此处因行为问题保留一点：该 skill 会在 "Reported From" 字段中填入正在运行的 agent 的名字。来源：`support-case-helper` SKILL.md v1.0.0。〔命令核实〕

**FL24**　Shipment-to-Amazon 的证据是所有权证明（itemized invoice、从其他卖家处的收据，或 packing slip；制造商则用签名的 packing slip）加交付证明。LTL/FTL 的交付证明是 Amazon 盖章的交付文件；小包裹是有效的 tracking ID（拒绝信中写作 "SPD shipments"；SCP 页面要求每个包裹一个）。来源：Amazon Services 拒绝文本（Canada，2022-07-25）；Indy_Amazon，US，2026-08-13；发票字段见库存包 inbound.md F2。〔官方文档〕

**FL25**　移除索赔的证据是 removal order ID、shipment ID、ASINs/FNSKUs、受影响数量和受影响商品的图片。SCP 页面另加 tracking 或交付证明、LPN 和成本证明。来源：Indy_Amazon 2026-08-13；supplychain.amazon.com *Reimbursements*。〔官方文档〕

**FL26**　（已收窄：价值证明的字段、可接受的文件、"完全一致"规则，以及 Amazon 两种说法的发票时限，都归 value-and-reversals VR12–VR14；Nano_Amazon 的帖子日期是 2025-06-12，Arish_Amazon 的是 2026-02-24。）此处保留：sourcing cost 文件在 Seller Central 的 Manage Your Sourcing Cost 中提交，不在 case 中提交。来源：US PDF 2025-02-24（"Visit the Manage Your Sourcing cost help page"）。〔官方文档〕

**FL27**　来源陷阱：supplychain.amazon.com/support/reimbursements 这个页面有两个名字。它自己的标题是 *Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS)*，要求 MCF 账户处于有效状态，并排除用 MCF 履行 Amazon.com 订单的情况。Amazon 的 AWD service terms（日期 2026-01-14）把 "MCF inventory reimbursement policy" 这几个字链接到同一地址。所以 inbound-shortfalls 的读法（AWD 条款所称的 MCF 政策，IN26）和本文件的读法（ASCS 项目的政策，适用于有效 MCF 账户）说的是同一个页面。它的索赔和争议通过 Supply Chain Portal 的 Contact Us 提交。它的时限、单件上限和兜底估值是它自己的，不是 FBA 的，但它的证据清单与 FBA 一致；每一项都在它自己的页面上读取（数值见 "Values that move"）。来源：SCP 页面；AWD service terms；US PDF 2025-02-24。〔官方文档〕

**FL28**　卖家看到的 case 状态是 "Pending Amazon Action" 或 "Pending Merchant Action"；卖家回复后，case 交回 Amazon。来源：Connor_Amazon，US，2025-01-31。〔官方文档〕（Support API 的四种状态归 sp-api-claims-surface SU10。）

**FL29**　已赔付的手动索赔会出现在 `GET_FBA_REIMBURSEMENTS_DATA` 中，并带有 `case-id`（财务包 P-ref-20）；这是 API 中从 case 到钱的唯一连接。读取 case 本身需要 sp-api-claims-surface SU8 中的角色。〔官方文档〕

**FL30**　Amazon 只为三件事说明了审核或回复时间：入库调查、重新测量，以及卖家对入库补充信息请求的回复；每项都在各自页面上读取（数值见 "Values that move"）。读过的页面都没有说明其他 FBA 索赔的审核时间。SCP 政策为 MCF 订单索赔说明了它自己的时间。来源：库存包 inbound.md F1–F2；NR_Amazon，US，2025-04-30（见 fee-overcharges FE4）；SCP 页面。〔官方文档〕

**FL31**　卖家报告 case 在没有回复的情况下被自动标为 "Answered"，例如挂起 14 天后（2026-08-11）。来源：论坛帖子（搜索结果）。〔从业者观点〕

**FL32**　Amazon 告诉卖家：对已关闭的 case 有疑问时，重开它，而不是开新 case；在 "no further action" 决定之后，不要重开或再次提出该问题。来源：Connor_Amazon，US，2025-01-31；2024-08-22 的支持消息（thread 6833e3db）。〔官方文档〕

**FL33**　卖家可以回复 case、说明需要更多时间，来延长这个 case。来源：Connor_Amazon，US，2025-01-31。〔官方文档〕

**FL34**　被停用的账户通过 Account Health 恢复；账户不处于正常状态时，索赔不符合资格。来源：TaylorR_Amazon，US，2024-11-26（thread 8e91e62f）；US PDF 2025-02-24。〔官方文档〕

**FL35**　已撤回。原因：重新测量的限制归 fee-overcharges FE4，见 fee-overcharges FE4。NR_Amazon 的帖子 ca22eab2 日期为 2025-04-30。

**FL36**　已撤回。原因：MYSC 更新次数限制和重复规则归 value-and-reversals，见 value-and-reversals VR11、VR22。

**FL37**　读过的 Amazon 页面都不对提交索赔收费。Amazon 提到的代价是：索赔被拒、行为后果（FL11）和冲回。来源：§ H。〔推断，基于所读页面〕

**FL38**　Professional 卖家可以通过邮件、请求回电或聊天联系支持；Individual 计划的卖家只能发邮件。来源：Connor_Amazon，US，2025-01-31（链接了 G64491）。〔官方文档〕

**FL39**　从业者给的菜单路径和时限会过时：2020–2024 年的中英文指南引用 "Other FBA Issue" 路径和 18 个月或 180 天的时限，这些已被 2024–2025 年的变化取代。来源：知无不言 2020、AMZ123 2022 和 2024、卖家之家 2024〔从业者观点〕；有日期的时限见财务包 P-ref-16〔官方文档〕。

**FL40**　有一家 ERP 让卖家在事件发生的店铺和站点对应的 Seller Central 中提交每个索赔，否则会有 "account association issues"；读过的 Amazon 页面都没有这样说。来源：SellerSpace 2025-03-20。〔从业者观点〕

**FL41**　SCP 政策为入库另加了一句自己的行为条款："Merchants who generate a high number of shipping problems affecting Amazon receiving operations may be subject to additional investigation and monitoring. These actions could result in delays to future reimbursements."。读过的 FBA 页面都没有这句。来源：SCP 页面，*Shipment to Amazon claims*（2026-11-13 读取）。〔官方文档〕

**FL42**　Amazon 2022 年在 Canada 站点的入库拒绝信，已经用了政策后来的措辞（"a large number of requests in a short time"），还加了一个兜底说法（"or otherwise engaging in any other activity that interferes with our capacity to help other sellers"）。所以 2025 年之前，Amazon 用过的措辞并不只有 2021 PDF 的 "high volumes"。来源：thread 481080e4（2022-07-25）。〔官方文档，转述〕

---

**本文件自己的读法（Seat's own）**：以下是本文件的解读，不是 Amazon 的规则，不作为结论进入 skill。
- 行为条款中的 "premature" 指在某类索赔的时限开始之前（§ C(c)）〔推断〕；
- 政策中的 "normal status" 就是账户健康报告中的 `NORMAL`（§ C）〔推断〕；
- 更多、更小的 case 是否计入 "a large number of requests"，未定（§ B(c)）〔推断〕；
- Indy_Amazon 的工具路径和 IDR 的 "Eligible for claim" 标签页可能是同一流程（FL4）〔推断，未定〕。
