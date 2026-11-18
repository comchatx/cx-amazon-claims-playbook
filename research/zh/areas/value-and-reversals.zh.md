# value-and-reversals.md 立场中文读本

对应英文文件：research/areas/value-and-reversals.md（§ 3 Positions，VR1–VR45）。

来源标签对照：[官方文档] = 亚马逊的页面、PDF、News 帖或员工论坛帖；[官方文档，转述] = 卖家引用的亚马逊原文；[命令核实] = 本地核查；[从业者观点] = 从业者的说法；[推断] = 本文推断。

随店铺或年份变化的数值不写在立场里，而是写在英文文件的 *Values that move* 表中，附店铺、日期和来源。

## 规则与历史

**VR1** 2025 年改规则之前，FBA 下单前的丢失（shipment to Amazon、FC operations、removals）按 "estimated proceeds" 估值。做法是：用 18 个月中位价和标价估一个售价，再 "minus referral fees and fulfillment fees"。亚马逊的 redline 把这整段划掉了。来源：R-US、R-UK、R-DE、R-CA、R-JP-EN、R-JP-JA（划线文字，经渲染）。[官方文档]

**VR2** 下单前的丢失，从各店铺文本给出的日期起，按 sourcing cost 估值。2025-02-24 重新生成的 US、CA、UK、DE、FR、IT、ES、US 中文版和 CA 中文版 redline，都写着 "After March 31, 2025" 和 "Manage Your Sourcing Cost"（中文："2025 年 3 月 31 日"、"管理您的采购成本"）。JP 见 VR41。这一条把 P-ref-14/15 扩展到这些站点。来源：R-* PDF（元数据 2025-02-24；US、CA、UK、DE、ZH、CA-ZH 经渲染；FR、IT、ES 只读了文本层，为英文）。[官方文档]

**VR3** 亚马逊的定义在各版草稿间措辞有变。US："cost to source a product from a manufacturer, wholesaler, or reseller, or to produce the item"。英国第一版草稿（2024-12-11）："the cost to acquire, purchase, or produce the item"。英国 2025-02-24 文本改用 US 的措辞。所有版本（含 JP）都把运费、装卸费和关税排除在外。来源：UK 2024-12-11 PDF；R-UK；R-US；R-JP-EN。[官方文档]

**VR4** sourcing cost 估值也适用于 "during inventory replenishment handled by Amazon or on behalf of Amazon to fulfillment centers or non-Amazon buildings in marketplaces where we provide the service" 时的丢失（JP 写作 "lost and damage claims for inventories handled by Amazon or on behalf of Amazon to fulfill shipments"）。来源：R-US 及同批文本；R-JP-EN。[官方文档]

**VR5** 亚马逊的估算基于 "comparable products sold by Amazon, by other sellers, and through other wholesale channels"。从各店铺文本给出的日期起，亚马逊会定期刷新估算；如果卖家已提供的成本受影响，会提醒卖家；受影响的商品显示在 MYSC 的 status 列。来源：R-US；R-JP-EN；KJ_Amazon 2025-04-30。[官方文档]

**VR6** 亚马逊声明，卖家的成本数据 "is not shared with any other seller in Amazon's store, including Amazon Retail"。来源：R-US；R-JP-EN；KJ_Amazon 2025-04-30。[官方文档]

## Manage Your Sourcing Cost

**VR7** MYSC 对每个 FNSKU、每个站点存一个 sourcing cost（有站点下拉框）。它列出 "with planned shipments or current inventory" 的在售 FNSKU。同一条员工帖又说，新 ASIN 要 "fully received and processed" 后才会出现。来源：KJ_Amazon 2025-04-30；Abbie_Amazon 2026-04-10（US 店铺）。[官方文档；2026 年那条帖子里的两句话不一致，两句都列出]

**VR8** 卖家成本获批后，自动用于获批日期*之后发放*的合格下单前赔偿。它不会重估更早的赔偿，也不需要定期重新提交。来源：cd2909d2 帖中卖家转述的拒绝消息（2026-02-22）；Arish_Amazon 2026-02-24；32451dd6 帖中转述的工单回复（2026-05-25）；均为 US 店铺。[官方文档；转述]

