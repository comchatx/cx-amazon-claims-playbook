# research/areas/fee-overcharges.md 中文解读

本文件逐条解读英文文件中编号为 FE 的立场，顺序和编号与原文一致。来源标签译为：官方文档、命令核实、推断、从业者观点。原文没有已撤回的立场；原文“Seat's own”一节写明，没有任何立场建立在本席位自己的选择上。FE1 的分类方式、第 1–15 节的顺序、FE34 表格的列，是本席位对有来源事实的排列，只是版式，不是结论，不作为规则进入任何 skill。

**FE1**
**定义。** 在本领域，费用多收是指：亚马逊对某个单件、某票货件或某个期间收取的费用，其依据不被亚马逊自己的规则支持。类型有：
- 测量或尺寸分段错误（配送费、仓储费、超龄附加费、退货费、移除费和入库配置费都依赖它）；
- 销售佣金（referral fee）类目错误；
- 符合条件的费率没有被套用（低价 FBA、合规的入库配置选项）；
- 亚马逊说会退还的费用（亚马逊造成入库延迟期间的低库存水平费）；
- 对从未收到的单件或货件收费；
- 重复的费用行。

因公布的费率调整、旺季、附加费或价格区间而上涨的费用，不算多收。来源：Roberto_Amazon 员工指南（ce0bea71，2026-04-17；ff7c3c15，2026-05-13）；News 00fd861e（2024-05-02）；Jameson_Amazon 0b434f7f。[官方文档；分类方式为推断]

**FE2**
**默认以亚马逊的测量为准。** 在欧盟认证制度之外，亚马逊核实的重量和尺寸决定所有按尺寸分段计算的费用。卖家自己的测量不能单独用来申诉。配送中心多次测量结果不一致时，取最大值。财务包 P-ful-2 已持有此规则。本文件新增两点：“取最大尺寸”规则，以及“personal measurements are not accepted”（不接受卖家自测）。来源：NR_Amazon ca22eab2（2025-04-30，US 字段）；Glenn_Amazon ae6a5220（回复 2023-11-14，US 字段）。[官方文档] 运行时读取：Seller Central 帮助页 GL7U4JFSDXUTQAJ 和 G6WAEPTECPT2JUH3，以卖家所在站点显示的为准。

**FE3**
**每个变体都是独立商品。** 一个变体的费用或测量，不能作为另一个变体的证据。一次重新测量只覆盖所申请的那个 FNSKU。有卖家报告：重新测量只改了某一个颜色或尺码，同组其他变体没变。来源：Glenn_Amazon ae6a5220（2023-11-06）[官方文档]；AMZ123 2021-04-20 [从业者观点]。

**FE4**
**重新测量的条件。**
- 需要配送中心里有一件可售单件。
- 如果某个 FNSKU 在规定期间内已被重新测量了规定次数，或账户本月额度已用完，申请会被拒。
- 亚马逊给出一个通常的处理时长。
- 亚马逊要求只提交预计会改变费用的申请。
- 提供 case ID 时，员工可以在月度额度之外再加一次申请。

没有任何 SP-API 操作可以申请或读取重新测量（见 sp-api-claims-surface SU12）。账户的月度额度，以及把处理时长当作回复时间，归 filing-and-conduct 管（见 filing-and-conduct FL35、FL30）。来源：NR_Amazon ca22eab2（2025-04-30，US 字段）；KJ_Amazon 958851b3（2024-09-20，US 字段）[官方文档]。运行时读取：每个 FNSKU 的限制，来自 Seller Central 帮助页 *Understanding item package weight and dimensions*（G6WAEPTECPT2JUH3，https://sellercentral.amazon.com/help/hub/reference/external/G6WAEPTECPT2JUH3），以卖家所在站点显示的为准。账户剩余次数读不到（只在 Seller Central 小工具里显示）。见到的数值在“Values that move”表中。

**FE5**
**历史：欧盟认证尺寸。**
- 从 2025-08-01 起，有德国营业地址的卖家被要求为 Amazon.de 认证包装尺寸 [从业者观点：Valuezon，2025 年 7 月，转述亚马逊]。
- Amazon.de 现有 ASIN 须在 2026-04-30 前完成认证，大件和重型大件除外（Global Selling 公告，2026-03-06）。
- 从 2026-05-05 起，amazon.co.uk、.fr、.it、.es 用认证尺寸计算 FBA 费用（亚马逊政策 PDF，创建于 2026-03-30）。标准件核验截止到 2026-07-05，并且也覆盖德国站大件 [从业者观点：cifnews 2026-05-18，转述亚马逊]。
- UK/FR/IT/ES 大件认证截止日为 2026-10-15 [从业者观点：九方 2026-09-01]。

