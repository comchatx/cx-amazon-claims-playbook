# sp-api-claims-surface.md 中文读本（SU 各条）

本文逐条读英文原文 `research/method/sp-api-claims-surface.md` 的 Positions 一节，编号和顺序与原文一致。共 60 条，没有撤回的条目。来源标注：官方文档 / 命令核实 / 推断 / 从业者观点。原文 *Seat's own* 一节列为本席自己的判断的内容，在相关条目里注明。

**SU1** 角色决定能调用哪些 operation、report、feed 和 notification。应用只要持有 Amazon 为某项读取列出的角色中的至少一个，就能读。来源：*Role Mappings for SP-API Operations*（2026-10-28），*Role Mappings for SP-API Types*（2026-09-09）。[官方文档]

**SU2** 以下报告只列 Amazon Fulfillment 一个角色：ledger 明细和汇总报告、`GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA`、`GET_FBA_INVENTORY_PLANNING_DATA`、`GET_FBA_OVERAGE_FEE_CHARGES_DATA`、`GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA`。来源：*Role Mappings for Types*；*FBA Reports*（2026-10-13）。[官方文档；以 grep 命令核实]（补充 finance P-ref-28 和 the door，它们只提到其中一部分。）

**SU3** `GET_FBA_REIMBURSEMENTS_DATA`、`GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`、两份 removal 报告、`GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA`、`GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA`、`GET_FBA_STORAGE_FEE_CHARGES_DATA` 和 `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA`，各自接受 Pricing 或 Amazon Fulfillment。`GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL` 还接受 Inventory and Order Tracking。来源：*FBA Reports*；*Role Mappings for Types*。[官方文档]

**SU4** Fulfillment Inbound v0 的 `getShipments`、`getShipmentItems`、`getShipmentItemsByShipmentId`，以及 v2024-03-20 的每个 operation，都只列 Amazon Fulfillment。来源：*Role Mappings for Operations*。[官方文档]（v0 这几项读取的含义由 stock pack P-inbound-2 负责。）

**SU5** Finances v0 `listFinancialEvents` 列出 AISP（仅 EU）、Amazon Fulfillment（仅 NA、FE）和 Finance and Accounting。`…ByOrderId` 只列 Finance and Accounting。来源：*Role Mappings for Operations*。[官方文档]（finance pack 的表格已有此项。）

**SU6** Catalog Items v2022-04-01（`includedData=dimensions`）需要 Product Listing。它给的尺寸是"associated with the item in the Amazon catalog"的尺寸。Amazon 为计费实测并存档的尺寸，在 fee preview 报告和 storage fee 报告里。来源：`catalogItems_2022-04-01.json`；*FBA Reports*。[官方文档] 两者可能不同，这一点是[推断]。

**SU7** Product Fees v0 的 `getMyFeesEstimateForSKU` 和 `…ForASIN` 接受十二个角色中的任意一个，包括 PL、PR、AF 和 FA。`getMyFeesEstimates` 需要 Pricing 或 Product Listing。它们返回的是某个价格下的费用估算，不是实际收取的费用。来源：*Role Mappings for Operations*；`productFeesV0.json`。[官方文档]

**SU8** Support API v2025-02-01（`listCases`、`getCase`、`listContacts`）需要 Selling Partner Support (Restricted)，这个角色不在卖家的应用里。如果有这个角色，能读到卖家 case 的状态、日期、主题，以及 Amazon 的邮件、电话、聊天往来和附件，报销 case 也在内。目前没有任何东西建在它上面。来源：*Support API*（2026-09-30）；*Role Mappings for Operations*。[官方文档]

**SU9** Support API 于 2026-09-30 上线。来源：*SP-API Release Notes*。[官方文档]

**SU10** Support API 的三个 operation 都是读取。`listCases` 不能按任何条件筛选：它只接受排序方式、每页条数和 token，没有日期、case 类型、报销、ID 或 marketplace 参数。一个 case 不带类型、金额或报销 ID。联系记录的附件通过会过期的 `downloadUrl` 获取。这些 operation 在模型里带有 usage plan，实际适用的速率在 `x-amzn-RateLimit-Limit` 里返回。每页条数的上下限、URL 有效期和默认速率见 *Values that move*。来源：`support_2025-02-01.json`。[命令核实]

