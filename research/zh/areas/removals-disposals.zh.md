# removals-disposals.md 的中文阅读

按原文顺序，保留原编号。来源标签：官方文档 / 命令核实 / 推断 / 从业者观点。原文说明：本文件的立场中没有"Seat's own"（本席自有）立场。

**RM1** 移除索赔覆盖的是：符合条件的商品离开 Amazon 设施、在送往卖家退货地址的途中，被 Amazon 或 Amazon 使用的承运人丢失或损坏。卖家违反政策而被退回的商品不在其内。来源：removals-claims 页面文字（EU redline 2024-08-20；US 页面的 Hopted copy）；Amazon Supply Chain 的 SCP 页面（另一个项目的页面）有同样的句子（2026-11-13 读）。Seller Central 的实时页面没有通过许可的途径读到。[官方文档]

**RM2** 所有移除索赔都要手动提交：Amazon 2024 年的每一篇自动化公告都这样说；截至 2026-11-13 读到的内容中，没有任何一篇宣布移除索赔自动化。这些公告及其所属站点归 fc-lost-damaged（post-to-store table）管；IDR 门户不含移除和仓库弃置这一点归 filing-and-conduct（FL5）管。来源：News 81c3235d、6605eede、d0fc997e（2026-11-13 读）。[官方文档；"没有宣布"为推断]

**RM3** Amazon 的移除索赔类型有：运输途中丢失（lost in transit）；运输途中损坏（damaged in transit）；收到的商品损坏、不符或不全（damaged, different or incomplete units received）；以及对客户退货评级的争议（grading disputes）。来源：EU redline 2024-08-20；News 96a05f4a（UAE，2024-08-06）。[官方文档]

**RM4** 在 Seller Central 提交移除索赔的入口是 "Resolve a removal order issue" 工具（G9ZB3H4DP4H72U6R），以移除订单 ID 为键（见 filing-and-conduct FL4）。来源：Indy_Amazon 0e07abc1（2026-08-13）；Hopted copy。[官方文档]

**RM5** News 公告中的时限，按其公告对象所写的站点来读；每篇公告属于哪个站点、这种读法带什么标签，归 fc-lost-damaged（post-to-store table）管。本文件补充一点：读到的移除相关公告，正文里都没有写出站点，所以没有一篇能用正文所写的站点去检验这个字段。来源：862f270b、d8f9a56c（2026-11-13 读）。[正文中没有站点一点为命令核实；字段的读法沿用 fc-lost-damaged 的标签]

**RM6** 运输途中丢失的移除索赔，既有最早提交日，也有最晚提交日；其他移除索赔有一个最晚提交日，从货物送回卖家之日起算。时长因站点、因日期而不同，要读该站点的 removals-claims 页面，以及带该站点 marketplace 字段的最新 News 公告。US 的证据：2024-07-24 发布，2024-10-23 生效，丢失为 "15-75 days from the shipment-creation date"，"All other removal claims must be filed within 60 days of the shipment being delivered back to you"（81c3235d，2026-11-13 读）。在此之前，US 帮助页面的文字是：丢失不早于 "14 days from the last confirmed movement"，所有索赔在 "18 months of the date the item was removed" 之内（Hopted copy，Wayback 2026-07-13；同样的文字在 2024-08-20 的 EU redline 中被划掉）。[官方文档]

**RM7** Amazon 的站点级公告可以一次改动全部移除时限，可以把评级争议时限的起算点从送达日改为移出日，还可以新增一个重新评估时限。2025-08-14 的 Australia 公告（2025-10-15 生效）三项都做了；没有找到带 US marketplace 字段、载有这些时限的公告。具体数值见 *Values that move*。来源：d8f9a56c（Australia 字段，2026-11-13 读）。[官方文档；US 没有为推断]

**RM8** 丢失类移除时限的起算点因站点而不同：UAE 公告从货件的发货日（ship date）起算，而 US、Canada、UK 和 Sweden 的公告从货件创建日起算；UAE 公告还给收到商品的问题（损坏、不符、不全）单设一个从送达日起算的时限。具体数值见 *Values that move*。来源：96a05f4a（UAE 字段，2024-08-06 发布，2024-09-05 生效，2026-11-13 读）。[官方文档]

**RM9** Amazon 自己的文字给出了丢失类移除索赔最早提交日的三种起算点：货件创建日、发货日、承运人最后一次确认的移动。早于这一天提交的索赔会以"过早"被拒。来源：RM6–RM8；被拒一点来自 ReclaimHQ。[官方文档；被拒一点为从业者观点]

**RM10** Amazon US 员工 2026-08-13 的帖子给移除的时限是 18 个月，"of the shipment being delivered or lost"。这个时长与 2024 年以前的帮助页面一致（那里从移出日起算，而不是从送达或丢失起算），与任何 News 公告都不一致。Amazon 自己的页面互相矛盾，读到的 Amazon 文字中没有一篇说明以哪个为准。来源：0e07abc1；RM6。[官方文档]