[官方文档 + 从业者观点，如上标注]

**FE6**
**认证规则。**
- 认证是指用“a device that complies with the EU Measuring Instruments Directive, such as, a tape measure”（符合欧盟测量仪器指令的工具，例如卷尺）测量。
- 截止日前没有核验的尺寸，视为已认证。
- 新 listing 必须带认证尺寸；在 Amazon.de，以创建 listing 时填写的尺寸为依据。
- 亚马逊会核验，发现不正确时可以用它自己的认证尺寸替换。
- 卖家通过重新测量小工具申诉，受月度额度限制。

来源：*FBA item package dimensions certification policy* PDF；Global Selling 公告 news-notices-260306（2026-03-06）。[官方文档] 运行时读取：卖家的站点和分段是否在该制度下，读政策 PDF（https://m.media-amazon.com/images/G/02/MP/phase-3policy.pdf）和亚马逊 Global Selling 公告。每个 ASIN 的认证状态无法通过 SP-API 读取。

**FE7**
**认证下的自动回溯补差。** 亚马逊的 Amazon.de 公告说：如果认证尺寸使 FBA 费用降低，系统会自动补偿一段回溯期内的费用差额（“最高追溯”，最多到规定天数）。公告把自动补偿限定在 Amazon.de 上销售的商品。从业者转述 UK/FR/IT/ES 阶段也一样。读过的亚马逊页面中，没有一页说美国有自动补差。来源：news-notices-260306（2026-03-06）[官方文档]；cifnews 186018（2026-05-18）、九方 11810（2026-09-01）[从业者观点]。运行时读取：回溯长度看该站点的认证公告。见到的长度在“Values that move”表中。

**FE8**
**矛盾：欧盟仓储费。** 2026-11-02 生效的 *Rate Card Europe Fees*（FAQ Q2）仍然说仓储体积以亚马逊的测量为准。认证政策（2026-05-05 生效）说在 UK/FR/IT/ES 用卖家认证尺寸计算“FBA fees”。读过的页面都没说仓储费是否属于认证范围。两者都保留，并注明各自日期。来源：欧盟费率卡 2026-11-02 [命令核实，PDFKit]；认证政策 PDF [官方文档]。

**FE9**
**两个 FBA 费用申诉时限。** 亚马逊员工说明：
- “itemized”（分项）FBA 费用错误，时限从每笔收费的日期起算。这类费用与 ASIN/FNSKU 挂钩，通常是重量或尺寸错误：配送费、客户退货费、月度仓储费、长期仓储费。
- “non-itemized”（非分项）错误有一个单独的、更长的时限：移除或销毁订单费、预处理和贴标费。

来源：Roberto_Amazon ce0bea71（2026-04-17，US 字段）和 ff7c3c15（2026-05-13，UK 字段）；Glenn_Amazon ae6a5220（2023-11-14，US 字段）；政策转载，连连 2020-09-15。[官方文档] 运行时读取：时限读 Seller Central 帮助页 *FBA fees reimbursement policy: Weight and dimensions*（GL7U4JFSDXUTQAJ，https://sellercentral.amazon.com/help/hub/reference/external/GL7U4JFSDXUTQAJ），以及卖家所在站点最新的亚马逊员工申诉指南；收费日期读 `listTransactions` 的 `postedDate`。按站点读到的时长在“Values that move”表中。JP、CA 及其他站点都没有读到时长。

**FE10**
**费用时限的历史。**
- 大约 2019 年 5 月，政策给重量和尺寸费用申诉加了时限。它取代了一个较宽松的时限，文章没说原来的时限是多少 [从业者观点：52by，2019-05-22]。
- 澳大利亚那条从 2025-10-15 起调整 FBA 库存索赔时限的 News 帖子，不涉及费用申诉（News d8f9a56c，AU 字段）[官方文档]。
- 财务包 P-ful-2 和调研中的那一行，代表的是分项时限。两者都没有非分项时限（FE9）。

**FE11**
**每笔收费只能申诉一次。** 在重量和尺寸费用政策、以及销售佣金政策下（后者的决定为最终决定），亚马逊都只允许每笔收费提出一项申诉。卖家引用的重量和尺寸政策原文还说：“Only one request needs to be created for an FNSKU”（一个 FNSKU 只需提交一次申请）。来源：政策转载（连连 2020-09-15）；Spencer_Amazon 3432aad2（2024-05-24）；Roberto_Amazon ce0bea71；9c2edbce 中卖家引用 GL7U4JFSDXUTQAJ（2024-12-10）。[官方文档]

