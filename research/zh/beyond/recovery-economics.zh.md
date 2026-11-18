# recovery-economics.md 立场中文读本

**EC1** 已撤回。理由：服务商的收费模式归 finance pack 管（P-tool-17 和 P-ref-31）。本次阅读新增的内容，已放在 *Corrections to other packs* 里，交给 finance pack。

**EC2** 已撤回。理由：服务商的条款不是 Amazon 的规则。"宣传费率与合同费率不同"的证据，已移到 *Corrections to other packs*，作为对 P-tool-17 的补充；§2 是证据。

**EC3** 已撤回。理由：合同条款不是 Amazon 的规则。这些内容留在 §2 作为证据，并提供给 finance pack 的工具参考。

**EC4** 一次审计还能索赔多少，受卖家所在站点每类索赔的时限约束，不受服务商回溯期（look-back）约束。服务商会宣传回溯期（数值见 *Values that move*）。Amazon 的时限按索赔类别、站点和日期各不相同（见各领域文件；哪篇帖子对应哪个站点，见 fc-lost-damaged 的帖子-站点对照表；finance P-ref-16）。所以回溯期是否超过时限，取决于索赔类别，也取决于哪条声明管辖卖家的站点。运行时读取：卖家站点显示的 FBA 库存赔偿政策（G200213130），以及该站点最新的 News 帖或员工帖。来源：服务商页面（§2）[从业者观点]；P-ref-16 [官方文档]；这个上限关系是 [推断]。

**EC5** Amazon 2024 年同一标题 *Update on Reimbursement Automation and Eligibility Window to file reimbursement claims* 下的帖子，给出了两个客户退货索赔时限。按"帖子对象标记站点"的读法，这是两个站点各自的规则，不是同一站点的自相矛盾：美国帖（81c3235d）的时限从"after the customer refund or replacement date"起算，上下限与加拿大帖（6605eede）和英国帖（d0fc997e）不同。对美国站，时间上仍有矛盾：2026-08-13 的美国员工帖（0e07abc1）又给了另一个时限。数值见 *Values that move*。今天哪条管辖某个站点，归 customer-returns 管；运行时按 EC4 的方法读取。来源：81c3235d、6605eede、d0fc997e、0e07abc1（2026-11-13 读取）；站点依据 §1(d) 和 fc-lost-damaged 的对照表 [官方文档；站点读法经一个对照样本命令核实，其余为推断]。

**EC6** Amazon 没有公布配送中心丢失率，没有公布无需索赔即赔付的案件比例，也没有公布赔偿总额。找到的所有"应得营收百分比"数字（1%、1–3%、3%、3.5%）都来自追偿服务商或工具厂商，都没有说明方法。来源：2026-11-13 的搜索和 §4 表格 [数字为从业者观点]。"没有公布"是本席位在所列搜索范围内的结论，是对 finance pack P-ref-31 的延伸 [推断]。

**EC7** 服务商的数字如果早于 2024-10-23（时限缩短）、2024-11-01 或 2025-01-15（自动赔付）、或 2025-03-31（按采购成本估值），衡量的就是一个 Amazon 后来已经改变的资金池。例子：亿数通 2020 年经雨果网发布的"1000W→10W"，以及 GETIDA 的"1% to 3%"（约 2023 年）。这些日期见 finance pack P-ref-13、P-ref-14 和 P-ref-16 [官方文档]。来源：§4 表格 [从业者观点]；这个解读是 [推断]。

**EC8** 对于在客户下单前丢失或损坏的单件，2025-03-31 估值变化带来的单件降幅是 1 − 采购成本 ÷（售价 − 费用）。从业者报告降幅为 50–75%（Nova Data："$18.50 to $6.20 per unit"；AMZ123 2026-11-02）。变化生效前受访的卖家预测降幅为 42%、50% 和 70%。运行时读取：卖家的成本（Manage Your Sourcing Cost；无 API），以及 §1(c) 所列的售价和费用。来源：finance pack P-ref-14 [官方文档]；Nova Data；AMZ123 tg6kPptK；Modern Retail 2024-12-20 [从业者观点]；公式是 [推断]。