**VR9** 亚马逊可以因四条政策理由拒绝卖家提交的成本：异常值；文件伪造或无法辨认；账户涉嫌欺诈或违规；在一次决定后的规定期限内重复提交且没有新信息（JP 把最后一条写作 "frequent cost updates for the same item or a reimbursement amount dispute decision … within the last [period]"）。期限按店铺在 G200213130 上读取（*Values that move*）。提交被拒后，仍按之前批准的金额或亚马逊的估算执行。来源：R-US 及同批文本；R-JP-EN。[官方文档]

**VR10** 系统判为异常值的金额会被自动拒绝，不给上传发票的步骤。亚马逊不告诉卖家发票为什么被接受或被拒。来源：Christine_Amazon 2025-11-25（US 店铺；MYSC，无上传步骤）；Glenn_Amazon 2026-01-15（UK 店铺）。Christine_Amazon 2025-06-04 说的是另一种自动拒绝：重估工具在成本 "significantly exceeds our internal thresholds" 或没有已批准成本时自动拒绝。[官方文档]

**VR11** 亚马逊限制每个 FNSKU 在一个期限内的成本更新次数。次数在运行时按店铺读取 *Manage Your Sourcing Cost* 帮助页（GN655EHATZUVWBC3），或读 Update status 列（"Number of attempts exceeded"）。亚马逊的说法因店铺和日期而不同：一条 Canada 店铺的 Seller Support 回复（转述，2025-03-19），以及 US 店铺的员工帖（2025-11-25 至 2026-02-24）；数值见 *Values that move*。已读来源无法确定次数是随时间改了，还是各店铺不同。[官方文档；转述；矛盾已附店铺和日期列出]

**VR12** 填入的成本必须等于价值证明文件上的数字。不一致本身就是一条拒绝理由（"value mismatch"）。来源：Bryce_Amazon 2025-04-04；cd2909d2 帖中转述的拒绝消息。[官方文档]

**VR13** 亚马逊列出的价值证明字段：
- 文件名称、编号和日期；
- 买方主体名称（与在亚马逊注册的一致）、地址和税号；
- 开票方主体名称、地址和编号；
- 产品代码、描述和数量；
- 单件成本或净值；
- 币种。

接受的文件：制造商发票、批发商发票、采购发票或商业发票；员工还提到零售收据，以及附付款证明的形式发票（pro forma）。格式：PDF、JPG、JPEG、PNG。来源：卖家抄录的 GN655EHATZUVWBC3（d23add81，Canada 店铺，2025-03-19）；Arish_Amazon 2026-02-24；Christine_Amazon 2025-12-01、2026-03-06；Nano_Amazon 2025-06-12。[官方文档；帮助页为转述]

**VR14** 亚马逊规定了价值证明发票的最长时限。该值在运行时按店铺读取 GN655EHATZUVWBC3。两条 US 店铺员工帖给出的值不同（2025-06-12 和 2025-12-01；见 *Values that move*）；两条都没引用帮助页原句，也没有更晚的来源说明哪个是现行的。[官方文档；矛盾已附日期列出]

**VR15** 对自产商品，员工提到：一份写明产品、单件成本和日期的内部成本文件；零部件发票加成本明细；以及开 Seller Support 工单请求人工审核。来源：Christine_Amazon 2026-03-06；Nano_Amazon 2025-06-12。[官方文档]

**VR16** MYSC 在 US、CA、UK、DE、FR、IT、ES 和 JP 都有证据。US、CA、UK 的证据是这些店铺论坛里的员工帖或转述帖，以及政策文本；DE、FR、IT、ES 的证据是 2025-02-24 的 redline；JP 的证据是 2025-02-19 的政策文本（VR41）。JP 门户今天是否显示该页面，未读到。来源：各论坛帖（US、CA d23add81、UK 8033bd61）、R-* PDF、R-JP-EN、R-JP-JA。[官方文档]

**VR17** 一张多产品发票，因为无法单独认出该 FNSKU 那一行而被拒。同一张发票把那一行标出来，通过工单提交后被接受。来源：Eagle Eye，Ivan Raineri，2026-09-12。[从业者观点]

**VR18** 没有任何 SP-API 操作能读写 MYSC，或提交估值争议（见 sp-api-claims-surface SU12；finance P-ref-29）。本文的补充：amzn/selling-partner-api-models db2936a 中，没有任何 model 含 `sourcingCost`、"sourcing cost"、`manufacturingCost` 或 "manufacturing cost"；也没有任何 `operationId` 名称涉及赔偿、争议或成本。单独 grep `sourcing` 只命中无关内容（Orders 的 "Sourcing On Demand"、Inbound v0 的 "item sourcing decisions"、仅限 vendor 的 Data Kiosk `sourcingView` 和 vendor 报告 schema、一个订单变更通知）。[命令核实，2026-11-13]