**RM11** 评级争议针对的是被 Amazon 评为客户损坏（customer-damaged）或有缺陷（defective）的客户退货。它要求商品通过移除订单实际退回，并在索赔中附上不同意评级的说明。来源：EU redline 2024-08-20。[官方文档]

**RM12** 评级争议时限的长度和起算点（移除货件送回卖家之日，或从网络移出之日）因站点、因日期而不同，要读该站点的 removals-claims 页面或工具。对 US，许可的来源给出两种读法，当前有效的那一种没有读到：较早的页面文字是从送达日起 30 天（Hopted copy，Wayback 2026-07-13）；2024-10-23 生效的 US 公告给 "all other removal claims" 从送回日起 60 天，评级争议是否包括在内只是推断（81c3235d）。本资料包别处记下的一个较新的 US 实时页面读法，来自一条 2026-11-10 已关闭的途径，2026-11-13 无法通过许可的途径确认。数值和其他站点见 *Values that move*。来源：Hopted copy；81c3235d；EU redline 2024-08-20；d8f9a56c；均为 2026-11-13 读。[官方文档；评级包括在 "all other" 中为推断；划除为命令核实]

**RM13** 已弃置的商品不能成为评级争议的对象，因为评级争议需要商品被退回。自动弃置或强制弃置可能在卖家行动之前就断掉这条路。来源：RM11；stock pack D7、D8；卖家帖子 8299f3f0。[从官方文字推断]

**RM14** Amazon 对移除索赔要求的材料清单：移除订单 ID；带有效追踪或送达证明的货件 ID（shipment ID）；ASIN/FNSKU 和数量；LPN；商品、商品包装、外箱和运单标签的图片；评级争议还要一段说明。来源：EU redline 2024-08-20（US copy 中没有标签图片这一项）。[官方文档]

**RM15** Removal Shipment Detail 没有 shipment-id 列，也没有送达日期。Amazon 索赔要求的货件 ID，不在读过的任何 SP-API 报告里。来源：FBA Reports 页面（2026-10-13）。[官方文档；"没有"一点通过读列清单命令核实]

**RM16** 外箱、标签和商品的照片只能在开箱时拍。Seller Support 曾要求提供每件商品拆箱后、带 LPN 标签的照片。来源：Mr Prime（2026-10-01）；卖家帖子 da0a8dbe（2025-06-25）。[从业者观点]

**RM17** 中国的从业者把连续的开箱视频当作核心证据。读到的 Amazon 文字中没有一篇提到视频。来源：环至美物流（2025-06-04）；搜狐（2025）。[从业者观点；"没有提到"为推断]

**RM18** 客户下单之前的移除索赔按采购成本（sourcing cost）估值；移出时已不可售的商品按 "a reduced estimated cost" 估值。在 US、UK、Japan 和 Canada（中文）文本中，redline 都划掉了移除索赔原先的 "estimated proceeds" 一句。US 2024-12-18 和 UK 2024-12-11 的文本把基准写作 "manufacturing cost"；US 2025-02-24 和 JP 文本写作 "sourcing cost"。JP 文本（截至 2025-02-19）还提到 IDR 门户上的 *Manage Your Sourcing cost* 页面，以及 "After April 1, 2025" 起对 Amazon 估值的定期更新。来源：2024-12-11 至 2025-02-24 的 Amazon 政策 PDF（JP 于 2026-11-13 重读）；US 生效日期见 finance pack P-ref-14。[官方文档；划除为命令核实]

**RM19** 已撤回。原因：单件赔付上限和估值争议时限归 value-and-reversals 管（VR29 和 VR20）；本文件读到的 JP 内容已在 *Notes for other files of this pack* 中移交过去。

**RM20** Removal Order Detail 的粒度是 订单 × SKU × disposition，含申请、取消、已弃置、已发出和处理中的数量，以及费用。Removal Shipment Detail 的粒度是 货件 × SKU，含承运人和追踪号，不含取消和已弃置的商品。两份报告都需要 Pricing 或 Amazon Fulfillment 角色，并且只能通过请求生成。来源：FBA Reports 页面。[官方文档]

**RM21** Amazon 没有公布 `order-type`、`order-status`、`order-source` 或 `disposition` 的取值集合。从业者报告的取值有：Return / Disposal / Liquidations（还有 Donation）；Pending / Completed / Cancelled（拼写不一）；Sellable / Unsellable。来源：FBA Reports 页面；GorillaROI；SellerSpace；InventoryLab。["没有公布"为官方文档；取值为从业者观点]