**FE12**
**重新测量是费用补偿之前的一步，客服可能要求先等待。** 一位美国员工把重新测量称为“a step that needs to occur prior to a successful reimbursement requests”（成功申请补偿之前必须先完成的一步）。在那个案例里，Seller Support 要求重新测量之前先等一段时间。来源：Bryce_Amazon 9c2edbce（2024-12-10，US）。[官方文档] 这个等待只针对那个案例：只有一句话，没找到规则页面。等待时长在“Values that move”表中。

**FE13**
**亚马逊可能按订单补回尺寸更正，不生成补偿 ID。** 亚马逊员工描述过一种重量尺寸更正的支付方式：每个受影响的订单一条“Fee Adjustment - Weight and Dimension Change”记录。它出现在 Seller Central Transaction View 的 Transaction Type “Other” 下，带订单 ID，金额在“Amazon fees”列，并且“these adjustments do not generate a reimbursement ID”（这些调整不生成补偿 ID）。所以它不会以补偿 ID 的形式出现在 `GET_FBA_REIMBURSEMENTS_DATA` 中。来源：Sandy_Amazon 29fbd69b（帖子 2025-02-05）。[官方文档] 这部分回答了财务包的未决问题 12（fulfilment-charges.md）：亚马逊的说法是按订单的费用调整，而不是一笔总额。`listTransactions` 里怎么编码，仍未见到。

**FE14**
**测量被更正，不等于过去的费用已退回。** 在美国，有卖家报告：亚马逊确认测量错误后仍拒绝退费（“The $88.93 fee was correctly calculated based on the (incorrect) measurements at that time”，按当时的（错误）测量，$88.93 的费用计算正确，2026 年）。在 4a8a5cd9 中，员工（Josh_Amazon）建议新开一个 case，“specifically requesting an order-level audit and refund”（专门要求按订单审核并退款）；在 fe4a0969 中，员工（Christine_Amazon）只说已在卖家的 case 里给出解决方案，结果没有显示。4a8a5cd9 的卖家报告的是没有收到补偿、陷入“automated loop”（自动回复循环），不是书面拒绝。从业者一致认为重新测量只修正以后的费用。来源：fe4a0969（2026-04-03）、4a8a5cd9（2026-10-08）[从业者观点，其中员工回复为官方文档]；Velocity Sellers、Leviathan Sellers、My Amazon Guy、Notifcentral [从业者观点]。

**FE15**
**亚马逊客服要过的材料。** 在 2025 年的一个案例里，Selling Partner Support 的 leadership team 要求一个文件，按 FNSKU 列出错误费用、正确费用、差额和总额；更早一次要求每行一个 FNSKU 和数量。员工指南要求提供货件 ID、FNSKU 和证据，例如测量数据和照片。来源：1c1a9399 中卖家转贴的客服消息（2025-04-04、2025-04-05）；Roberto_Amazon ce0bea71。[官方文档；客服消息由卖家转述] case 的具体操作归 filing-and-conduct。

**FE16**
**仓储费可以作为分项费用申诉。** 亚马逊 2026 年的员工指南把月度仓储费和长期仓储费列为分项 FBA 费用错误。政策的证据规则指定月度仓储费报告和长期仓储费报告为所用尺寸的来源。一位客服说仓储费“can never be reimbursed”（永远不能补偿，2025 年），与这两点冲突，作为卖家报告保留。来源：ce0bea71；连连转载 2020；29fbd69b [官方文档 / 从业者观点，如标注]。

**FE17**
**显示所用测量的报告。**
- `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` 按 SKU 提供尺寸和重量（只有美国有分段；欧盟是 `product-size-weight-band`）。它是当前快照，刷新频率和请求限制归 sp-api-claims-surface SU20。
- `GET_FBA_STORAGE_FEE_CHARGES_DATA` 按 FNSKU、配送中心和月份提供尺寸、重量、`item_volume` 和分段。
- 两者都需要 Pricing 或 Amazon Fulfillment 角色。

来源：FBA Reports 页面（updatedAt 2026-10-13）[命令核实]；角色见财务包 P-ful-20 和 SU3。