**SU11** Amazon 各页面对 Support API 的说法互相矛盾。角色页（2026-11-12）说该角色可以"retrieve, search, and manage support cases"，但模型里既没有搜索筛选，也没有写操作。教程（2026-09-30）把这个角色叫"the Support role"。联系记录教程描述了一个联系记录的 `status`（`VALID`/`EXPIRED`），但模型的 `Contact` 没有这个字段。来源：上述页面；`support_2025-02-01.json`。[官方文档；命令核实]

**SU12** Amazon 模型里的 394 个 operation 中，没有一个能提交索赔、开 case、附证据或录入采购成本。也没有一个能更新、回复或重开 FBA 报销 case 或 support case，申请重新测量，对费用或报销金额提出异议，或在丢失损坏（IDR）页面里操作。模型里唯一创建索赔的写操作是 Shipping v2 `createClaim`，那是承运商索赔（见 SU13）。来源：db2936aa 版本的模型；main 上的 b13d1d10（2026-11-11）没有新增 operation。[命令核实]（本条是整个 pack 中这一说法的归属处；filing-and-conduct FL1、inbound-shortfalls IN29、removals-disposals RM35 和 value-and-reversals VR18 都指向这里。它把 finance P-ref-29 的范围扩展到重新测量、金额异议和 IDR 页面。）

**SU13** SP-API 唯一创建索赔的 operation 是 Shipping API v2 `createClaim`。它按 tracking ID 对一个包裹提交承运商索赔（`LOST_IN_TRANSIT`、`DAMAGED_IN_TRANSIT`、`DELIVERED_NOT_RECEIVED`、`ITEM_MISSING_SWITCHEROO`、`COD_ABUSE`）。它不是 FBA 库存报销，也不在 Role Mappings 页面上。来源：`shippingV2.json`；*Role Mappings for Operations*。[命令核实]

**SU14** Amazon 的 agentic toolkit（`amzn/selling-partner-agentic-toolkit`，12 个 skill，最后推送 2026-11-11）没有报销或索赔的 skill 或工具。它的 `support-case-helper` "by default"不调用任何 SP-API 工具；"If no such tool exists (current state)"时，把卖家引到 Seller Central Help Center。来源：该仓库。[命令核实]

**SU15** ledger 明细的回溯期写在 Amazon *FBA Reports* 页面上 ledger 明细的说明里。在 Amazon 的 SP-API 页面中，它是唯一写明回溯期的索赔报告。具体值见 *Values that move*。来源：*FBA Reports*。[官方文档]（ledger 由 stock pack P-stock-states-30 负责。）

**SU16** Amazon 的 SP-API 页面没有写明 reimbursements、FBA returns、replacements 和 removal 报告的回溯期。一位 Amazon 开发者支持工程师说，这类限制由 Seller Central 报告团队管理，写在 Seller Central 的报告说明里。来源：*FBA Reports*；issue #2974（2022-07-15）。[官方文档；工程师的话为从业者观点]

**SU17** 数据服务商的连接器会按报告类型设定自己的回溯期和延迟。这些是服务商的设置，不是 Amazon 的，要在服务商页面上读。读到的值见 §3 的 Fivetran 表和 *Values that move*。来源：Fivetran "Amazon Selling Partner – Reports"（无日期，未写 marketplace）。[从业者观点]

**SU18** 报告的回溯期和索赔窗口是两回事：报告能往回查 18 个月，不代表更早的事件还能索赔。好几家服务商的页面把两者混为一谈。来源：finance P-ref-16（窗口）；§3 中的服务商页面。[推断，依据 Amazon 分开的表述]

**SU19** Amazon 为 FBA 报告的两次生成设了最短间隔：近实时报告一个值，每日报告一个值，写在 *FBA Reports* 开头。从业者说这个冷却期按卖家、按报告类型计算，跨所有应用共用。具体值见 *Values that move*。来源：*FBA Reports* [官方文档]（stock pack W20）；Airbyte 文档 [从业者观点]。