**EC9** Amazon 发言人称，估值变化的目的是"a more consistent approach as more sellers are using our supply chain services"。发言人还表示"Specific cost data is not shared with any other seller in Amazon's store, including Amazon Retail"。来源：Mira Dix，Modern Retail 引述，2024-12-20 [官方文档，经媒体转述]。

**EC10** 按索赔类别，单件价值取决于丢失发生的时点。下单前的丢失（配送中心丢失或损坏、入库、移除）按采购成本估值（P-ref-14）。客户退货索赔按下单后口径、扣除费用后估值，基数是退款或售价：确切基数在本 pack 内部有争议（见 value-and-reversals VR27 与 customer-returns RT42 的分歧；finance P-ref-40 引用 2024-12-18 的美国 PDF 为"the refund amount or the sales price of the replacement item on the original order minus applicable fees"）。只要下单后价值高于采购成本，一件退货的单件价值就高于一件仓内货。来源：finance pack P-ref-14 和 P-ref-40 [官方文档]；这个比较是 [推断]。

**EC11** SPS Commerce：
- 以约 $210M 收购 Carbon6（Seller Investigators、ChargeGuard）；2025-01-02 宣布；按 2026-06-30 新闻稿于 2025-02-07 完成，按 10-Q 为 "effective February 4, 2025"；"$210.2 million, net of cash acquired"；预计贡献约 $40M 的 2025 财年营收（未复读）；
- 2026-06-30 宣布已完成出售其 3P Revenue Recovery 业务，现金 $9.5M，估计亏损约 $20M（新闻稿）或 $23.5M（Q2 电话会）；新闻稿给出的理由是聚焦 1P；
- 在 Q4 2025、Q1 2026 和 Q3 2026 电话会上提到了 Amazon 的政策变化和抽成（take-rate）模式。

来源：SPS 新闻稿 2026-06-30；SEC 10-Q（截至 2025-09-30 的季度）；Nasdaq / RTT News 2025-01-02；Motley Fool Q4 2025 文字稿 2026-02-12；MarketBeat via Yahoo 2026-04-30；Investing.com Q3 2026 文字稿 2026-10-29 [从业者观点：一家服务商的自述；延伸 finance pack P-ref-32]。

**EC12** 已撤回。理由：其实质内容（每位客户每年追回约 $11,500）是本席位对 SPS 数字做的除法，已移到 *Seat's own*。SPS 的原始数字本身仍留在 EC11 和 §3。

**EC13** 已撤回。理由：其实质内容（每年追回约 $960 或更少）是本席位根据 SPS 收取的一项费用做的推断，已移到 *Seat's own*。相关引语留在 §3。

**EC14** SPS 在 Q3 2026 说损害追偿收益的"short shipment"和"redispute"变化，涉及的是供应商发给 Amazon Retail 的货（1P vendor 追偿），不是 FBA 卖家的索赔。它们不是关于 FBA 赔偿的证据。来源：Investing.com Q3 2026 文字稿（Chad Collins："when one of our suppliers makes a short shipment to Amazon"）[从业者观点]；范围判断是 [推断]。

**EC15** 在客户退货上，服务商说法互相矛盾：
- GETIDA 称 Amazon 在 64 天内自动赔付 98.5% 的 FBA 客户退货问题，数据来自"over 2 million"个数据点；
- sellerboard 称未退回的客户退货"almost entirely seller-initiated"。

Amazon 的帖子说"almost all … customer returns cases"会主动赔付。对某个站点，这个比例在运行时从 `GET_FBA_REIMBURSEMENTS_DATA`（Pricing 或 Amazon Fulfillment）读取：看客户退货行（卖家报告中见到的 `reason` 值是 `CustomerReturn`；Amazon 没有公布 `reason` 值清单，P-ref-19、P-ref-35），区分 `case-id` 为空和有值。把这些行与 Finances `listTransactions`（Finance and Accounting）里的退款、以及 `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`（Amazon Fulfillment 或 Pricing）关联，可以看出多少退款是未经申请就赔付的，多少根本没赔。来源：finance pack P-ref-31（GETIDA）、P-ref-13、P-ref-20；sellerboard 2026-07-14 [从业者观点；P-ref-13 为官方文档]。