**FE18**
**能给分段变化定日期的读取，在五个角色之外。** Data Kiosk `economics` 按商品返回已收取的费用，每个日期区间带 `properties`（例如 Product Size Tier），并在亚马逊调费日期处切分，附 `amountPerUnitDelta`。它能显示商品的分段和单件配送费是何时变化的。Economics 数据集需要 Selling Partner Insights 角色，不在五个角色之内（见 sp-api-claims-surface SU33）。所以这里只列出它能打开什么，不在其上构建任何东西（FE50）。它的起始日期限制和保留期归 SU34。来源：analytics_economics_2024_03_15.graphql [命令核实]；角色要求据亚马逊 *Correction: Data Kiosk role requirements*，经 SU33 [官方文档]。

**FE19**
**陷阱：Fee Preview 没有历史。** 亚马逊在 Fee Preview 报告里不保留历史，重新测量也不发通知。所以在五个角色下，分段变化只能靠比较读取方自己保存的、带日期的报告副本来定日期。Data Kiosk `economics` 的历史能定日期，但需要五个角色之外的角色（FE18、FE50）。来源：FBA Reports 页面 [命令核实]；Velocity Sellers 2026-09-06 [从业者观点]；由此得出的结论为 [推断]。

**FE20**
**陷阱：费率调整看起来像多收。** 在以下情况下，配送费会在测量没变的情况下上涨：
- 假日旺季（P-ful-1、P-ful-22）；
- 燃油和物流附加费（P-ful-8）；
- 跨过价格区间（P-ful-25）；
- 年度调费。

亚马逊的调费日期和旺季日期归财务包（P-ful-*）。来源：上述财务包立场；Leviathan Sellers 2026-10-26 [从业者观点]。（`economics` 会在亚马逊调费日期处切分区间，但不会在跨价格区间时切分 [命令核实]；它在五个角色之外，FE50。）

**FE21**
**信号：SKU 估算对比 ASIN 估算。** 单件入库后，`getMyFeesEstimateForSKU` 使用亚马逊实测的尺寸；`getMyFeesEstimateForASIN` 使用目录尺寸。同一价格下两者的配送费不同，说明实测尺寸和目录尺寸不一致。来源：Product Fees API 页面和 productFeesV0.json（P-ful-19 已持有）；这种用法为 [推断]。

**FE22**
**2022 年取消了销售佣金申诉时限。** 2022-03-16，亚马逊从销售佣金补偿政策中去掉了 90 天申诉时限，并推出了费用类目指南。有卖家报告电话客服引用 90 天的“Internal Policy”（内部政策，约 2023 年）。来源：News *Fee categories made easier to understand*（972575，2022-03-16）[官方文档，日期命令核实]；CA 论坛 5c1e41df [从业者观点]。

**FE23**
**2023-01-13 起的销售佣金补偿依据。** 按“the referral fee rate effective at the date of the disputed transaction”（争议交易发生当日有效的佣金费率）补偿。“contrary to guidelines that are in effect at the time of the fee transaction”（与收费时有效的指南相悖）的申诉会被拒绝。每笔收费只能申诉一次。该政策“does not apply to other fee reimbursements”（不适用于其他费用补偿）。来源：Spencer_Amazon 3432aad2（2024-05-24，UK 字段）。[官方文档] 这把财务包 selling-fees.md A5 中只有搜索摘要的那一行升级为已读页面。没有读到同一政策的 US 字段文本。运行时读取：Seller Central 帮助页 *Referral fees reimbursement policy*（GRRJCFXD6474GRLY，https://sellercentral.amazon.com/help/hub/reference/external/GRRJCFXD6474GRLY）和费用类目指南，以卖家所在站点显示的为准。

**FE24**
**陷阱：SP-API 的 Fee Preview 没有费用类目。** SP-API 的 Fee Preview 报告没有费用类目列（只有 `product-group` 和 `estimated-referral-fee-per-unit`），尽管亚马逊 2022 年的帖子说 Seller Central 的 Fee Preview 会显示即将发生的费用类目变化。来源：FBA Reports 页面 [命令核实]；News 972575 [官方文档]。

**FE25**
**入库配置费：报价对比实收。** 发货流程中显示的入库配置费“is just an estimate”（只是估算）。实际费用在收货后规定天数收取，依据入库地点和实收数量。免费的优化选项要求合规，包括每个商品至少有规定数量的相同箱子或托盘，且每箱数量相同、商品组合相同。Seller Central 的入库配置费报告按计划、货件和 SKU 显示计划是否合规；没有 SP-API 报告提供这一点。来源：Dominic_Amazon 0d8742f3（2024-09-14）；Jameson_Amazon 5d437c4b（2024-11-01）（都是 US 字段）[官方文档]；P-ful-6（没有 SP-API 报告）。运行时读取：时间和选项规则读 Seller Central 帮助页 *FBA inbound placement service fee*（GC3Q44PBK8BXQW3Z）；报价读 `listPlacementOptions`。见到的数值在“Values that move”表中。