**SU20** fee preview 报告的刷新间隔、`dataStartTime` 必须往前推的时长，以及每个卖家的请求次数限制，都写在 *FBA Reports* 上该报告自己的条目里。同一条目注明其尺寸分段列和未来费用列只适用于一个站点。具体值见 *Values that move*。来源：*FBA Reports*。[官方文档]

**SU21** Amazon-fulfilled shipments 报告每次请求的时间跨度、每个时间窗内的请求上限（Seller Central 的请求也计入），以及发货后的延迟，都写在 *FBA Reports* 上该报告自己的条目里。具体值见 *Values that move*。来源：*FBA Reports*。[官方文档]

**SU22** long-term storage fee 报告要求的请求时间跨度写在 *FBA Reports* 上它的条目里。具体值见 *Values that move*。来源：*FBA Reports*。[官方文档]

**SU23** 部分 FBA 报告只在部分站点提供。站点列表写在 *FBA Reports* 上每份报告的"Amazon store availability"一行或说明里（replacements；inventory planning；Fee Preview 的部分列）。具体值见 *Values that move*。读取处：*FBA Reports*。[官方文档]

**SU24** 一位开发者报告：无论 `marketplaceIds` 填什么，`GET_FBA_REIMBURSEMENTS_DATA` 都返回同样的行；在冷却期内对同一区域另一站点再次请求，会被取消。Amazon 支持当时给出的间隔是 238 分钟（2021）。来源：issue #1847。[从业者观点]

**SU25** removal shipment detail 报告对同一日期范围、在不同时间请求，返回过不同的行数（2024、2026）。Amazon Developer Services 说："there is no guaranteed time until all updates have been properly reflected throughout Amazons backend."来源：issue #4333、#5323。[从业者观点；Amazon 员工]

**SU26** removal shipment detail "will not include canceled returns or disposed items"，并且类型为"Return"的行不带目的地址。来源：*FBA Reports* [官方文档]；issue #5344 [从业者观点]。

**SU27** Amazon 页面上 ledger 明细的示例 `"reportOptions":{"eventType":""}` 会被 API 拒绝（"length greater than or equal to 1"）。不填 `eventType` 会返回全部事件。来源：issue #4747（2025-04-21）[从业者观点]；页面上仍印着这个示例 [官方文档]。不填即返回全部事件，这一点是从"Default is the empty string"[推断]出来的。

**SU28** Seller Central 按站点本地时间显示 ledger 请求的时间范围，包括夏令时。来源：issue #5339，Amazon 员工回复（2026-07-31）。[从业者观点]

**SU29** 没有任何 SP-API 报告类型对应 Seller Central 的 Payments Date Range（交易）报告。工具在那里按 `Fee Adjustment` 读取的尺寸费退款，通过 API 要从 Finances 或 settlement 报告里取。来源：*Role Mappings for Types*；*Payment Reports*（2026-09-09）[命令核实：没有 `GET_DATE_RANGE_FINANCIAL_TRANSACTION_DATA`]；领星 FBA费差异 [`Fee Adjustment` 一行为从业者观点]。

**SU30** Deferred Transaction Report（`GET_DATE_RANGE_FINANCIAL_HOLDS_DATA`，Finance and Accounting）必须先在 Seller Central 的 Payments Reports Repository 里申请一次，API 才能取到。来源：*Payment Reports*。[官方文档]

**SU31** 没有任何通知类型会通告报销、ledger 调整、入库收货或差异，或 support case 的变化。`TRANSACTION_UPDATE` 在"whenever there is a new transaction posted to the seller's account"时发送，它不在 Role Mappings for Types 页面上；报销入账会不会触发它，是[推断]。来源：*Notification Type Values*（2026-10-28，26 个类型标题）；*Role Mappings for Types*。[命令核实]

**SU32** Fulfillment Inbound v2024-03-20 的货件商品只有 `quantity`，没有已收数量。通过 API 按货件、按 SKU 读已收件数，要用 v0 的 `QuantityReceived`。来源：`fulfillmentInbound_2024-03-20.json`、`fulfillmentInboundV0.json`。[命令核实]（由 stock pack I3、P-inbound-2 负责。）