**EC16** 一位卖家测得 2023 年入库准确率为 99.943%：发出 123,228 件，少收 70 件，口径是预期收货对比实际收货，多收的不计。另一位卖家报告"since May 2023"丢了"over 1300 units"（2023-08-25），后来又报告"the 1500 units Amazon lost on FC transfer"（2024-01-30）。这些是单个卖家的计数，不是 FBA 的比率。来源：sellersasksellers.com，ASV_Vites 2024-01-30；packetfire 2023-08-25 和 2024-01-30 [从业者观点]。

**EC17** 追偿计算器使用的丢失率输入没有来源：
- ecomcalctools：配送中心丢失为吞吐价值的 0.3–1.0%（"Documented US FBA range"；"Loss rates are documented US FBA defaults"）；仅在其示例计算中，入库丢失为入库价值的 0.5–1.0%，调整为在库价值的 0.05–0.15%；
- 船长BI："会有1%-3%的出错率"。

卖家自己的比率在运行时读取：从 `GET_LEDGER_DETAIL_VIEW_DATA`（Amazon Fulfillment）读调整事件对比收货，从 Fulfillment Inbound v0 `getShipmentItems`（`QuantityShipped` 对比 `QuantityReceived`，Amazon Fulfillment）读取。来源：ecomcalctools（2026-06-17）；m.captainbi.com [从业者观点]。

**EC18** 没有找到关于 FBA 丢失、损坏或赔偿比率的同行评审研究或行业研究。最接近的已发表研究衡量的是别的东西：
- 门店库存记录不准确（DeHoratius & Raman 2008：369,567 条记录中 65% 有误）；
- 门店损耗（NRF NRSS 2023：FY2022 销售额的 1.6%，大部分是盗窃）；
- 线上退货率（NRF / Happy Returns 2025：美国线上销售额的 19.3%）。

没有一项衡量的是 Amazon 配送中心。来源：如上所列 [研究文献；DeHoratius & Raman 仅读了摘要]。

**EC19** 一笔应得金额按类别由这几项构成：经过该环节的件数 × 发生率 × 单件价值 × Amazon 未主动赔付的比例。然后时限再截掉已经不能索赔的部分。每项输入都是卖家自己的，运行时从 §5 参数表所列的读取来源获得。这是本席位基于 P-ref-13、P-ref-14 和 P-ref-40 建立的模型 [推断]。

**EC20** 已撤回。理由：其实质内容（$60–$6,850 的区间和 $635 的中间情形）依赖本席位自选的发生率，已和 §5 一起移到 *Seat's own*。EC19 保留模型的形式。

**EC21** FBA 费用赔偿申请有一个时限，从被争议的扣费日期起算，Amazon 给出了两个：一个针对逐项费用（与 ASIN 或 FNSKU 挂钩，通常是重量或尺寸错误：配送费、客户退货费、月度仓储费和长期仓储费），一个更长的针对非逐项费用（移除或弃置订单费、预处理和贴标）。所以一个尺寸测错的 SKU，卖家还能追回的是单件多收金额乘以逐项时限内被收费的件数；而非逐项错误可以追溯得更远。这两个时限归 fee-overcharges 管（见 fee-overcharges FE9）；数值见 *Values that move*。运行时读取：站点显示的 *FBA fees reimbursement policy: Weight and dimensions*（GL7U4JFSDXUTQAJ），以及该站点最新的争议扣费员工指南；扣费日期取 `listTransactions` 的 `postedDate`。来源：FE9；Roberto_Amazon ce0bea71（美国，2026-04-17，2026-11-13 复读）[官方文档]；推论是 [推断]。

**EC22** 服务商公布的成功率：
- GETIDA："more than 90% of claims we open"；"63% of previously unsuccessful claims"；"roughly 40% of claims require Proof of Inventory Ownership or Proof of Delivery"；
- Seller Investigators："95.9%"，经 AmpliSell 转述；
- Nova Data：有文档时"90%+"，无文档时"Under 40%"。