**FE26**
**对从未收到的货件收取入库配置费。** 当对从未收到的货件收取了入库配置费时，亚马逊员工让卖家开 Seller Support case。读过的页面都没说丢件补偿是否包括该单件已付的入库配置费。来源：Jameson_Amazon 0b434f7f [官方文档]。

**FE27**
**历史：合作承运人测量调整。** 从 2025-06-12 起，对“domestic US Amazon Partnered Carrier shipments”（美国国内亚马逊合作承运人货件），如果小包裹或 LTL 货件中卖家填写的重量、尺寸或货运等级与承运人实测不同，会产生费用调整：卖家填高了就退款，填低了就加收。它显示在 Inbound Performance 看板的“Inaccurate transportation weight/dims”下。有卖家报告对这类收费的申诉被驳回。来源：News_Amazon a7e7de46（发布于 2025-05-12，US 字段）[官方文档]；Sellers Ask Sellers 6055（转述，2025-05-19）；论坛 6c798198 [从业者观点]。

**FE28**
**亚马逊造成延迟期间的低库存水平费。** 亚马逊会退还由亚马逊或亚马逊管理的入库和处理延迟造成的低库存水平费。退款按月进行，在次月规定的某一天前到账。帮助页称这一补偿是自动的（经 P-ful-7）。读过的页面都没说退款覆盖延迟的哪一部分；搜索摘要中的说法只保留在第 7 节，不在本立场内。来源：News 00fd861e（2024-05-02，US 字段）[官方文档]；GV43F6S76Y9DHYRH，经 P-ful-7。运行时读取：退款时间和条件读 Seller Central 帮助页 *Low-inventory-level fee*（GV43F6S76Y9DHYRH）；卖家每周的收费标记读 `GET_FBA_INVENTORY_PLANNING_DATA`（Amazon Fulfillment 角色）。见到的日期在“Values that move”表中。

**FE29**
**退货费的类别跟随类目归属。** 适用按件退货费还是高退货率阈值规则，取决于商品的类目归属，由亚马逊决定。一个鞋类护理商品被认定属于鞋类，费用被判为正确。来源：308297d2 中引用的客服回复（2024-05-27）[从业者观点，转述]；类别规则见 P-ful-9。

**FE30**
**陷阱：退货费的计费单件无法对应到订单。** 从找到的任何报告都无法把退货处理费的计费单件对应到具体退货：卖家报告 Seller Central 的退货费报告没有订单号，也没有 SP-API 报告拆分这项费用。来源：aa114d9f（2025-01-07）[从业者观点]；财务包 fulfilment-charges.md 的报告表 [在那里命令核实]。

**FE31**
**低价 FBA。** 低价 FBA 费率自动适用于符合条件的单件，无需报名。读过的亚马逊页面都没说是哪个价格、在哪个时点决定是否符合条件。按亚马逊所列条件符合、却按标准费率收费的单件，属于配送费多收 [推断]。来源：sell.amazon.es 低价 FBA 页面（2026）[官方文档]；P-ful-25。运行时读取：卖家所在站点的价格门槛和尺寸限制，读 P-ful-25 中的页面和 *Low-price FBA rates*（https://sell.amazon.es/en/tarifas-precio-bajo-logistica-de-amazon，ES/EU）。按站点和日期读到的门槛和限制在“Values that move”表中。该页西班牙 FAQ 那一行与其较早的条件集一致，是过时的一行，不是矛盾。

**FE32**
**陷阱：Finances 能看到的比申诉时限更远。** 能显示多收的数据，回溯得比申诉时限更远：`listTransactions` 通过多次分段调用覆盖更长期间（P-ref-23）。早于分项时限的收费在数据里看得见，但已超过亚马逊规定的期限。来源：P-ref-23；FE9。[推断]（Data Kiosk `economics` 能看得更远，但在五个角色之外：FE50。）

**FE33**
**陷阱：费用更正的名称不确定。** 费用更正进入卖家资金记录时用的名称，亚马逊没有列出：`Fee Adjustment`、`INCORRECT_FEES_ITEMS`、`INCORRECT_FEES_NON_ITEMIZED`、`NonSubscriptionFeeAdj` 和 `RE_EVALUATION`，是服务商报告的。把两个 `INCORRECT_FEES_*` 名称对应到亚马逊的分项/非分项时限，只是按名字对应。来源：财务包 fulfilment-charges.md “What practitioners add”和 P-ref-33 [从业者观点]；Synder 和 AMALYTIX 术语表（只看到搜索摘要）[从业者观点]；对应关系为 [推断]。

