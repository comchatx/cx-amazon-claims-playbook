# Fee overcharges: how a wrong fee is found, what Amazon's rules let the seller recover, and by when

Research seat for brief 548 (claims playbook), area **fee-overcharges**. Date read for every page: **2026-11-13** unless a position says otherwise.

Summary. A fee overcharge is a fee Amazon charged on a basis its own rules did not support for that unit, shipment or period. The usual cases are a wrong measurement or size tier, a wrong referral-fee category, a low-price or placement rate not applied, a low-inventory-level fee during an Amazon-caused delay, storage on a wrong volume, and a returns fee on the wrong class. A rate change is not an overcharge.

Amazon's rule in the US is that its own measurement governs. Since 2025–2026 the EU has a second regime in which the seller certifies the dimensions (DE, then UK/FR/IT/ES). Amazon's DE notice states an automatic look-back true-up under that regime; no Amazon page read states one for the US. Amazon staff state two windows, one for itemised FBA fee errors and a longer one for non-itemised ones. The referral-fee dispute has had no dispute window since 2022, but each charge allows one claim and the decision is final. Every length, limit and threshold is in "Values that move", with its store and date. Fees charged on units that are no longer in Amazon's stock (lost, damaged, in a removal order), on stranded units, on partnered-carrier transport that was never used, on unplanned prep and labelling, the inbound defect fee and AWD fees on box dimensions are covered in sections 11–15. No SP-API operation requests a remeasurement, certifies a dimension or files a dispute (see sp-api-claims-surface SU12; the Support API is SU8–SU10). On the seller's five roles, the reads that detect an overcharge are the Fee Preview report, the Storage Fees report, the Inbound Performance report, the Reimbursements report and Finances. Data Kiosk `economics` would add dated fee history, but it needs the Selling Partner Insights role, which is outside the five (see sp-api-claims-surface SU33). Nothing in this file is built on it (FE50).

Ownership. Rates, fee lines and where each charge posts belong to the finance pack (cx-amazon-finance-playbook), research/areas/fulfilment-charges.md (P-ful-*) and selling-fees.md (P-sell-*), and are cited here, not repeated. This file covers the overcharge itself: how it is found and how it is claimed. Pointers to other areas:
- Lost, damaged and inbound units: fc-lost-damaged, inbound-shortfalls.
- Returns money: customer-returns.
- Removal fees as claims: removals-disposals.
- Reimbursement value: value-and-reversals.
- Roles, report mechanics and API limits: sp-api-claims-surface.
- Case mechanics, limits and penalised conduct: filing-and-conduct.
- Vendors' fees and recovery figures: recovery-economics.
- Which store each Amazon News post is for (the post-to-store table) and the automation dates: fc-lost-damaged.
- The per-unit cap, the valuation-dispute window and the MYSC limits: value-and-reversals.
- The Support API, "no operation files a claim", and roles: sp-api-claims-surface.
- IDR and case routes, their limits, and conduct: filing-and-conduct.
- Stock pack (cx-amazon-stock-playbook, research/README.md): states of stock (W*), inbound mechanics (I*), stranded, removal and disposal mechanics (S*), storage charging (C*). Cited by id.

Tags: **[read in official docs]** Amazon's own page, staff post, model or PDF; **[command-verified]** checked here by a command over a downloaded page or the models clone (amzn/selling-partner-api-models, commit db2936a, 2026-10-29); **[opinion]** a named practitioner, vendor or seller; **[inferred]** this seat's reading of sourced facts; **seat's own** = no source, enters no skill.

Routes. Every Seller Central help page (G-number) tried came back as a JavaScript shell. That was checked by curl on 2026-11-13 for GL7U4JFSDXUTQAJ, G6WAEPTECPT2JUH3 and G37G73BJXHF75ACH on .com, .co.uk, sellercentral-europe, .in, .com.au, .sg, -japan and .ae, under both `/help/hub/reference/external/` and `/gp/help/external/`: about 160–170 KB each, with no policy text. Help-page text therefore comes by four routes, each named where it is used:
- Amazon staff forum posts that restate the page (forum `datePublished` read from the raw page).
- The listing seat's reading of 2026-10-14, as relayed through the finance pack.
- Amazon's own PDFs and Global Selling notices.
- Reprints by named third parties.

Every read in this file was a plain GET. No POST was sent to an Amazon host, and the help hub's content call was not used (the office closed that route on 2026-11-10). A help page that serves a script shell stays unread, and its fact carries the tag of the route it came through.

Store of a forum post. A Seller Forums post's store is its `marketplaceId` field in the page data, not the host it is served on. The method and the post-to-store table are fc-lost-damaged's. Several staff posts this file cites from the .ca, .co.uk and sellercentral-europe hosts carry the US field (ATVPDKIKX0DER). Each citation below names the field as read on 2026-11-13: US ATVPDKIKX0DER, UK A1F83G8C2ARO7P, CA A2EUQ1WTGCTBG2, IN A21TJRUUN4KGV, AU A39IBJ37TRP1C6.

---

## 1. Measurement: whose dimensions set the fee

### 1a. Amazon's rule (US and the default)

- The rule that Amazon's verified measurement governs, the request window and the remeasurement limits are already held: finance pack P-ful-2 (sources GL7U4JFSDXUTQAJ v14, G37G73BJXHF75ACH v5, G6WAEPTECPT2JUH3 v11, read 2026-10-14 by the listing seat) and listing pack inventory-and-fulfillment.md G9–G11.
- Amazon staff restatement, US forum, NR_Amazon, *Importance of Accurate Product Measurements*, https://sellercentral.amazon.com/seller-forums/discussions/t/ca22eab2-3fbe-4826-ab22-74a842fac674, posted 2025-04-30 (`datePublished` 2025-04-30T20:39:30Z, marketplace field US), read 2026-11-13 [read in official docs]:
  - "Item package weight and dimensions refer to the weight and dimensions of an individual product … The weight and dimensions also include the item's packaging, such as a box or polybag".
  - "To calculate dimensional weight, multiply the package's overall length, width, and height, then divide by 139. The greater of dimensional weight and unit weight is used to calculate fees for any item that's eligible to receive dimensional weight". The divisor is a US figure. Other stores' divisors are held in P-ful-26.
  - "If one or more of these dimensions differ across the package (such as a bulge), measure the longest or thickest part of that dimension".
  - "The most common cause of differences between seller and fulfillment center measurements is the type of packing material in use".
  - Remeasurement: "we will locate a sellable unit belonging to your inventory and remeasure it in one of our fulfillment centers, typically within 10 days of request". "We recommend to only submit requests that you believe will result in a change to your fees (when you submit too many remeasurement requests that don't result in fees changes, we may not be able to process requests that are impacting fees in a timely manner)".
  - "Before you submit your request, please ensure you have the weight and dimension data used in the FBA fee calculation from the corresponding fee report (i.e. FBA dashboard)".
  - "A product is not eligible for a remeasurement request if it has already been remeasured twice in the past 60 days, there are no available units for your listing in the FC, and/or your seller account has exceeded the monthly remeasurement request limit".
  - "Amazon will reimburse the FBA fees if we confirm that they were charged using inaccurate weight or dimensions (when the weight or dimensions that the seller provides vary from our verified measurement, our measurement will govern)".
- Amazon staff, Glenn_Amazon, reply in *Amazon Overcharging For Incorrect Weight and Dimensions*, https://sellercentral.amazon.ca/seller-forums/discussions/t/ae6a5220-e749-4726-8660-d5a64e35dd6c. Served on the .ca host, but the thread and the reply carry the US marketplace field. Thread posted 2023-11-06, reply 2023-11-14 (`createdAt`), read 2026-11-13 [read in official docs]:
  - "you must submit your request within 90 days of the date on which the fee was charged".
  - "Only products measured at the Fulfillment Center will be eligible to contest dimensions. I apologize but your personal measurements are not accepted."
  - "if Amazon measures the product multiple times and has inconsistent dimensions, Amazon will use the largest dimensions."
  - "Each variation is it's own product so the fee of one variation cannot be used to contest the fee of a separate member of the variation."
- Amazon staff, KJ_Amazon, in *Wrong FBA fulfillment fees …*, https://sellercentral.amazon.co.uk/seller-forums/discussions/t/958851b3-3d11-4dec-950d-7644e6206869, posted 2024-09-20. Served on the .co.uk host, with the US marketplace field [read in official docs]: "type "remeasure" into the search box and follow the instructions in the widget. There is a monthly remeasurement request limit, but if you include a Case ID I can request an additional request for you."
- Amazon staff, Dominic_Amazon, *Optimizing Item Package Weight and Dimensions to Manage FBA Fees*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/c6f1274b-6484-4c24-b6f6-3c2da5e3f468, posted 2024-08-22. Served on the EU host, with the US marketplace field [read in official docs]: "A wide range of FBA fees, including fulfillment, storage, removal, and disposal, are all calculated based on the item package weight and dimensions." "there are monthly limits on the number of requests you can make."
- Policy text, Chinese reprint. LianLian Global (连连国际) reprinted the Chinese version of *FBA fees reimbursement policy: Weight and dimensions* at https://global.lianlianpay.com/channel/10-19426.html (dated 2020-09-15, read 2026-11-13). Amazon's words, relayed:
  - "重要： 要符合此政策规定的赔偿条件，您必须在收费之日起 90 天内提交申请。" (to qualify, the request must be submitted within 90 days of the date the fee was charged).
  - Evidence: "从相应的费用报告（例如，月度仓储费报告或长期仓储费报告）中获取计算亚马逊物流费用时所使用的重量和尺寸数据。" (take the weight and dimensions used in the fee from the matching fee report, e.g. the monthly storage fee report or the long-term storage fee report).
  - "对于每笔收费，您只能提出一项索赔。" (one claim per charge).
  - A seller quoting the current English page in a 2024 US thread (9c2edbce, below) adds: "Only one request needs to be created for an FNSKU." [read in official docs, relayed]