都没有说明分母或方法。来源：getida.com/pricing；AmpliSell 2026-11-09；Nova Data 指南 [从业者观点]。

**EC23** 没有找到按佣金代为索赔、且有当前公开费率的中文工具或服务。存在一个中文"0 佣金"索赔助手：船长BI（"船长索赔0抽佣"；它的对比表把其他服务列为"25% 佣金"），当前版本只覆盖配送中心丢失或损坏。亿数通（2020）提供过索赔工具，但所读文章没有写它的收费。ERP（领星、积加、赛狐、易仓）免费额外估算，由卖家自己提交。马帮和店小秘没有索赔服务。来源：m.captainbi.com/amz_claim.html；cifnews 81125；mabangerp news 4114；finance pack P-ref-39 [从业者观点]。

**EC24** 中文索赔助手回溯固定的时间段（船长BI："首次索赔可追溯到18个月之前"，即首次索赔回溯一个给定时长；数值见 *Values that move*）。这段时间里超出 Amazon 对该类别所设时限的项目不能索赔。时限按 EC4 的方法读取。来源：m.captainbi.com [从业者观点]；推论是 [推断]。

**EC25** 自己提交、付一定比例给服务商、用订阅或 ERP 工具、录入采购成本，还是放弃某一类，是卖家自己的选择。§6 把这些选择并排列出，并写明每个选择改变什么：佣金、时间、由谁提交、在成本获批后发放的、符合条件的下单前赔偿的估值基础（value-and-reversals VR8；被拒的录入见 VR9，不可售单位见 VR25），以及时限到期后资金作废。来源：§2 服务商页面、SellerHow 2026-08-16 [从业者观点]；P-ref-14 [官方文档]。

**EC26** 卖家自己的历史赔付记录（Amazon 按类别、按是否立案赔了多少）在 `GET_FBA_REIMBURSEMENTS_DATA` 里。按 `reason` 汇总 `amount-total`，把 `quantity-reimbursed-cash` 与 `-inventory` 分开，并通过 `original-reimbursement-id` 冲抵撤销。需要 Pricing 或 Amazon Fulfillment 角色。这是唯一对该站点成立的"追偿数字"。来源：finance pack P-ref-17、P-ref-19、P-ref-20 [官方文档]；这种用法是 [推断]。

**EC27** Amazon 无需索赔即赔付的比例，是卖家所在站点的事实，不是所有站点通用的一个数字：一类索赔还剩多少要靠卖家去索，取决于 Amazon 在那个站点是否主动赔付。对英国仓内丢失的货，Amazon 自己的英国帖子说法不一（fc-lost-damaged FC5：英国自动赔付帖 d0fc997e，对比英国员工帖 2f44617d 说这类索赔要手动），所以对英国站，仓内丢失这一类可能整件丢失价值都要靠索赔。运行时读取：在该站点自动赔付日期之后，该站点 `GET_FBA_REIMBURSEMENTS_DATA`（Pricing 或 Amazon Fulfillment）里是否出现 `case-id` 为空的 `Lost_Warehouse` 和 `Damaged_Warehouse` 行，对比库存流水中的丢失和损坏调整（`GET_LEDGER_DETAIL_VIEW_DATA`，Amazon Fulfillment）。来源：d0fc997e、2f44617d（2026-11-13 读取；站点依据 §1(d)）[官方文档]；把 `case-id` 为空读作"主动赔付"是一种解读（P-ref-20）[推断]。

**EC28** 所读页面中，没有一页给出卖家以前能追回的金额在 Amazon 2024–2025 变化后还剩多少比例可以索赔。Amazon 没有公布（EC6）；最接近的服务商数字（Threecolts 的"sellers recover 40% of what they're owed"；finance pack 转述的"40% left behind"）没有说明方法或日期基准。对某个站点，这个比例在运行时从它自己的 `GET_FBA_REIMBURSEMENTS_DATA` 读取：按 `reason`、按 `case-id` 为空与有值分别看金额，并比较该站点自动赔付日期和 2025-03-31 之前与之后。来源：§4 表格 [从业者观点]；P-ref-31 [从业者观点]；这种读法是 [推断]。