**FE34**
**服务商的检测方法并列。** 从业者用不同的检测方法。没有一种是亚马逊的，也没有一种是标准方法。[从业者观点]

| 方法 | 应收费用取自 | 实收费用取自 | 何时标记 | 如何匹配退款 | 谁 |
|---|---|---|---|---|---|
| 按订单比较，应收费用由卖家维护 | 亚马逊预估费用，或卖家按自己的箱规和价格、依站点费率算出的值（卖家可改） | 订单上的费用 | 有任何差额；金额 =（实收 − 应收）× 数量 | Date Range 交易报告中的“Fee Adjustment”行，正数 | 领星 Lingxing *FBA费差异*（见 sp-api-claims-surface SU44） |
| 按订单比较亚马逊自己的预估 | 费用报告中的亚马逊预估 | 订单上的费用 | 差额超过服务商默认百分比，针对最近发货的订单 | 亚马逊的“是否赔偿”字段 | 赛狐 Sellfox *FBA运费差异* |
| Fee Preview 基线对比 | 较早一份带日期的 Fee Preview 副本 | 当前副本 | 价格没变但费用变了 | 无 | Velocity Sellers；My Amazon Guy；Notifcentral |
| SKU 估算对比 ASIN 估算 | `getMyFeesEstimateForASIN`（目录尺寸） | `getMyFeesEstimateForSKU`（实测） | 同一价格下两者不同 | 无 | 本席位对 P-ful-19 的解读（FE21）[推断] |

服务商的默认阈值是服务商自己的，不是本文件的阈值。来源：Lingxing FBAFeeDifference；Sellfox fba-shipping-cost-difference；Velocity Sellers 2026-09-06；My Amazon Guy 2026-05-04；Notifcentral 2026-08-07。

**FE35**
**实测影响（举例，不是比率）。**
- 美国卖家报告每单从 $40.43 涨到 $88.93，共 29 单（$1,392；2026-04-03）。
- 2026-03-31 至 2026-06-29 期间 378 单，USD 438.52（2026-10-08）。
- 被误测为 48 lb 后，$12.93 的费用按 $28.51 收取（2024-12-10）。
- 据称一位德国女装卖家认证 500 多个 ASIN 后，每件节省 €0.75（一个中文来源的搜索摘要，未打开）。

来源：fe4a0969、4a8a5cd9、9c2edbce [从业者观点]。都只是个案：没有找到关于频率或金额的研究。

**FE36**
**包装是测量差异的主要原因。** 亚马逊指出包装材料是卖家与配送中心测量差异最常见的原因，并把松散的袋口和提手按边到边量进去。首次入库后改了包装，是从业者提到的重新测量原因之一。来源：NR_Amazon ca22eab2（2025-04-30）；Dominic_Amazon c6f1274b（2024-08-22）[官方文档]；Velocity Sellers [从业者观点]。

**FE37**
**亚马逊指定的 FBA 费用错误申诉路径。** 亚马逊员工指南给出的 FBA 费用错误 case 路径是 Help > Contact Us > Shipping & FBA > FBA Issue > “Fees Charged in Error”。销售佣金则指定 Selling Partner Support，并附 Custom Unified Transaction 报告。没有 SP-API 操作能提交其中任何一种（见 sp-api-claims-surface SU8、SU12）。case 操作和行为规范归 filing-and-conduct。来源：ce0bea71（US 字段）/ ff7c3c15（UK 字段）[官方文档]。

**FE38**
**单件被认定丢失或损坏后，停止收仓储费。** 亚马逊员工说：“once an item is identified as lost or damaged, we also promptly stop charging other applicable fees, such as storage fees”（一旦单件被认定丢失或损坏，我们会立即停止收取仓储费等其他相关费用）。对已作为丢失或损坏调出的单件收取仓储费，在这句话里没有依据 [推断]。读过的亚马逊文本都没说：
- 从丢失到被认定之间收取的仓储费是否退还；
- 丢件补偿是否包括该单件已付的费用（其金额归 value-and-reversals）。

来源：KJ_Amazon，1ce28534 中的回复（2025-04-30，US 字段）[官方文档]。运行时读取：丢失或损坏调整的日期读 Inventory Ledger（fc-lost-damaged），对照 `GET_FBA_STORAGE_FEE_CHARGES_DATA` 中按 FNSKU、配送中心和月份的 `average_quantity_on_hand`。