**VR19** Data Kiosk `analytics_economics_2024_03_15` 提供卖家填写的 `cost.costOfGoodsSold`。亚马逊说它来自 SKU Central 和 Revenue Calculator，不是 MYSC；没有读到任何内容表明两处存的是同一个值。它所需的角色不在卖家应用的角色之内（见 sp-api-claims-surface SU33）。来源：schema 文本，commit db2936a。[字段及其所述来源为命令核实；两者分开为推断]

## 争议

**VR20** 亚马逊为赔偿估值争议设了期限。已读的所有政策文本（US、CA、UK、DE、FR、IT、ES、JP；US 和 CA 中文版）都从赔偿发放时起算；唯一写明重估期限的 News 帖（d8f9a56c，2025-10-15 生效）是发给 Australia 店铺的，从首次索赔时起算。期限长度是按店铺的值，运行时读取卖家店铺显示的 G200213130，以及该店铺最新一条关于索赔期限的 News 帖（*Values that move*）。UK 的文本从 90 天（员工 2024-10-26；PDF 2024-12-11）改成了 60 天（R-UK 2025-02-24），redline 没有标出这处改动。来源：§ 5 中的 PDF；9d4ff2a6；d8f9a56c；2025-04 至 2026-06 的员工帖（US 店铺）。[官方文档；News 帖的店铺为命令核实]

**VR21** 员工给出两条估值争议途径。(1) Get Help 下的自助流程 "Dispute a reimbursement claim"（Sofi_Amazon 和拒绝消息提到它；Christine_Amazon 2025-06-04 提到一个位于 help-hub solution `WF_fba_reimbursement_revaluation` 的 "reimbursement re-evaluation tool"；两者是同一流程属推断，该 URL 未读）。它把已批准的 MYSC 成本用于按 "sellable" 赔付的下单前事件，含 missing-from-inbound。(2) Get Help 下的 "Submit a reimbursement claim dispute"，可上传文件，由人工审核。重开工单是第三条路，员工说它不是同一流程。均出自 US 店铺的帖子。来源：Christine_Amazon 2025-06-04 和 2025-11-25；Sofi_Amazon 2026-06-05；cd2909d2 帖中转述的拒绝消息。[官方文档]

**VR22** 政策的重复提交规则同样适用于 "reimbursement amount dispute[s]"，不只是成本更新。期限按店铺在 G200213130 上读取（*Values that move*）。来源：R-US 及已读的每份 redline，含 R-JP-EN 和 R-JP-JA。[官方文档]

**VR23** 一笔赔偿按估算付款后，成本才获批；卖家用工单要求调整，被拒，理由是 "Since the reimbursement was processed before your sourcing cost was approved"。员工改指自助争议途径，须在争议期限内（VR20）。来源：转述的工单回复 2026-05-25；Sofi_Amazon 2026-06-05（32451dd6 帖，US 店铺）。[官方文档；转述]

**VR24** 时间上的陷阱。尝试次数锁（VR11）导致的拒绝，可能比从赔偿起算的争议期限（VR20）更久。一个有日期的 US 案例中，期限在 11/16 截止，而下一次允许更新是 11/23。来源：Seller_T7bkq3pJHibSr，2025-10-23。[从业者观点]

## 不可售、下单后、单件上限

**VR25** 下单前在丢失、损坏或移除时已不可售的商品，按 "a reduced estimated cost" 赔付（JP：只对不可售商品的移除索赔这样写）。亚马逊可能要求提供文件来确定这个值，没有页面给出折减比例。来源：R-US 及同批文本；R-JP-EN、R-JP-JA。[官方文档]

**VR26** 下单后在丢失或损坏时已不可售的商品，按 "the discounted sale price of that order minus applicable fees" 赔付（UK/DE："and VAT"）。这句话是在 US、CA、UK、DE 的 2024-12/2025-02 redline 中新插入的；2025-02-19 的 JP 文本没有这句。来源：R-US、R-UK、R-DE、R-CA；R-JP-EN、R-JP-JA。[官方文档]