**RM22** 两份移除报告都没有站点或 marketplace 列。ERP 反映，在 NA 和 EU 统一账户中，它们分不清一笔移除属于哪个站点。来源：FBA Reports 页面；Lingxing；SellerSpace。[官方文档；从业者观点]

**RM23** 一个移除订单可能分成很多个包裹，从多个运营中心发出，历时数周；Amazon 没有给出固定的处理时间，某个订单的实际跨度要从它自己的 `request-date`、`shipment-date` 和 `last-updated-date` 读出。证据：Amazon 员工（US，stock pack E-R2）："typically take 10 to 14 business days … may increase to 90 days or more during peak removal periods … allow an additional two weeks for the carrier"；PrepVia（2026-08-25）：一个 600 件的移除 "can arrive as a dozen boxes over five weeks, from four different fulfillment centers"。[官方文档；从业者观点]

**RM24** 一个移除订单可能显示 "Completed" 并已收费，而其中一些追踪号从未有过移动。来源：卖家帖子 d804ff56（2025-06-13）。[从业者观点]

**RM25** Amazon 会取消移除订单中无法移除的商品，例如与待处理客户订单绑定的商品。被取消的商品留在 Amazon 网络中，或者已经卖出。来源：Jameson_Amazon 3ead5335（2024-11-12）；PrepVia。[官方文档；从业者观点]

**RM26** 移除费和弃置费现在按件入账，每件商品移出或弃置时入账一次；改变之前，是整个订单完成时才入账。改变的日期因站点而不同，要读各站点的 News 公告。证据：US "Effective March 1 … new orders created on or after March 1"（News 2f4edad8，marketplace 字段为 US，文章 2026-01-29，由 2026-02-15 修订）；UK "Effective from May 1, 2026"（News 862f270b，https://sellercentral.amazon.co.uk/seller-forums/discussions/t/862f270b-81cd-4d78-8a02-7b95156040e6，2026-04-09 发布，marketplace 字段为 UK）。两篇都是 2026-11-13 读。来源：这两篇公告；stock pack P-holding-costs-30。[官方文档]

**RM27** 按件收费之下，如果某个订单和 FNSKU 的移除费或弃置费找不到对应的已发出或已弃置商品，这笔费用在 Amazon 公布的规则里没有依据。来源：RM26。[推断]

**RM28** 政策排除以下商品：应卖家要求弃置的、Amazon 行使某项权利而弃置的、待弃置的。从业者则主张，Amazon 未经请求弃置的商品可以获得赔付。两者说法不一致。来源：政策 PDF 2024-12-18；Seller Labs（2026-03-18）；Seller Investigators。[官方文档；从业者观点]

**RM29** 清算买家发现的损坏或短少，以 `RemovalShipmentAdjustmentEvent` 的形式回来（对该移除订单的负 `RevenueAdjustment`），而不是以赔付的形式。清算销售以 `RemovalShipmentEvent` 入账，其 `TransactionType` 为 `WHOLESALE_LIQUIDATION`。来源：financesV0.json（commit db2936aa）。[命令核实]

**RM30** `listTransactions` 通过关联标识 `REMOVAL_SHIPMENT_ITEM_ID` 链接移除明细行。Finances v0 通过 `MerchantOrderId`（即移除订单 id）和 `RemovalShipmentItemId` 链接。来源：finances_2024-06-19.json、financesV0.json。[命令核实]

**RM31** 从业者报告，移除赔付的原因（reason）为 `REMOVAL_ORDER_LOST` 和 `REMOVAL_ORDER_DAMAGED`。Amazon 没有公布原因清单。来源：Synder；Lingxing OpenAPI doc；finance pack P-ref-19。[从业者观点]

**RM32** 移除记在 ledger detail 的 `VendorReturns` 事件类型下。来源：FBA Reports 页面列出了 `VendorReturns`，并说 ledger 显示 "removals"。[推断]

**RM33** 移除索赔要求 ASIN 在索赔时符合 FBA 限制。有卖家报告：一笔已受理的移除索赔，后来因该 ASIN 被认定为禁售而停用，遭到拒绝。来源：政策的资格清单；卖家帖子 dd5bdcce（2025-05-24）。[官方文档；从业者观点]

**RM34** 有卖家报告，在提交了几次移除丢失赔付请求之后被暂停账户（2019）。Amazon 关于"研究不足、过早或大量请求"的行为规则归 filing-and-conduct 管（FL11）。来源：卖家帖子 e93106ad（2019-01-09）。[从业者观点]

**RM35** 没有任何 SP-API 操作可以发起移除索赔、上传索赔证据、取消移除订单，或对危险品分类提出异议；读取已提交的案例归受限的 Support API（见 sp-api-claims-surface SU8、SU10、SU12）。来源：db2936aa 的模型；stock pack S17。[命令核实]

**RM36** 一些中文指南把帮助页面的 "no sooner than 14 days"（不早于 14 天）误译成了"14天内提交"。来源：百运网 2025-04-05，对照英文页面文字。[通过比对命令核实；来源为从业者观点]