**SU33** Data Kiosk 的 Economics 数据集需要 Selling Partner Insights，这个角色不在五个角色之内。Amazon 的更正页这样写。2025-04-23，一位开发者的 Economics 查询被拒（"Unauthorized to access requested fields"），Amazon 开发者支持当天重复了这一点。Data Kiosk 页面和 operations 页面仍为 Data Kiosk 的 operation 列 Brand Analytics；字段的角色在创建查询时检查。来源：*Data Kiosk API*（2026-10-20）；*Correction: Data Kiosk role requirements* [官方文档]；issue #567 [从业者观点；Amazon 员工]。（更正 finance P-ref-28 和 P-api-23，它们把这一点留作未定；fee-overcharges FE18 依赖这个数据集。）

**SU34** Data Kiosk 最早可用的 `startDate` 和结果保留期写在各数据集的 schema 里：`startDate` 的说明，以及叶子字段上的 `@resultRetention`。具体值见 *Values that move*。来源：db2936aa 版本的 Economics、Seller Analytics 和 Sales and Traffic schema。[命令核实]

**SU35** Economics 在 2026-09-30 增加了 removal、disposal、deal、coupon 和 fuel 费用；在 2025-12-22 去掉了 FNSKU 粒度。来源：*SP-API Release Notes*。[官方文档]

**SU36** Finances v0 的 `listFinancialEvents`、`…ByGroupId` 和 `…ByOrderId` 于 2025-07-21 被弃用。移除日期以 *SP-API Deprecation Schedule* 上的为准，Amazon 曾改动过其他资源的移除日期（值见 *Values that move*）。来源：*SP-API Deprecation Schedule*。[官方文档]（由 finance P-ref-24 负责；本次重读未变。）

**SU37** Orders v0（`getOrders`、`getOrder`、`getOrderItems`、`getOrderAddress`、`getOrderBuyerInfo`、`getOrderItemsBuyerInfo`）于 2026-01-28 被弃用。移除日期在 schedule 上读取（值见 *Values that move*）。继任者是 Orders v2026-01-01（`searchOrders`、`getOrder`），角色列表相同。来源：*SP-API Deprecation Schedule*；*Release Notes* 2026-01-28；*Role Mappings for Operations*。[官方文档]

**SU38** `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE` 和 `…_XML` 于 2026-11-11 被移除（2025-03-17 弃用）。来源：*SP-API Deprecation Schedule*。[官方文档]（the door 已有此项。）

**SU39** 弃用时间表写的 `analytics_salesAndTraffic_2023_11_15` 数据集移除日期是 2026-03-27；2025-08-27 的 release note 写的是 2026-02-26。来源：这两个页面。[官方文档]

**SU40** Role Mappings for Types（2026-09-09）仍列着时间表已移除的类型：SnS 报告、旧的 settlement flat 和 XML 报告，以及 `ORDER_STATUS_CHANGE`。一个类型出现在该页上，不能说明它还能用。来源：这两个页面。[命令核实]

**SU41** 2025-01 到 2026-11-04 之间，没有任何 release note 或弃用公告新增、修改或移除 FBA 索赔报告类型、ledger 或 reimbursements 报告。也没有任何一条提到报销索赔、IDR 页面或 Case Log。来源：*SP-API Release Notes*；*Deprecation Schedule*。[命令核实：grep]

**SU42** 旧索赔指南提到的六种库存 adjustment、receipt 和 reconciliation 报告类型，已于 2023-01-31 移除（2022-06-13 弃用；时间表那一行列了六种类型，除 adjustments、receipts 和 reconciliation 外，还有 current-inventory、inventory-summary 和 monthly-inventory）。来源：*SP-API Deprecation Schedule*。[官方文档] "由 Inventory Ledger 取代"这句话不在时间表上，是 stock pack（W25）的说法，在本文中为[推断]。（由 stock pack W25 / P-stock-states-27 负责。）