**VR27** 客户退货索赔的估值依据，要读卖家店铺显示的 G200213130；2026-11-13 无法通过允许的途径读到线上页面。redline 文本：US、CA、UK、DE 的 redline（2024-12 至 2025-02，经渲染）和 R-JP-EN 划掉 "refund amount or the … of the replacement item"，插入 "sales"，读作 "the sales price on the original order minus applicable fees"（UK/DE："and VAT"；JP："and consumption tax"）；R-ZH 和 R-CA-ZH 只插入 "销售"。customer-returns 文件对线上 US 页面的读法（退款或换货价依据，RT42）是通过帮助中心的内容调用读到的，该途径已于 2026-11-10 被 office 关闭；本文不采用它，这也是现行依据不作定论的原因。来源：经渲染的 R-US、R-UK、R-DE、R-CA、US 2024-12-18 PDF、UK 2024-12-11 PDF、R-JP-EN、R-ZH、R-CA-ZH。[redline 部分为官方文档；线上文本未读]

**VR28** 数据上的陷阱。亚马逊带 redline 的政策 PDF 在文本层里保留了划线文字。直接提取文本会把新旧措辞混在一起，只有渲染后才能看出哪句是现行的。[命令核实：同一批 PDF 渲染后，P-ref-40 引用的那几句上有划线]

**VR29** 亚马逊对单件赔偿设了上限，上限的金额和币种因店铺而不同。运行时读取卖家店铺显示的 G200213130；没有任何操作返回它。各店铺数值见 *Values that move*。一件价值更高的商品按上限赔付，是按政策付款。来源：§ 5 中的每份政策文本；9d4ff2a6（UK 员工）。[官方文档]

## 读报告

**VR30** `GET_FBA_REIMBURSEMENTS_DATA` 没有估值依据、当时生效成本、上限或店铺的列。要找出低估的行，只能拿 `amount-per-unit` 与别处读到的依据比较：MYSC（Seller Central）、卖家自己的成本，或订单依据（VR27）。来源：亚马逊 *Report Type Values – FBA* 页面（18 列，2026-11-13 读取）；P-ref-19；VR18。[根据官方列推断]

**VR31** 一行应采用的依据取决于其 reason 类别。仓库、入库和移除类 reason 用 sourcing cost；客户退货和客服类 reason 用订单依据（VR27）。这一归类来自政策的两个标题和 P-ref-35 的 reason 值。`Lost_Outbound` / `Damaged_Outbound` 归哪边未读到；该索赔类型归 customer-returns。[推断] 这种分组是本席位自己的读法，不是发现（见 *Seat's own*）。

**VR32** 与一条下单前赔偿行比较的成本，是其 `approval-date` 时生效的成本，不是今天 MYSC 的值。MYSC 只显示当前值和最后一次更新。来源：VR8；53eb4da7 帖（Last-updated 列）。[推断] 用 `approval-date` 定位是本席位自己的读法（见 *Seat's own*）。

**VR33** 有卖家报告，一件与原物明显不同的客户退货经移除流程赔付，按 sourcing cost 付款，约为 "roughly 30-60% of actual buy cost"，而不是按订单依据。来源：Seller_6xcCLJodrIRK8，2026-08-05，a2c0b1c6 帖（US 店铺）；customer-returns 文件从另外两个帖子报告了 US 错发商品索赔的同样情况（见 customer-returns RT17）。[从业者观点]

## 补货与现金；撤销

**VR34** 亚马逊可以用 "with a new item of the same FNSKU" 替换来处理有效索赔，而不付钱。这样的行移动的是件数，不是钱。来源：政策（所有版本，含 JP）；P-ref-17。[官方文档]

**VR35** 已撤回。理由：一个 2018 年的卖家帖、没有亚马逊回复，不足以支撑一条立场；其中的报告作为证据留在 § I(b) 和待解问题 5。

**VR36** 亚马逊政策写明撤销赔偿的两个理由：赔付有误，或已赔商品被找到并退回库存。政策没有规定时限，也没有规定撤销金额的规则。来源：所有 redline，英文、中文和日文（"Amazon は販売事業者のアカウントに適用された返金額を回収する権利を保持します"）。[官方文档]

**VR37** 对撤销有疑问的卖家，员工让其去查库存流水（看商品是否加回库存），并联系 Seller Support。没有员工帖提到撤销的争议期限。来源：TaylorR_Amazon 2024-11-29；Micah_Amazon 2024-02-20；Nano_Amazon 2025-03-20；Jameson_Amazon 2025-01-17（均为 US 店铺）。[官方文档]