**FE39**
**调查中单件的仓储费没有说明。** 亚马逊把调查中（researching）单件定义为“misplaced or warehouse damaged units that are actively being confirmed”（正在确认中的错放或仓库损坏单件）（stock W14、W15）。读过的亚马逊文本都没说它们是否承担仓储费，也没说仓储报告的数量是否包含它们（未决问题 15）。来源：stock W14、W15；读过的页面中均无相关内容。[由缺失推断]

**FE40**
**移除订单处理期间不收仓储费。** 亚马逊员工说：“Once a removal order is successfully created, we do not charge storage fees on the units during the processing period until its completion.”（移除订单成功创建后，处理期间直到完成，我们不对这些单件收取仓储费。）对已创建的移除或弃置订单中的单件在处理期间收取仓储费，在这句话里没有依据 [推断]。超龄附加费自己的截止规则见 stock C6，清货见 stock S19。来源：TaylorR_Amazon，cd0bbea1 中的回复（2025-06-27，US 字段）[官方文档]；同一帖子里有卖家报告移除失败期间仓储费仍在收 [从业者观点]。运行时读取：订单的申请日期和数量读 Removal Order Detail（stock S18；removals-disposals RM20），对照仓储报告的月份。

**FE41**
**丢失或取消的移除订单上的移除费。**
- 移除或弃置费用错误属于非分项 FBA 费用错误，适用员工指南中较长的时限（FE9）。
- 没有对应已移除或已弃置单件的费用，归 removals-disposals（见 removals-disposals RM26、RM27）。
- 读过的亚马逊文本都没说运输途中丢失的移除件的补偿是否包括该单件已付的移除费。服务商把“Lost Removal Order”列为针对单件的索赔，不是针对费用的。

来源：ce0bea71 [官方文档]；GETIDA *How we help*（© 2026）[从业者观点]。运行时读取：Removal Order Detail 的 `removal-fee`；`GET_FBA_REIMBURSEMENTS_DATA` 中的移除补偿行（其 `reason` 见 removals-disposals RM31）。

**FE42**
**亚马逊造成的滞留库存上的仓储费。** 亚马逊把“system errors”（系统错误）列为滞留原因之一。读过的亚马逊文本都没有对滞留单件退还仓储费，不论原因；一位卖家直接问这个问题，也没有员工回答。移除订单在处理期间停收仓储费（FE40）。亚马逊造成的滞留是否使仓储费成为员工指南中的“fee charged in error”（错误收费），没有说明。来源：Bryce_Amazon f77cbf98（2024-03-12，US 字段）[官方文档]；stock S1–S3 和 stuck-stock.md O17；f77cbf98 和 00896ca4 中的卖家 [从业者观点]。运行时读取：`GET_STRANDED_INVENTORY_UI_DATA` 的 `stranded-reason`、`date-stranded`（stock S2），以及背后的 listing 问题（stock S8）。

**FE43**
**合作承运人收费：作废时限决定能否全额退款。** 确认合作承运人运输选项即同意该收费。在对应货件类型的时限内作废，可全额退款；超出时限，“may apply”（可能会收费）。非合作承运人货件可以随时作废。时限按每个选项记录在 `Quote.voidableUntil`。来源：stock I16（规则）；fulfillmentInbound_2024-03-20.json 的 `Quote`、`cancelInboundPlan` [命令核实]；TaylorR_Amazon 407a9a34（2025-01-14，US 字段）[官方文档]。运行时读取：`listTransportationOptions` 的 `quote.voidableUntil` 和 `quote.cost`（Amazon Fulfillment）；计划状态 `VOIDED` / 货件状态 `CANCELLED`（stock I7）；收费和任何退款在 Finances 中。时限长度在“Values that move”表中。

**FE44**
**承运人未履行运输时的合作承运人收费。** 读过的亚马逊文本都没有规定：作废时限过后，承运人没有取件、或货件在取件前被关闭时，合作承运人收费可以退还。英国卖家报告 Seller Support 以作废时限已过为由拒绝，员工只要了 case ID。服务商把这列为一种索赔（GETIDA 的“Cancelled Shipping Costs”；Threecolts 的“unused shipping labels”）。亚马逊员工指南在两类费用中都没提合作承运人收费，所以其申诉时限没有说明。来源：85f330d7（2025-05-01/13，UK 字段）、753ca151（2020-10-28，UK 字段）、2072bdbf（2024-09-17，UK 字段）[从业者观点；员工回复为官方文档]；GETIDA *How we help*；recovery-economics 服务商表 [从业者观点]。