**SU43** 领星（Lingxing）用卖家自己填写的 CASE ID 把索赔和付款对上：当这个 ID 出现在 Reimbursements 报告的 `case-id` 里，就算赔付。它在每个候选项旁边显示 ledger 的 `Reference ID`。它的诊断限每个 case 一个 SKU、每天十个 SKU，这是工具自己的规则，不是 Amazon 的。其他从业者改用 FNSKU 加日期范围来匹配（§7 把各种做法并列）。来源：领星帮助"费用诊断"（无日期，2026-11-13 读取）。[从业者观点]

**SU44** 有一个工具，领星，用（实收费用 − 应收费用）× 数量来估算尺寸多收的金额，尺寸取自 fee preview 报告中 Amazon 实测的尺寸。这是 §7 和 fee-overcharges FE34 并列的做法之一。来源：领星帮助"FBA费差异"。[从业者观点]

**SU45** 截至 2026-11-13，Amazon Seller Central 上 Reimbursements 报告（G200732720）、customer returns（G200453320）和报销政策（G200213130）的帮助页，在美国站、英国站和 `/gp/help/external` 路径上用普通 GET 取到的都只是 JavaScript 空壳。它们的回溯期文字没有读到。本文不再读它们：help hub 的内容接口是 office 于 2026-11-10 关闭的路径。来源：本席的抓取。[命令核实]

**SU46** 受限角色要求开发者提供"additional information about your data use and security controls"。来源：*Roles in the Selling Partner API*（2026-11-12）。[官方文档]

**SU47** `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE`（按退货日期的自发货退货报告，含五个 SAFE-T 列、`Order Amount` 和 `Refunded Amount`）需要 Inventory and Order Tracking 或 Direct to Consumer Shipping (Restricted)，两者都不在五个角色之内。它只覆盖自发货退货，不含 FBA 退货，也不含无需退货的退款。它可以单次请求或定时生成，每次请求的跨度写在 *Returns Reports* 上（值见 *Values that move*）。来源：*Returns Reports*（2026-10-28）；*Role Mappings for Types*。[官方文档；命令核实]

**SU48** Seller Fulfilled Prime 退货报告（`GET_CSV_MFN_PRIME_RETURNS_REPORT`、`GET_XML_MFN_PRIME_RETURNS_REPORT`）的角色里有 Pricing，所以在应用之内。它们只覆盖 Seller Fulfilled Prime 退货。CSV 版本带有同样的 `SafeT-…` 列和 `Refunded-Amount`。来源：*Returns Reports*；*Role Mappings for Types*。[官方文档；命令核实]（finance pack 的退款表有这些角色；customer-returns RT39 只指向非 Prime 报告。）

**SU49** `GET_V2_SELLER_PERFORMANCE_REPORT`（按 marketplace 的 `accountStatuses` 和 Account Health 指标）只列 Selling Partner Insights 一个角色，不在五个之内。它只能单次请求。来源：*Performance Reports*（2026-10-28）；*Role Mappings for Types*。[官方文档；命令核实]

**SU50** 入库和费用相关文件在 SU4 之外依赖的 Fulfillment Inbound 读取，也都只列 Amazon Fulfillment：v2024-03-20 的 `listTransportationOptions`、`listPlacementOptions`、`listShipmentPallets`、`listPrepDetails`、`listInboundPlanItems` 和 `getInboundPlan`，以及 v0 的 `getBillOfLading` 和 `getLabels`。FBA Inbound Eligibility v1 `getItemEligibilityPreview` 也一样。来源：*Role Mappings for Operations*（2026-10-28）。[官方文档；命令核实]

**SU51** MCF 订单读取（Fulfillment Outbound v2020-07-01 的 `getFulfillmentOrder`、`listAllFulfillmentOrders`、`getPackageTrackingDetails`）列 Amazon Fulfillment。模型里有包裹状态 `UNDELIVERABLE`（"lost or destroyed"），追踪事件"Shipment damaged"和"Lost by carrier"，以及退回商品处置 `CarrierDamaged` 和 `FulfillerDamaged`。没有任何 operation 能提交 MCF 索赔。来源：`fulfillmentOutbound_2020-07-01.json`；*Role Mappings for Operations*。[命令核实]