- History. A Chinese trade article of 2019-05-22 reports that the 90-day limit had just been added to the policy ("这个90天索赔的政策已经在后台更新了"). Before that, it says, the time limit was less strict ("之前的赔偿政策时间限制没有这么严格"); it does not say what the earlier limit was (邦阅网 52by, https://www.52by.com/article/24979) [opinion].

What practitioners add:
- **Amazon sends no notice of a remeasure.** The fee changes from the day the new measurement applies.
  - Velocity Sellers (Jake Schwarzbaum, 2026-09-06): "There is no notification, so a saved baseline is the only reliable detector." Its method is a dated Fee Preview copy compared with a later one, for SKUs whose fee moved with no price change [opinion].
  - Notifcentral (Archit Mathur, 2026-08-07, updated 2026-10-30) says Amazon measures at receipt, during picking and in periodic catalogue maintenance [opinion].
- **Seller-side measurement method.** Velocity Sellers describes measuring the unit as a customer receives it, laid flat, with bag flaps and handles extended, and singles out SKUs near a tier edge (its own margin, about half an inch). [opinion: Velocity Sellers; the "flat, extended" part mirrors NR_Amazon above; the margin is the vendor's, not Amazon's.]
- **Remeasure limits seen in practice.** The monthly account limit belongs to filing-and-conduct (see filing-and-conduct FL35). The practitioner figures this seat found are in "Values that move": Sellerise 2023, with reset on the 1st and shown in the widget; Regan跨境 on AMZ123 (https://www.amz123.com/t/2kIZ4A7n); a seller relayed by Notifcentral. All are [opinion]. Amazon's own wording is only "based on the number of offers with inventory in your account" (P-ful-2).
- **Repeated or opposite remeasures.** AMZ123 (2021-04-20, https://www.amz123.com/t/Waa8JqhS) relays seller cases:
  - Only the best-selling colour was mis-measured.
  - A remeasure moved two of three same-size SKUs up to the higher fee instead of down.
  - A second remeasure a month later matched the seller's own figure.
  - Support's reply: "以库房测量为准" (the warehouse measurement stands) [opinion].
- **Multi-unit versus single-unit scan.** My Amazon Guy (Steven Pope, 2026-05-04) advises asking for a multi-unit scan; no Amazon page read says a seller can choose the scan type [opinion].

Into a skill: Amazon's measurement governs outside the certification regime. Measurements are edge-to-edge, at the thickest point, including loose material. Inconsistent measurements resolve to the largest. Each variation is judged on its own. A remeasurement needs a sellable unit in an FC and is limited per FNSKU and per account. Amazon gives no notice when a remeasure changes a tier. Seller tape measurements are not, by themselves, accepted to contest a measurement (staff, 2023).

Read at run time:
- The dimensions, weight and tier Amazon holds per SKU: `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` (`longest-side`, `median-side`, `shortest-side`, `length-and-girth`, `item-package-weight`, `product-size-tier` (US only), `product-size-weight-band` (EU)).
- The same per FC and month: `GET_FBA_STORAGE_FEE_CHARGES_DATA` (`longest_side`, `median_side`, `shortest_side`, `weight`, `item_volume`, `product_size_tier`, `month_of_charge`).
- The tier in force per date range would be Data Kiosk `economics` `Fee.properties` / `FeeComponent.properties`. It is not readable on the five roles (Selling Partner Insights; see sp-api-claims-surface SU33; FE50). On the five roles, the only tier history is a dated Fee Preview copy kept by the reader.
- The window and limits: Seller Central help *FBA fees reimbursement policy: Weight and dimensions* (GL7U4JFSDXUTQAJ, https://sellercentral.amazon.com/help/hub/reference/external/GL7U4JFSDXUTQAJ) and *Understanding item package weight and dimensions* (G6WAEPTECPT2JUH3), as the seller's own Seller Central shows them.
- The account's remaining monthly remeasure count: cannot be read (Seller Central widget only).

### 1b. The EU certification regime (2025–2026): the seller's certified dimensions set the fee

Amazon's words:
- *FBA item package dimensions certification policy*, Amazon PDF, https://m.media-amazon.com/images/G/02/MP/phase-3policy.pdf. The PDF was created 2026-03-30, per its metadata [command-verified: text extracted with macOS PDFKit], and read 2026-11-13 [read in official docs].
  - "Effective May 5, 2026, we'll use the certified dimensions that eligible sellers provide to calculate Fulfillment by Amazon (FBA fees) for products listed on amazon.co.uk, amazon.fr, amazon.it and amazon.es."
  - "Dimensions are certified when they are taken with a device that complies with the EU Measuring Instruments Directive, such as, a tape measure."
  - "This policy applies to all active and new FBA listings in our UK, France, Italy, and Spain stores. We will notify you in advance once the policy applies in additional European stores."
  - "If eligible, you'll have at least 60 days to verify your existing dimensions, and you must provide certified dimensions for all new product listings."
  - "If you don't verify that your current item package dimensions are certified by the deadline, or provide updated certified dimensions, we will assume that your existing dimensions are certified dimensions."
  - "We'll validate your item package dimensions, and if we find that they're incorrect, we'll use our own certified dimensions. If you disagree with our certified measurements, you can submit an appeal via the Remeasure FBA products and confirm fees widget."
  - The file name ("phase-3") implies earlier phases. The two below are the ones found.
- Amazon Global Selling China notice *亚马逊FBA新规 | 4/30前认证商品包装尺寸，省物流费！*, https://globalselling.amazon.com/news/news-notices-260306 (gs.amazon.cn redirects there), dated 2026-03-06, read 2026-11-13 [read in official docs]:
  - Scope: "此政策适用于亚马逊德国站点，但是大件及重型大件商品暂不包含。" (Amazon.de; large and heavy bulky items excluded for now).
  - Deadline: "卖家需要在2026年4月30日前，通过卖家平台认证现有ASIN的包装尺寸，或提供更新后的认证尺寸。" (certify existing ASINs' package dimensions, or give updated certified ones, by 2026-04-30).
  - New ASINs: "对于新的ASIN，亚马逊将以您创建Listing时输入的产品包装尺寸作为确认依据。" (the package dimensions entered at listing creation are taken as the basis).
  - **"如果您提供的认证尺寸使得亚马逊物流费用降低，系统将自动补偿过去90天的费用差额。"** (if the certified dimensions lower FBA fees, the system automatically compensates the fee difference for the past 90 days). The heading over it reads "费用补偿，最高追溯90天" (up to 90 days back), and the introduction limits the automatic part to Amazon.de: "对于在 Amazon.de 上销售的商品，系统将自动提供赔偿" (re-read 2026-11-13).
  - "若您不同意亚马逊认证后的尺寸，您仍可以通过"重新测量"功能直接提交申请，但需遵守每月测量次数的限制。" (an appeal goes through remeasurement, within the monthly limit).
  - Processing: "约30天内完成认证，旺季期间(11、12月)可能需要更长时间" (about 30 days; longer in November and December).
  - Default: "如果您在截止日期前未完成认证或更新尺寸，系统将默认您现有ASIN当前的尺寸数据已经通过认证" (unverified existing dimensions are deemed certified).
  - Where: Seller Central → 库存 → 亚马逊物流库存 → "验证尺寸" link (single item), or a bulk Excel template in centimetres.

What practitioners add:
- Valuezon (Averest Consulting, July 2025, https://valuezon.de/en/news/fba-fees-certified-item-dimensions-mandatory-from-august/): "Starting from August 1, 2025, Amazon will require sellers with a German business address to provide certified packaging dimensions for FBA products". "Between August 1 and September 30, affected sellers will receive an email" [opinion, relaying Amazon]. So the 2026-03-06 notice reads as the phase for sellers without a German address [inferred].
- 雨果网 cifnews (2026-05-18, https://www.cifnews.com/article/186018, reposting the Amazon Global Selling WeChat account):
  - The UK/FR/IT/ES phase for standard-size items runs to 2026-07-05 ("7/5前完成") and also covers German large items.
  - "如果您已在第一波（4月30日截止）中完成了德国站标准件商品的认证，相同 ASIN 无需在其他站点（英/法/意/西）重复操作" (ASINs certified in the first wave need not be redone in UK/FR/IT/ES).
  - "如果同一FNSKU在多个站点上架，您只需在其中一个站点完成认证即可" (one store suffices per FNSKU).
  - It repeats the automatic 90-day compensation.
  - [opinion, relaying Amazon]
- 九方通逊 (2026-09-01, https://www.jiufanglogistics.cn/news/11810.html): "亚马逊英国、法国、意大利、西班牙四站上线FBA大件商品包装尺寸主动认证" (large-item certification in UK/FR/IT/ES), due by 2026-10-15. "认证后若费用档位下调，系统自动退还过去90天多收运费" (if the tier falls after certification, the system refunds 90 days of overcharge) [opinion].

The contradiction to keep:
- The *Rate Card Europe Fees* effective 2026-11-02 still says, for storage: "Amazon will be entitled to make its own measurement of the cubic metre or weight of any packaged unit … and in the event of any conflict between such measurement and information provided by the seller, Amazon's measurement will govern." (FAQ Q2, https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf) [command-verified: extracted with PDFKit].
- The certification policy says certified seller dimensions calculate "FBA fees" in UK/FR/IT/ES from 2026-05-05.
- Whether "FBA fees" there includes storage, or only fulfilment fees (a practitioner LinkedIn post, seen only as a search summary, lists local/Pan-EU FBA, EFN and Remote Fulfilment), is not stated on any page read. 九方 (2026-09-01) words the large-item phase as certified dimensions replacing the warehouse measurement for the "配送费" (fulfilment/delivery fee) only [opinion]; cifnews (2026-05-18) does not mention storage. Both Amazon texts are kept, unresolved.

Into a skill:
- In the EU stores under certification, the fee basis is the seller's certified (or deemed-certified) dimension, unless Amazon's validation substitutes its own.
- A certified dimension that lowers the fee is trued up automatically for a look-back period that the store's notice states. The length is in "Values that move".
- Outside those stores and tiers (the US, and any store or tier not yet phased in), Amazon's measurement governs (1a).
- Which regime applies to a seller is store-, tier- and date-dependent. It is read, not assumed.

Read at run time:
- Whether the seller's store and tier are under certification, and the deadlines: Amazon's *FBA item package dimensions certification policy* (https://m.media-amazon.com/images/G/02/MP/phase-3policy.pdf) and the Global Selling notice (https://globalselling.amazon.com/news/news-notices-260306), plus any later notice for further stores. No SP-API operation shows certification status [command-verified: no "remeasur" in any model or schema of the clone db2936a or of upstream main b13d1d1 (2026-11-10); "certif" occurs only as "certificate" / "GiftCertificate" / "wacCertificate", none about dimensions].
- The dimensions now used: the Fee Preview report as above.

---

## 2. The windows: how long an overcharge stays claimable

Amazon's words:
- Amazon staff guide, US forum, Roberto_Amazon, *📘 A Seller's Guide to Disputing Incorrect Charges on Amazon*, https://sellercentral.amazon.com/seller-forums/discussions/t/ce0bea71-dd81-4a08-808a-893ecc1572dd, posted 2026-04-17 (marketplace field US). The same text was posted on the EU host as *Spotted an Incorrect Charge? Here's What to Do*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/ff7c3c15-8655-4086-af58-9b726d178e77, on 2026-05-13 (marketplace field UK). Both read 2026-11-13 [read in official docs; text extracted from the raw page]:
  - "FBA Fee Errors (Itemized) — Fees tied to specific ASINs/FNSKUs, such as fulfillment (pick & pack) fees, customer returns fees, monthly storage fees, and long-term storage fees. These are typically related to incorrect weight or dimension measurements. Requests must be submitted within 90 days of the disputed charge."
  - "FBA Fee Errors (Non-Itemized) — Fees not directly tied to weight/dimension issues, such as removal/destroy order fees and prep and labeling fees. These follow an 18-month statute of limitations."
  - "Referral Fee Disputes — … only one claim per charge is allowed, and Amazon's appeal decision is final."
  - Route: "Go to Help > Contact Us > Shipping & FBA > FBA Issue and select "Fees Charged in Error."" "Include shipment IDs, FNSKUs, and supporting evidence (e.g., product measurements, photos)." Referral disputes: "Pull your Custom Unified Transaction report from the Reports Repository for the disputed period."
  - "fees are sometimes charged more than once for the same event."
- The *Update to FBA inventory reimbursement claim windows* News post (posted 2025-08-14, effective 2025-10-15, https://sellercentral.amazon.com/seller-forums/discussions/t/d8f9a56c-882f-437c-ad34-cccd11cfa465, read 2026-11-13) carries the Australia marketplace field (A39IBJ37TRP1C6; the post-to-store table is fc-lost-damaged's). It lists lost/damaged, customer returns, removals and re-evaluation only and says nothing on fee claims [read in official docs]. For Australia, the fee window is a separate policy that the 2025-10-15 change did not touch [inferred]. No post for another store's window change was read here. The inventory windows are held in the finance pack (P-ref-16) and in the claim-kind files.

What practitioners add:
- Leviathan Sellers (Harishchandra Bind, 2026-10-26, updated 2026-11-07, https://www.leviathansellers.com/blog/amazon-fba-fee-overcharge) restates the itemised / non-itemised split from the 2026-04-17 staff guide. Its reading is that "each charge has its own window", so the window runs per charge, not per SKU [opinion].
- Velocity Sellers (2026-09-06): brands "typically find the overcharge 60 to 120 days in", so part of it is already outside the itemised window when found [opinion].

Into a skill:
- The window for a weight- or dimension-driven ("itemised") FBA fee is counted from each charge's date. For a non-itemised FBA fee error it is a longer, separate limit.
- The referral-fee dispute has no dispute window (section 4), but allows one claim per charge.
- None of these windows is in any API.

Read at run time:
- The current windows: Seller Central help *FBA fees reimbursement policy: Weight and dimensions* (GL7U4JFSDXUTQAJ) and the latest Amazon staff guide (as of 2026-11-13: ce0bea71 US / ff7c3c15 EU).
- The date each fee was charged: `listTransactions` `postedDate` (Finances 2024-06-19), or settlement V2 `posted-date`.

---

## 3. What happens after a remeasure: automatic correction or not

Amazon's words:
- Amazon staff, US forum, Sandy_Amazon (Community manager team), in *Amazon overcharged me storages fees and says it could never be reimburset …*, https://sellercentral.amazon.com/seller-forums/discussions/t/29fbd69b-3933-4d25-84d4-69b0eaa62ac0. The thread was posted 2025-02-05; read 2026-11-13 [read in official docs; text extracted from the raw page]:
  - "Their investigation shows that the initial change occurred in December, and the adjustment was properly processed according to the payments report. Please be aware that these adjustments do not generate a reimbursement ID. Instead, reimbursements are issued per affected order."
  - "Under "Transaction Type" dropdown, select "Other" In this report, each "Fee Adjustment - Weight and Dimension Change" entry represents a reimbursed order (order ID will be present on the "Order ID" column). The "Amazon fees" column shows the reimbursement amount for each specific order."
- Amazon staff, US forum, Bryce_Amazon, in *what should I do if Amazon overcharges FBA fees without compensation?*, https://sellercentral.amazon.com/seller-forums/discussions/t/9c2edbce-af2e-4a7b-8fc8-1cec205b4f35, posted 2024-12-10 [read in official docs]: "The recommendation from Seller Support was to wait 30 days before requesting remeasurement (a step that needs to occur prior to a successful reimbursement requests)."
- Amazon Selling Partner Support, "Leadership team", messages of 2025-04-04 and 2025-04-05. A seller pasted them into *Fraudulent FBA storage fees*, https://sellercentral.amazon.com/seller-forums/discussions/t/1c1a9399-ad90-433c-8a04-6ae301b86a6d (posted 2025-03-31) [read in official docs, relayed by the seller]:
  - "Reimbursement request for weights, dimensions, or fees …" asks for "a .txt/.csv file with a valid format of one FNSKU, QTY per line".
  - Then: "provide the list of the FNSKUs, the incorrect FBA Fee, the correct FBA Fee, the difference, and the total amount that needs to be reimbursed. You may provide these in one Excel file."

Sellers report the opposite outcome [opinion]:
- *Amazon made a measurement error, corrected it, but refuses to refund overcharged FBA fees*, https://sellercentral.amazon.com/seller-forums/discussions/t/fe4a0969-6e01-4991-946c-ccd033080e80, posted 2026-04-03. The fee went from $40.43 to $88.93 per order, 29 orders, $1,392. Support's quoted reply: "The $88.93 fee was correctly calculated based on the (incorrect) measurements at that time." Christine_Amazon (staff) replied only that "the team in charge was able to provide you with a resolution on case …".
- *FBA Fee Overcharge & Refund – Re-measurement Confirmed but No Reimbursement, Stuck in Automated Loop*, https://sellercentral.amazon.com/seller-forums/discussions/t/4a8a5cd9-31b7-4ab8-a3e9-654f749e3fe2, posted 2026-10-08. The wrong measurement applied from 2026-03-31; a remeasure confirmed the correct one on 2026-06-29; 378 orders, USD 438.52. Josh_Amazon (staff) advised "open a new case specifically requesting an order-level audit and refund of the overcharged FBA fees for the affected period".
- A support agent's line in 29fbd69b: "once the storage fees have been charged, they can never be reimbursed as per Amazon's policies". The staff guide of 2026-04-17 lists monthly and long-term storage among disputable itemised fees (section 2), and the policy reprint names the storage reports as evidence (1a). Both are kept; the staff guide is the later and more specific Amazon text [inferred].
- Practitioners agree that a remeasure corrects future fees only, and past ones need a separate request:
  - Velocity Sellers: "Amazon does not automatically refund fees charged on a dimension it later corrects."
  - Leviathan Sellers.
  - My Amazon Guy: "Once remeasurement confirms the error, submit a reimbursement claim using the corrected data."
  - Notifcentral.

  [opinion]

Into a skill:
- Amazon's own statements show both paths exist in the US: per-order "Fee Adjustment - Weight and Dimension Change" credits with no reimbursement ID (2025), and refusals after a confirmed remeasure (2026, seller reports).
- So a corrected measurement is not, by itself, evidence that past fees came back. Only the seller's own Finances rows show it.
- Under the EU certification regime the look-back true-up is stated as automatic for Amazon.de (1b; the length is read from the store's notice).

Read at run time: whether any adjustment posted for the affected orders.
- Finances `listTransactions` over the period, filtered to the order IDs: how a weight/dimension fee adjustment is typed in `transactionType` / `breakdownType` / `description` is not documented (open question 2).
- Settlement V2 rows (`transaction-type`, `amount-description`, `order-id`).
- Seller Central Transaction View → "Other" → "Fee Adjustment - Weight and Dimension Change": Seller Central only.

---

## 4. Referral fee on the wrong category

Already held: the fee category is Amazon's assignment and can differ from the browse category; a wrong category is disputed per charge; one claim per charge (finance pack P-sell-5, selling-fees.md A5). This seat adds the dated rules and reads the pages the finance pack had only as a snippet:
- News_Amazon, *Fee categories made easier to understand*, https://sellercentral.amazon.com/forums/t/fee-categories-made-easier-to-understand/972575. The page markup gives 2022-03-16 [command-verified: `datetime` attribute on the raw page]; read 2026-11-13 [read in official docs]:
  - "We've also updated our referral fee reimbursement policy to remove the 90-day dispute window."
  - "fitness trackers will be included in only one fee category, to ensure that all products of a kind have the same rate."
  - "We've also upgraded the Fee Preview report to include any upcoming changes to an ASIN's fee category. ASINs are continually audited and updated".
- Spencer_Amazon, *Referral Fees Series. Part 3*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/3432aad2-9c07-4551-85bb-798325231de0, posted 2024-05-24 (marketplace field UK) [read in official docs]:
  - "Effective January 13, 2023, the requirements and limitations below apply to the reimbursement of referral fees."
  - "This policy does not apply to other fee reimbursements."
  - "Any reimbursement will be based on the referral fee rate effective at the date of the disputed transaction."
  - "For each fee charge, you may only file one claim."
  - "Disputes contrary to guidelines that are in effect at the time of the fee transaction will be declined."
- Ezra_Amazon, *WRONG FEE CATEGORY*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a28e70af-2805-4ae2-9a37-9430f939e624 (reply 2024-03-18, marketplace field India): links the *Referral fees reimbursement policy* (GRRJCFXD6474GRLY, unread, JS shell). "Amazon retains the right to assess the validity of referral fee disputes", including for products the guidelines do not name [read in official docs].
- A seller reports being told by phone that reimbursement is limited to the last 90 days by "Internal Policy" (https://sellercentral.amazon.ca/seller-forums/discussions/t/5c1e41df-cf5b-4bb0-8329-8b9f0001187e, posted 2023-10-12, marketplace field CA). This conflicts with the 2022 News post. Kept as a seller report [opinion].
- GETIDA (Part 5 of its FBA reimbursement series, about 2023) gives as an example an item charged at a 15% Kitchen rate instead of an 8% Electronics rate [opinion].

Into a skill:
- A wrong-category referral fee is reimbursed at the rate in force on the transaction date, against the fee-category guidelines in force then.
- One claim per charge; Amazon's decision is final.
- No dispute window has been stated by Amazon since 2022-03-16.
- The data pitfall: the SP-API Fee Preview columns carry `product-group` and `estimated-referral-fee-per-unit` but no fee-category column [command-verified: FBA Reports page, updatedAt 2026-10-13, curl]. The upcoming-category column the 2022 post describes is a Seller Central view.

Read at run time:
- The charged referral fee per order: `listTransactions` breakdowns (the `Commission` line), settlement V2 `ItemFees` / `Commission`.
- The rate for the category: Seller Central help *Selling on Amazon fee schedule* (G200336920) as the seller's store shows it (P-ref-2, P-sell-*).
- The per-unit estimate at the current price: `getMyFeesEstimateForSKU`.
- The fee category Amazon assigned: cannot be read through the SP-API on the pages read (open question 8).

---

## 5. Low-price FBA rate not applied

- Already held: US "Products priced under $10 will automatically receive Low-Price FBA rates"; the 2027 narrowing; the EU caps by store and category (P-ful-25, B2, B3, B6).
- Amazon, *Low-price FBA rates*, https://sell.amazon.es/en/tarifas-precio-bajo-logistica-de-amazon (© 2026, read 2026-11-13) [read in official docs]:
  - The page lists two sets of criteria. Before 2026-01-05: "£10 in the United Kingdom €11 in Germany €12 in France, Italy, Spain, Belgium, the Netherlands and Ireland 140 SEK in Sweden 55 PLN in Poland". From 2026-01-05, with category exclusions: "£20 in the United Kingdom €20 in Germany, France, Italy, Spain, Belgium, the Netherlands and Ireland SEK 230 in Sweden PLN 85 in Poland" (VAT included). The page's Spain FAQ ("€12 or less") matches the earlier set: a stale line on the page, not a third rule.
  - Maximum "35 x 25 x 12 cm" and "400 g" in both sets.
  - "no action is required from the seller".
- Not stated on any page read: which price, at which moment, decides eligibility (listing price, sale price, at order or at shipment). A seller in a thread on the .ca host with the US marketplace field (https://sellercentral.amazon.ca/seller-forums/discussions/t/38503cfc-a612-400b-8653-45244f24b5c9, 2025-06-08) says "based on the item's sale price, excluding taxes and shipping charges" [opinion, not staff].

Into a skill: a unit eligible by price, category and size that was charged the standard fulfilment rate is an overcharge of the fulfilment fee. Which price decides is unknown; see open question 6.

Read at run time: the price on the order (Orders `getOrderItems` `ItemPrice`), the fulfilment fee charged on that order (`listTransactions`), the low-price thresholds for the store (pages in P-ful-25), and the fee at a given price (`getMyFeesEstimateForSKU` with `PriceToEstimateFees`).

---

## 6. Inbound placement fee and inbound transport adjustments

Amazon's words:
- Jameson_Amazon, *When and how will the Placement Fees charged?*, https://sellercentral.amazon.com/seller-forums/discussions/t/5d437c4b-6e3d-49a2-8754-8c77ce1dc4c7, posted 2024-11-01 [read in official docs]:
  - "To qualify for the Amazon-optimized inbound option with no inbound fee, your shipments must include at least five identical cartons or pallets per item. Each carton or pallet must contain the same quantity per item and the same item mix."
  - "You'll be charged the FBA inbound placement service fee 45 days after your shipment is received, based on the inbound location and the quantities received."
  - Seller Central views: Payments → Transaction view → "Service fees" ("Locate your shipment ID under the Order ID field"), and the "FBA inbound placement service fee downloadable report", which "will show the inbound placement service fee charges on shipping plan, shipment, and SKU levels, and will help you identify if your shipping plan was compliant".
- Dominic_Amazon, in *Amazon is rediculously charging inbound placement fees and defect fees*, https://sellercentral.amazon.com/seller-forums/discussions/t/0d8742f3-cabc-40af-a6c1-44981cc4d3f2, thread posted 2024-09-14 [read in official docs]. The seller pasted Seller Support's reply; Dominic_Amazon answered "this is correct and the guidance provided by Seller Support is correct" and restated it: "The fee preview shown at workflow level is just an estimate. However, the actual fee is charged 45 days after your shipment is received, based on the inbound location and the quantities received. The shipment needs to be compliant to qualify for the optimized shipment."
- Jameson_Amazon, *Lost inventory and reimbursement of inventory placement fees*, https://sellercentral.amazon.com/seller-forums/discussions/t/0b434f7f-87e8-458a-a47a-743447103533 (about 2024): if a placement fee is charged on a shipment that was never received, "open a case with Seller Support". The reply does not say whether a lost-unit reimbursement covers the placement fee [read in official docs].
- Partnered-carrier measurement adjustments: News_Amazon, *Fee adjustments for partnered carrier shipment measurements*, https://sellercentral.amazon.com/seller-forums/discussions/t/a7e7de46-f082-499c-a132-4d1278f72104, posted 2025-05-12 (marketplace field US), read 2026-11-13 [read in official docs]. Sellers Ask Sellers relayed the same text on 2025-05-19 (https://sellersasksellers.com/t/fee-adjustments-for-partnered-carrier-shipment-measurements/6055):
  - "If the measured weight, dimensions, or freight class (when applicable) of your small parcel or less-than-truckload shipment differs from what you provided at shipment creation, you see a notification in the Inbound Performance dashboard."
  - Scope, in the post's opening line: "domestic US Amazon Partnered Carrier shipments".
  - "Starting on June 12, 2025, these measurement differences will result in a fee adjustment including a credit to your account if your provided measurements were too high or a charge if they were too low."
  - Where to see it: Inbound Performance dashboard → "Inaccurate transportation weight/dims" under "Defect group" → "View details".
- Placement is not charged in the EU: no EU rate card has a placement section (P-ful-6, C5).

What practitioners and sellers add [opinion]:
- Plan quote versus charge, both threads on the EU host with the US marketplace field:
  - *Wrongly charged Inbound Placement Fee* (2025-04-24, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/aa8bc021-10dd-4dd1-be40-ed1fb9dfda54): an $85 quote against $878 charged.
  - *Issue with Incorrect Placement Fee* (2025-03-19, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/e5ba7d69-030e-4c77-a9e1-f7cad75b7fb7): $1,000 quoted against $2,700 charged, for US shipments.
- Optimized-split plans recharged at minimal-split rates after part-shipments were marked abandoned or received late: 0d8742f3 above; and *[Sad] Amazon charged both an FBA inbound placement service fee and an inbound defect fee* (2025-10-30, https://sellercentral.amazon.com/seller-forums/discussions/t/7940364d-5681-4cf7-9fc7-aca2fee379ed), where the seller's split shipments were not received within 30 days of the first. A search snippet relays that abandoning part of an optimized plan is charged at the minimal-split rate [opinion, snippet only].
- Partnered-carrier reweigh disputes rejected despite photos and documents: *Partnered Carrier Fee Adjustments that began on June 12th, 2025*, https://sellercentral.amazon.com/seller-forums/discussions/t/6c798198-da2a-424c-8d39-29befc10e044. KJ_Amazon replied only "I reached out to our partner team".

Into a skill:
- The placement fee charged is set by the option's compliance, the inbound location and the received quantities. The plan-time figure is an estimate.
- An overcharge case exists when the charged option differs from the option the shipments met, or when the fee is charged on quantities or shipments never received.
- Partnered-carrier inbound transport has, since 2025-06-12, been adjusted both ways after carrier measurement.

Read at run time:
- The quote: `listPlacementOptions` `fees` / `discounts` (Fulfillment Inbound 2024-03-20, Amazon Fulfillment role).
- The confirmed option: `listPlacementOptions` status, or the plan.
- Received quantities: `listShipmentItems` / the inbound reads owned by inbound-shortfalls.
- The charge: `listTransactions` (posted a stated number of days after receipt, FE25; the shipment ID rides as the order ID on the Seller Central view; how it rides in `listTransactions` is held as open in the finance pack).
- Plan compliance: Seller Central's "FBA inbound placement service fees" report only (P-ful-6: no SP-API report).
- The carrier measurement difference: Inbound Performance dashboard, Seller Central only. `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA` (`problem-type`, `fee-type`, `fee-total`) may carry it (open question 11).

---

## 7. Low-inventory-level fee charged during an Amazon-caused delay

Amazon's words:
- Already held: the help page says "we'll automatically reimburse you if the low-inventory-level fees are charged" when an Amazon inbound delay caused them; method and exemptions are held (P-ful-7, D1).
- News_Amazon, *Update to low-inventory-level fee*, https://sellercentral.amazon.com/seller-forums/discussions/t/00fd861e-fed1-454a-970b-9d3e8384eb6a, posted 2024-05-02, read 2026-11-13 [read in official docs]:
  - "Low-inventory-level fees incurred due to excessive inbounding and processing times caused by Amazon or Amazon-managed services will be credited back to you by the 15th day of the following month." "For example, May charges with excessive inbound delays will be credited back by June 15."
  - The same post: "By May 31, you'll be credited back for any low-inventory-level fees incurred between April 1 and May 14", and from May 15 the fee "will not apply to products that have sold less than 20 units in the past 7 days".
- A search summary relays further staff replies of 2024 [read in official docs, via search summary only; pages not opened]:
  - Amazon "reimburse[s] the fees for the days in excess of the threshold".
  - Qualifying conditions are "prepare shipments for on-time pickup" (Amazon-managed transport) and "provide accurate shipment tracking information" (other carriers).
  - Disputes "can be raised on the fee with support".

Into a skill:
- Amazon states the credit for an Amazon-caused inbound delay as automatic and monthly, posted by a day of the following month. The day is in "Values that move". How much of the delay the credit covers is not stated on any page read: the "days in excess of the threshold" wording comes only from a search summary (above), and it enters no position.
- A seller's evidence of an uncaptured delay is the shipment's carrier and check-in dates.
- The fee's method changes on 2027-02-01 (P-ful-7). A charge before and after that date is judged by the method then in force.

Read at run time:
- The weekly flag and exemption: `GET_FBA_INVENTORY_PLANNING_DATA` (`Low-Inventory-Level fee applied in current week?`, `Exempted from Low-Inventory-Level fee?`, `Short term historical days of supply`, `Long term historical days of supply`; Amazon Fulfillment role).
- The fee charged: `listTransactions`. In Data Kiosk, `LOW_INVENTORY_LEVEL_FEE` is a value of `PreviewFeeType`, used only by `economicsPreview`, a forward estimate whose start date "must be not earlier than today"; it is not a named component of charged fees in `economics`, whose component breakdown is offered only for `FBA_FULFILLMENT_FEE` and `FBA_STORAGE_FEE` (`FeeType`) with free-text component names [command-verified: analytics_economics_2024_03_15.graphql, clone db2936a and upstream b13d1d1]. Whether a charged low-inventory-level amount shows as a component of the fulfilment fee in `economics` is unseen. Both datasets need Selling Partner Insights, outside the five roles (see sp-api-claims-surface SU33; FE50).
- Inbound timing: Fulfillment Inbound shipment reads (owned by inbound-shortfalls).
- The threshold and credit wording: Seller Central help *Low-inventory-level fee* (GV43F6S76Y9DHYRH).

---

## 8. Storage on a wrong volume

- Already held: storage is charged on daily average volume and collected in the following month. `GET_FBA_STORAGE_FEE_CHARGES_DATA` is Amazon's per-FNSKU, per-FC estimate (P-ful-3, P-ful-4; stock pack holding-costs.md R1).
- The report's columns include `longest_side`, `median_side`, `shortest_side`, `measurement_units`, `weight`, `item_volume`, `product_size_tier`, `fulfillment_center` and `estimated_monthly_storage_fee` [command-verified: FBA Reports page, updatedAt 2026-10-13]. So the volume Amazon used is visible per FC and month.
- Amazon's evidence rule names "月度仓储费报告或长期仓储费报告" (the monthly storage fee report or the long-term storage fee report) as the source of the dimensions used (1a, 2020 reprint). Monthly and long-term storage are itemised disputable fees under the 90-day window (section 2).
- Sellerise (2023-03-21) relays Amazon's advice to check for "discrepancies in the weight and dimensions indicated in different marketplace reports" before asking for a remeasure [opinion].
- A seller reports storage rising from about $5 to $10,000 a month after Amazon "updated our weights and sizing" (1c1a9399, 2025-03-31) [opinion].

Into a skill: a storage overcharge from measurement shows as a change in `item_volume` / `product_size_tier` for the FNSKU across months or FCs with no packaging change. Like the fulfilment fee, it is an itemised fee under the itemised window (section 2; the length is read there).

Read at run time: `GET_FBA_STORAGE_FEE_CHARGES_DATA` month by month (Pricing or Amazon Fulfillment role); the posted storage charge in `listTransactions` (account-level, `TimeRangeContext`, P-ful-16); and, for the aged surcharge, `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` (`per-unit-volume`).

---

## 9. Returns processing fee on the wrong class or count

- Already held: the US high-return-rate fee and the per-unit apparel and shoes fee, thresholds, timing, the EU 50% rule. No SP-API report breaks the returns fee down (P-ful-9; fulfilment-charges.md "Returns-processing breakdown").
- What decides the class is the product's category assignment.
  - In *Unreasonable Return Processing Fee* (EU host, US marketplace field, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/308297d2-226a-4f41-9cdf-f0b986eab027, 2024-05-27), a seller of shoe brushes was charged the per-return fee. Support's quoted reply: "Shoe brushes are considered shoe care products, and shoe care kits are also considered items subject to a return processing fee … these return processing fees are accurate and therefore a refund cannot be claimed".
  - A seller reports that the Returns Processing Fees report carries no order numbers, so charged units cannot be matched to returns (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/aa114d9f-a993-44d4-b810-ee7573f154b2, 2025-01-07).
  - [opinion]
- The staff guide of 2026-04-17 lists "customer returns fees" among itemised fees under the itemised window (section 2) [read in official docs].

Into a skill: a returns-fee overcharge is either a class error (the product treated as apparel/shoes or not) or a count error (units above the threshold). The count cannot be matched per order from any read found.

Read at run time: the fee charged (`listTransactions`). Data Kiosk `HIGH_RETURN_RATE_FEE` / `RETURN_PROCESSING_FEE` are `PreviewFeeType` values of `economicsPreview`, which estimates fees from today forward, so they show the expected fee, not a charged one [command-verified: analytics_economics_2024_03_15.graphql]. The dataset is not readable on the five roles (SU33; FE50). The returns themselves: `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` (owned by customer-returns). The over-threshold unit breakdown is in Seller Central's Amazon Fulfillment report only (P-ful-9).

---

## 10. How practitioners detect an overcharge, and the data's pitfalls

Practitioners [opinion]:
- **Baseline and diff.** These practitioners compare dated Fee Preview copies by SKU and read a fee change with no price change as a likely remeasure (Velocity Sellers 2026-09-06; My Amazon Guy 2026-05-04; Notifcentral 2026-08-07).
- **Order-level charged versus expected.** The Lingxing formula is held in sp-api-claims-surface SU44. FE34 sets the vendors' choices side by side.
  - 领星 Lingxing, *FBA费差异* help (https://www.lingxing.com/help/article/FBAFeeDifference, no date): "预计赔偿金额：= (实收FBA费-应收费用) x 该笔订单的购买数量" (expected = (fee charged − correct fee) × quantity). The correct fee is a seller-maintained field that starts at Amazon's estimated fee or a reference value computed from the seller's own carton specification and price under the store's rate rules. Credits are matched in the Date Range transaction report by "Transaction Type=Fee Adjustment", where "正数为赔偿的FBA费" (a positive amount is a reimbursed FBA fee).
  - 赛狐 Sellfox, *FBA运费差异* (https://www.sellfox.com/help/features/fba-shipping-cost-difference, no date): the expected fee "初始化等于后台预估FBA费" (starts as Amazon's estimate from the fee report). The charged fee comes from the order. Orders are flagged above a default 20% difference, from orders shipped in the last two days. "是否赔偿" (reimbursed or not) is read from Amazon.
  - These are vendor methods, not Amazon's.
- **Rate changes.** Holiday peak, the fuel and logistics surcharge and price bands raise fees without any measurement change (Leviathan Sellers 2026-10-26).
- **Duplicate fee lines.** More than one fulfilment-fee line on one order is a duplicate charge (Leviathan Sellers; Amazon's own guide says "fees are sometimes charged more than once for the same event", section 2).
- Recovery vendors list the claim type as "Pick & Pack overcharge" (GETIDA) or "Incorrect weights and dimensions" (Seller Investigators), as held in the finance pack, refunds-reimbursements-adjustments.md. Vendors and their fees belong to recovery-economics.

Amazon's reads, and their pitfalls:
- The Fee Preview report is a current snapshot with no history. Its refresh interval and request limit are sp-api-claims-surface SU20's [command-verified: FBA Reports page]. The tier column is US-only (`product-size-tier`); the EU has `product-size-weight-band`. A baseline must be kept by the reader [inferred].
- Data Kiosk `economics` needs Selling Partner Insights, which is outside the five roles (SU33). What follows is what it would open; nothing in this file is built on it (FE50). It holds charged fees per product and date range, back to the start-date limit in SU34. Each `Fee` and `FeeComponent` carries `properties`, for example "Product Size Tier, an important property that determines the amountPerUnit of FBA_FULFILLMENT_FEE". Ranges are split at Amazon fee-change dates, with `amountPerUnitDelta` across a fee change [command-verified: analytics_economics_2024_03_15.graphql]. This is the read that shows when a product's tier or per-unit fee changed. A change inside a range that is not an Amazon fee-change date is not split out (open question 4). Result retention is SU34's (P-ful-18 holds the role conflict).
- `getMyFeesEstimateForSKU` uses Amazon's measured dimensions once units are received; `getMyFeesEstimateForASIN` uses catalog size (P-ful-19). The same price giving two different fulfilment fees is a sign that measured and catalog dimensions differ [inferred].
- Catalog Items 2022-04-01 `includedData=dimensions` returns `item` and `package` dimensions per ASIN (Product Listing role) [command-verified: catalogItems_2022-04-01.json]. Whether these are Amazon's FC measurement or catalogue contributions is not stated in the model (open question 9).
- Finances keeps fees per order for the window a claim needs. The per-call span and the recent-hours gap of `listTransactions` are P-ref-23's. Finances sees further back than the itemised claim window (section 2), so an overcharge older than that window is visible in the data but past Amazon's stated limit [inferred].
- Fee-correction names in Finances and settlements are not an Amazon list. `Fee Adjustment` (transaction type), `INCORRECT_FEES_ITEMS`, `INCORRECT_FEES_NON_ITEMIZED`, `NonSubscriptionFeeAdj` and `RE_EVALUATION` are reported by practitioners (held: finance pack fulfilment-charges.md "What practitioners add", P-ref-33). `INCORRECT_FEES_ITEMS` and `INCORRECT_FEES_NON_ITEMIZED` map onto Amazon's itemised/non-itemised split of 2026, by name only [inferred; open question 3].

---

## 11. Storage and removal fees on units that are no longer Amazon's stock to store

Amazon's words:
- KJ_Amazon, reply in *New Reimbursement Policy and its consequences for Small Sellers*, https://sellercentral.amazon.co.uk/seller-forums/discussions/t/1ce28534-f796-4f93-af3f-11fc33465c91. The thread was posted 2025-04-26 and the reply on 2025-04-30 (`createdAt`); the reply carries the US marketplace field. Read 2026-11-13 [read in official docs]: "once an item is identified as lost or damaged, we also promptly stop charging other applicable fees, such as storage fees."
  - The seller's post quoted in that reply says the policy "will not reimburse shipping fees or additional charges like labeling, placement, etc." The reply does not deny it. The valuation rule, including the definition of sourcing cost that "excludes costs such as shipping, handling, customs duties, or other costs" (US policy PDF of 2024-12-19), belongs to value-and-reversals and is not restated here.
- TaylorR_Amazon, reply in *Charged for stranded inventory Amazon won't return*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/cd0bbea1-5a00-4f80-bd13-ad12b102c66c. The thread was posted 2025-06-24 and the reply on 2025-06-27; both carry the US field. Read 2026-11-13 [read in official docs]: "Once a removal order is successfully created, we do not charge storage fees on the units during the processing period until its completion."
- Held by the stock pack, not repeated: the aged surcharge's cut-off for units in a removal or disposal order (stock C6); storage and aged charges stopping when a liquidation is submitted (stock S19); researching as "misplaced or warehouse damaged units that are actively being confirmed" and its time limits (stock W14, W15).
- Removal and disposal fees are "non-itemized" FBA fee errors under the longer limit in Amazon's staff guide (section 2, FE9). The per-unit charging rule and the inferred rule that a removal fee needs a removed or disposed unit belong to removals-disposals (see removals-disposals RM26, RM27).

What practitioners and sellers add [opinion]:
- A seller reports storage still being charged on stranded units across more than 30 failed removal requests (cd0bbea1, 2025-06-24). Another seller in the same thread had heard the rule that TaylorR_Amazon then confirmed.
- A seller reports long-term storage charged after inventory was lost (seen in search results only; thread not identified) [opinion, snippet].
- Recovery vendors list "Lost Removal Order" ("Inventory has been requested to be removed from FBA but not all inventory arrived", GETIDA *How we help*, © 2026, read 2026-11-13) as a claim for the units, not for the fee. No vendor page read names a storage-fee-on-lost-units claim of its own.

Not found on any page read:
- Whether storage charged between a unit's loss and the adjustment that identifies it is refunded.
- Whether researching units bear storage.
- Whether a lost-in-transit removal reimbursement includes the removal fee paid on that unit.

Into a skill:
- Amazon staff state that storage stops once a unit is identified as lost or damaged, and that units in a created removal order bear no storage while the order is processed.
- A storage line on an FNSKU, FC and month whose units had already been adjusted out as lost or damaged, or were already inside a created removal order, has no basis in those statements [inferred].
- A removal or disposal fee is a non-itemised fee error under the staff guide's longer limit.

Read at run time:
- The date units were adjusted lost or damaged: the Inventory Ledger, owned by fc-lost-damaged.
- The units Amazon charged storage on: `GET_FBA_STORAGE_FEE_CHARGES_DATA` `average_quantity_on_hand` per FNSKU, FC and `month_of_charge`. Whether that count includes researching or removal-pending units is not stated (open question 15).
- The removal order's creation date and its quantities: Removal Order Detail (stock S18; removals-disposals RM20).
- The removal fee per order line: Removal Order Detail `removal-fee`, and Finances.

## 12. Storage on stranded units that Amazon caused

Amazon's words:
- Bryce_Amazon, *Resolving Stranded FBA inventory*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/f77cbf98-0f2f-4834-8d3f-9eb9cfe84c8e, posted 2024-03-12 (US field), read 2026-11-13 [read in official docs]: "Product listing issues, infringement concerns, or system errors can also result in stranded inventory." In the same thread a seller asked "Why should sellers have to pay storage fees or removal fees/disposal fees when listings are falsely flagged or Amazon has a system error?" No staff reply answers it [opinion: the seller].
- What stranding is, its reasons, its automatic removal and the stranded report: stock S1–S5 (and the stock pack's `stuck-stock/references/stranded.md`). The stock pack records as open that no Amazon sentence it read says in terms that stranded units accrue storage (stuck-stock.md O17).
- No Amazon page read offers a storage credit for stranded units, whatever the cause. Amazon's staff guide lists storage among itemised FBA fee errors "typically related to incorrect weight or dimension measurements" (section 2). It does not say whether a stranding Amazon caused makes the storage a "fee charged in error".
- A seller whose account was deactivated reports $3,000 a month in storage on stranded stock (https://sellercentral.amazon.com/seller-forums/discussions/t/00896ca4-2983-4741-9577-db40a2e2eda2, 2025-03-12, US field) [opinion]. The thread shows no staff reply.

Into a skill:
- No Amazon rule read provides for refunding storage on stranding Amazon caused. A seller's case for it rests on the stranding reason and its dates, not on a named policy.
- A removal order stops storage while it is processed (section 11).

Read at run time: the stranded reason and its date, from `GET_STRANDED_INVENTORY_UI_DATA` (`stranded-reason`, `date-stranded`; stock S2); the listing issue behind it, from the Listings Items API (stock S8); and the storage charged over those months, from the storage fee report.

## 13. Partnered-carrier charges on cancelled shipments and unused labels

Amazon's words:
- The void rule is held by the stock pack: confirming a partnered-carrier transportation option agrees to the charge, which can be voided within a window by shipment type; outside it, charges "may apply"; the limits do not apply to non-partnered options; `cancelInboundPlan` cancels the whole plan (stock I16). The window lengths are in "Values that move".
- The v2024-03-20 model carries the deadline per option: `Quote` ("The estimated shipping cost associated with the transportation option") has `cost`, `expiration` and `voidableUntil` ("Voidable until timestamp"). `cancelInboundPlan` says "Charges may apply if the cancellation is performed outside of a void window" [command-verified: fulfillmentInbound_2024-03-20.json at db2936a, lines 1356, 14131–14150].
- TaylorR_Amazon, reply in *Unused Shipping Label Refund*, https://sellercentral-europe.amazon.com/seller-forums/discussions/t/407a9a34-1e72-4b5b-a1ae-5b8e8e04cb9a. The thread was posted 2024-12-23 and the reply on 2025-01-14 (US field). Read 2026-11-13 [read in official docs]: "To get a full refund of shipping charges from an Amazon partnered carrier, you must void the shipment within the specified cancellation window", with separate windows for small parcel and pallet shipments, and "You can void shipments with a non-partnered carrier at any time."
- Sarah_Amzn, in *Pallet Collection Not being Refunded* (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/85f330d7-e6e3-4424-b4ba-1ff3f49c1646, UK field, 2025-05-13), asked only for the case ID [read in official docs].

What sellers and vendors add [opinion]:
- UK sellers (UK field) describe partnered charges for service never given:
  - a pallet the carrier did not collect, where Seller Support declined because the void window had passed (85f330d7, 2025-05-01);
  - a carrier that cancelled the collection itself, refused for the same reason (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/753ca1510c223bf63e95a5fbb12e0c1a, 2020-10-28);
  - a shipment closed before the partnered carrier collected it (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/2072bdbf-3b96-4327-918e-a61f03af0067, 2024-09-17).

  No outcome is shown in these threads.
- Vendors list the claim kind: GETIDA's "Cancelled Shipping Costs": "Shipping charges have been paid to Amazon for inbound partner carrier shipments but were not used" (*How we help*, © 2026, read 2026-11-13). Threecolts Margin Pro lists "unused shipping labels" (recovery-economics vendor table).
- Partnered-carrier measurement adjustments after carrier reweigh are section 6 (FE27).

Into a skill:
- Within the void window the partnered charge is refunded in full by voiding. Outside it, Amazon's texts say only that charges "may apply".
- No Amazon page read provides for refunding a partnered charge when the carrier did not perform. Vendors treat it as a claim kind.
- Amazon's staff guide does not name partnered-carrier charges in either fee class, so the window for such a request is not stated (open question 17).

Read at run time:
- The option chosen, its quote and its void deadline: `listTransportationOptions` `quote.cost`, `quote.voidableUntil` (Amazon Fulfillment).
- Whether the plan or shipment was cancelled, and when: `getInboundPlan` status `VOIDED`, and shipment status `CANCELLED` (stock I7).
- Whether the carrier ever moved it: the shipment's tracking (inbound-shortfalls).
- The charge and any refund: Finances `listTransactions`.
- Whether a refund was requested inside the window cannot be read; Seller Central shows only the void action.

## 14. Unplanned prep and labelling fees; the inbound defect fee

Amazon's words, unplanned services:
- KJ_Amazon, *FBA Inbound Convenience Fees*, https://sellercentral.amazon.co.uk/seller-forums/discussions/t/7c433b9f-77c9-40a6-aaf6-5871daf3ce67, posted 2025-01-24 (US field), read 2026-11-13 [read in official docs]: "FBA may charge these fees (also known as FBA inbound convenience fees) if the items you shipped to the fulfillment centers did not include the required label or prep." The post sends the reader to the *Unplanned Services* help page for rates and for "how you can dispute any fees you believe were charged in error".
- Roberto_Amazon, reply of 2024-07-30 (US field) in *Discrepancy in Box Weight / Box Over Weight*, https://sellercentral.amazon.in/seller-forums/discussions/t/b8734d29-8e4a-4f21-8648-bfa42b623429 [read in official docs]: "If you wish to appeal the unplanned service fees, please raise a dispute in the problems tab under Shipment summary."
- Bryce_Amazon, replies of 2025-08-04 and 2025-08-08 (US field) in *New FBA Prep Rule (Jan 1, 2026) – Seller Risk & Unplanned Prep Fees*, https://sellercentral.amazon.com/seller-forums/discussions/t/32e1d348-10b4-46ae-ae29-74a0cb3b182a [read in official docs]:
  - "If we determine that a product has missing or improper prep/label, we will flag it as a defect and apply the prep/label."
  - "products with missing or defective labels could be untraceable in our facilities. These products aren't eligible for reimbursements."
  - "Prep defects flagged in the Inbound Performance Dashboard do not impact the overall Account Health Rating."
- The *Unplanned services* help page (201000230) is a script shell to a plain GET (checked 2026-11-13, about 171 KB with no policy text). By search summary only: a fee is charged "only when we provide you an image to help illustrate the reported problem", and "we will only consider investigation requests you submit within 30 days of when the problem is reported to you" [opinion, snippet; the finance pack carries the same snippet at fulfilment-charges.md I3].
- Amazon's 2026 staff guide puts "prep and labeling fees" among non-itemised FBA fee errors, under the longer limit (section 2). That conflicts with the help page's dispute limit as relayed by the snippet. Both are kept: the guide is read, the help page is not.
- Held elsewhere: the end of US prep and label service on 2026-01-01 (stock I19); the Inbound Performance report's columns, and the fact that it itemises these fees (finance P-ful-24; stock inbound.md D5).

Amazon's words, the inbound defect fee:
- Held elsewhere: one inbound defect fee replaced the double charge from 2026-01-15 (finance P-ful-24, fulfilment-charges.md J1). Abandoning or deleting a shipment of a multi-shipment plan creates a defect subject to the fee and re-prices placement (stock I13).
- News_Amazon, *Temporary peak season extensions for international FBA shipments*, https://sellercentral.amazon.com/seller-forums/discussions/t/f25ba535-e06e-4fa3-8bb0-cb3a095fd696, posted 2026-10-30 (US field), read 2026-11-13 [read in official docs] (also in the stock pack, inbound.md §D1):
  - "You won't be charged the deleted or abandoned defect fee as long as your remaining shipments are received within 45 days of the first receive."
  - "The defect will still be flagged on your Inbound Performance Dashboard but the fee is waived for eligible shipments … Any inbound defect fees already charged on eligible shipments will be reimbursed. Go to your Reimbursement report to view details. No action is required."
- The *Inbound defect fees* help page (GL5XA3MNXAJKJE8E) is a script shell to a plain GET (checked 2026-11-13). No dispute window for the defect fee was found on any page read.

What sellers add [opinion]:
- A seller charged both a placement fee and an inbound defect fee after split shipments arrived late (7940364d, section 6).
- AMZ123 posts (2026-10/11) relay the peak waiver. One says some sellers saw no refund mail and should check the account themselves (search summary only).

Into a skill:
- An unplanned prep or label fee is charged per unit when Amazon applies prep or labels that the shipment lacked, and it is disputed from the shipment's problems view.
- The limit for that dispute is stated two ways: from the problem report on the help page (snippet only), and under the non-itemised limit in the staff guide.
- An inbound defect fee that Amazon waives under a stated programme is credited automatically and shown in the Reimbursements report, not only in Finances.

Read at run time:
- Each unplanned-service or defect fee per shipment, carton and FNSKU: `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA` (`issue-reported-date`, `problem-type`, `coaching-level`, `fee-type`, `fee-total`; Pricing or Amazon Fulfillment).
- Receive dates of a plan's shipments: inbound reads (inbound-shortfalls).
- A defect-fee credit: `GET_FBA_REIMBURSEMENTS_DATA`. Its `reason` value for this credit is unseen (open question 19).
- The posted charge: Finances. A settlement row reads `amount-type` `Inbound Defect Fee` (finance pack reconciliation.md, issue #5353).

## 15. AWD fees on box dimensions; Subscribe & Save; former Small and Light

AWD, Amazon's words: *Amazon Warehousing & Distribution Service Terms*, "Dated: January 14, 2026", https://supplychain.amazon.com/legal/service-terms/warehouse-and-distribution, read 2026-11-13 [read in official docs]. Section 4.2, *AWD fee reimbursement for box dimensions*:
- "This provision applies to the reimbursement of AWD storage and transportation fees that we determine were charged using inaccurate box dimensions. This provision does not apply to fee types besides AWD storage and transportation fees."
- "we will reimburse you the difference between the fees as charged and the fees based on the corrected measurements. If the dimensions that you provide vary from our verified measurement, our measurement will govern."
- "A box is not eligible for a remeasurement request if the box has already been remeasured twice in the past 60 days, or if there are no available boxes of that MSKU at an AWD site."
- "Claim window: You must submit your request within 90 days of the date on which the fee was charged. Claims submitted outside of this window are not eligible for reimbursement."
- "review the dimension data in your fee reports … contact Amazon Support or your account manager and open a research request. Amazon will only accept one claim per fee charge."
- inbound-shortfalls IN33 hands this window to this file. AWD's scope and readability are the stock pack's: W38 (AWD is not readable on the five roles) and W41.

Into a skill: AWD storage and transportation fees follow their own box-dimension rule. It has the same shape as the FBA rule (Amazon's measurement governs, a per-box remeasure limit, a window from the charge date, one claim per charge) but sits in the AWD terms, and the request goes to Amazon Support or the account manager. The values are in "Values that move".

Read at run time: the terms in force (supplychain.amazon.com, the dated page). AWD fee lines and box dimensions cannot be read on the five roles (stock W38); Finances shows the charges.

Subscribe & Save: no Amazon page read names a fee claim of its own for Subscribe & Save. What the programme is, its eligibility and its Replenishment API are stock O13 and O14. A fee on a Subscribe & Save order is one of the order's ordinary fee lines and falls under the sections above [inferred].

Former Small and Light: the programme closed in 2023 and Low-Price FBA is a rate by price (stock G21). A unit once in Small and Light has no separate claim. Its fulfilment fee is judged under section 5 (low-price FBA) or the standard rate [inferred].

---

## Positions

FE1. **Definition.** For this area, a fee overcharge is a fee charged on a basis Amazon's own rule did not support for that unit, shipment or period. The types are:
- a wrong measurement or tier (fulfilment, storage, aged, returns, removal and placement fees ride on it);
- a wrong referral-fee category;
- an eligible rate not applied (low-price FBA, compliant placement option);
- a fee Amazon says it credits (low-inventory-level during Amazon-caused inbound delay);
- a fee on units or shipments never received;
- a duplicate fee line.

A fee rise from an announced rate change, peak period, surcharge or price band is not an overcharge. Sources: Roberto_Amazon staff guide (ce0bea71, 2026-04-17; ff7c3c15, 2026-05-13); News 00fd861e (2024-05-02); Jameson_Amazon 0b434f7f. [read in official docs; the grouping is inferred]

FE2. **Amazon's measurement governs, by default.** Outside the EU certification regime, the weight and dimensions Amazon verifies set every size-tier-based fee. Seller measurements alone are not accepted to contest them, and repeated inconsistent FC measurements resolve to the largest. Already held in finance pack P-ful-2. Added here: the "largest dimensions" rule and "personal measurements are not accepted". Sources: NR_Amazon ca22eab2 (2025-04-30, US field); Glenn_Amazon ae6a5220 (reply 2023-11-14, US field). [read in official docs] Read at run time: Seller Central help GL7U4JFSDXUTQAJ and G6WAEPTECPT2JUH3, as the seller's store shows them.

FE3. **Each variation is its own product.** A fee or measurement on one variation is no evidence for another, and a remeasure covers the FNSKU requested. Sellers report remeasures that changed one colour or size and not its siblings. Sources: Glenn_Amazon ae6a5220 (2023-11-06) [read in official docs]; AMZ123 2021-04-20 [opinion].

FE4. **Remeasurement conditions.**
- A remeasure needs a sellable unit in an FC.
- It is refused for an FNSKU already remeasured a stated number of times in a stated period, or once the account's monthly limit is used.
- Amazon states a typical turnaround.
- Amazon asks that only requests expected to change fees be filed.
- Staff can add a request beyond the monthly limit when given a case ID.

No SP-API operation requests or reads a remeasurement (see sp-api-claims-surface SU12). The monthly account limit and the turnaround as a reply time are filing-and-conduct's (see filing-and-conduct FL35, FL30). Sources: NR_Amazon ca22eab2 (2025-04-30, US field); KJ_Amazon 958851b3 (2024-09-20, US field) [read in official docs]. Read at run time: the per-FNSKU limit from Seller Central help *Understanding item package weight and dimensions* (G6WAEPTECPT2JUH3, https://sellercentral.amazon.com/help/hub/reference/external/G6WAEPTECPT2JUH3), as the seller's store shows it. The account's remaining count cannot be read (Seller Central widget only). The values seen are in "Values that move".

FE5. **History: EU certified dimensions.**
- From 2025-08-01, sellers with a German business address were asked to certify package dimensions for Amazon.de [opinion: Valuezon, July 2025, relaying Amazon].
- Amazon.de existing ASINs were to be certified by 2026-04-30, large and heavy bulky excluded (Global Selling notice, 2026-03-06).
- From 2026-05-05, certified dimensions calculate FBA fees on amazon.co.uk, .fr, .it, .es (Amazon policy PDF, created 2026-03-30). The standard-size verification ran to 2026-07-05 and also covered DE large items [opinion: cifnews 2026-05-18, relaying Amazon].
- UK/FR/IT/ES large-item certification was due 2026-10-15 [opinion: 九方 2026-09-01].

[read in official docs + opinion as marked]

FE6. **Certification rules.**
- Certification means measured "with a device that complies with the EU Measuring Instruments Directive, such as, a tape measure".
- Dimensions not verified by the deadline are deemed certified.
- New listings must carry certified dimensions; on Amazon.de, the dimensions entered at listing creation are the basis.
- Amazon validates and may replace incorrect dimensions with its own certified dimensions.
- A seller appeals through the remeasure widget, within the monthly limit.

Sources: *FBA item package dimensions certification policy* PDF; Global Selling notice news-notices-260306 (2026-03-06). [read in official docs] Read at run time: whether the seller's store and tier are under the regime, from the policy PDF (https://m.media-amazon.com/images/G/02/MP/phase-3policy.pdf) and Amazon's Global Selling notices. Certification status per ASIN cannot be read through the SP-API.

FE7. **Automatic look-back true-up under certification.** Amazon's Amazon.de notice states that if the certified dimensions lower FBA fees, the system automatically compensates the fee difference for a look-back period ("最高追溯", up to a stated number of days). It limits the automatic part to items sold on Amazon.de. Practitioners relay the same for the UK/FR/IT/ES phases. No Amazon page read states an automatic true-up in the US. Sources: news-notices-260306 (2026-03-06) [read in official docs]; cifnews 186018 (2026-05-18), 九方 11810 (2026-09-01) [opinion]. Read at run time: the look-back length from the store's certification notice. The lengths seen are in "Values that move".

FE8. **Contradiction, EU storage.** The *Rate Card Europe Fees* effective 2026-11-02 (FAQ Q2) still says Amazon's measurement governs storage volume. The certification policy (effective 2026-05-05) says certified seller dimensions calculate "FBA fees" in UK/FR/IT/ES. No page read says whether storage falls under certification. Both stand, with their dates. Sources: EU rate card 2026-11-02 [command-verified, PDFKit]; certification policy PDF [read in official docs].

FE9. **The two FBA-fee windows.** Amazon staff state:
- A window counted from each charge's date for "itemized" FBA fee errors. These are fees tied to an ASIN/FNSKU, typically weight or dimension errors: fulfilment, customer returns, monthly storage, long-term storage.
- A separate, longer limit for "non-itemized" errors: removal or destroy orders, prep and labelling.

Sources: Roberto_Amazon ce0bea71 (2026-04-17, US field) and ff7c3c15 (2026-05-13, UK field); Glenn_Amazon ae6a5220 (2023-11-14, US field); policy reprint, LianLian 2020-09-15. [read in official docs] Read at run time: the windows from Seller Central help *FBA fees reimbursement policy: Weight and dimensions* (GL7U4JFSDXUTQAJ, https://sellercentral.amazon.com/help/hub/reference/external/GL7U4JFSDXUTQAJ) and from the latest Amazon staff guide on disputing charges for the seller's store; the charge date from `listTransactions` `postedDate`. The lengths read, by store, are in "Values that move". No length was read for JP, CA or any other store.

FE10. **History of the fee window.**
- The policy added a limit on weight and dimension fee claims around May 2019. It replaced a less strict limit that the article does not state [opinion: 52by, 2019-05-22].
- The Australia News post that revised FBA inventory claim windows from 2025-10-15 does not cover fee claims (News d8f9a56c, AU field) [read in official docs].
- Finance pack P-ful-2 and the survey's row stand for the itemised window. Neither holds the non-itemised limit (FE9).

FE11. **One claim per charge.** Amazon allows one claim per fee charge under both the weight-and-dimension fee policy and the referral-fee policy (whose decision is final). The weight-and-dimension policy text, as a seller quotes it, adds: "Only one request needs to be created for an FNSKU". Sources: policy reprint (LianLian 2020-09-15); Spencer_Amazon 3432aad2 (2024-05-24); Roberto_Amazon ce0bea71; seller quoting GL7U4JFSDXUTQAJ in 9c2edbce (2024-12-10). [read in official docs]

FE12. **A remeasure is a step before a fee reimbursement, and support may set a wait.** A US staff member called remeasurement "a step that needs to occur prior to a successful reimbursement requests". In that case Seller Support had set a wait before the remeasure. Source: Bryce_Amazon 9c2edbce (2024-12-10, US). [read in official docs] The wait was specific to that case: one statement, and no rule page found. Its length is in "Values that move".

FE13. **Amazon can credit a dimension correction per order, without a reimbursement ID.** Amazon staff described a weight and dimension correction paid as one "Fee Adjustment - Weight and Dimension Change" entry per affected order. It shows under Transaction Type "Other" in Seller Central's Transaction View, with the order ID and the amount in the "Amazon fees" column, and "these adjustments do not generate a reimbursement ID". So it does not appear in `GET_FBA_REIMBURSEMENTS_DATA` by reimbursement ID. Source: Sandy_Amazon 29fbd69b (thread 2025-02-05). [read in official docs] This answers in part the finance pack's open question 12 (fulfilment-charges.md): Amazon's word is per-order fee adjustments, not one lump. The `listTransactions` encoding is still unseen.

FE14. **A corrected measurement does not prove past fees came back.** In the US, sellers report refusals after Amazon confirmed a wrong measurement ("The $88.93 fee was correctly calculated based on the (incorrect) measurements at that time", 2026). In 4a8a5cd9 staff (Josh_Amazon) advised a new case "specifically requesting an order-level audit and refund"; in fe4a0969 staff (Christine_Amazon) said only that a resolution had been given on the seller's case, and the outcome is not shown. The seller in 4a8a5cd9 reports no reimbursement and an "automated loop", not a written refusal. Practitioners agree that a remeasure fixes future fees only. Sources: fe4a0969 (2026-04-03), 4a8a5cd9 (2026-10-08) [opinion, with staff replies read in official docs]; Velocity Sellers, Leviathan Sellers, My Amazon Guy, Notifcentral [opinion].

FE15. **What Amazon support has asked for.** In a 2025 case, Selling Partner Support's leadership team asked for a file listing, per FNSKU, the incorrect fee, the correct fee, the difference and the total; earlier, one FNSKU and quantity per line. The staff guide asks for shipment IDs, FNSKUs and evidence such as measurements and photos. Sources: support messages relayed in 1c1a9399 (2025-04-04, 2025-04-05); Roberto_Amazon ce0bea71. [read in official docs; the support messages are relayed by a seller] Case mechanics belong to filing-and-conduct.

FE16. **Storage fees are disputable as itemised fees.** Amazon's 2026 staff guide lists monthly and long-term storage among itemised FBA fee errors. The policy's evidence rule names the storage and long-term storage reports as the source of the dimensions used. A support agent's statement that storage fees "can never be reimbursed" (2025) conflicts with both; it is kept as a seller report. Sources: ce0bea71; LianLian reprint 2020; 29fbd69b [read in official docs / opinion as marked].

FE17. **The reads that show the measurement used.**
- `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` carries the dimensions and weight per SKU (tier only in the US; `product-size-weight-band` in the EU). It is a current snapshot whose refresh and request limits are sp-api-claims-surface SU20's.
- `GET_FBA_STORAGE_FEE_CHARGES_DATA` carries dimensions, weight, `item_volume` and tier per FNSKU, FC and month.
- Both need the Pricing or Amazon Fulfillment role.

Sources: FBA Reports page (updatedAt 2026-10-13) [command-verified]; roles in finance pack P-ful-20 and SU3.

FE18. **The read that would date a tier change, outside the five roles.** Data Kiosk `economics` returns charged fees per product, with `properties` (for example Product Size Tier) per date range, split at Amazon fee-change dates with `amountPerUnitDelta`. It would show when a product's tier and per-unit fulfilment fee changed. The Economics dataset needs the Selling Partner Insights role, which is outside the five roles (see sp-api-claims-surface SU33). So this read is listed with what it would open, and nothing is built on it (FE50). Its start-date limit and retention are SU34's. Source: analytics_economics_2024_03_15.graphql [command-verified]; role per Amazon's *Correction: Data Kiosk role requirements* via SU33 [read in official docs].

FE19. **Pitfall: no history in the Fee Preview.** Amazon keeps no history in the Fee Preview report and sends no notice of a remeasure. On the five roles, a tier change is therefore dated only by comparing dated copies of the report that the reader has kept. Data Kiosk `economics` history would date it, but needs a role outside the five (FE18, FE50). Sources: FBA Reports page [command-verified]; Velocity Sellers 2026-09-06 [opinion]; the consequence is [inferred].

FE20. **Pitfall: rate changes look like overcharges.** A fulfilment fee rises without any measurement change across:
- the holiday peak (P-ful-1, P-ful-22);
- the fuel and logistics surcharge (P-ful-8);
- a price-band crossing (P-ful-25);
- an annual fee change.

The dates of Amazon's fee changes and peak periods are the finance pack's (P-ful-*). Sources: finance pack positions cited; Leviathan Sellers 2026-10-26 [opinion]. (`economics` splits ranges at Amazon fee-change dates but not at a price-band crossing [command-verified]; it is outside the five roles, FE50.)

FE21. **Signal: SKU estimate against ASIN estimate.** `getMyFeesEstimateForSKU` uses Amazon's measured dimensions once units are received; `getMyFeesEstimateForASIN` uses the catalog size. At the same price, a different fulfilment fee between the two is a sign that the measured and catalog dimensions differ. Sources: Product Fees API page and productFeesV0.json (held P-ful-19); the use is [inferred].

FE22. **Referral-fee dispute window removed, 2022.** On 2022-03-16, Amazon removed the 90-day dispute window from the referral fee reimbursement policy and introduced fee category guidelines. A seller reports a phone agent citing a 90-day "Internal Policy" (about 2023). Sources: News *Fee categories made easier to understand* (972575, 2022-03-16) [read in official docs, command-verified date]; CA forum 5c1e41df [opinion].

FE23. **Referral reimbursement basis, from 2023-01-13.** Reimbursement is at "the referral fee rate effective at the date of the disputed transaction". Disputes "contrary to guidelines that are in effect at the time of the fee transaction will be declined". One claim per charge. The policy "does not apply to other fee reimbursements". Source: Spencer_Amazon 3432aad2 (2024-05-24, UK field). [read in official docs] It upgrades the snippet-only line in finance pack selling-fees.md A5 to a read page. No US-field text of the same policy was read. Read at run time: Seller Central help *Referral fees reimbursement policy* (GRRJCFXD6474GRLY, https://sellercentral.amazon.com/help/hub/reference/external/GRRJCFXD6474GRLY) and the fee category guidelines, as the seller's store shows them.

FE24. **Pitfall: no fee category in the SP-API Fee Preview.** The SP-API Fee Preview report has no fee-category column (`product-group` and `estimated-referral-fee-per-unit` only), though Amazon's 2022 post says the Seller Central Fee Preview shows upcoming fee-category changes. Sources: FBA Reports page [command-verified]; News 972575 [read in official docs].

FE25. **Placement fee: quote against charge.** The placement fee shown in the shipping workflow "is just an estimate". The fee is charged a stated number of days after receipt, on the inbound location and the quantities received. The no-fee optimized option needs compliance, including a stated minimum of identical cartons or pallets per item, with the same quantity and the same item mix. Seller Central's placement fee report shows plan compliance by plan, shipment and SKU; no SP-API report does. Sources: Dominic_Amazon 0d8742f3 (2024-09-14); Jameson_Amazon 5d437c4b (2024-11-01) (both US field) [read in official docs]; P-ful-6 (no SP-API report). Read at run time: the timing and option rules from Seller Central help *FBA inbound placement service fee* (GC3Q44PBK8BXQW3Z); the quote from `listPlacementOptions`. The values seen are in "Values that move".

FE26. **Placement fee on a shipment never received.** Amazon staff direct a seller to open a Seller Support case when a placement fee is charged on a shipment never received. No page read says whether a lost-unit reimbursement includes the placement fee paid on that unit. Source: Jameson_Amazon 0b434f7f [read in official docs].

FE27. **History: partnered-carrier measurement adjustments.** From 2025-06-12, on "domestic US Amazon Partnered Carrier shipments", a difference between the seller-entered and the carrier-measured weight, dimensions or freight class of a small parcel or LTL shipment results in a fee adjustment: a credit if the seller's figures were too high, a charge if too low. It shows in the Inbound Performance dashboard under "Inaccurate transportation weight/dims". Sellers report that their disputes of such charges were rejected. Sources: News_Amazon a7e7de46 (posted 2025-05-12, US field) [read in official docs]; Sellers Ask Sellers 6055 (relay, 2025-05-19); forum 6c798198 [opinion].

FE28. **Low-inventory-level fee during Amazon-caused delay.** Amazon credits low-inventory-level fees caused by Amazon or Amazon-managed inbound and processing delays. The credit is monthly, posted by a stated day of the following month. The help page calls the reimbursement automatic (via P-ful-7). How much of a delay the credit covers is not stated on any page read; the search-summary wording is kept only in section 7, outside this position. Sources: News 00fd861e (2024-05-02, US field) [read in official docs]; GV43F6S76Y9DHYRH via P-ful-7. Read at run time: the credit timing and conditions from Seller Central help *Low-inventory-level fee* (GV43F6S76Y9DHYRH); the seller's weekly fee flag from `GET_FBA_INVENTORY_PLANNING_DATA` (Amazon Fulfillment role). The day seen is in "Values that move".

FE29. **Returns fee class follows category assignment.** Whether the per-return fee or the high-return-rate threshold rule applies follows the product's category assignment, which Amazon decides. A shoe-care product was held to be in the shoes class and the fee accurate. Source: support reply quoted in 308297d2 (2024-05-27) [opinion, relayed]; class rules held in P-ful-9.

FE30. **Pitfall: returns fee units cannot be matched to orders.** The returns processing fee's charged units cannot be matched to individual returns from any report found: sellers report the Seller Central returns-fee report has no order numbers, and no SP-API report breaks the fee down. Sources: aa114d9f (2025-01-07) [opinion]; finance pack fulfilment-charges.md, report table [command-verified there].

FE31. **Low-price FBA.** Low-price FBA rates apply automatically to eligible units, with no enrolment. No Amazon page read states which price, at which moment, decides eligibility. A unit eligible on Amazon's stated criteria but charged the standard rate is a fulfilment-fee overcharge [inferred]. Sources: sell.amazon.es low-price FBA page (2026) [read in official docs]; P-ful-25. Read at run time: the price thresholds and size limits for the seller's store, from the pages in P-ful-25 and *Low-price FBA rates* (https://sell.amazon.es/en/tarifas-precio-bajo-logistica-de-amazon, ES/EU). The thresholds and limits read, by store and date, are in "Values that move". The page's Spain FAQ line matches its earlier criteria set; it is a stale line, not a contradiction.

FE32. **Pitfall: Finances sees further back than the claim window.** The data that shows an overcharge reaches further back than the claim window: `listTransactions` covers longer periods by repeated spans (P-ref-23). Charges older than the itemised window are visible in the data but past Amazon's stated limit. Sources: P-ref-23; FE9. [inferred] (Data Kiosk `economics` would reach further, outside the five roles: FE50.)

FE33. **Pitfall: fee-correction names are open.** Fee corrections reach the seller's money records under names Amazon does not list: `Fee Adjustment`, `INCORRECT_FEES_ITEMS`, `INCORRECT_FEES_NON_ITEMIZED`, `NonSubscriptionFeeAdj` and `RE_EVALUATION`, as reported by vendors. The pairing of the two `INCORRECT_FEES_*` names with Amazon's itemised/non-itemised windows is by name only. Sources: finance pack fulfilment-charges.md "What practitioners add" and P-ref-33 [opinion]; Synder and AMALYTIX glossaries (seen as search summaries) [opinion]; the pairing is [inferred].

FE34. **Vendor detection methods, side by side.** Practitioners use different detection methods. None is Amazon's, and none is the method. [opinion]

| Choice | Expected fee taken from | Charged fee taken from | Unit flagged when | Credit matched by | Who |
|---|---|---|---|---|---|
| Order-level difference with a seller-kept expected fee | Amazon's estimated fee, or a value the seller computes from their own carton specification and price under the store's rates (seller-editable) | the order's fee | any difference; amount = (charged − expected) × quantity | "Fee Adjustment" rows in the Date Range transaction report, positive amount | 领星 Lingxing *FBA费差异* (held in sp-api-claims-surface SU44) |
| Order-level difference against Amazon's own estimate | Amazon's estimate from the fee report | the order's fee | difference above a vendor default percentage, on recently shipped orders | Amazon's "reimbursed or not" field | 赛狐 Sellfox *FBA运费差异* |
| Baseline and diff of the Fee Preview | a dated earlier copy of the Fee Preview | the current copy | the fee moved with no price change | none | Velocity Sellers; My Amazon Guy; Notifcentral |
| SKU estimate against ASIN estimate | `getMyFeesEstimateForASIN` (catalogue size) | `getMyFeesEstimateForSKU` (measured) | the two differ at one price | none | this seat's reading of P-ful-19 (FE21) [inferred] |

The vendor default threshold is the vendor's own and is not a threshold of this file. Sources: Lingxing FBAFeeDifference; Sellfox fba-shipping-cost-difference; Velocity Sellers 2026-09-06; My Amazon Guy 2026-05-04; Notifcentral 2026-08-07.

FE35. **Measured effects (examples, not rates).**
- US sellers report $40.43 → $88.93 per order over 29 orders ($1,392; 2026-04-03).
- 378 orders and USD 438.52 over 2026-03-31 to 2026-06-29 (2026-10-08).
- $12.93 charged at $28.51 after a mis-measure to 48 lb (2024-12-10).
- One German womenswear seller reportedly saved €0.75 per unit after certifying 500+ ASINs (search summary of a Chinese source, not opened).

Sources: fe4a0969, 4a8a5cd9, 9c2edbce [opinion]. Individual cases only: no study of frequency or size was found.

FE36. **Packaging drives most measurement differences.** Amazon names the packing material as the most common cause of seller-versus-FC differences, and measures loose bag flaps and handles edge to edge. A packaging change after first receipt is a cause practitioners name for remeasures. Sources: NR_Amazon ca22eab2 (2025-04-30); Dominic_Amazon c6f1274b (2024-08-22) [read in official docs]; Velocity Sellers [opinion].

FE37. **Amazon's named route for FBA fee errors.** Amazon's staff guide names the case path for FBA fee errors as Help > Contact Us > Shipping & FBA > FBA Issue > "Fees Charged in Error". For referral fees it names Selling Partner Support, with the Custom Unified Transaction report. No SP-API operation files either (see sp-api-claims-surface SU8, SU12). Case mechanics and conduct are filing-and-conduct's. Sources: ce0bea71 (US field) / ff7c3c15 (UK field) [read in official docs].

FE38. **Storage stops when a unit is identified lost or damaged.** Amazon staff state that "once an item is identified as lost or damaged, we also promptly stop charging other applicable fees, such as storage fees". A storage charge on units already adjusted out as lost or damaged has no basis in that statement [inferred]. No Amazon text read says:
- whether storage charged between the loss and its identification is refunded;
- whether the lost-unit reimbursement covers fees paid on the unit (its value is value-and-reversals').

Source: KJ_Amazon, reply in 1ce28534 (2025-04-30, US field) [read in official docs]. Read at run time: the date of the lost or damaged adjustment from the Inventory Ledger (fc-lost-damaged), against `GET_FBA_STORAGE_FEE_CHARGES_DATA` `average_quantity_on_hand` per FNSKU, FC and month.

FE39. **Storage on researching units is not stated.** Amazon defines researching units as "misplaced or warehouse damaged units that are actively being confirmed" (stock W14, W15). No Amazon text read says whether they bear storage, or whether the storage report's quantity counts them (open question 15). Sources: stock W14, W15; absence across the pages read. [inferred from absence]

FE40. **No storage while a removal order is processed.** Amazon staff state that "Once a removal order is successfully created, we do not charge storage fees on the units during the processing period until its completion." Storage charged on units inside a created removal or disposal order, during its processing, has no basis in that statement [inferred]. The aged surcharge's own cut-off is stock C6, and liquidation is stock S19. Sources: TaylorR_Amazon, reply in cd0bbea1 (2025-06-27, US field) [read in official docs]; a seller in the same thread reports storage continuing while removals failed [opinion]. Read at run time: the order's request date and quantities from Removal Order Detail (stock S18; removals-disposals RM20), against the storage report's months.

FE41. **Removal fees on removal orders that were lost or cancelled.**
- A removal or disposal fee error is a non-itemised FBA fee error under the staff guide's longer limit (FE9).
- A fee with no matching removed or disposed unit is removals-disposals' (see removals-disposals RM26, RM27).
- No Amazon text read says whether the reimbursement for a removal lost in transit includes the removal fee paid on that unit. Vendors list "Lost Removal Order" as a claim for the units, not the fee.

Sources: ce0bea71 [read in official docs]; GETIDA *How we help* (© 2026) [opinion]. Read at run time: Removal Order Detail `removal-fee`; the removal reimbursement line in `GET_FBA_REIMBURSEMENTS_DATA` (removals-disposals RM31 for its `reason`).

FE42. **Storage on stranded units that Amazon caused.** Amazon names "system errors" among the causes of stranding. No Amazon text read refunds storage on stranded units, whatever the cause, and a seller's direct question on it drew no staff answer. A removal order stops storage while it is processed (FE40). Whether a stranding Amazon caused makes storage a "fee charged in error" under the staff guide is not stated. Sources: Bryce_Amazon f77cbf98 (2024-03-12, US field) [read in official docs]; stock S1–S3 and stuck-stock.md O17; seller in f77cbf98 and 00896ca4 [opinion]. Read at run time: `GET_STRANDED_INVENTORY_UI_DATA` `stranded-reason`, `date-stranded` (stock S2), and the listing issue behind it (stock S8).

FE43. **Partnered-carrier charges: the void window decides a full refund.** Confirming a partnered-carrier transportation option agrees to the charge. Voiding within the window for the shipment type refunds it in full; outside it, charges "may apply". A non-partnered shipment can be voided at any time. The window is carried per option as `Quote.voidableUntil`. Sources: stock I16 (the rule); fulfillmentInbound_2024-03-20.json `Quote`, `cancelInboundPlan` [command-verified]; TaylorR_Amazon 407a9a34 (2025-01-14, US field) [read in official docs]. Read at run time: `listTransportationOptions` `quote.voidableUntil` and `quote.cost` (Amazon Fulfillment); plan status `VOIDED` / shipment status `CANCELLED` (stock I7); the charge and any refund in Finances. The window lengths are in "Values that move".

FE44. **Partnered-carrier charges for transport never performed.** No Amazon text read provides for refunding a partnered-carrier charge when the carrier did not collect, or the shipment closed before collection, once the void window had passed. UK sellers report Seller Support declining on the void window, and staff asking only for the case ID. Vendors list the claim kind ("Cancelled Shipping Costs", GETIDA; "unused shipping labels", Threecolts). Amazon's staff guide names partnered-carrier charges in neither fee class, so their filing limit is not stated. Sources: 85f330d7 (2025-05-01/13, UK field), 753ca151 (2020-10-28, UK field), 2072bdbf (2024-09-17, UK field) [opinion; staff reply read in official docs]; GETIDA *How we help*; recovery-economics vendor table [opinion].

FE45. **Unplanned prep and labelling fees.** Amazon applies prep or labels that a shipment lacked, charges a fee per unit, and flags the defect in the Inbound Performance dashboard. The fee is disputed from the problems tab under the shipment's summary. Units with missing or defective labels "aren't eligible for reimbursements". The dispute limit is stated two ways, and both stand: from when the problem is reported, on the unread help page (via search summary only); and as a non-itemised error under the staff guide's longer limit. Sources: KJ_Amazon 7c433b9f (2025-01-24, US field); Roberto_Amazon b8734d29 (2024-07-30, US field); Bryce_Amazon 32e1d348 (2025-08-04, 2025-08-08, US field); ce0bea71 [read in official docs]; help page 201000230 by search summary [opinion, snippet]. Read at run time: `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA` (`issue-reported-date`, `problem-type`, `fee-type`, `fee-total`; finance P-ful-24); the help page's limit as the seller's Seller Central shows it. The values seen are in "Values that move".

FE46. **Inbound defect fee credits post to the Reimbursements report.** Amazon waived the deleted or abandoned defect fee for international plans in a stated date range whose remaining shipments arrived within a stated number of days of the first receive. It reimbursed fees already charged on those shipments automatically, "Go to your Reimbursement report to view details". The fee's triggers and the 2026 single fee are held elsewhere (stock I13; finance P-ful-24, J1). No dispute window for the defect fee was found. Sources: News_Amazon f25ba535 (2026-10-30, US field) [read in official docs]; GL5XA3MNXAJKJE8E unread (script shell). Read at run time: Inbound Performance report `fee-type` / `fee-total`; `GET_FBA_REIMBURSEMENTS_DATA`; receive dates of the plan's shipments (inbound-shortfalls). The scope and window of the waiver are in "Values that move".

FE47. **AWD fees on box dimensions have their own rule.** For AWD storage and transportation fees only:
- Amazon reimburses the difference between the fees as charged and the fees on corrected measurements, and Amazon's measurement governs.
- A box is ineligible for remeasurement after a stated number of remeasures in a stated period, or when no box of that MSKU is at an AWD site.
- Requests must be made within a window counted from the charge date, one claim per fee charge, through Amazon Support or the account manager as a research request.

Source: AWD Service Terms §4.2, dated 2026-01-14, read 2026-11-13 [read in official docs]. The window is handed here by inbound-shortfalls IN33. AWD is not readable on the five roles (stock W38). Read at run time: the dated terms page. The values are in "Values that move".

FE48. **Subscribe & Save has no fee claim of its own.** No Amazon page read names a fee claim specific to Subscribe & Save. Its fees are the order's ordinary fee lines, under the positions above. Sources: stock O13, O14; absence. [inferred]

FE49. **Former Small and Light units have no separate claim.** Small and Light closed in 2023, and Low-Price FBA is a rate by price (stock G21). A former Small and Light unit's fee is judged under FE31 or the standard rate. Source: stock G21. [inferred]

FE50. **Detection that rests on Data Kiosk `economics` is outside the five roles.** The Economics dataset needs Selling Partner Insights, which is not one of the seller's five roles (see sp-api-claims-surface SU33; finance P-ful-18 holds the conflicting role pages). What it would open:
- charged fees per product per date range, with the properties that set them (size tier), split at Amazon fee-change dates (FE18, FE20);
- history further back than Finances (FE32; reach in SU34);
- charged fee components;
- the `economicsPreview` fee types for the low-inventory-level and returns fees (sections 7, 9).

Nothing in this file is built on it. On the five roles, the same questions are read from dated Fee Preview copies, the Storage Fees report, Finances and the Inbound Performance and Reimbursements reports. Sources: SU33; analytics_economics_2024_03_15.graphql [command-verified]. [read in official docs]

### Corrections to other packs

- **Finance pack P-ful-2** ("Amazon's own measurement sets every size-tier-based fee") is **outdated for the EU**. From 2025–2026, certified seller dimensions calculate FBA fees on Amazon.de and on UK/FR/IT/ES, with an automatic look-back true-up when certification lowers the fee (FE5–FE7; values in "Values that move"). P-ful-2 also lacks the non-itemised limit (FE9) and the separate AWD box-dimension rule (FE47).
- **Finance pack fulfilment-charges.md A2** quotes the EU rate card's storage clause "Amazon's measurement will govern" without the certification policy beside it. The two now conflict (FE8).
- **Finance pack fulfilment-charges.md open question 12** (how a fee correction after a remeasure posts) is partly answered. Amazon staff (2025-02-05) describe per-order "Fee Adjustment - Weight and Dimension Change" entries under "Other", with no reimbursement ID (FE13).
- **Finance pack selling-fees.md A5 / P-sell-5**:
  - The 2023-01-13 referral policy, held there as "snippet only; source post not opened", is now read (Spencer_Amazon, 2024-05-24, UK marketplace field; FE23).
  - Add the 2022-03-16 removal of the referral dispute window (FE22).
  - The Roberto_Amazon post cited there without a date is dated 2026-05-13 and carries the UK marketplace field. Its US twin is dated 2026-04-17. It also states the itemised / non-itemised FBA fee windows (FE9).
- **Finance pack fulfilment-charges.md I3 and J1** (unplanned services; inbound defect fee). Additions:
  - Amazon staff name the dispute route for unplanned service fees: the problems tab under the shipment summary (Roberto_Amazon, 2024-07-30, US field; FE45).
  - The 2026 staff guide puts prep and labelling fee errors under the non-itemised limit, against the help page's limit, which I3 carries as a snippet (FE45).
  - Amazon reimbursed inbound defect fees automatically under the 2026 international peak waiver, shown in the Reimbursements report (News f25ba535, 2026-10-30, US field; FE46).
- **Survey notes 04-job-money.md**: the rows "FBA fee / dimension overcharge … 90 days" stand for the itemised class. Add the non-itemised limit and the EU certification regime.
- **Stock pack holding-costs.md P10** (storage rides on Amazon's measurement) needs the same EU caveat as P-ful-2.
- **Stock pack stuck-stock.md O17 and C1 (storage charging)**. Two Amazon staff statements the stock pack does not hold:
  - storage stops "promptly" once a unit is identified as lost or damaged (KJ_Amazon, 2025-04-30, US field; FE38);
  - no storage is charged on units in a created removal order during its processing (TaylorR_Amazon, 2025-06-27, US field; FE40).

  Neither settles O17 (whether stranded units accrue storage), but the second bounds it.

Within this pack (for the owners of those files, not edited here): filing-and-conduct dates NR_Amazon ca22eab2 "≈2024" (FL30, FL35). The page's `datePublished` is 2025-04-30T20:39:30Z, with the US marketplace field (re-read 2026-11-13). Several staff posts across the pack that are cited by host (".ca forum", "UK forum", "EU forum") carry the US marketplace field. The post-to-store table in fc-lost-damaged is the place to settle them.

---

## Values that move

A value that differs by store or by date is never a position's substance. The positions state the rule and where it is read; the value sits here. "Field" is the forum post's `marketplaceId` as read.

| Value | As read | Store | Date of the source | Read on | Source | Position |
|---|---|---|---|---|---|---|
| Itemised FBA fee error window | 90 days from the disputed charge | US field; UK field | 2026-04-17; 2026-05-13 | 2026-11-13 | Roberto_Amazon ce0bea71; ff7c3c15 | FE9 |
| Itemised (weight/dimension) fee window, earlier statements | "within 90 days of the date on which the fee was charged" | US field (on the .ca host); Chinese reprint, store not named | 2023-11-14; 2020-09-15 | 2026-11-13 | Glenn_Amazon ae6a5220; LianLian reprint | FE9 |
| Non-itemised FBA fee error limit | 18 months ("statute of limitations") | US field; UK field | 2026-04-17; 2026-05-13 | 2026-11-13 | ce0bea71; ff7c3c15 | FE9, FE41, FE45 |
| Fee window, JP, CA, AU, IN, MX and other stores | not read | — | — | 2026-11-13 | none found; the CA-host and UK-host staff posts read carry US fields | FE9 |
| Remeasure eligibility per FNSKU | "remeasured twice in the past 60 days" | US field; Chinese reprint | 2025-04-30; 2020-09-15 | 2026-11-13 | NR_Amazon ca22eab2; LianLian | FE4 |
| Remeasure turnaround | "typically within 10 days of request" | US field | 2025-04-30 | 2026-11-13 | ca22eab2 (also filing-and-conduct FL30) | FE4 |
| Monthly remeasure limit per account | Amazon names no number. Practitioners: "20-30 requests per month" (Sellerise); 20 (Regan跨境, AMZ123); 40 (a seller relayed by Notifcentral) [opinion] | US (Sellerise); store not named (others) | 2023-03-21; 2025-11-27; 2026-08-07 | 2026-11-13 | as named; home filing-and-conduct FL35 | FE4 |
| Support-set wait before a remeasure (one case) | 30 days | US | 2024-12-10 | 2026-11-13 | Bryce_Amazon 9c2edbce | FE12 |
| Certification true-up look-back | 90 days ("最高追溯90天"), automatic for Amazon.de | DE | 2026-03-06 | 2026-11-13 | Global Selling news-notices-260306 | FE7 |
| Same, later phases | 90 days [opinion, relaying Amazon] | UK, FR, IT, ES | 2026-05-18; 2026-09-01 | 2026-11-13 | cifnews 186018; 九方 11810 | FE7 |
| Certification processing time | about 30 days; longer in November and December | DE | 2026-03-06 | 2026-11-13 | news-notices-260306 | FE6 |
| Certification deadlines and start | DE existing ASINs by 2026-04-30; UK/FR/IT/ES fees on certified dimensions from 2026-05-05; at least 60 days to verify; UK/FR/IT/ES standard size by 2026-07-05 [opinion]; large items by 2026-10-15 [opinion] | DE; UK, FR, IT, ES | 2026-03-06; PDF 2026-03-30; 2026-05-18; 2026-09-01 | 2026-11-13 | notice; policy PDF; cifnews; 九方 | FE5, FE6 |
| Dimensional-weight divisor | 139 | US | 2025-04-30 | 2026-11-13 | ca22eab2 (other stores: P-ful-26) | section 1a |
| Placement fee charge timing | "45 days after your shipment is received" | US field | 2024-09-14; 2024-11-01 | 2026-11-13 | 0d8742f3; 5d437c4b | FE25 |
| No-fee optimized option, carton minimum | "at least five identical cartons or pallets per item" | US field | 2024-11-01 | 2026-11-13 | 5d437c4b | FE25 |
| Low-inventory-level fee credit day | "by the 15th day of the following month" | US field | 2024-05-02 | 2026-11-13 | News 00fd861e | FE28 |
| Low-inventory-level exemption of 2024-05-15 (history) | products that "sold less than 20 units in the past 7 days" | US field | 2024-05-02 | 2026-11-13 | 00fd861e (current rule: P-ful-7) | section 7 |
| Low-price FBA price thresholds from 2026-01-05 (VAT included) | £20 UK; €20 DE, FR, IT, ES, BE, NL, IE; SEK 230 SE; PLN 85 PL | as listed | © 2026 | 2026-11-13 | sell.amazon.es low-price FBA page | FE31 |
| Same, before 2026-01-05 | £10 UK; €11 DE; €12 FR, IT, ES, BE, NL, IE; SEK 140 SE; PLN 55 PL | as listed | © 2026 | 2026-11-13 | same page | FE31 |
| Low-price FBA size limit | 35 x 25 x 12 cm, 400 g (both sets) | EU stores as listed, UK | © 2026 | 2026-11-13 | same page (US: P-ful-25) | FE31 |
| Partnered-carrier void window | small parcel 24 hours; LTL one hour (model); "Pallet shipments … one hour" (staff); non-partnered "at any time" | model: marketplace not named; staff post US field | model at db2936a (2026-10-29); 2025-01-14 | 2026-11-13 | `cancelInboundPlan` description; TaylorR_Amazon 407a9a34; stock I16 | FE43 |
| Partnered-carrier measurement adjustment start | 2025-06-12, "domestic US Amazon Partnered Carrier shipments" | US field | 2025-05-12 | 2026-11-13 | News a7e7de46 | FE27 |
| Unplanned services dispute limit | "within 30 days of when the problem is reported to you" [opinion, search summary of the unread help page] | US help page | not shown | 2026-11-13 | 201000230 via search; finance fulfilment-charges.md I3 | FE45 |
| Inbound defect fee waiver, 2026 peak | international plans created 2026-08-01 to 2026-11-30; remaining shipments received within 45 days of the first receive (was 30); automatic closure 90 days | US field | 2026-10-30 | 2026-11-13 | News f25ba535 | FE46 |
| AWD box-dimension fee claim window | "within 90 days of the date on which the fee was charged" | AWD (US; stock W41 for later stores) | terms dated 2026-01-14 | 2026-11-13 | AWD Service Terms §4.2 | FE47 |
| AWD box remeasure limit | "remeasured twice in the past 60 days" | AWD | 2026-01-14 | 2026-11-13 | same | FE47 |
| Referral fee dispute window | none since 2022-03-16; a phone agent's "Internal Policy" of 90 days is a seller report [opinion] | US (News); CA field (seller) | 2022-03-16; 2023-10-12 | 2026-11-13 | News 972575; 5c1e41df | FE22 |
| Fee Preview refresh and request limit | held in sp-api-claims-surface SU20 | — | — | — | SU20 | FE17, FE19 |
| `economics` start-date limit and retention | held in sp-api-claims-surface SU34 | — | — | — | SU34 | FE18, FE50 |
| `listTransactions` span per call and recent gap | held in finance P-ref-23 | — | — | — | P-ref-23 | FE32 |

## Seat's own

None of this file's positions rests on the seat's own choice. FE1's grouping of overcharge types, the order of sections 1–15 and the columns of FE34's table are this seat's arrangement of sourced facts. They are a layout, not a finding, and enter no skill as a rule.

---

## Open questions for a first run on a real account

1. In the US, does any fee adjustment post automatically after a remeasure that lowers a tier, or only on request? Read `listTransactions` for the orders between the wrong-measurement start and the remeasure date.
2. How "Fee Adjustment - Weight and Dimension Change" is encoded in `listTransactions` (`transactionType`, `description`, `breakdowns[].breakdownType`, related identifiers) and in settlement V2 (`transaction-type`, `amount-type`, `amount-description`).
3. Do `INCORRECT_FEES_ITEMS` and `INCORRECT_FEES_NON_ITEMIZED` correspond to Amazon's itemised and non-itemised classes? Do they appear in `GET_FBA_REIMBURSEMENTS_DATA` `reason`, in settlement rows, or both?
4. If the Selling Partner Insights role were ever held (FE50): does Data Kiosk `economics` split a date range when a product's size tier changes mid-range (not an Amazon fee-change date), or does it report one `Fee` with mixed properties?
5. Under EU certification, how does the automatic look-back compensation post: as one adjustment, per order, and under which name? Does it cover storage?
6. Which price decides low-price FBA eligibility and the US price band: listing price, sale price after promotion, at order or at ship? Read the fulfilment fee on orders whose price crossed a threshold.
7. Is the itemised window counted from the fee's `postedDate`, the shipment date, or the settlement date, when they differ?
8. Can the fee category Amazon assigned to an ASIN be read through any SP-API surface (Product Type Definitions, Catalog `classifications`, Fee Preview)? Or is it Seller Central only?
9. Are Catalog Items `dimensions.package` values Amazon's FC measurement, or catalogue contributions? Compare them with the Fee Preview dimensions for the same ASIN.
10. Do the Fee Preview dimensions and the Storage Fees report dimensions ever differ for one FNSKU, or across FCs within one month?
11. Does `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA` carry partnered-carrier measurement adjustments or placement-compliance failures, or are both Seller Central only?
12. Is the `listPlacementOptions` fee for the confirmed option comparable to the placement line posted after receipt (FE25)? Which `listTransactions` fields carry the shipment ID?
13. The account's remaining monthly remeasure count and the certification status of each ASIN: confirm both are Seller Central only.
14. Does a lost-unit reimbursement include the placement fee paid on that unit (FE26)?
15. Does `GET_FBA_STORAGE_FEE_CHARGES_DATA` `average_quantity_on_hand` count researching units, units already adjusted lost or damaged, and units inside a created removal order? Compare it with the ledger and Removal Order Detail for one FNSKU and month (FE38–FE40).
16. Does the reimbursement for a removal lost in transit include the removal fee paid on that unit (FE41)?
17. What filing limit, if any, does the "Fees Charged in Error" route apply to partnered-carrier charges for a carrier that never collected (FE44)?
18. Which limit does a dispute of an unplanned prep or label fee meet in practice: the help page's, counted from the problem report, or the staff guide's non-itemised one (FE45)?
19. Under which `reason` does an inbound defect fee credit appear in `GET_FBA_REIMBURSEMENTS_DATA`, and does it carry the shipment ID (FE46)?
20. Do the fee windows and the remeasure limits differ in JP, CA, AU, IN or MX? No page with those stores' fields was read (FE9).
21. Does any Amazon text in a store other than the US state the storage-stop rules of FE38 and FE40?
22. Is storage on stranded units ever credited when the stranding reason was Amazon's own error, and through which route (FE42)?

---

## Pages read

| Title | Address | Publisher | Page date | Read on | Used for |
|---|---|---|---|---|---|
| 📘 A Seller's Guide to Disputing Incorrect Charges on Amazon (Roberto_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/ce0bea71-dd81-4a08-808a-893ecc1572dd | Amazon (staff, US forum) | 2026-04-17 | 2026-11-13 | 90-day / 18-month windows, route, duplicates (FE9, FE37) |
| Spotted an Incorrect Charge? Here's What to Do (Roberto_Amazon) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/ff7c3c15-8655-4086-af58-9b726d178e77 | Amazon (staff, EU host, UK field) | 2026-05-13 | 2026-11-13 | Same text, EU (FE9, FE11) |
| Importance of Accurate Product Measurements (NR_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/ca22eab2-3fbe-4826-ab22-74a842fac674 | Amazon (staff) | 2025-04-30 | 2026-11-13 | Measurement, remeasure conditions, reimbursement rule (FE2, FE4, FE36) |
| Amazon Overcharging For Incorrect Weight and Dimensions (Glenn_Amazon reply) | https://sellercentral.amazon.ca/seller-forums/discussions/t/ae6a5220-e749-4726-8660-d5a64e35dd6c | Amazon (staff, .ca host, US field) | thread 2023-11-06, reply 2023-11-14 | 2026-11-13 | 90 days, largest dimensions, variations (FE2, FE3) |
| Wrong FBA fulfillment fees … (KJ_Amazon reply) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/958851b3-3d11-4dec-950d-7644e6206869 | Amazon (staff, .co.uk host, US field) | 2024-09-20 | 2026-11-13 | Monthly limit, extra request with case ID (FE4) |
| Optimizing Item Package Weight and Dimensions to Manage FBA Fees (Dominic_Amazon) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/c6f1274b-6484-4c24-b6f6-3c2da5e3f468 | Amazon (staff, EU host, US field) | 2024-08-22 | 2026-11-13 | Fees riding on dimensions, packaging (FE36) |
| Amazon overcharged me storages fees … (Sandy_Amazon replies) | https://sellercentral.amazon.com/seller-forums/discussions/t/29fbd69b-3933-4d25-84d4-69b0eaa62ac0 | Amazon (staff) / seller | 2025-02-05 | 2026-11-13 | Per-order Fee Adjustment, no reimbursement ID (FE13, FE16) |
| what should I do if Amazon overcharges FBA fees without compensation? (Bryce_Amazon reply) | https://sellercentral.amazon.com/seller-forums/discussions/t/9c2edbce-af2e-4a7b-8fc8-1cec205b4f35 | Amazon (staff) / seller | 2024-12-10 | 2026-11-13 | Remeasure before reimbursement; policy text quoted by seller (FE11, FE12, FE35) |
| Amazon made a measurement error, corrected it, but refuses to refund … | https://sellercentral.amazon.com/seller-forums/discussions/t/fe4a0969-6e01-4991-946c-ccd033080e80 | Seller (Christine_Amazon reply) | 2026-04-03 | 2026-11-13 | Refusal after correction (FE14, FE35) |
| FBA Fee Overcharge & Refund – Re-measurement Confirmed but No Reimbursement … | https://sellercentral.amazon.com/seller-forums/discussions/t/4a8a5cd9-31b7-4ab8-a3e9-654f749e3fe2 | Seller (Josh_Amazon reply) | 2026-10-08 | 2026-11-13 | Refusal; order-level audit (FE14, FE35) |
| Fraudulent FBA storage fees | https://sellercentral.amazon.com/seller-forums/discussions/t/1c1a9399-ad90-433c-8a04-6ae301b86a6d | Seller (support messages pasted; Bryce_Amazon reply) | 2025-03-31 | 2026-11-13 | What support asked for (FE15); storage effect |
| Update to FBA inventory reimbursement claim windows | https://sellercentral.amazon.com/seller-forums/discussions/t/d8f9a56c-882f-437c-ad34-cccd11cfa465 | Amazon (News, AU field) | posted 2025-08-14, eff. 2025-10-15 | 2026-11-13 | No fee window in it (FE10) |
| FBA item package dimensions certification policy (PDF) | https://m.media-amazon.com/images/G/02/MP/phase-3policy.pdf | Amazon | created 2026-03-30; eff. 2026-05-05 | 2026-11-13 | EU certification (FE5–FE8) |
| 亚马逊FBA新规 \| 4/30前认证商品包装尺寸，省物流费！ | https://globalselling.amazon.com/news/news-notices-260306 (via gs.amazon.cn) | Amazon Global Selling (China) | 2026-03-06 | 2026-11-13 | DE certification, 90-day automatic compensation (FE5–FE7) |
| 7/5前完成！亚马逊FBA商品包装尺寸认证扩展至欧洲站 | https://www.cifnews.com/article/186018 | 雨果网 (repost of Amazon Global Selling WeChat) | 2026-05-18 | 2026-11-13 | UK/FR/IT/ES phase (FE5, FE7) |
| 九方第36周海外仓资讯 | https://www.jiufanglogistics.cn/news/11810.html | 九方通逊 | 2026-09-01 | 2026-11-13 | Large-item certification, 2026-10-15 (FE5, FE7) |
| FBA fees: certified item dimensions mandatory from August | https://valuezon.de/en/news/fba-fees-certified-item-dimensions-mandatory-from-august/ | Valuezon (Averest Consulting) | July 2025 | 2026-11-13 | DE phase from 2025-08-01 (FE5) |
| Rate Card Europe Fees, effective 2 November 2026 (PDF) | https://m.media-amazon.com/images/G/02/sell/images/261014-FBA-Rate-Card-EN.pdf | Amazon | eff. 2026-11-02 | 2026-11-13 | Storage measurement clause (FE8) |
| FBA Reports (report type values) | https://developer-docs.amazon/sp-api/docs/report-type-values-fba.md | Amazon (SP-API docs) | updatedAt 2026-10-13 | 2026-11-13 | Fee Preview and Storage Fees columns (FE17, FE19, FE24) |
| analytics_economics_2024_03_15.graphql | amzn/selling-partner-api-models, schemas/data-kiosk (clone db2936a) | Amazon (GitHub) | commit 2026-10-29 | 2026-11-13 | `properties`, `amountPerUnitDelta` (FE18, FE20) |
| catalogItems_2022-04-01.json; all models (grep "remeasur", "certif") | amzn/selling-partner-api-models (clone db2936a) | Amazon (GitHub) | commit 2026-10-29 | 2026-11-13 | Catalog dimensions; no remeasure op (FE4, FE6) |
| Fee categories made easier to understand | https://sellercentral.amazon.com/forums/t/fee-categories-made-easier-to-understand/972575 | Amazon (News) | 2022-03-16 | 2026-11-13 | Referral window removed; Fee Preview category (FE22, FE24) |
| Referral Fees Series. Part 3 (Spencer_Amazon) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/3432aad2-9c07-4551-85bb-798325231de0 | Amazon (staff, EU host, UK field) | 2024-05-24 | 2026-11-13 | 2023-01-13 referral policy (FE23) |
| WRONG FEE CATEGORY (Ezra_Amazon reply) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/a28e70af-2805-4ae2-9a37-9430f939e624 | Amazon (staff, IN field) | 2024-03-18 | 2026-11-13 | Policy ID GRRJCFXD6474GRLY (section 4) |
| Amazon overcharged me on referral fees … | https://sellercentral.amazon.ca/seller-forums/discussions/t/5c1e41df-cf5b-4bb0-8329-8b9f0001187e | Seller (CA field) | 2023-10-12 | 2026-11-13 | "Internal Policy" 90 days (FE22) |
| Update to low-inventory-level fee | https://sellercentral.amazon.com/seller-forums/discussions/t/00fd861e-fed1-454a-970b-9d3e8384eb6a | Amazon (News) | 2024-05-02 | 2026-11-13 | Credit by the 15th (FE28) |
| When and how will the Placement Fees charged? (Jameson_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/5d437c4b-6e3d-49a2-8754-8c77ce1dc4c7 | Amazon (staff) | 2024-11-01 | 2026-11-13 | Placement rules, Seller Central views (FE25) |
| Amazon is rediculously charging inbound placement fees and defect fees (Dominic_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/0d8742f3-cabc-40af-a6c1-44981cc4d3f2 | Amazon (staff) / seller | 2024-09-14 | 2026-11-13 | "just an estimate" (FE25) |
| Lost inventory and reimbursement of inventory placement fees (Jameson_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/0b434f7f-87e8-458a-a47a-743447103533 | Amazon (staff) | about 2024 ("2 years ago") | 2026-11-13 | Fee on unreceived shipment (FE26) |
| Amazon placement fee by mistake — I did not order these services | https://sellercentral.amazon.com/seller-forums/discussions/t/ab7cb5c7-c514-4004-bf19-d6d001f49790 | Seller (Bryce_Amazon reply) | about 2024 | 2026-11-13 | Disputed placement fee, escalation (section 6) |
| Wrongly charged Inbound Placement Fee | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/aa8bc021-10dd-4dd1-be40-ed1fb9dfda54 | Seller | 2025-04-24 | 2026-11-13 | Quote against charge (section 6) |
| Issue with Incorrect Placement Fee | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/e5ba7d69-030e-4c77-a9e1-f7cad75b7fb7 | Seller | 2025-03-19 | 2026-11-13 | Quote against charge (section 6) |
| [Sad] Amazon charged both an FBA inbound placement service fee and an inbound defect fee | https://sellercentral.amazon.com/seller-forums/discussions/t/7940364d-5681-4cf7-9fc7-aca2fee379ed | Seller | 2025-10-30 | 2026-11-13 | Optimized split recharged (section 6) |
| Fee adjustments for partnered carrier shipment measurements | https://sellersasksellers.com/t/fee-adjustments-for-partnered-carrier-shipment-measurements/6055 | Sellers Ask Sellers (relays Amazon announcement) | 2025-05-19 | 2026-11-13 | 2025-06-12 adjustments (FE27) |
| Partnered Carrier Fee Adjustments that began on June 12th, 2025 | https://sellercentral.amazon.com/seller-forums/discussions/t/6c798198-da2a-424c-8d39-29befc10e044 | Seller (KJ_Amazon reply) | about 2025 | 2026-11-13 | Disputes rejected (FE27) |
| Unreasonable Return Processing Fee | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/308297d2-226a-4f41-9cdf-f0b986eab027 | Seller (support reply quoted) | 2024-05-27 | 2026-11-13 | Returns fee class (FE29) |
| Amazon please assist regarding reconciliation of Returns Processing Fee | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/aa114d9f-a993-44d4-b810-ee7573f154b2 | Seller | 2025-01-07 | 2026-11-13 | No order numbers in the report (FE30) |
| Low-price FBA rates | https://sell.amazon.es/en/tarifas-precio-bajo-logistica-de-amazon | Amazon | © 2026 | 2026-11-13 | EU low-price thresholds and contradiction (FE31) |
| Low-Price FBA fees (.ca host, US field) | https://sellercentral.amazon.ca/seller-forums/discussions/t/38503cfc-a612-400b-8653-45244f24b5c9 | Seller | 2025-06-08 | 2026-11-13 | Which price decides (section 5) |
| 用亚马孙FBA发货的商品因尺寸或重量问题被多收费怎么办？如何索赔？ | https://global.lianlianpay.com/channel/10-19426.html | 连连国际 LianLian Global (policy reprint) | 2020-09-15 | 2026-11-13 | Policy text in Chinese (FE9, FE11, FE16) |
| 卖家注意！亚马逊这项索赔政策变成了90天 | https://www.52by.com/article/24979 | 邦阅网 | 2019-05-22 | 2026-11-13 | 2019 introduction of 90 days (FE10) |
| 崩溃！亚马逊尺寸测量频失误，卖家FBA费用凭空大涨！ | https://www.amz123.com/t/Waa8JqhS | AMZ123 | 2021-04-20 | 2026-11-13 | Seller cases (FE3) |
| (Regan跨境 remeasure article) | https://www.amz123.com/t/2kIZ4A7n | AMZ123 | 2025-11-27 (per finance pack) | 2026-11-13 | 20/month claim, route (FE4) |
| The True Cost of an FBA Remeasurement … | https://www.velocitysellers.com/2026/09/06/amazon-fba-remeasurement-fee-overcharge-cost-data-deep-dive-2026/ | Velocity Sellers (Jake Schwarzbaum) | 2026-09-06 | 2026-11-13 | No notice, baseline diff, lag (FE14, FE19) |
| Amazon FBA Fee Overcharges: How to Claim | https://www.leviathansellers.com/blog/amazon-fba-fee-overcharge | Leviathan Sellers (Harishchandra Bind) | 2026-10-26, upd. 2026-11-07 | 2026-11-13 | Detection checks, windows restated (FE20) |
| Amazon Remeasured Your Product and Your FBA Fee Jumped | https://www.notifcentral.com/blog/fba-fee-remeasurement-cubiscan | Notifcentral (Archit Mathur) | 2026-08-07, upd. 2026-10-30 | 2026-11-13 | When Amazon measures; no auto refund (FE14) |
| How to Recover Money From Amazon FBA Fee Overcharge | https://myamazonguy.com/?p=160046 | My Amazon Guy (Steven Pope) | 2026-05-04 | 2026-11-13 | Remeasure then claim; multi-unit scan (FE14) |
| Quick guide to FBA auditing & reimbursements, Part 5 of 6 | https://getida.com/quick-guide-to-fba-auditing-reimbursements/ | GETIDA | about 2023 | 2026-11-13 | Category fee example (section 4) |
| Sellerise Reimbursement Tool Guide: measuring dimensions (PDF) | https://sellerise.com/landing/assets/files/reimbursement-guides/measure-dimensions/EN-Measure-dimensions.pdf | Sellerise | 2023-03-21 | 2026-11-13 | Monthly limit 20–30; report cross-check (FE4, section 8) [command-verified: PDFKit] |
| FBA费差异 | https://www.lingxing.com/help/article/FBAFeeDifference | 领星 Lingxing | not shown | 2026-11-13 | Order-level method, Fee Adjustment matching (FE34) |
| FBA运费差异 | https://www.sellfox.com/help/features/fba-shipping-cost-difference | 赛狐 Sellfox | not shown | 2026-11-13 | Expected fee = Amazon estimate, 20% flag (FE34) |
| New Reimbursement Policy and its consequences for Small Sellers (KJ_Amazon reply) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/1ce28534-f796-4f93-af3f-11fc33465c91 | Amazon (staff, .co.uk host, US field) | thread 2025-04-26, reply 2025-04-30 | 2026-11-13 | Storage stops on lost or damaged units (FE38) |
| Charged for stranded inventory Amazon won't return (TaylorR_Amazon reply) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/cd0bbea1-5a00-4f80-bd13-ad12b102c66c | Amazon (staff) / seller, US field | 2025-06-24; reply 2025-06-27 | 2026-11-13 | No storage during removal processing (FE40, FE42) |
| Resolving Stranded FBA inventory (Bryce_Amazon) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/f77cbf98-0f2f-4834-8d3f-9eb9cfe84c8e | Amazon (staff), US field | 2024-03-12 | 2026-11-13 | Stranding causes incl. system errors; unanswered storage question (FE42) |
| Unjust FBA Storage Fees – Request for Release of Funds and Inventory | https://sellercentral.amazon.com/seller-forums/discussions/t/00896ca4-2983-4741-9577-db40a2e2eda2 | Seller, US field | 2025-03-12 | 2026-11-13 | Storage on stranded stock while deactivated (FE42) |
| Update to the FBA inventory reimbursement policy (News) | https://sellercentral.amazon.com/seller-forums/discussions/t/68864b6f-0ab8-41ef-be18-069c33df6336 | Amazon (News), US field | 2024-12-18 (updated 2024-12-19) | 2026-11-13 | Context only: valuation is value-and-reversals' (section 11) |
| FBA inventory reimbursement policy, US (PDF) | https://m.media-amazon.com/images/G/01/rainier/help./PC__Kiwi_Comms_redlined_policy_US_clean.pdf | Amazon | created 2024-12-19 | 2026-11-13 | Sourcing cost excludes shipping, handling and other costs; pointed to value-and-reversals (section 11) [command-verified: PDFKit] |
| Unused Shipping Label Refund (TaylorR_Amazon reply) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/407a9a34-1e72-4b5b-a1ae-5b8e8e04cb9a | Amazon (staff) / seller, US field | 2024-12-23; reply 2025-01-14 | 2026-11-13 | Void windows, full refund (FE43) |
| Pallet Collection Not being Refunded (Sarah_Amzn reply) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/85f330d7-e6e3-4424-b4ba-1ff3f49c1646 | Seller / Amazon, UK field | 2025-05-01; reply 2025-05-13 | 2026-11-13 | Charge for a pallet not collected (FE44) |
| Amazon partnered carrier issue - can't get refund for shipment that didn't happen | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/753ca1510c223bf63e95a5fbb12e0c1a | Seller, UK field | 2020-10-28 | 2026-11-13 | Carrier cancelled; refund refused (FE44) |
| Shipment closed before partnered carrier could deliver | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/2072bdbf-3b96-4327-918e-a61f03af0067 | Seller, UK field | 2024-09-17 | 2026-11-13 | Closed before collection (FE44) |
| 24 hours to void Amazon-partnered carrier charges and get a full refund | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/b13f34f8898016504c99019133aeb446 | Seller (quoting the workflow), UK field | 2022-10-02 | 2026-11-13 | Workflow wording of the void window (section 13) |
| fulfillmentInbound_2024-03-20.json (`Quote.voidableUntil`, `cancelInboundPlan`) | amzn/selling-partner-api-models (clone db2936a) | Amazon (GitHub) | commit 2026-10-29 | 2026-11-13 | Void deadline per option (FE43) [command-verified] |
| Fee adjustments for partnered carrier shipment measurements (News) | https://sellercentral.amazon.com/seller-forums/discussions/t/a7e7de46-f082-499c-a132-4d1278f72104 | Amazon (News), US field | 2025-05-12 | 2026-11-13 | Original of the 2025-06-12 adjustments (FE27) |
| FBA Inbound Convenience Fees (KJ_Amazon) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/7c433b9f-77c9-40a6-aaf6-5871daf3ce67 | Amazon (staff), US field | 2025-01-24 | 2026-11-13 | Unplanned service fees and their dispute (FE45) |
| Discrepancy in Box Weight / Box Over Weight (Roberto_Amazon reply) | https://sellercentral.amazon.in/seller-forums/discussions/t/b8734d29-8e4a-4f21-8648-bfa42b623429 | Amazon (staff) / seller, US field | 2024-07-24; reply 2024-07-30 | 2026-11-13 | Dispute route: problems tab under shipment summary (FE45) |
| New FBA Prep Rule (Jan 1, 2026) – Seller Risk & Unplanned Prep Fees (Bryce_Amazon replies) | https://sellercentral.amazon.com/seller-forums/discussions/t/32e1d348-10b4-46ae-ae29-74a0cb3b182a | Amazon (staff) / seller, US field | 2025-08-01; replies 2025-08-04, 2025-08-08 | 2026-11-13 | Prep/label applied and flagged; no reimbursement for unlabelled units (FE45) |
| Changes to Unplanned Service Fees (old forum, seller relaying Amazon text) | https://sellercentral.amazon.com/forums/t/changes-to-unplanned-service-fees/430974 | Seller, US field | 2018-11-30 | 2026-11-13 | History: fee preview mode, 2018 (section 14; no position) |
| Temporary peak season extensions for international FBA shipments (News) | https://sellercentral.amazon.com/seller-forums/discussions/t/f25ba535-e06e-4fa3-8bb0-cb3a095fd696 | Amazon (News), US field | 2026-10-30 | 2026-11-13 | Defect fee waived and reimbursed (FE46) |
| Amazon Warehousing & Distribution Service Terms | https://supplychain.amazon.com/legal/service-terms/warehouse-and-distribution | Amazon | dated 2026-01-14 | 2026-11-13 | §4.2 AWD box-dimension fee claims (FE47) |
| How we help (claim types) | https://getida.com/how-we-help/ | GETIDA | © 2026 | 2026-11-13 | "Cancelled Shipping Costs", "Lost Removal Order" (FE41, FE44) |
| Inbound defect fee: deleted or abandoned shipments | https://synder.com/fees-amazon/inbound-defect-fee-deleted-or-abandoned-shipments/ | Synder | undated | 2026-11-13 | Checked; no dispute or window text (not used) |

**Unread** (JS shell or blocked), with where their text was quoted:
- *FBA fees reimbursement policy: Weight and dimensions* GL7U4JFSDXUTQAJ. JS shell on every mirror tried. Quoted by staff (ae6a5220, ca22eab2), by a seller (9c2edbce), in the LianLian 2020 reprint, and by the listing seat (v14, 2026-10-14, via the finance pack).
- *Understanding item package weight and dimensions* G6WAEPTECPT2JUH3 and *Product dimensions and volume* G37G73BJXHF75ACH. JS shells; held via the listing seat (P-ful-2).
- *Referral fees reimbursement policy* GRRJCFXD6474GRLY. Not fetched; quoted by Spencer_Amazon (3432aad2).
- *FBA inbound placement service fee* GC3Q44PBK8BXQW3Z and *Low-inventory-level fee* GV43F6S76Y9DHYRH. Held via P-ful-6 and P-ful-7.
- The Amazon Partnered Carrier program FAQ. (The original News post of the 2025-06-12 carrier adjustments, a7e7de46, is now read.)
- *Unplanned services* (201000230) and *Inbound defect fees* (GL5XA3MNXAJKJE8E): script shells to a plain GET on 2026-11-13 (about 171 KB each, no policy text). Unplanned-services text is carried only as a search summary, tagged.
- *Send to Amazon: Change or cancel your shipment* (GCUH6KKZA6PRA4E7): not fetched. The void windows are carried by the model, a staff reply and stock I16.
- Threecolts Margin Pro's claim-type page: not re-read; its "unused shipping labels" comes through recovery-economics' vendor table.
- Searches for an Amazon text on storage charged on researching units, and for a Japanese or Canadian fee window, were cut short when this session's web-search budget ran out on 2026-11-13.
- The original Seller Central News posts for the DE (2025) and UK/FR/IT/ES (2026) certification phases. Relayed by Valuezon and cifnews; Amazon's PDF and the Global Selling notice were read.
- A Zhihu article on computing expected FBA fees (https://zhuanlan.zhihu.com/p/643581745): HTTP 403.
- 蓝海亿观 egainnews article 5827: timeout.
- 赛贝 saibeiip guide-d1952: encoded page.
- Synder and AMALYTIX fee glossaries for `INCORRECT_FEES_*`: seen as search summaries only.
- FBA Service Terms / Business Solutions Agreement clauses on measurement: not reached. The session's web-search budget ran out before they were located.

---

## Verification (2026-11-13)

An adversarial check of this file's load-bearing positions against their cited sources, each re-opened on 2026-11-13 (forum pages as raw HTML with `datePublished`; PDFs extracted with macOS PDFKit; SP-API models in the clone db2936a and in upstream amzn/selling-partner-api-models main, head b13d1d1 of 2026-11-10).

Checked and confirmed:
- NR_Amazon ca22eab2 (2025-04-30): divisor 139, thickest point, packing material as the most common cause, 10-day remeasure, twice in 60 days, "our measurement will govern", the fee-report evidence line (FE2, FE4, FE36).
- Glenn_Amazon ae6a5220 (thread 2023-11-06): 90 days from the charge, "personal measurements are not accepted", "largest dimensions", each variation its own product (FE2, FE3).
- KJ_Amazon 958851b3 (2024-09-20): monthly limit and an extra request with a case ID (FE4).
- Roberto_Amazon ce0bea71 (US, 2026-04-17) and ff7c3c15 (EU, 2026-05-13, "Itemised" spelling): itemised 90 days, non-itemised 18 months, one referral claim per charge and final, route, duplicates (FE9, FE11, FE37).
- News d8f9a56c (posted 2025-08-14, effective 2025-10-15): lists lost/damaged, customer returns and removal windows only (FE10).
- Sandy_Amazon 29fbd69b (thread 2025-02-05): per-order "Fee Adjustment - Weight and Dimension Change", no reimbursement ID; the support agent's "can never be reimbursed" line (FE13, FE16).
- Bryce_Amazon 9c2edbce (2024-12-10): 30-day wait, remeasure "prior to a successful reimbursement"; "Only one request needs to be created for an FNSKU" quoted by a seller; $12.93 / $28.51 (FE11, FE12, FE35).
- fe4a0969 (2026-04-03) and 4a8a5cd9 (2026-10-08): figures and quotes (FE14, FE35).
- 1c1a9399 (2025-03-31): the support file formats (FE15).
- Certification policy PDF (created and modified 2026-03-30): every quoted line (FE5, FE6).
- Global Selling notice news-notices-260306 (page date 2026-03-06): scope, 2026-04-30 deadline, automatic 90-day compensation, ~30-day processing, deemed certification (FE5–FE7).
- EU rate card effective 2026-11-02 (created 2026-10-15), FAQ Q2 *How are Storage Fees calculated?*: "Amazon's measurement will govern" (FE8).
- Valuezon (July 2025), cifnews 186018 (2026-05-18), 九方 11810 (2026-09-01): the relayed phases (FE5, FE7).
- News 972575 (`datetime` 2022-03-16): referral dispute window removed, Fee Preview upcoming fee category (FE22, FE24).
- Spencer_Amazon 3432aad2 (2024-05-24): every quoted line of the 2023-01-13 referral policy (FE23).
- News 00fd861e (2024-05-02): credit by the 15th of the following month (FE28).
- Jameson_Amazon 5d437c4b (2024-11-01) and Dominic_Amazon 0d8742f3 (thread 2024-09-14): placement rules and "just an estimate" (FE25).
- Sellers Ask Sellers 6055 (2025-05-19): the 2025-06-12 carrier adjustment text (FE27).
- FBA report type values page (updatedAt 2026-10-13): Fee Preview columns (no fee-category column; `product-size-tier` US only; `product-size-weight-band` EU), 72-hour refresh and once-a-day limit, Storage Fees columns, inventory-planning low-inventory columns, long-term storage `per-unit-volume`, non-compliance `problem-type` / `fee-type` / `fee-total`, roles (FE17, FE19, FE24).
- analytics_economics_2024_03_15.graphql: two-year start date, `properties` with the Product Size Tier example, split at Amazon fee-change dates, `amountPerUnitDelta`, 30-day retention (FE18, FE20).
- LianLian reprint (2020-09-15): 90 days, storage reports as evidence, one claim per charge (FE9, FE11, FE16); 52by (2019-05-22) (FE10).
- sell.amazon.es *Low-price FBA rates*: criteria and "no action is required" (FE31).
- Velocity Sellers (2026-09-06) and Leviathan Sellers (2026-10-26) quotes.

Changed:
- "No 'certif' in any model" was literally wrong: "certif" occurs as certificate / GiftCertificate / wacCertificate. Restated as no dimension-certification or remeasure operation, checked also at upstream b13d1d1.
- Section 7: `LOW_INVENTORY_LEVEL_FEE` is a `PreviewFeeType` of `economicsPreview` (a forward estimate from today), not a component of charged fees in `economics`. Corrected.
- Section 9: `HIGH_RETURN_RATE_FEE` / `RETURN_PROCESSING_FEE` via `economicsPreview` give an expected fee, not the fee charged. Corrected.
- Section 1a / FE10: 52by says the earlier limit was "less strict", not that no limit applied. Corrected.
- Section 5 / FE31: the "€12 contradiction" is the page's pre-2026-01-05 criteria set; UK £20 and the earlier £10 / €11 / €12 set added.
- FE14: staff in the two threads did not both point to a new order-level case; corrected per thread.
- FE28: "only the days beyond the threshold" rests on a search summary; marked unsupported by a read page.
- Section 6 / FE27: the "just an estimate" line is Seller Support's reply that Dominic_Amazon confirmed and restated; carrier adjustment scope "domestic US Amazon Partnered Carrier shipments" quoted.
- Moving values taken out of position substance and kept as dated evidence: remeasure limits and turnaround (FE4), look-back length (summary, 1b, section 3, FE7, corrections list), placement charge delay and carton minimum (FE25), credit day (section 7, FE28), the itemised window length (section 8, section 10 Finances pitfall).
- Imperative practitioner advice (baseline and diff, half-inch margin, multi-unit scan, "rule out rate changes first", "look for duplicates") rewritten as reported methods or facts.
- Global Selling notice: added that the automatic compensation is worded for items sold on Amazon.de and capped "最高追溯90天"; FE8 gains 九方's fulfilment-fee-only wording as opinion.
- Upstream models: b13d1d1 (2026-11-10) changed only the economics schema (new `PreviewFeeType` values, a dynamic-sandbox directive); nothing about remeasurement, certification or fee disputes. The Support API 2025-02-01 reads cases only (FE37).
- No local file path was found in the file.

Remaining doubts:
- The Seller Central help pages (GL7U4JFSDXUTQAJ, G6WAEPTECPT2JUH3, GRRJCFXD6474GRLY, GC3Q44PBK8BXQW3Z, GV43F6S76Y9DHYRH) were not re-read: JavaScript shells. Their current windows and limits stand only on staff restatements.
- Glenn_Amazon's and Sandy_Amazon's reply dates are not shown on the page; only the thread dates are.
- The UK/FR/IT/ES and large-item phases, and their 90-day compensation, rest on practitioner relays; no Amazon News post for them was read.
- FE8 (does certification cover storage) stays unresolved.
- FE21 (`getMyFeesEstimateForSKU` versus `ForASIN` dimensions) and the Sellerise, AMZ123, Notifcentral, My Amazon Guy, GETIDA, Lingxing and Sellfox claims were not re-opened in this check.
- No newer certification notice for further stores, or for the US, was found by one web search.

---

## Revision (2026-11-13)

Made after the completeness critic's round-one review (sections A–H, J and K, as they touch this file). Every new read was a plain GET of a public page or a grep of the models clone at db2936a. No POST was sent, the help hub's content call was not used, and no SP-API host or seller data was touched.

Moving values out of positions:
- FE4, FE7, FE9, FE12, FE25, FE28 and FE31 now state the rule and where it is read. Their values (remeasure limits and turnaround, look-back length, the two fee windows, the support-set wait, placement timing and carton minimum, the low-inventory-level credit day, the low-price thresholds and size limits) moved to the new "Values that move" table, with store, source date and read date.
- FE17, FE18 and FE32 now point to SU20, SU34 and P-ref-23 for the Fee Preview limits, the `economics` reach and retention, and the `listTransactions` span.
- The same values were taken out of the summary, the 1b and section 7 "Into a skill" lines, and the section 6 and section 10 "Read at run time" lines.

Settled:
- FE28: the "days in excess of the threshold" clause rests on a search summary. It is out of the position and stays only in section 7 as unsupported evidence.
- FE34: recast from one vendor method into four choices side by side (Lingxing, Sellfox, baseline and diff, SKU against ASIN estimate). The Lingxing formula is pointed to SU44.
- FE18, FE19, FE20, FE32, and sections 1a, 7, 9 and 10: Data Kiosk `economics` and `economicsPreview` need Selling Partner Insights, outside the five roles (SU33). The new FE50 lists what the dataset would open; nothing is built on it. FE18 is retitled "would date".
- FE37 and FE4 no longer restate the Support API or the absence of a claim operation; they point to SU8 and SU12. The monthly remeasure limit and the turnaround as a reply time point to filing-and-conduct FL35 and FL30.

Store attribution (critic A1, A11): each forum post is now tagged with the `marketplaceId` read from its page data.
- The "CA forum" Glenn_Amazon reply (now dated 2023-11-14), the "UK forum" KJ_Amazon reply, Dominic_Amazon's "EU forum" post and several seller threads carry the US field.
- Roberto_Amazon's EU-host twin (ff7c3c15) and Spencer_Amazon's referral post carry the UK field. Ezra_Amazon's reply (2024-03-18) carries the India field.
- News d8f9a56c carries the Australia field, so FE10's "2025-10-15 revision" is now stated as Australia's.
- NR_Amazon ca22eab2's 2025-04-30 date was re-read. filing-and-conduct's "≈2024" is noted for its owner.

FE27 now rests on the original News post (a7e7de46, 2025-05-12, US field) instead of the Sellers Ask Sellers relay.

Added (sections 11–15; positions FE38–FE50):
- Storage on units identified as lost or damaged (FE38).
- Storage on researching units, not stated (FE39).
- No storage during removal processing (FE40).
- Removal fees on lost or cancelled removal orders (FE41).
- Storage on stranded units that Amazon caused (FE42).
- Partnered-carrier void window and `Quote.voidableUntil` (FE43).
- Partnered-carrier charges for transport never performed: GETIDA "Cancelled Shipping Costs", Threecolts "unused shipping labels" (FE44).
- Unplanned prep and label fees, their dispute route and the conflicting limits (FE45).
- Inbound defect fee credits through the Reimbursements report (FE46).
- AWD box-dimension fee claims, the window inbound-shortfalls IN33 hands to this file (FE47).
- Subscribe & Save (FE48) and former Small and Light (FE49), one line each: no separate claim.
- The Data Kiosk role (FE50).

Pointers added: the homes of the post-to-store table, the cap and dispute window, the Support API and the IDR routes; stock W14, W15, W38, W41, I7, I13, I16, I19, S1–S3, S8, S18, S19, C6, O13, O14, G21; removals-disposals RM20, RM26, RM27, RM31; finance P-ful-24 and fulfilment-charges.md I3 and J1.

Other changes:
- Corrections to other packs: added entries for finance fulfilment-charges.md I3/J1 and for stock stuck-stock.md O17/C1. The P-ful-2 entry also names the AWD rule.
- New "Seat's own" section. Open questions 15–22 added; questions 4, 5, 7 and 12 reworded so they carry no value.

Still open:
- The Seller Central help pages behind FE2, FE4, FE9, FE23, FE25, FE28, FE45 and FE46 stay unread. They are script shells, and the content-call route is closed.
- JP and CA fee windows: no page with those stores' fields was found before the search budget ran out.
- FE5's DE and later-phase dates and the UK/FR/IT/ES look-back still rest on Valuezon, cifnews and 九方, and FE10's 2019 history on 52by. No Amazon News post for them was read.
- FE33 still rests on vendor glossaries.