**RM37** 2026 年仍有许多从业者页面写 15–75 / 60 天，另一些写 15–135 / 120。两组都没有注明站点。来源：PrepVia、Mr Prime、ReclaimHQ；SellerSprite、Olifant、Marketplace Officer。[从业者观点]

**RM38** 对 Amazon 归为不可配送危险品（unfulfillable dangerous goods）的商品，Amazon 可以弃置，并以 Business Solutions Agreement 为依据；资格原因代码要求卖家在通知后规定的工作日数内联系 Seller Support。天数见 *Values that move*。来源：`FBA_INB_0015`，db2936aa 的 `fbaInbound.json`；帖子 ebd40f57（2024-08-02）中转述的 Seller Support 文字。[官方文档；命令核实]

**RM39** 根据 Australian Business Solutions Agreement，如果 Amazon 合理判断存在安全、健康或责任风险，可以立即弃置不合格商品（Unsuitable Unit），卖家 "deemed to have consented"；其他情况在通知期之后弃置；所有权转给 Amazon，Amazon 可以保留任何所得。本轮没有读其他站点的协议。来源：AU BSA PDF，2024-06-12 创建，F-7.2、F-7.3、定义部分（2026-11-13 读）。[官方文档]

**RM40** 读到的 Amazon 文字中，没有一篇让危险品分类后被弃置的商品可以获得赔付，包括卖家认为分类错误的情形：政策排除不符合 FBA 商品限制的商品，也排除 Amazon 行使某项权利而弃置的商品；转述的 Seller Support 文字说，这类商品 "may be subject to disposal without reimbursement, even if they have not been previously identified by Amazon as hazardous materials"；员工把 DG 项目批准后的立即弃置称为 "the correct actions"（2026-08-10）。卖家按丢失和损坏政策申请赔付，没有读到结果。来源：US 政策 PDF 2024-12-18；帖子 ebd40f57、978f97fe、29f8a8cd（2026-11-13 读）。[官方文档；分类错误的情形是从"没有文字"推断；卖家的申请为从业者观点]

**RM41** Amazon 指明的、针对危险品分类的申诉方式是复审：在 Amazon 规定的时间内提交安全数据表（safety data sheet）或豁免表（exemption sheet），否则商品被弃置，费用由卖家承担。复审在弃置之前进行；没有读到弃置之后的途径。来源：Michelle_Amazon（2025-06-06，帖子 5c1c2d65）；ebd40f57 中的 Seller Support 文字；上传工具见 sell.amazon.com 博客（2025-01-04）。[官方文档；"弃置后无途径"为推断]

**RM42** 卖家报告：ASIN 被归为危险品期间，移除订单无法创建或会失败，因此商品可能还没离开就被弃置。来源：帖子 ebd40f57（2024-08-02）、cb7207be（2025-12-04）。[从业者观点]

**RM43** 滞留商品（stranded units）的移除，一旦商品离开，就和其他移除一样，适用 removals 页面的范围、时限和证据要求；按滞留设置弃置、或没有设置而被弃置的，落入政策的排除类别。滞留本身归 stock pack 管（S1 到 S8，stranded.md）。来源：§ A、§ I；stock pack S3、S15。[从政策措辞推断]

**RM44** removals 页面的范围句覆盖的是送往卖家退货地址途中的商品；清算订单上的商品是送往清算商的，所以按字面这句话不覆盖它们；读到的 Amazon 文字中，没有一篇指明可以为"到达清算商之前丢失的清算商品"或"低于一般回收率的所得"索赔。来源：范围句（§ A）；Topher_Amazon 6fee30d4（2025-06-23）；stock pack S19。[从措辞和"没有文字"推断]

**RM45** US 的清算付款事件不带数量也不带 SKU（`FBALiquidationEvent`：`PostedDate`、`OriginalRemovalOrderId`、`LiquidationProceedsAmount`、`LiquidationFeeAmount`）；每个 FNSKU 的清算件数，要从 `TransactionType` 为 `WHOLESALE_LIQUIDATION` 的 `RemovalShipmentEvent` 行读出，再按订单 id 与 Removal Order Detail 关联。来源：db2936aa 的 financesV0.json；FBA Reports 页面。[命令核实]

**RM46** 一份日本站的英文 redline 写明：移除索赔按采购成本（sourcing cost）估值，IDR 门户上有 *Manage Your Sourcing cost*，2025-04-01 之后定期更新估值。这与 value-and-reversals 的 VR16（JP 没有来源）有关。来源：JP redline，PDF 2025-02-19 创建，"as of 02/19"（2026-11-13 重读）；站点是从 JPY 上限、"consumption tax" 和 G/09 路径读出的。[官方文档；站点为推断]