**SU52** Reimbursements 报告带 `currency-unit`，但没有站点或 marketplace 列。ledger 明细带 `Country` 和 `Store`。所以一笔报销属于哪个站点，在报销行上看不出来。来源：*FBA Reports* 的字段列表（2026-10-13）。[官方文档] Pan-EU、EFN 或 Remote Fulfillment 卖家的报销行只能通过订单或 ledger 对应到站点，这一点是[推断]。

**SU53** Settlement 报告由 Amazon 定时生成，不能主动请求；Reports API 保留报告有一个写明的最长期限（值见 *Values that move*）。因此，超过这个保留期的 settlement 报告，无法通过 API 取到，也无法重新生成 [推断]。来源：*Settlement Reports*（2026-10-14）；`reports_2021-06-30.json` [官方文档；命令核实]；服务商帮助页（搜索摘要）[从业者观点]。这条推断是本席自己的判断（*Seat's own*），依据 Amazon 的两条表述。

**SU54** Data Kiosk Seller Analytics 按发货日期统计退货件数，它的 schema 写明了退货数据的延迟（值见 *Values that move*）。按 operations 页面，它的角色是 Brand Analytics。Amazon 的更正页早于这个数据集，没有提到它。来源：`analytics_sellerAnalytics_2025_03_31.graphql`；*Role Mappings for Operations*。[命令核实；官方文档]

**SU55** Economics schema 把支持的费用类型指向 Seller Central 帮助页（`economics` 指向 GZ8Y22NL2FSRY8M5，`economicsPreview` 指向 GQNVDV46U9JQ25HY），两页都没有读。schema 自己的 `PreviewFeeType` 枚举列出了预览费用类型，自 main b13d1d10 起其中包括 removal 和 disposal 费用。来源：db2936aa 和 main 上的 `analytics_economics_2024_03_15.graphql`。[命令核实]

**SU56** Support API 的模型不接受 marketplace 参数，也没写 `listCases` 能查到多久以前的记录；它的页面说它"available in all Amazon stores"。卖家的 case 能列到多久以前，没有写明。来源：`support_2025-02-01.json`；*Support API*（2026-09-30）。[命令核实；官方文档]

**SU57** Data Kiosk Sales and Traffic 里的索赔指标是 A-to-z Guarantee 索赔（"applies to seller-fulfilled orders only"）和 chargeback 索赔的数量与比率。没有一个统计 FBA 报销索赔。来源：`analytics_salesAndTraffic_2024_04_24.graphql`。[命令核实]

**SU58** 清算收入以 Finances v0 的 `FBALiquidationEventList` 入账，在 `listFinancialEvents` 下；读过的报告类型中，没有一个按 removal order 列出清算收入。来源：`financesV0.json`；*FBA Reports*。[命令核实]（清算应得多少由 removals-disposals 负责。）

**SU59** stranded 和 reserved 库存报告列 Pricing 或 Amazon Fulfillment，只能单次请求，"updated in near real-time"。stranded 报告带 `date-stranded`、`stranded-reason` 和 `Date-to-take-auto-removal`。来源：*FBA Reports*。[官方文档]（stranded 由 stock pack `stuck-stock/references/stranded.md` 负责。）

**SU60** Selling Partner Support (Restricted) 是为应用单独申请的，和应用的其他角色分开：2026-10 有一位开发者问 Amazon，怎样把它加到已批准的应用上而不影响其他角色。Amazon 没有回复。来源：issue #5422。[从业者观点]（受限角色的要求见 SU46。）

**SU61** FBA 报告生成一次后，等待期过完之前 Amazon 不会生成更新的版本（SU19），所以在等待期内，已经生成的那份报告就是 Amazon 手上最新的内容；`getReports`（`GET /reports/2021-06-30/reports`，`reportTypes`）列出已经生成的报告。*FBA Reports* 没说等待期内再请求会得到什么。各条目写的是：赔偿、FBA 退货和补发报告「Content updated daily」，两份移除报告「Content updated in near real-time」，库存流水明细的条目两样都没写。来源：*FBA Reports* 开头和各条目（2026-10-13 版，2026-11-23 读取）；`reports_2021-06-30.json`。[官方文档]「已经生成的那份就是最新内容」是由开头那句[推断]。