**VR38** 数据上的陷阱。卖家报告撤销发生在付款后 5 到 16 个月；其中有一件在 FC 被判 "damaged" 的商品，后来被撤销赔偿并作为可售加回；还有批量撤销（2,350 件），却看不到任何一件退回库存。来源：0f7ea6ce、e23102e6、af89a498、9742b13e 帖（均为 US 店铺）。[从业者观点]

**VR39** Finances v0 的 `ReimbursementClawback` 是仅限 India 的 Easy Ship 值，不标记 FBA 撤销。FBA 撤销表现为报告 reason `Reimbursement_Reversal`，以及 finance 包所载的结算描述（P-ref-33）。来源：financesV0.json `AdjustmentType` 描述。[命令核实]

**VR40** 流水代码 N 和 O 移动件数的原因是 "because you received an Amazon reimbursement" 或 "because Amazon has reimbursed you for them"。所以加回件数的流水行不一定是实物找到：N 或 O 行是与赔偿相关的所有权变动，F 行才是找到。来源：stock 包 W30（亚马逊的原因表）。[官方文档，由 stock 包持有；对应关系的读法为推断]

## 日本、语言、币种、跨境证明

**VR41** 亚马逊 JP 政策（英文和日文文本，PDF 创建于 2025-02-19，"as of 02/19"）规定：shipment-to-Amazon、移除和 FC-operations 索赔按商品的 sourcing cost（"原価"）赔付；卖家在 IDR 门户的 "Manage Your Sourcing cost" 页面（"原価の管理"）填写；否则用亚马逊的估算；估算从其自己的日期起刷新；拒绝理由相同，有重复提交规则；单件上限以日元计；估值争议期限从赔偿起算（数值见 *Values that move*）。这就政策文本解决了待解问题 3 的 JP 部分，并与 removals-disposals RM18 一致。来源：R-JP-EN、R-JP-JA（2026-11-13 渲染）。[官方文档]

**VR42** 同一店铺、同一日期的亚马逊文本，在客户退货依据上可能因语言而不同：R-JP-EN 划掉了退款金额和换货价格，而 R-JP-JA 保留两者，并在旁边加上原订单售价（"元の注文の販売価格、返金額または交換商品の価格から、適用される手数料と消費税を差し引いたもの"）。来源：R-JP-EN、R-JP-JA，逐字符划线和颜色核查。[命令核实]

**VR43** 已读的亚马逊文本都没有说明：在 Pan-European 调拨中、EFN 下他国 FC 中、或经 Remote Fulfillment 售出的 US 库存中丢失的商品，赔偿记入哪个店铺、用什么币种，以及其估值在哪个店铺争议。数据中有：报告每行的 `currency-unit`，没有店铺列；Finances v0 `AdjustmentEvent` 有 `StoreName`，每个金额有 ISO 4217 `CurrencyCode`，没有 marketplace id。来源：*Report Type Values – FBA*；financesV0.json（db2936a）；其他跨境费用见 finance 包的 reconciliation.md；sp-api-claims-surface SU24。[字段为官方文档和命令核实；其余为未找到]

**VR44** 亚马逊的价值证明清单要求买方是 "your business name registered with Amazon"，并要求写明交易币种；员工说发票上的公司名 "must exactly match your Amazon registration"。已读的亚马逊文本都没有规定语言，也没有对中国大陆增值税发票（发票）、1688 订单收据或支付平台收据作出规定。如果发票买方是与销售账户不同的主体（例如香港或大陆的采购公司为一家 US LLC 采购），发票上的买方就不是注册的那家公司。来源：转述的 GN655EHATZUVWBC3（d23add81）；Christine_Amazon 2025-12-01。[官方文档；转述；关联公司情形是根据字段推断]

**VR45** 中国从业者报告：中文发票被拒、英文发票被接受；并把以下几种成本证明并列提出：可在国家税务总局查验网站查验的大陆增值税发票（专票或普票）；供应商开具的、以店铺币种计、带供应商税号的英文商业发票；供应商或货代开具的商业发票或形式发票；合同加付款记录和盖章收据；报关单据（一个 Canada 店铺案例中报关单据被认为不清晰而被拒）。来源：贾科斯，易销AI，2025-08-07（Canada 和 Germany 案例）；AMZ123 跨境小蚂蚁 2024-12-27。[从业者观点]