**FE45**
**计划外预处理和贴标费。** 货件缺少预处理或标签时，亚马逊会代为处理，按件收费，并在 Inbound Performance 看板上标记缺陷。这项费用在货件摘要下的问题（problems）标签页中申诉。标签缺失或有缺陷的单件“aren't eligible for reimbursements”（不符合补偿条件）。申诉时限有两种说法，两者都保留：一是从问题报告时起算，见于未读的帮助页（只有搜索摘要）；二是作为非分项错误，适用员工指南中较长的时限。来源：KJ_Amazon 7c433b9f（2025-01-24，US 字段）；Roberto_Amazon b8734d29（2024-07-30，US 字段）；Bryce_Amazon 32e1d348（2025-08-04、2025-08-08，US 字段）；ce0bea71 [官方文档]；帮助页 201000230，经搜索摘要 [从业者观点，摘要]。运行时读取：`GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA`（`issue-reported-date`、`problem-type`、`fee-type`、`fee-total`；财务 P-ful-24）；卖家 Seller Central 中帮助页显示的时限。见到的数值在“Values that move”表中。

**FE46**
**入库缺陷费的退款显示在 Reimbursements 报告中。** 对于在规定日期范围内创建的国际计划，如果其余货件在首次收货后规定天数内到达，亚马逊免收删除或放弃货件的缺陷费。对这些货件已收取的费用，亚马逊自动退还，“Go to your Reimbursement report to view details”（到 Reimbursement 报告查看详情）。该费用的触发条件和 2026 年的单一费用见别处（stock I13；财务 P-ful-24、J1）。没有找到缺陷费的申诉时限。来源：News_Amazon f25ba535（2026-10-30，US 字段）[官方文档]；GL5XA3MNXAJKJE8E 未读（脚本空壳）。运行时读取：Inbound Performance 报告的 `fee-type` / `fee-total`；`GET_FBA_REIMBURSEMENTS_DATA`；计划内各货件的收货日期（inbound-shortfalls）。免收的范围和时限在“Values that move”表中。

**FE47**
**AWD 按箱尺寸收费有自己的规则。** 只针对 AWD 仓储费和运输费：
- 亚马逊补偿实收费用与按更正后测量计算的费用之间的差额，以亚马逊的测量为准。
- 一个箱子在规定期间内已被重新测量规定次数后，或 AWD 仓库里没有该 MSKU 的箱子时，不能申请重新测量。
- 申请必须在从收费日期起算的时限内提出，每笔收费只能申诉一次，作为调查请求通过 Amazon Support 或客户经理提交。

来源：AWD Service Terms §4.2，日期 2026-01-14，读于 2026-11-13 [官方文档]。该时限由 inbound-shortfalls IN33 移交本文件。AWD 在五个角色下不可读取（stock W38）。运行时读取：带日期的条款页面。数值在“Values that move”表中。

**FE48**
**Subscribe & Save 没有单独的费用索赔。** 读过的亚马逊页面都没有提到 Subscribe & Save 专属的费用索赔。它的费用就是订单的普通费用行，适用以上各立场。来源：stock O13、O14；无相关内容。[推断]

**FE49**
**原 Small and Light 单件没有单独的索赔。** Small and Light 于 2023 年关闭，低价 FBA 是按价格适用的费率（stock G21）。原 Small and Light 单件的费用按 FE31 或标准费率判断。来源：stock G21。[推断]

**FE50**
**依赖 Data Kiosk `economics` 的检测在五个角色之外。** Economics 数据集需要 Selling Partner Insights，它不是卖家的五个角色之一（见 sp-api-claims-surface SU33；财务 P-ful-18 持有互相冲突的角色页面）。它能打开的是：
- 按商品、按日期区间的已收费用，带决定费用的属性（尺寸分段），在亚马逊调费日期处切分（FE18、FE20）；
- 比 Finances 更远的历史（FE32；可回溯范围见 SU34）；
- 已收费用的组成部分；
- 低库存水平费和退货费的 `economicsPreview` 费用类型（第 7、9 节）。

本文件不在其上构建任何东西。在五个角色下，同样的问题从带日期的 Fee Preview 副本、Storage Fees 报告、Finances、Inbound Performance 报告和 Reimbursements 报告中读取。来源：SU33；analytics_economics_2024_03_15.graphql [命令核实]。[官方文档]
