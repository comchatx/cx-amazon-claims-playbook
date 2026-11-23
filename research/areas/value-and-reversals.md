# Value and reversals: reimbursements paid under value, and reimbursements Amazon takes back

**Summary.** A unit lost or damaged before a customer order has been reimbursed since 2025-03-31 at its *sourcing cost*: the seller's approved figure on Manage Your Sourcing Cost, or Amazon's estimate where there is none. A unit lost after an order is reimbursed at the order's sale price minus fees. An approved cost applies only to reimbursements issued after its approval date. An earlier reimbursement is revalued only by a per-transaction dispute within a window. Every policy text read counts it from the reimbursement; one News post, issued for the Australia store, counts it from the initial claim. The window's length is read at run time for the seller's store (values by store and date in *Values that move*). Japan's policy (2025-02-19) also values pre-order losses at sourcing cost. No SP-API operation reads or writes the seller's sourcing cost, the estimate or a dispute. The Reimbursements report shows what was paid per unit, but not the basis it was valued on. Amazon reverses a reimbursement when it was paid in error or the unit is found. It has published no time limit for reversing and no rule for the amount reversed.

Area scope: valuation of FBA inventory reimbursements, Manage Your Sourcing Cost (MYSC), valuation disputes / re-evaluation, unsellable-unit valuation, post-order and customer-return valuation, the per-unit cap, telling an under-valued line in `GET_FBA_REIMBURSEMENTS_DATA`, inventory-vs-cash reimbursement, reversals and clawbacks. Pointers to neighbours (not researched here): what is lost in an FC → fc-lost-damaged; inbound shortfall claims → inbound-shortfalls; returns not received → customer-returns; removal claims → removals-disposals; fee refunds → fee-overcharges; roles, reports and what the API cannot do → sp-api-claims-surface; how a case is opened, limits, penalised conduct → filing-and-conduct; service fees and recovery figures → recovery-economics.

**Already held elsewhere (one fact, one home).** The finance pack (cx-amazon-finance-playbook) research/areas/refunds-reimbursements-adjustments.md holds the base: P-ref-14 (sourcing-cost rule), P-ref-15 (date move, page rename), P-ref-16 (claim windows page by page), P-ref-17 (cash / inventory columns), P-ref-18 (reversals), P-ref-19 / P-ref-20 (report and its join keys), P-ref-35 (reason values), P-ref-36 (ledger ↔ report naming), P-ref-40 (the policy PDF). The stock pack (cx-amazon-stock-playbook) research/areas/stock-states.md holds the ledger reason codes (W30: F, N, O) and reconciliation reasons (W31); research/areas/inbound.md holds P-inbound-29. This file builds past them and corrects some of them (see *Corrections to other packs*, at the end of § 3).

**Relation to the released finance skill.** The finance pack's released skill `refunds-and-reimbursements` (references/reimbursements.md) already states, by P-ref id, the scope, the sourcing-cost value, cash or units, reversals, claim windows and the report's columns. This file is the claims side of the same facts: what a reimbursement *should* have been worth and when Amazon may take it back. Each correction below names the finance or stock position it concerns; that pack owns the fix. Which pack carries valuation and reversals once the claims pack is published is not a finding of this file (see *Seat's own*).

**Homes inside this pack.** This file is the home of the per-unit cap (VR29), the valuation-dispute window (VR20) and the Manage Your Sourcing Cost limits (VR9, VR11, VR14, VR22). fc-lost-damaged FC33/FC34, inbound-shortfalls IN22, removals-disposals RM19 and filing-and-conduct FL26/FL36 point here for these. Facts homed elsewhere are pointed to: the post-to-store table for News posts (fc-lost-damaged), the Support API and "no operation files a claim" (sp-api-claims-surface SU12), case routes and conduct (filing-and-conduct).

How pages were reached. Seller Forums threads were read by plain GET of the public thread page; each post's date is the `datetime` of its `<time>` element (UTC). The store a thread was posted to is its thread-level `"marketplaceId"` (beside `"pinnedToCategory"`), and the page's `<link rel="canonical">` names the same store's host [command-verified 2026-11-13 on every thread cited here; the two agree on each. Calibration: the 2024-12-18 policy post da761b17, whose text names amazon.ca, reads Canada on both; its twin a941ac02, whose text names amazon.co.uk, reads UK on both]. The store reading for News posts is homed in fc-lost-damaged's post-to-store table; it is used here only for the threads this file cites. Amazon's policy PDFs on m.media-amazon.com were downloaded and rendered page by page, so struck-through and inserted text could be told apart (a text extraction alone merges them; see § F). Seller Central help pages (G-numbers) returned JavaScript shells to a plain GET (`/help/hub/reference/external/<ID>`, `/gp/help/external/<ID>`, sellercentral-europe, .co.uk); they stay unread. Their words here come from Amazon's PDFs, Amazon staff forum posts or seller posts quoting them, and the route is named each time. The help hub's content call (`…/help/hub/mons-api/GetHelpTopic`), through which the customer-returns file read G200213130 v47, was closed by the office on 2026-11-10; nothing read through it is carried here, and where that file's reading differs from this one the difference is stated as unsettled.

---

## 1. Sub-topics

### A. History of the valuation rule (dated)

**(a) Amazon's words.**

- *Before 2025 (pre-order losses valued at estimated proceeds).* The pre-change policy text, still visible as struck-through text in Amazon's redlines (§ F), valued shipment-to-Amazon, FC-operations and removal claims at "the estimated proceeds of a sale of that item", where "Estimated proceeds means the estimated sale price of the item for which you are being reimbursed minus referral fees and fulfillment fees". The estimated sale price compared "The median price at which you have sold the item on Amazon over the past 18 months", other sellers' 18-month median (UK: "average"), and current list prices. The UK version adds "The estimated reimbursement amount excludes local standard applicable VAT rate". [official, struck text] *FBA inventory reimbursement policy* redlines (§ 5 rows R-US, R-UK, R-DE, R-CA), read 2026-11-13.
- *Announced 2024-12-18 (News posts for the US, Canada and UK stores; the Canada copy updated 2024-12-19).* "Effective March 10, 2025, we'll reimburse you based on the product manufacturing cost of the affected inventory. 'Manufacturing cost' means your cost to source a product from a manufacturer, wholesaler, reseller, or produce the item if you are the manufacturer. It excludes costs such as shipping, handling, customs duties, or other costs." "you can view and manage manufacturing costs in the Inventory Defect and Reimbursement portal starting in late January using a new Manage Your Manufacturing Cost page." "For items that are lost or damaged after a customer order in Amazon's store, we'll continue to reimburse you for the sales price on the original order minus applicable fees." "Note: This article was updated on December 19, 2024, to include a clarified definition of 'manufacturing cost.'" [official] News_Amazon, *Update to the FBA inventory reimbursement policy*, issued as one post per store on 2024-12-18: US 68864b6f (5.3K views), Canada da761b17 (https://sellercentral.amazon.com/seller-forums/discussions/t/da761b17-58cc-4734-98d2-5608e1d11419, moderator-updated 2024-12-19), UK a941ac02 ("Fulfilment", "programme"); the quoted sentences are in all three, except that the UK post carries no "updated on December 19, 2024" note; read 2026-11-13. (The finance pack holds 68864b6f and a941ac02, E4, and calls a941ac02 the "EU copy"; its store field is the UK's.)
- *First UK redline (PDF created 2024-12-11).* Defines "'Manufacturing cost' means the cost to acquire, purchase, or produce the item", which is not the US wording. Its live dispute line reads "within 90 days after we have issued the reimbursement". [official] `_PC__Kiwi_Comms_redlined_policy_UK_clean_version.pdf`, read 2026-11-13.
- *US redline (PDF created 2024-12-18).* Uses "manufacturing cost", "Manage Your Manufacturing Cost" and "After March 10, 2025". Its dispute line reads "within 60 days". [official] `PC__Kiwi_Comms_redlined_policy_US_clean.pdf`, read 2026-11-13.
- *Moved to 2025-03-31; page renamed.* The finance pack holds News ed8abc33 (P-ref-15). Amazon's redlines regenerated on 2025-02-24 for US, CA, UK, DE, FR, IT, ES and US-Chinese all read "sourcing cost", "Manage Your Sourcing Cost" and "After March 31, 2025". [official] PDFs R-US, R-CA, R-UK, R-DE, R-FR, R-IT, R-ES, R-ZH; read 2026-11-13. FR/IT/ES are not rendered, but their text layers (read in verification, 2026-11-13) are in English and carry "Sourcing cost", "Manage Your Sourcing cost" and "After March 31, 2025" like R-DE; R-ZH reads "2025 年 3 月 31 日之后". The Canada Chinese redline (R-CA-ZH, created 2025-02-24, rendered 2026-11-13) has the same text as R-ZH with "5,000 加元".
- *Japan (PDFs created 2025-02-19, "※This Help page is as of 02/19").* Amazon's JP policy redline in English (R-JP-EN) and in Japanese (R-JP-JA), rendered 2026-11-13, insert the same pre-order / post-order split: "For shipment to Amazon claims, removal claims, and fulfillment center operations claims, we will reimburse you the sourcing cost of the item"; the page is "Manage Your Sourcing cost" on the "Inventory Defect & Reimbursement (IDR) portal". The Japanese text names the value "原価" (cost) and the page "「原価の管理」ページ" / "商品原価の管理", not "調達コスト": "商品の原価を販売事業者に返金します". The refresh sentence reads "After April 1, 2025" / "2025 年4 月1 日より", not "After March 31". The struck text is the same 18-month estimated-proceeds block as the US one. [official] R-JP-EN, R-JP-JA (§ 5). This reconciles with removals-disposals RM18, which read R-JP-EN's text layer.

**(b) Practitioners.** AMZ123 contributor 跨境小蚂蚁 (2024-12-27) wrote that the page "管理您的制造成本" was not yet open and would open in mid-to-late January. Its example: a product "valued at 100" is reimbursed "20" if the seller has no invoice ("那它也只会赔偿你20") [opinion]. A seller on the Canada News thread da761b17 (Seller_fgBEgnL5gJsWx, 2024-12-18) read Amazon's new tool as also applying the manufacturing cost to refunded-but-not-returned orders [opinion; contradicted by Amazon's post-order text, § F].

**(c) Into a skill:** the dated sequence (pre-2025 estimated proceeds → 2024-12-18 announcement → 2025-03-31 effective, page renamed), with each store's own dates read in its own text (JP's refresh date differs; *Values that move*). A reimbursement's `approval-date` is the nearest date the report carries for placing it before or after the change; the policy text does not say whether the change applies by loss date, claim date or reimbursement date [inferred]. **Read at run time:** the current text of *FBA inventory reimbursement policy* (G200213130), https://sellercentral.amazon.com/gp/help/external/G200213130, as the seller's store shows it.

### B. Pre-order losses: sourcing cost and Amazon's estimate

**(a) Amazon's words (2025-02-24 redlines, identical in US / CA / UK / DE except currency, spelling and the "Get Help" / "Get support" link name).**

- Scope: "For shipment to Amazon claims, removals claims, and fulfillment center operations claims that occur before fulfillment, we will reimburse you the sourcing cost of the item. This also covers lost and damage claims during inventory replenishment handled by Amazon or on behalf of Amazon to fulfillment centers or non-Amazon buildings in marketplaces where we provide the service."
- Estimate: "If you don't provide your sourcing cost, we'll use our own cost estimate for reimbursement calculations, which will be displayed on the same page. To generate an estimate of the item's sourcing cost, we evaluate the sourcing cost of comparable products sold by Amazon, by other sellers, and through other wholesale channels."
- Definition: "'Sourcing cost' means your cost to source a product from a manufacturer, wholesaler, or reseller, or to produce the item if you are the manufacturer. It excludes costs such as shipping, handling, customs duties, or other costs. If you provide your sourcing cost, we may ask you to provide additional information to validate the amount. Visit the Manage Your Sourcing cost help page for accepted proof-of-value documentation details."
- Privacy: "Your specific cost data is not shared with any other seller in Amazon's store, including Amazon Retail."
- Refresh: "After March 31, 2025, we will periodically refresh our cost estimates to provide the most up-to-date valuation of the inventory. If the refresh affects any cost you previously provided, we'll alert you and give you time to review the refreshed estimates and update any item(s) where you would like to provide an updated value directly. You may also monitor any impacted items via the status column in the Manage Your Sourcing Cost page."
- Chinese (US policy, Amazon's own translation, R-ZH): "我们将向您赔偿商品的采购成本" (we will reimburse the sourcing cost); page name "管理您的采购成本"; "我们将定期重新估算成本" (we will periodically re-estimate).
- Staff on the estimate: "We calculate our estimate by evaluating the sourcing cost of comparable products sold by Amazon, by other sellers, and through other wholesale channels. We understand that this may not reflect your true cost" [official, staff] KJ_Amazon, 2025-04-30, thread c7c767bc, read 2026-11-13.

**(b) Practitioners.**

- Sellers say Amazon's estimate is below their invoice cost. Seller_3qllv6SY8mdjV (2025-03-10): estimate $18.01 against a known cost of $31.05 on a $64.99 item ("28% of the retail price"). Seller_ALZGvM9vhFf03 (2025-03-04): "most items are estimated 20%-50% below invoice costs". Seller_krASjOzmEcPhQ (2025-03-10): "typically 30-40% lower". Seller_8xPb0zS1apmF2 (2025-11-24): estimate $12.40 on a ~$100 item bought at "a bit less than half". Seller_hLty6uwgHEkk6 (2026-06-15): estimate "roughly one third" of cost. [opinion, each one seller's account]
- Jewellery and precious-metal sellers report estimates below the metal's melt value. Seller_nBUcRErQhJ4JW, 2025-03-21 to 2025-04-10: a 2.02 g gold ring estimated at $97 against $118 gold content. Seller_hyTAk3eMuFoyd, 2025-03-25: a coin estimated at $130 with "$180 value in gold content". [opinion]
- The figures sellers quote for the value lost (Nova Data "50-75% lower", AMZ123 "50%到75%") are held by the finance pack (§ practitioners) and belong to recovery-economics.

**(c) Into a skill:** the scope (pre-order: shipment-to-Amazon, FC operations, removals, and replenishment such as AWD-to-FC moves), the definition (shipping, handling, duties excluded), the estimate's existence, its periodic refresh and the alert, and that the seller's figure overrides the estimate only once approved (§ C). **Read at run time:** MYSC in Seller Central for the FNSKU's current estimate or seller-submitted figure. No SP-API operation returns either (VR18).

### C. Manage Your Sourcing Cost: what a seller enters, when it applies, where it exists

**(a) Amazon's words.**

- Path and action (staff, repeated verbatim in several threads): "From the inventory drop-down menu in Seller Central, select 'Inventory Defect and Reimbursement.' From the Inventory Defect and Reimbursement portal, click 'Manage Your Sourcing Cost' in the top right corner … Locate the specific inventory FNSKU/ASIN listing, select the 'Update' button in the Action column … enter your value in the 'sourcing cost' field … click 'Save changes' … In the status column, you can view the status of your submission. If any action is needed from you, it will be also be listed." "Providing your cost data is optional". [official, staff] KJ_Amazon, 2025-04-30 (c7c767bc, ca7ad06b) and 2025-06-03 (b0f2ffee); read 2026-11-13.
- Unit of entry: per FNSKU ("view and manage the sourcing cost of your FBA inventory items or FNSKUs", same posts).
- Which FNSKUs appear: "The Manage Your Sourcing Cost page displays active listings (FNSKUs) with planned shipments or current inventory in the fulfillment network." The same post says new ASINs "won't appear until they're fully received and processed at the FBA warehouse", and to "Verify you've selected the correct marketplace from the dropdown menu". [official, staff] Abbie_Amazon, 2026-04-10, thread 270bbfe9, read 2026-11-13. The two sentences of this one post do not agree (planned shipments vs fully received); both are stated here.
- Not retroactive: "Once a sourcing cost for a FNSKU is approved, it automatically applies to eligible 'Pre-order' lost and damage reimbursement events issued after the approval date. However, if you have previous reimbursements that are still within the 60-day eligibility window, you can request re-evaluation using your approved value." [official, relayed] Amazon's decline message as quoted by Seller_sTpKyEC5gbktd, 2026-02-22, thread cd2909d2. Confirmed by staff: an approved cost "remains on file and will automatically apply to eligible future reimbursements for that FNSKU" and is not re-submitted every 60 days [official, staff] Arish_Amazon, 2026-02-24, same thread. A seller's case shows a cost approved on 2026-05-25 for a reimbursement paid on 2026-05-18, denied in the case: "Since the reimbursement was processed before your sourcing cost was approved, we are unable to make any additional adjustments to this specific transaction at this time" [official, relayed] Seller_nBlnNSgvanOwA, 2026-05-25, thread 32451dd6. Staff answered that the case route differs from the self-service dispute route (§ D) [official, staff] Sofi_Amazon, 2026-06-05.
- Tags and columns: a "Seller submitted" tag in the sourcing cost column marks an accepted seller value. "The Last-updated and Update status columns show the decline reason and timestamp." [official, relayed] thread cd2909d2 (decline message); Arish_Amazon 2026-02-24.
- Decline reasons (policy, all 2025-02-24 redlines): "Your submission is an outlier compared to similar products or our cost estimate." "Any documentation is forged, tampered with, or illegible." "Your account is suspected of fraud, significant policy violations, or non-compliant selling activities." "You already submitted and received a decision on a cost update request or reimbursement amount dispute for the same item within the last 30 days and have not supplied any new information to reconsider our decision." "If we decline your submitted sourcing cost, we will reimburse you based on a previously approved amount that you submitted or our estimate of your sourcing cost for the item." Decline statuses as Amazon's message words them: "'Submitted value falls outside policy guidelines' - This status applies if the submitted sourcing cost value was an outlier compared to similar products or our cost estimate"; "The proof-of-value documentation provided doesn't meet one or more of the requirements"; "If your request was declined due to a value mismatch: The sourcing cost value you requested may not match the value shown in your proof-of-value documentation" (thread cd2909d2). Sellers also quote "Number of attempts exceeded" (Seller_T7bkq3pJHibSr, 2025-10-23, thread 9d920446) and "Proof of value document does not meet requirements" (b48840c1, 2025-06-12).
- Outlier auto-rejection skips the upload step: "If your submitted cost falls too far outside that range (either way too high or way too low compared to their estimate), it gets auto-rejected without the invoice upload step." [official, staff] Christine_Amazon, 2025-11-25, thread 236be908. The same staff member earlier: "The tool's 2-minute auto-denial is typically triggered when the submitted cost significantly exceeds our internal thresholds or when the sourcing cost documentation is not already approved"; "The 'attempts exceeded' lockout is a security feature that cannot be overridden" [official, staff] Christine_Amazon, 2025-06-04, thread 53eb4da7. That 2025-06-04 post is about the reimbursement re-evaluation tool's denial, not the MYSC submission screen; only the 2025-11-25 post speaks of the MYSC upload step being skipped.
- Attempts per FNSKU, two Amazon statements:
  - "If you have received a decision on a cost update request or reimbursement amount dispute for the same FNSKU within the last 30 days, you must wait for that 30-day period to end before submitting a new value. We allow only one cost update per FNSKU within a 30-day window." [official, relayed: a Seller Support case reply quoted by Seller_MQQBHDfSDIKMC, 2025-03-19, thread d23add81, posted to the **Canada** store (thread field A2EUQ1WTGCTBG2; canonical sellercentral.amazon.ca)]
  - "You get two attempts within a 30-day period to update the cost for each FNSKU. After both attempts are used up, you have to wait 30 days from the first denial before trying again." [official, staff] Christine_Amazon 2025-11-25; "two attempts per FNSKU within 30 days" Christine_Amazon 2025-12-01 (acd6c179); "up to two cost update requests per FNSKU within a 30-day period" Arish_Amazon 2026-02-24. All three threads were posted to the **US** store (thread field ATVPDKIKX0DER).
  - What settles and what does not: the two statements come from different stores (Canada, US) and dates (2025-03, 2025-11 to 2026-02). No source read gives the Canada count after 2025-03 or the US count before 2025-11, so whether the count changed over time or differs by store is not settled. The repeat rule in the policy ("a decision … within the last 30 days" with no new information) is a separate limit, and the Canada reply quotes both side by side.
- Frequency: "If your cost changes, you can submit a cost update for an FNSKU at any time. However, we'll monitor the frequency of submissions for each FNSKU. Submissions may be declined if we observe a pattern of frequent updates for the same FNSKU." And "the entered cost value should match the value on your proof-of-value document." [official, staff] Bryce_Amazon, 2025-04-04, thread f844fc37.
- Proof-of-value requirements (help page *Manage Your Sourcing Cost*, GN655EHATZUVWBC3, unread by a permitted route; its list as a seller copied it from the page on 2025-03-19, thread d23add81, Canada store): "Document name (for example, Manufacturer Invoice, Commercial Invoice)"; "Document number"; "Document date"; "Buyer entity name (that is, your business name registered with Amazon), address and identification (VAT No., C.I.F, N.I.F or similar)"; "Issuer entity name … address and identification"; "Product details such as product code (for example, SKU, ASIN, item number, serial number, model number or similar), description and quantity"; "Clear indication of the sourcing cost or purchase price (for example, value per listed item or net value)"; "Indication of currency of transaction". [official, relayed]
- Accepted documents and formats (staff): "manufacturer invoices, wholesaler invoices, purchase invoices, and commercial invoices" (Arish_Amazon 2026-02-24); "manufacturer or wholesaler invoices, commercial invoices, or retail receipts" (Christine_Amazon 2026-03-06, thread 5fb2d2f8); "Only PDF, JPG, JPEG, or PNG accepted (no Excel, Word, or screenshots)"; "Business name on invoice must exactly match your Amazon registration" (Christine_Amazon 2025-12-01). [official, staff]
- Invoice age, two Amazon statements: "Ensure your invoice is recent (within the last 365 days)" [official, staff] Nano_Amazon, 2025-06-12, thread b48840c1; "Invoice age - Must be less than 5 years old" [official, staff] Christine_Amazon, 2025-12-01, thread acd6c179. Both threads are US-store. Neither post cites the help page's own sentence, and the help page is unread, so the later date (2025-12-01) is the only order between them; it is not shown to supersede the earlier one. 易销AI (2025-08-07) gives 365 days as the rule [opinion].
- Self-manufactured goods: the requirements are "structured around sellers who purchase finished goods". Staff names "a formal manufacturer invoice or internal cost document … the product name or SKU, the unit cost, and the date", component invoices "paired" with a cost breakdown, and a Seller Support case asking for "a manual review by the reimbursement team" [official, staff] Christine_Amazon, 2026-03-06, thread 5fb2d2f8. Nano_Amazon (2025-06-12) adds "If using a pro forma invoice, include proof of payment" and "For products manufactured in-house, provide a detailed cost breakdown".
- Why an invoice was refused: "Amazon does not share why invoices are or are not accepted." [official, staff] Glenn_Amazon, 2026-01-15, thread 8033bd61, posted to the **UK** store (thread field A1F83G8C2ARO7P; canonical sellercentral.amazon.co.uk; this file earlier gave it as .ca).
- Bulk: a seller with 40,000+ ASINs reported (2025-03-04, thread ec56a47b) that the "bulk inventory uploader" did not work and "does not have a field for 'documentation link'" [opinion]. No Amazon text on a MYSC bulk upload was found.
- Marketplaces where the page is evidenced: the US (the US-store threads above); Canada (thread d23add81, Canada store; R-CA and R-CA-ZH "Manage Your Sourcing cost"); the UK (thread 8033bd61, UK store, with Glenn_Amazon's reply; R-UK; a UK seller thread held by the finance pack, cfea683e); DE, FR, IT and ES (2025-02-24 redlines naming the page); Japan (R-JP-EN "Manage Your Sourcing cost" page on the IDR portal; R-JP-JA "原価の管理", 2025-02-19); an EU blog case in euros (Eagle Eye, below). The earlier Japanese search for 調達コスト missed the JP texts because Amazon's Japanese word is 原価. Whether the JP portal shows the page today is unread (open question 3).

**Chinese cross-border evidence for a cost (what Amazon's fields say, and what Chinese practitioners report).**

- Amazon's fields that bear on it, as relayed from GN655EHATZUVWBC3 (d23add81, Canada store, 2025-03-19): "Buyer entity name (that is, your business name registered with Amazon), address and identification (VAT No., C.I.F, N.I.F or similar)"; "Indication of currency of transaction". Staff: "Business name on invoice must exactly match your Amazon registration" (Christine_Amazon, 2025-12-01, US); a pro forma "include proof of payment" (Nano_Amazon, 2025-06-12, US); "no Excel, Word, or screenshots" (Christine_Amazon, 2025-12-01). [official, relayed and staff]
- No Amazon text read states a language for the document, or whether a mainland-China VAT invoice (发票, "fapiao"), a 1688 order receipt or a payment-platform receipt is accepted. Amazon's Global Selling Chinese pages read here (gs.amazon.cn zhishi article-250305-3, 2025-03, and article-250807-3, 2025-08) speak of proof of *ownership* for inbound claims, not proof of value; the first says "亚马逊不接受形式发票或类似合同作为所有权证明" (pro forma invoices are not accepted as proof of ownership). That is the inbound document (see inbound-shortfalls § D); for proof of value, US staff accept a pro forma with proof of payment (above). The two rules concern different documents. [official]
- An invoice whose buyer is an entity other than the one registered with Amazon (for example a Hong Kong or mainland purchasing company buying for a US LLC that sells) does not carry "your business name registered with Amazon" in the buyer field, which the relayed list and the staff post require [inferred from the field; no Amazon text read addresses a related-company buyer].
- 贾科斯 (易销AI, 2025-08-07) [opinion]: names mainland "增值税发票（VAT Invoice）专票/普票均可" as the type Amazon most trusts, "必须真实、可查验" through the State Taxation Administration's check site (inv-veri.chinatax.gov.cn); lists as often refused "发票信息与亚马逊后台不一致（如买方名称或地址不同）", invoices that cannot be traced or verified, and dates older than 365 days. Its two cases: a Canada-store loss where a "中文普通发票" was refused and a customs-declaration invoice was found "凭证不清晰"; a Germany-store unsellable return paid €9 where a Chinese "增值税普票" was refused as "无法验证采购成本", then an English commercial invoice in euros with the supplier's tax number, plus a cost entry, was approved at €68.7 after about four working days. As stopgaps where no invoice can be had: a commercial or pro forma invoice from the supplier or forwarder, a contract with payment record and a stamped receipt ("必须盖章"), or customs papers. It advises English invoices in USD/CAD/EUR.
- AMZ123 跨境小蚂蚁 (2024-12-27) [opinion]: the seller's own figure is proven with "采购发票+物流发票及更多资料".
- 1688 order receipts: no Amazon text and no practitioner page on their acceptance as proof of value was read in this pass (the web search budget ran out before a Chinese search on 1688 receipts could be made; open question 13).

**(b) Practitioners.**

- Ivan Raineri, Eagle Eye (blog, 2026-09-12, euros, marketplace unnamed): estimate €20, invoice €55. Attempt 1 (cost from memory, no invoice) was rejected as too high. Attempt 2 (a multi-product invoice) was rejected because the system could not isolate the line. A support case with the line highlighted got the cost approved about two weeks after the first attempt. 23 reimbursements within 60 days of payment were then revalued at €55, "€805" in all. [opinion]
- 贾科斯 (易销AI, 2025-08-07), a Canada-store case: a CAD 20 first reimbursement on a CAD 500 item. A Chinese ordinary invoice was refused, then a customs-declaration invoice was found "凭证不清晰" (unclear). After the real purchase price was entered on the "采购成本" page with an invoice, a new dispute case raised the payment. The author advises English invoices in USD/CAD/EUR, dated "≤ 最近365天，建议90天内" (within 365 days, ideally 90) [opinion]. Its other points are under *Chinese cross-border evidence* above. The finance pack holds 知无不言 Y13803977312 ("亚马逊要的是可被证明的采购/生产成本…需要和发票保持一致").
- Seller_T7bkq3pJHibSr (2025-10-23, thread 9d920446) gives a dated sequence. Reimbursed 09/17 at $168.20. On 10/04, $600 then $549.99 were refused "outside of policy guidelines", and $504 was refused "Number of attempts exceeded". Retries on 10/16 and 10/20 were refused the same way. The 60-day window closed 11/16, before the next eligible update date of 11/23. [opinion]
- Seller_hLty6uwgHEkk6 (2026-06-15, thread 0ad71762): support staff made update attempts on the seller's behalf, which used up the seller's monthly attempts. A senior-leadership case reply (relayed) said Amazon "cannot override the lockout" and "cannot manually correct the sourcing cost". [opinion, relayed]
- Seller_0DUSg9wgB1yYB (2025-06-02, thread 53eb4da7): each use of the re-evaluation tool sends a request to MYSC, which refreshes "Last-updated (UTC)" and counts as an attempt [opinion; Amazon staff did not confirm or deny].
- Seller_ALZGvM9vhFf03 (2025-03-04): "EACH ITEM WE UPDATE creates a request for documentation" [opinion].

**(c) Into a skill:** MYSC is per FNSKU and per marketplace. An approved cost applies forward from its approval date; earlier reimbursements need a dispute (§ D). Decline reasons and a repeat rule (a repeat within a stated period of a decision, without new information, may be declined) are policy; the period is read on G200213130 (*Values that move*). The count of cost updates per FNSKU per period and the maximum invoice age are values Amazon's staff have stated differently by store and date (*Values that move*). An outlier value is refused before any document is asked for. The documentation fields, as relayed, including a buyer entity that is the business registered with Amazon and the currency of the transaction; no Amazon text read states a document language or rules on Chinese tax invoices or 1688 receipts. The seller's choices and what each changes (Amazon's estimate stays and pays at the estimate; or the seller submits a figure that must equal the document's figure, using attempts) are the seller's to make; no choice is preferred here. **Read at run time:** MYSC (sourcing cost, "Seller submitted" tag, Update status, Last-updated) for each FNSKU and marketplace, in Seller Central only. The help page *Manage Your Sourcing Cost* (GN655EHATZUVWBC3), https://sellercentral.amazon.com/help/hub/reference/external/GN655EHATZUVWBC3, as the seller's store shows it, for the current attempt count, invoice age and document list.

### D. Disputing a value: the re-evaluation window and its routes

**(a) Amazon's words.**

- Policy (US 2024-12-18 and all 2025-02-24 redlines; unmarked text, neither struck nor inserted): "If you don't agree with our valuation of a unit, you can file a claim on Contact Us in Seller Central within 60 days after we have issued the reimbursement." JP (2025-02-19): "you can file a claim using the Contact Us page in Seller Central within 60 days after we issued the reimbursement"; "返金が行われてから60 日以内にセラーセントラルのお問い合わせから異議申し立てを提出できます". R-CA-ZH as R-ZH. UK: "If you don't agree with the Amazon valuation of a unit, you can file a claim using the Get support page in Seller Central within 60 days…"; DE (and the FR/IT/ES text layers): "…file a claim on Get support in Seller Central within 60 days…". And: "You can dispute a reimbursement claim using the Get Help page in Seller Central." [official] R-US, R-CA, R-UK, R-DE, R-ZH ("可在我们发放赔偿后的 60 天内通过卖家平台中的联系我们提出索赔").
- Earlier UK text: "…within 90 days after we have issued the reimbursement" [official] UK PDF created 2024-12-11, unmarked text. A UK-store staff post of 2024-10-26 says the same: "you can dispute Amazon's valuation within 90 days if you disagree", with "The max is £2,000 per unit" (Angie_Amazon, thread 9d4ff2a6, UK store field and canonical .co.uk) [official, staff]. R-UK (2025-02-24) reads 60 days in unmarked text. So the UK's 90 days is the pre-2025 UK text, and the 60 days is the UK text from the 2025-02-24 redline on; the redline does not mark the change. A third-party copy of the older help page (Hopted, undated, no sourcing-cost text) also reads 90 days, and its post-order and unsellable wording is the pre-2025 one [opinion as a copy; the original is unread].
- News of 2025-08-14 (effective 2025-10-15): "Re-evaluation requests: Within 90 days of initial claim" [official] News_Amazon d8f9a56c, *Update to FBA inventory reimbursement claim windows* (held as P-ref-16; re-read 2026-11-13). The post's text names no store, but its thread field is A39IBJ37TRP1C6 (**Australia**) and its canonical link is sellercentral.amazon.com.au [command-verified 2026-11-13; the post-to-store table is fc-lost-damaged's]. It counts from the initial *claim*, while the policy counts from the issued *reimbursement*. No post with a US, Canada, UK, EU or JP store field carrying a re-evaluation window was found (removals-disposals RM7 reached the same).
- The customer-returns file reports the live US G200213130 as "within 60 days after we have issued the reimbursement", read through the help hub's content call; that route is barred (2026-11-10) and the reading is not carried here.
- Staff, the 60-day reading (2025-04 to 2026-06), in five threads:
  - "If you do not agree with the listed valuation of a unit, the best next step is to file a dispute using Contact Us in Seller Central within 60 days after we have issued the reimbursement." KJ_Amazon, 2025-04-30 (ca7ad06b, c7c767bc) and 2025-06-03 (b0f2ffee); Josh_Amazon, 2025-05-30 (27d8463a).
  - "First verify that you are within the 60-day window from the original reimbursement date. Ensure your sourcing costs are properly documented in Manage Sourcing Costs BEFORE submitting any re-evaluation request. Use the reimbursement re-evaluation tool at: https://sellercentral.amazon.com/help/hub/solution/WF_fba_reimbursement_revaluation" Christine_Amazon, 2025-06-04 (53eb4da7).
  - "You'll be able to dispute a claim for reevaluation if you're issued a reimbursement you disagree with. You can submit that request through Get Help up to 60 days after the reimbursement." Bryce_Amazon, 2025-04-04 (f844fc37).
  - Decline reason 3 as Amazon words it: "Outside Eligibility Window - The reimbursement transaction exceeds the 60-day re-evaluation window from when the original transaction was issued." (cd2909d2, relayed).
- Two routes, as staff describe them:
  - (1) *Self-service "Dispute a reimbursement claim"* ("Seller Central > Help > Get Support > select 'Dispute a reimbursement claim'"). It recognises an approved cost. Its "key requirements are: within 60 days of original reimbursement, units reimbursed in 'sellable' condition, and it applies to pre-order lost or damaged events (which includes missing from inbound)" [official, staff] Sofi_Amazon, 2026-06-05, thread 32451dd6. The decline message says the same: "specifically for pre-order lost or damaged events including shipment to Amazon claims, removal claims, and fulfillment centre operations claims … the units must have been reimbursed in 'sellable' condition" (cd2909d2).
  - (2) *Transaction dispute with documents, reviewed by people*: "If you have a specific reimbursement transaction where you disagree with the amount, you can dispute that individual transaction through the 'Get Help' option in Seller Central within 60 days of the transaction. Select 'Submit a reimbursement claim dispute' - this goes to a different review process where you CAN submit your supporting documentation." [official, staff] Christine_Amazon, 2025-11-25, thread 236be908. Staff contrasted "reopening the case to request manual adjustment" (denied on timing) with the self-service workflow (Sofi_Amazon 2026-06-05).
- The policy's repeat rule covers disputes too: "a cost update request or reimbursement amount dispute for the same item within the last 30 days" (2025-02-24 redlines; the period is read on G200213130). A seller names a "30-day lockout period" after a denied dispute (Seller_8xPb0zS1apmF2, 2025-05-21, thread 27d8463a) [opinion]; the staff answer restated the 60-day rule only (Josh_Amazon 2025-05-30).
- How the value is reviewed (US redline, struck): the 18-month median-price method was struck in 2025 (§ F). A seller replying on a forum (Seller_i6S8knzW6zU6Z, 2025-03-06, thread c2302e97) still cites it as what a dispute reviews [opinion; outdated per Amazon's redline].

**(b) Practitioners.** Eagle Eye (2026-09-12) and sellers in threads 53eb4da7, 9d920446 and 32451dd6 describe the same sequence: the cost must be approved before the transaction dispute succeeds, and the 30-day attempt lock can outlast the 60-day window. Seller_0DUSg9wgB1yYB (2025-06-02): the re-evaluation tool "automatically denied in exactly 2 minutes" while no approved cost existed [opinion]. AMZ123 速推站外 (2026-11-02, held in the finance pack): the "60天差额追回" story is not a universal right [opinion]. Clawback (blog, 2026-07-05): "Anything below your documented cost is a dispute candidate". It gives no dispute window ("Disputes have their own windows") and still writes about 18 months for warehouse-loss claims, which Amazon's notices replaced (P-ref-16) [opinion; outdated on the claim window]. Refunzo (Jimi Patel, 2025-08-19) lists supplier invoices, shipment records and product details as evidence for a reversal dispute, with no window [opinion].

**(c) Into a skill:** a value dispute is a per-reimbursement act. Its window is a per-store value: every policy text read (US, CA, UK, DE, FR, IT, ES, JP, US-Chinese, CA-Chinese) counts it from the reimbursement's issue; the Australia News post (2025-08-14, effective 2025-10-15) counts it from the initial claim. The value is read for the seller's store, not assumed (*Values that move*). The self-service route needs an approved MYSC cost, a sellable unit and a pre-order event. The documented route takes uploads and a human review. A repeat within the policy's repeat period (§ C) without new information may be declined. Which route a seller uses, and whether, is the seller's choice. **Read at run time:** `approval-date` of each line in `GET_FBA_REIMBURSEMENTS_DATA` (the start of the count). The policy page G200213130 as the seller's store shows it, and the latest Seller Forums News post on claim windows whose store field is the seller's store (fc-lost-damaged's post-to-store table), give the window length. The Get Help options "Dispute a reimbursement claim" / "Submit a reimbursement claim dispute" exist in Seller Central only.

### E. Unsellable units: the reduced estimate

**(a) Amazon's words.**

- Pre-order (live text, 2025-02-24 redlines): "For items that were in unsellable condition when lost, damaged or removed from the Amazon fulfillment network, we will reimburse at a reduced estimated cost of the unit, and we may request additional information or documentation to help us determine this adjusted value." Chinese: "我们将以商品成本估算折扣价进行赔偿" [official] R-US, R-ZH.
- Post-order (inserted text, same redlines): "For items that were in unsellable condition when lost or damaged, we reimburse you at a valuation consistent with the discounted sale price of that order minus applicable fees." UK/DE add "and VAT". [official]
- Struck (pre-2025) text: "For unsellable items, we reimburse you at a valuation consistent with the estimated proceeds of the discounted sale of the unit." [official, struck]
- JP (R-JP-EN, R-JP-JA, 2025-02-19): the reduced estimate is stated for removal claims only: "For removal claim of unsellable items, we will reimburse at a reduced estimated cost of the unit"; "販売不可商品の返送/所有権の放棄に関する申請については、商品の原価から割り引いた金額を返金します". The JP texts carry no post-order unsellable sentence. [official]
- No Amazon page read gives the discount rate.

**(b) Practitioners.** None found that measures the reduction. 易销AI's DE case (§ C) is an unsellable customer return paid €9 on a €139 item, raised to €68.7 after an English invoice and a cost entry [opinion]. Seller_6xcCLJodrIRK8 (2026-08-05, thread a2c0b1c6) says materially-different customer returns are "consistently being coded as 'removal order issues,' which routes them into the sourcing-cost bucket", paying "roughly 30-60% of actual buy cost" [opinion].

**(c) Into a skill:** two different unsellable rules, pre-order (a reduced estimated *cost*) and post-order (the order's *discounted sale price* minus fees). The self-service dispute route covers only units reimbursed as sellable (§ D). **Read at run time:** `condition` on the reimbursement line. Its values for unsellable units are unseen (the finance pack saw `NewItem` only; open question 1).

### F. Post-order losses and customer returns: what the redlines say, what is unread, and a reading error to avoid

**(a) Amazon's words.**

- Status of the text. What follows is the text of Amazon's redlines as rendered, the newest dated 2025-02-24. The live help page G200213130 serves a script shell to a plain GET and could not be read by a permitted route on 2026-11-13. The customer-returns file (RT42, its correction 3) quotes a live US page (v47) reading "the refund amount or the price of the replacement item on the original order minus applicable fees", that is, the pre-2025 sentence the redlines strike. That reading came through the help hub's content call, a route the office closed on 2026-11-10, so it is not carried here and not used to correct anyone; it is the reason the current basis is stated as unsettled.
- Redline text (2025-02-24 redlines R-US, R-CA, R-UK, R-DE, and R-ZH; the same strikes are already in the US PDF of 2024-12-18 and the UK PDF of 2024-12-11): "If we elect to reimburse you for a customer return claim, the value of the reimbursement is based on the refund or replacement given to the customer on your FBA order. If Amazon refunded or replaced an item on your FBA order, we calculate the reimbursement value as the sales price on the original order minus applicable fees." UK/DE: "minus applicable fees and VAT". Chinese: "我们将以原始订单的销售价格减去适用费用的方式来计算赔偿金额".
- Rendered, the redline strikes "refund amount or the" and "of the replacement item" and inserts "sales" (red, underlined). The pre-2025 sentence therefore read "the refund amount or the price of the replacement item on the original order minus applicable fees"; the text layer reads "the refund amount or the sales price of the replacement item …" because it keeps the inserted word alongside the struck ones. [command-verified: per-character strike and colour check of R-US, R-CA, R-UK, R-DE and the US 2024-12-18 PDF, 2026-11-13]
- Japan's two texts of the same date do not agree. R-JP-EN (2025-02-19) makes the same strike and insertion as the US ("…the [refund amount or the] {sales} price [of the replacement item] on the original order minus applicable fees and consumption tax"). R-JP-JA inserts the sales price *beside* the refund and replacement price and strikes neither: "{元の注文の販売価格、}返金額または交換商品の価格から、適用される手数料と消費税を差し引いたものが補てん額として算出されます" (the sales price on the original order, the refund amount or the replacement item's price, minus applicable fees and consumption tax). [command-verified: per-character strike and colour check, 2026-11-13] R-ZH and R-CA-ZH insert only "销售" ("原始订单的{销售}价格减去适用费用") and strike nothing in that sentence.
- The whole 18-month price-indicator block and the "Estimated proceeds" note are struck through. They were the pre-2025 basis for pre-order claims. The current text puts them under no heading.
- A plain text extraction of these PDFs keeps struck text alongside inserted text with no marker. Read without the rendering, the struck sentences look live.
- News post (2024-12-18) and staff (2026-08-13, held as finance E4): post-order losses are reimbursed at "the sales price on the original order minus applicable fees".

**(b) Practitioners.** Seller_6xcCLJodrIRK8 (2026-08-05) reads the policy as "refund/replacement value given to the customer on the original order" and reports a different valuation in practice (§ E) [opinion]. sellerboard, Nova Data and others (finance pack) do not separate the two bases.

**(c) Into a skill:** a post-order loss (customer-return claim) is valued on the order: the redlines of 2024-12 to 2025-02 say the original order's sales price minus applicable fees (VAT out in UK/DE; consumption tax out in JP); the JP Japanese redline names sales price, refund amount or replacement price; the live page is unread by a permitted route. Which basis applies today, and whether a partial refund sets the value, is read on G200213130 as the seller's store shows it and on the line itself (open question 2). **Read at run time:** the order's item price and fees through the Finances API for `amazon-order-id` (the finance pack's reads), compared with `amount-per-unit` on lines whose `reason` is customer-return-type.

### G. The per-unit cap (a value that moves by marketplace)

**(a) Amazon's words.** "The maximum reimbursement amount for a single unit of any FBA eligible item is $5,000. For items valued at more than $5,000, we recommend that you consider buying third-party insurance." The same sentence, with each store's figure and currency, is in every policy text read: R-US, R-CA, R-UK, R-DE, the FR/IT/ES text layers, R-ZH, R-CA-ZH ("5,000 加元"), R-JP-EN ("675,000 JPY") and R-JP-JA ("1 ユニットあたりの最大補てん額は675,000 円です"); a UK-store staff post of 2024-10-26 gives the UK figure ("The max is £2,000 per unit", 9d4ff2a6). The values by store, with dates, are in *Values that move*. The Supply Chain Portal's MCF reimbursement figure is a different programme's (see inbound-shortfalls IN22). [official]

**(b) Practitioners.** GETIDA restates "The maximum per unit, though, is $5,000" (undated blog) [opinion].

**(c) Into a skill:** a per-unit cap exists and differs by marketplace. A line paid at the cap on a unit worth more is not under-valued by policy. **Read at run time:** G200213130 as the seller's store shows it. No operation returns the cap.

### H. Telling an under-valued line in `GET_FBA_REIMBURSEMENTS_DATA`

**(a) Amazon's words / the data.** Columns and role: the finance pack, P-ref-19. The report carries `amount-per-unit`, `amount-total`, `currency-unit`, `condition`, `reason`, `case-id`, `amazon-order-id`, `approval-date`. No column names the valuation basis (seller cost, Amazon estimate, reduced estimate, sale price), whether a seller-submitted cost was on file, or the cap. [official columns; absence checked against the 18 columns on Amazon's *Report Type Values – FBA* page, developer-docs, read 2026-11-13.]

- The comparison values sit in different places:
  - The seller's approved sourcing cost or Amazon's estimate: MYSC, Seller Central only (§ C).
  - The seller's own cost record: the seller's books.
  - The sale price and fees on a post-order loss: the order's finance events.
- Data Kiosk's economics dataset carries a seller-provided per-unit cost: `cost: PerUnitCost` — "The off Amazon cost provided by the seller for this product (per unit). The off Amazon cost can be provided on [SKU Central] and [Revenue Calculator]"; `costOfGoodsSold`: "Cost to manufacture or acquire the product." [command-verified] `schemas/data-kiosk/analytics_economics_2024_03_15.graphql` in amzn/selling-partner-api-models (commit db2936a, 2026-10-29; the newer main commit b13d1d1, 2026-11-10, changes this schema only by adding fee types and a sandbox directive, not the cost fields). Amazon names SKU Central and the Revenue Calculator as its source, not MYSC. Nothing read says the two stores share a value [inferred: two separate entry pages named]. The Economics dataset's role is outside the seller app's five roles (see sp-api-claims-surface SU33).
- Reason → basis (from the policy's two headings; reason values from P-ref-35):
  - Pre-order: `Lost_Warehouse`, `Damaged_Warehouse`, `Lost_Inbound`, `Damaged_Inbound`, removal-related.
  - Post-order: `CustomerReturn`, `CustomerServiceIssue`.
  - `Lost_Outbound` / `Damaged_Outbound`: open. The post-order heading reads "Post-Order Lost or Damaged Events (customer return claims)" in R-JP-EN and "Post-Order Lost or Damaged Events" in R-US, and the section under it speaks only of customer-return claims; the claim kind is the customer-returns file's.
  [inferred]
- Timing: the cost in force is the one approved before the reimbursement was issued (§ C), so a line is compared with the cost approved as of its `approval-date` [inferred from Amazon's "issued after the approval date"]. MYSC shows only the current value and its last update (open question 4).
- Currency and store on unified and cross-border accounts:
  - The report carries `currency-unit` per line and no marketplace or store column (the 18 columns on *Report Type Values – FBA*, developer-docs `.md` twin, read 2026-11-13) [read in official docs].
  - Finances v0 `AdjustmentEvent` (type `FBAInventoryReimbursement`) carries `StoreName` ("The name of the store where the event occurred") and a `Currency` (`CurrencyCode`, ISO 4217) on `AdjustmentAmount`, `PerUnitAmount` and `TotalAmount`, and no marketplace id; a financial event group's `OriginalTotal` is "in the currency of the marketplace in which the transactions occurred" [command-verified, financesV0.json, models commit db2936a].
  - A sourcing cost is entered per marketplace (§ C) [official, staff on the marketplace dropdown], and the proof-of-value list asks for the "currency of transaction" [relayed].
  - Where money for other cross-border events lands, as far as Amazon's texts say, is held by the finance pack (research/areas/reconciliation.md, cross-border charges: EU removal fees "in the currency of the country where your inventory is stored"; Remote Fulfillment orders appear in the store "where the customer bought your product"). No Amazon text read says in which store and currency a reimbursement posts for a unit lost in a Pan-European transfer, in another country's FC under EFN, or in US stock sold through Remote Fulfillment, nor in which store a valuation dispute for it is filed. A developer reports that the reimbursements report returns the same rows whatever `marketplaceIds` names within a region (see sp-api-claims-surface SU24). [absence across the pages read; open question 12]

**(b) Practitioners.**

- Clawback (2026-07-05): compare per-unit amounts in Payments → Reimbursements against documented manufacturing cost per SKU [opinion].
- sellerboard (finance pack) lists "cases where Amazon reimbursed less than your product's cost of goods sold" [opinion].
- 积加 Gerpgo (finance pack) values expected reimbursements at "最近一次赔偿单价" (the most recent reimbursed unit price). That measure inherits any under-valuation [opinion, with seat note].

**(c) Into a skill:** an under-valued line is one whose `amount-per-unit` is below the basis the policy assigns to its reason:
- pre-order: the approved sourcing cost as of `approval-date`, or the estimate;
- post-order: the order's basis as the store's current policy states it (§ F: the redlines' sales price minus fees; unsettled for the live text);
- unsellable: lower by policy;
- capped: at the marketplace cap.

The test needs a cost Amazon does not expose by API. Where the seller supplies their cost, the comparison is with the seller's figure; whether Amazon holds the same figure is read in MYSC. **Read at run time:** `GET_FBA_REIMBURSEMENTS_DATA` (the line), the Finances API by `amazon-order-id` (post-order basis), Data Kiosk `analytics_economics_2024_03_15` `cost.costOfGoodsSold` (the SKU Central cost, if the seller entered one), MYSC in Seller Central (Amazon's held value).

### I. Inventory reimbursed (units put back) vs cash

**(a) Amazon's words.** "If we determine that your reimbursement claim is valid, we replace the lost or damaged item with a new item of the same FNSKU or reimburse you for it." Chinese: "我们将用 FNSKU 相同的新商品替换丢失或已残损商品，或者向您提供赔偿". [official] All redlines. Report columns `quantity-reimbursed-cash`, `-inventory`, `-total`: P-ref-17. Ledger: N "because you received an Amazon reimbursement", O "because Amazon has reimbursed you for them" (stock pack W30).

**(b) Practitioners.**

- Seller_xQqUFHevJCtYw (2018-01-11, thread 618623ce…): customer non-returns reimbursed with "Quantity Reimbursed [Cash]: 0 and Quantity Reimbursed [Inventory]: 1".
- Replies in the same thread:
  - "excess" received units (Seller_X9AxWaXfNnGAl).
  - Units from a holding account: "if they check the holding account and it's there, it's considered a 'reimbursement in quantity', vs. a found item" (Seller_la6yWqhB9Jzwb).
- [opinion, 2018; no Amazon reply in the thread]
- amzbase (guide, undated): "Inventory reimbursement is Amazon replacing units — no cash moves" [opinion].

**(c) Into a skill:** a unit put back carries no money, and its value to the seller is the unit itself. A line with `quantity-reimbursed-inventory` > 0 is not valued by `amount-per-unit` for those units (inferred; open question 5). **Read at run time:** the cash and inventory columns per line, and the ledger detail (`GET_LEDGER_DETAIL_VIEW_DATA`, Adjustments, codes N/O) for the unit's arrival.

### J. Reversals, clawbacks and found units

**(a) Amazon's words.**

- Policy (all redlines; English and Chinese): "If a reimbursement was made in error, or if a reimbursed item is later found and returned to your inventory, we reserve the right to reverse the reimbursement credit that was applied to your account." "如果赔偿有误，或者获得赔偿的商品随后被找到并退回至您的库存，我们有权撤销向您的账户发放的赔偿款项。" Reimbursed units, "including lost items that are found after reimbursement, may be listed for sale on Amazon warehouse or other channels". [official]
- The policy states no time limit for a reversal, and does not say whether a reversal is at the original amount or at a current value [official, by absence across all PDFs read].
- Staff on checking a reversal:
  - "I would start with checking your inventory ledger to verify if these units were added to your inventory. If you have concerns, open a case with Seller Support to confirm." TaylorR_Amazon, 2024-11-29, thread 353fbc51.
  - "check your FBA Inventory details to check if the inventory was found and is being transferred between warehouses or otherwise being prepared for sale." Micah_Amazon, 2024-02-20, thread 9742b13e.
  - "For guidance on disputing a reimbursement reversal, please contact Seller Support directly." Nano_Amazon, 2025-03-20, thread c2302e97.
  - "opening a case with Seller Support so that team can take a further look" Jameson_Amazon, 2025-01-17, thread af89a498 (US store by its thread field and canonical link; this file earlier gave it as .ca).
  - [official, staff]
- Money lines (held in the finance pack, P-ref-33, P-ref-21):
  - settlement `REVERSAL_REIMBURSEMENT`, `COMPENSATED_CLAWBACK`, `MISSING_FROM_INBOUND_CLAWBACK`;
  - in the Finances v0 model, `ReimbursementClawback` is "An Amazon Easy Ship reimbursement clawback … This value is used only in the India marketplace" [command-verified, financesV0.json `AdjustmentType`]. It is not the FBA reversal.

**(b) Practitioners (all [opinion]).**

- *Time:* reversals 5 months (thread 0f7ea6ce, 2024-12-17), 6 months (e23102e6, 2024-02-11), 7 months (same thread), 16 months (af89a498, 2024-12-28) and "more than a year" (finance P-ref-18) after payment.
- *Damaged then "found" sellable:* a unit damaged in 2023-08 was reversed in 2024-12 and "added back to sellable inventory" (af89a498).
- *Bulk:* 2,350 units reversed at once with no unit visible as returned to stock, and a request for a per-unit reversal report (9742b13e, 2024-02-20 / 2024-03-12).
- *Value:* found units returned when the price had dropped ($1,249 → $849, e23102e6), or expired, then charged removal or disposal (My Amazon Guy, 2025-10-31, held as P-ref-18).
- *No ledger match:* finance P-ref-18 (58e0b08d).
- *Reversals after the seller's own window:* "amazon has no claim window for when they can randomly reverse reimbursements but I have one" (finance P-ref-18). One seller believes that "After a certain time, I believe 18 months" found items are not reversed (Seller_jDBIXSKlN1wEw, e23102e6).
- *Causes listed by a vendor:* Refunzo (2025-08-19) adds late customer returns arriving sellable after the window, and "Fee or inventory adjustments".
- *Chinese:* 知无不言 十一郎与流氓 (held in the finance pack): "如果后面货找到的话，还会扣除".

**(c) Into a skill:**
- A reversal row points to its original (P-ref-18/20). Policy allows two causes: error, or found-and-returned.
- The found side is a ledger event (F, or N/O for ownership corrections) on the same FNSKU. A reversal with no such event in the ledger is a mismatch the seller can raise through Seller Support. That is the seller's choice.
- Amazon publishes no reversal deadline and no reversal-amount rule.
- A reversal of a sourcing-cost reimbursement takes back what was paid. Whether it ever differs from the original `amount-total` is unread (open question 6).

**Read at run time:** `GET_FBA_REIMBURSEMENTS_DATA` rows with `reason` `Reimbursement_Reversal` and their `original-reimbursement-id`, and `GET_LEDGER_DETAIL_VIEW_DATA` Adjustments for the FNSKU (F, N, O codes, reconciliation reason "Inventory found" / "Reimbursed", stock pack W30/W31). For the money: the settlement report or Finances (finance pack reads).

---

## 2. Practitioner coverage note

English sources read:
- Amazon staff forum posts (KJ, Christine, Arish, Sofi, Bryce, Nano, Josh, Glenn, Abbie, Jameson, TaylorR, Micah, Kris);
- sellers' forum threads (US, CA);
- Eagle Eye;
- Clawback;
- Refunzo;
- GETIDA;
- My Amazon Guy (via finance);
- Hopted (copy).

Chinese sources read:
- Amazon's own Chinese policy PDF (R-ZH; a CA Chinese PDF exists, found by search, not read);
- AMZ123 (跨境小蚂蚁, 2024-12-27);
- 易销AI (贾科斯, 2025-08-07);
- AMZ123 / 知无不言 posts held in the finance pack.

Not found:
- no Chinese help-centre page (领星, 赛狐) on sourcing-cost disputes or on reversal matching beyond what the finance pack holds (Lingxing nets reversals; Gerpgo subtracts `Reimbursement_Reversal`);
- no published research measuring sourcing-cost estimates against invoices.

---

## 3. Positions

Tags:
- [read in official docs] = Amazon's page, PDF, News post or staff forum post;
- [relayed] = Amazon text quoted by a seller;
- [command-verified] = checked locally;
- [opinion] = practitioner;
- [inferred].

A value that differs by store or year is not stated in a position; it is in *Values that move*, with store, date and source.

**Rule and history**

- **VR1.** Before the 2025 change, FBA pre-order losses (shipment to Amazon, FC operations, removals) were valued at "estimated proceeds": an estimated sale price from 18-month median and list prices, "minus referral fees and fulfillment fees". Amazon's redlines strike this whole block. Sources: R-US, R-UK, R-DE, R-CA, R-JP-EN, R-JP-JA (struck text, rendered). [read in official docs]
- **VR2.** Pre-order losses are valued at sourcing cost from the date each store's text gives. The redlines regenerated on 2025-02-24 for US, CA, UK, DE, FR, IT, ES, US-Chinese and CA-Chinese all carry "After March 31, 2025" and "Manage Your Sourcing Cost" (Chinese: "2025 年 3 月 31 日", "管理您的采购成本"); JP is VR41. This extends P-ref-14/15 to these marketplaces. Sources: R-* PDFs (metadata 2025-02-24; US, CA, UK, DE, ZH, CA-ZH rendered; FR, IT, ES text layer only, in English). [read in official docs]
- **VR3.** Amazon's definition changed wording between drafts. US: "cost to source a product from a manufacturer, wholesaler, or reseller, or to produce the item". First UK draft (2024-12-11): "the cost to acquire, purchase, or produce the item". The UK 2025-02-24 text uses the US wording. Shipping, handling and customs duties are excluded in all versions, JP included. Sources: UK 2024-12-11 PDF; R-UK; R-US; R-JP-EN. [read in official docs]
- **VR4.** Sourcing-cost valuation also covers losses "during inventory replenishment handled by Amazon or on behalf of Amazon to fulfillment centers or non-Amazon buildings in marketplaces where we provide the service" (JP: "lost and damage claims for inventories handled by Amazon or on behalf of Amazon to fulfill shipments"). Source: R-US and peers; R-JP-EN. [read in official docs]
- **VR5.** Amazon's estimate is built from "comparable products sold by Amazon, by other sellers, and through other wholesale channels". From a date each store's text gives, Amazon periodically refreshes estimates and alerts a seller whose provided cost is affected; impacted items show in MYSC's status column. Sources: R-US; R-JP-EN; KJ_Amazon 2025-04-30. [read in official docs]
- **VR6.** Amazon states that a seller's cost data "is not shared with any other seller in Amazon's store, including Amazon Retail". Source: R-US; R-JP-EN; KJ_Amazon 2025-04-30. [read in official docs]

**Manage Your Sourcing Cost**

- **VR7.** MYSC holds one sourcing cost per FNSKU per marketplace (marketplace dropdown). It lists active FNSKUs "with planned shipments or current inventory". The same staff post says new ASINs appear only once "fully received and processed". Sources: KJ_Amazon 2025-04-30; Abbie_Amazon 2026-04-10 (US store). [read in official docs; the two sentences of the 2026 post disagree, both stated]
- **VR8.** An approved seller cost applies automatically to eligible pre-order reimbursements *issued after the approval date*. It does not revalue earlier reimbursements and is not re-submitted periodically. Sources: decline message relayed in thread cd2909d2 (2026-02-22); Arish_Amazon 2026-02-24; case reply relayed in 32451dd6 (2026-05-25); all US store. [read in official docs; relayed]
- **VR9.** Amazon may decline a submitted cost for four policy reasons: outlier, forged or illegible documents, account suspected of fraud or violations, and a repeat within a stated period of a decision without new information (JP words the last as "frequent cost updates for the same item or a reimbursement amount dispute decision … within the last [period]"). The period is read on G200213130 for the store (*Values that move*). A declined submission leaves the previously approved amount or Amazon's estimate in force. Source: R-US and peers; R-JP-EN. [read in official docs]
- **VR10.** A value Amazon's system judges an outlier is rejected automatically, with no step to upload an invoice. Amazon does not tell the seller why an invoice was or was not accepted. Sources: Christine_Amazon 2025-11-25 (US store; MYSC, no upload step); Glenn_Amazon 2026-01-15 (UK store). Christine_Amazon 2025-06-04 describes a separate automatic denial in the re-evaluation tool when the cost "significantly exceeds our internal thresholds" or no cost is approved. [read in official docs]
- **VR11.** Amazon limits the number of cost updates per FNSKU within a period. The count is read at run time on the *Manage Your Sourcing Cost* help page (GN655EHATZUVWBC3) for the store, or from the Update status column ("Number of attempts exceeded"). Amazon's statements differ by store and date: a Canada-store Seller Support reply (relayed, 2025-03-19) and US-store staff posts (2025-11-25 to 2026-02-24); values in *Values that move*. No source read settles whether the count changed over time or differs by store. [read in official docs; relayed; contradiction stated with store and date]
- **VR12.** The entered cost must equal the figure on the proof-of-value document. A mismatch is itself a decline reason ("value mismatch"). Sources: Bryce_Amazon 2025-04-04; decline message relayed in cd2909d2. [read in official docs]
- **VR13.** The proof-of-value fields Amazon lists:
  - document name, number and date;
  - buyer entity name (as registered with Amazon), address and tax ID;
  - issuer entity name, address and ID;
  - product code, description and quantity;
  - per-unit or net cost;
  - currency.
  Accepted documents: manufacturer, wholesaler, purchase or commercial invoices; staff also name retail receipts, and a pro forma with proof of payment. Formats: PDF, JPG, JPEG, PNG. Sources: GN655EHATZUVWBC3 as copied by a seller (d23add81, Canada store, 2025-03-19); Arish_Amazon 2026-02-24; Christine_Amazon 2025-12-01, 2026-03-06; Nano_Amazon 2025-06-12. [read in official docs; the help page relayed]
- **VR14.** Amazon states a maximum age for a proof-of-value invoice. It is read at run time on GN655EHATZUVWBC3 for the store. Two US-store staff posts state different values (2025-06-12 and 2025-12-01; *Values that move*); neither cites the help page's sentence, and no later source read settles which is current. [read in official docs; contradiction stated with dates]
- **VR15.** For self-manufactured goods, staff name an internal cost document showing product, unit cost and date, component invoices with a cost breakdown, and a Seller Support case for manual review. Source: Christine_Amazon 2026-03-06; Nano_Amazon 2025-06-12. [read in official docs]
- **VR16.** MYSC is evidenced for US, CA, UK, DE, FR, IT, ES and JP. US, CA and UK by staff or relayed posts in those stores' forums and by policy texts; DE, FR, IT and ES by the 2025-02-24 redlines; JP by its 2025-02-19 policy texts (VR41). Whether the JP portal shows the page today is unread. Sources: threads (US, CA d23add81, UK 8033bd61), R-* PDFs, R-JP-EN, R-JP-JA. [read in official docs]
- **VR17.** A multi-product invoice whose line for the FNSKU cannot be isolated was refused. The same invoice with the line highlighted, sent through a support case, was accepted. Source: Eagle Eye, Ivan Raineri, 2026-09-12. [opinion]
- **VR18.** No SP-API operation reads or writes MYSC or files a valuation dispute (see sp-api-claims-surface SU12; finance P-ref-29). Supplement for this file's terms: no model in amzn/selling-partner-api-models db2936a contains `sourcingCost`, "sourcing cost", `manufacturingCost` or "manufacturing cost", and no `operationId` names a reimbursement, dispute or cost; a grep for `sourcing` alone hits only unrelated text (Orders' "Sourcing On Demand", Inbound v0's "item sourcing decisions", the vendor-only Data Kiosk `sourcingView` and vendor report schemas, an order-change notification). [command-verified, 2026-11-13]
- **VR19.** Data Kiosk `analytics_economics_2024_03_15` exposes a seller-entered `cost.costOfGoodsSold`. Amazon says it comes from SKU Central and the Revenue Calculator, not MYSC, and no read shows the two hold the same value. Its role is outside the seller app's (see sp-api-claims-surface SU33). Source: schema text, commit db2936a. [command-verified for the field and its stated source; the separation is inferred]

**Disputes**

- **VR20.** Amazon sets a window for disputing a reimbursement's valuation. Every policy text read (US, CA, UK, DE, FR, IT, ES, JP; US- and CA-Chinese) counts it from the reimbursement's issue; the one News post that states a re-evaluation window (d8f9a56c, effective 2025-10-15) was issued for the Australia store and counts it from the initial claim. Its length is a per-store value read at run time on G200213130 as the seller's store shows it and in that store's latest News post on claim windows (*Values that move*). The UK's text moved from 90 days (staff 2024-10-26; PDF 2024-12-11) to 60 (R-UK 2025-02-24) without the redline marking the change. Sources: the PDFs in § 5; 9d4ff2a6; d8f9a56c; staff posts 2025-04 to 2026-06 (US store). [read in official docs; store of the News post command-verified]
- **VR21.** Staff name two routes for disputing a value. (1) The self-service Get Help workflow "Dispute a reimbursement claim" (Sofi_Amazon and the decline message name it; Christine_Amazon 2025-06-04 names a "reimbursement re-evaluation tool" at help-hub solution `WF_fba_reimbursement_revaluation`; that the two are one workflow is inferred, the URL is unread). It applies an already approved MYSC cost to pre-order events reimbursed as "sellable", missing-from-inbound included. (2) "Submit a reimbursement claim dispute" under Get Help, where documents can be uploaded for human review. A case reopening is a third path, and staff say it is not the same process. All in US-store threads. Sources: Christine_Amazon 2025-06-04 and 2025-11-25; Sofi_Amazon 2026-06-05; decline message relayed in cd2909d2. [read in official docs]
- **VR22.** The policy's repeat rule covers "reimbursement amount dispute[s]" as well as cost updates. Its period is read on G200213130 for the store (*Values that move*). Source: R-US and every redline read, R-JP-EN and R-JP-JA included. [read in official docs]
- **VR23.** A cost approved after a reimbursement was paid at the estimate was refused as a case adjustment "Since the reimbursement was processed before your sourcing cost was approved". Staff pointed to the self-service dispute instead, within the dispute window (VR20). Sources: case reply relayed 2026-05-25; Sofi_Amazon 2026-06-05 (thread 32451dd6, US store). [read in official docs; relayed]
- **VR24.** Pitfall of timing. A decline under the attempt lock (VR11) can outlast the dispute window counted from the reimbursement (VR20). In one dated US case, the window closed 11/16 and the next update was allowed 11/23. Source: Seller_T7bkq3pJHibSr, 2025-10-23. [opinion]

**Unsellable, post-order, cap**

- **VR25.** Pre-order units unsellable when lost, damaged or removed are reimbursed at "a reduced estimated cost" (JP: stated for removal claims of unsellable items only). Amazon may ask for documents to set it, and no page gives the reduction. Source: R-US and peers; R-JP-EN, R-JP-JA. [read in official docs]
- **VR26.** Post-order units unsellable when lost or damaged are reimbursed at "the discounted sale price of that order minus applicable fees" (UK/DE: "and VAT"). This sentence was inserted in the 2024-12/2025-02 redlines for US, CA, UK and DE; the JP texts of 2025-02-19 carry no such sentence. Source: R-US, R-UK, R-DE, R-CA; R-JP-EN, R-JP-JA. [read in official docs]
- **VR27.** The basis of a customer-return claim is read on G200213130 as the seller's store shows it; the live page could not be read by a permitted route on 2026-11-13. The redlines' text: the US, CA, UK and DE redlines (2024-12 to 2025-02, rendered) and R-JP-EN strike "refund amount or the … of the replacement item" and insert "sales", reading "the sales price on the original order minus applicable fees" (UK/DE: "and VAT"; JP: "and consumption tax"); R-ZH and R-CA-ZH insert "销售" only. The customer-returns file's reading of a live US page (the refund-or-replacement basis, RT42) came through the help hub's content call, which the office closed on 2026-11-10; it is not carried here, and it is why the current basis is not stated as settled. Source: rendered R-US, R-UK, R-DE, R-CA, US 2024-12-18 PDF, UK 2024-12-11 PDF, R-JP-EN, R-ZH, R-CA-ZH. [read in official docs, for the redlines; live text unread]
- **VR28.** Pitfall of the data. Amazon's redlined policy PDFs keep struck text in their text layer. A text extraction mixes old and new wording, and only a rendering shows which is live. [command-verified: the same PDFs read through rendering show strikes at the sentences P-ref-40 quotes]
- **VR29.** Amazon caps the reimbursement for a single unit, and the cap differs by store in amount and currency. It is read at run time on G200213130 as the seller's store shows it; no operation returns it. Values by store in *Values that move*. A line paid at the cap on a unit worth more is paid as the policy states. Sources: every policy text in § 5; 9d4ff2a6 (UK staff). [read in official docs]

**Reading the report**

- **VR30.** `GET_FBA_REIMBURSEMENTS_DATA` lists eighteen columns on *FBA Reports*, `approval-date`, `reimbursement-id`, `case-id`, `amazon-order-id`, `reason`, `sku`, `fnsku`, `asin`, `product-name`, `condition`, `currency-unit`, `amount-per-unit`, `amount-total`, `quantity-reimbursed-cash`, `quantity-reimbursed-inventory`, `quantity-reimbursed-total`, `original-reimbursement-id` and `original-reimbursement-type` (read 2026-11-23), and none for the valuation basis, the cost in force, the cap or the store. An under-valued line can only be found by comparing `amount-per-unit` with a basis read elsewhere: MYSC (Seller Central), the seller's own cost, or the order's basis (VR27). Sources: Amazon's *Report Type Values – FBA* page (18 columns, read 2026-11-13); P-ref-19; VR18. [inferred from official columns]
- **VR31.** The basis a line should have follows its reason class. Warehouse, inbound and removal reasons take sourcing cost; customer-return and customer-service reasons take the order basis (VR27). The policy's two headings and P-ref-35's reason values give this. Where `Lost_Outbound` / `Damaged_Outbound` fall is unread; the claim kind belongs to customer-returns. [inferred]
- **VR32.** The cost to compare a pre-order line with is the cost in force at its `approval-date`, not today's MYSC value. MYSC shows only the current value and its last update. Sources: VR8; thread 53eb4da7 (Last-updated column). [inferred]
- **VR33.** A materially-different customer return reimbursed through removal handling was reported paid at sourcing cost, "roughly 30-60% of actual buy cost", rather than at the order basis. Source: Seller_6xcCLJodrIRK8, 2026-08-05, thread a2c0b1c6 (US store); the customer-returns file reports the same pattern for US wrong-item claims from two further threads (see customer-returns RT17). [opinion]

**Inventory vs cash; reversals**

- **VR34.** Amazon may settle a valid claim by replacing the unit "with a new item of the same FNSKU" instead of paying. Such a line moves units, not money. Sources: policy (all versions, JP included); P-ref-17. [read in official docs]
- **VR35.** (withdrawn: a single 2018 seller thread with no Amazon reply cannot carry a position; its reports stay as evidence in § I(b) and open question 5.)
- **VR36.** Amazon's policy names two grounds for reversal: error, or a reimbursed item found and returned to inventory. It states no time limit and no rule for the amount reversed. Sources: all redlines, English, Chinese and Japanese ("Amazon は販売事業者のアカウントに適用された返金額を回収する権利を保持します"). [read in official docs]
- **VR37.** Staff send a seller who doubts a reversal to the inventory ledger (to see whether the units were added back) and to Seller Support. No staff post names a dispute window for a reversal. Sources: TaylorR_Amazon 2024-11-29; Micah_Amazon 2024-02-20; Nano_Amazon 2025-03-20; Jameson_Amazon 2025-01-17 (all US store). [read in official docs]
- **VR38.** Pitfall of the data. Sellers report reversals 5 to 16 months after payment, including a unit "damaged" in the FC later reversed and added back as sellable, and bulk reversals (2,350 units) with no unit visible as returned. Sources: threads 0f7ea6ce, e23102e6, af89a498, 9742b13e (all US store). [opinion]
- **VR39.** Finances v0 `ReimbursementClawback` is an India-only Easy Ship value and does not mark FBA reversals. FBA reversals show as report reason `Reimbursement_Reversal` and settlement descriptions held in the finance pack (P-ref-33). Source: financesV0.json `AdjustmentType` description. [command-verified]
- **VR40.** Ledger codes N and O move units "because you received an Amazon reimbursement" or "because Amazon has reimbursed you for them". So a ledger row that adds units back is not always a physical find: an N or O row is an ownership move tied to a reimbursement, an F row a find. Sources: stock pack W30 (Amazon's reason table). [read in official docs, held by the stock pack; the matching reading is inferred]

**Japan, language, currency, cross-border evidence**

- **VR41.** Amazon's JP policy (English and Japanese texts, PDFs created 2025-02-19, "as of 02/19") values shipment-to-Amazon, removal and FC-operations claims at the item's sourcing cost ("原価"), lets the seller enter it on the IDR portal's "Manage Your Sourcing cost" page ("原価の管理"), applies Amazon's estimate otherwise, refreshes estimates from a date of its own, carries the same decline reasons and a repeat rule, a per-unit cap in yen and a valuation-dispute window counted from the reimbursement (values in *Values that move*). This settles the JP part of open question 3 for the policy text, and agrees with removals-disposals RM18. Sources: R-JP-EN, R-JP-JA (rendered, 2026-11-13). [read in official docs]
- **VR42.** Amazon's own texts of the same store and date can differ by language on the customer-return basis: R-JP-EN strikes the refund amount and replacement price, while R-JP-JA keeps both and adds the original order's sales price beside them ("元の注文の販売価格、返金額または交換商品の価格から、適用される手数料と消費税を差し引いたもの"). Source: R-JP-EN, R-JP-JA, per-character strike and colour check. [command-verified]
- **VR43.** No Amazon text read says in which store and currency a reimbursement posts for a unit lost in a Pan-European transfer, in another country's FC under EFN, or in US stock sold through Remote Fulfillment, or in which store its valuation is disputed. What the data carries: the report's `currency-unit` per line and no store column; Finances v0 `AdjustmentEvent` `StoreName` and an ISO 4217 `CurrencyCode` per amount, with no marketplace id. Sources: *Report Type Values – FBA*; financesV0.json (db2936a); for other cross-border charges, the finance pack's reconciliation.md; sp-api-claims-surface SU24. [read in official docs and command-verified for the fields; the rest is absence]
- **VR44.** Amazon's proof-of-value list asks for the buyer to be "your business name registered with Amazon" and for the currency of the transaction, and staff say the business name on the invoice "must exactly match your Amazon registration". No Amazon text read states a required language, or rules on a mainland Chinese VAT invoice (发票), a 1688 order receipt or a payment-platform receipt. An invoice whose buyer is a different entity from the selling account (a Hong Kong or mainland purchasing company buying for a US LLC) does not show the registered business as buyer. Sources: GN655EHATZUVWBC3 relayed (d23add81); Christine_Amazon 2025-12-01. [read in official docs; relayed; the related-company case inferred from the field]
- **VR45.** Chinese practitioners report Chinese-language invoices refused and English ones accepted, and name these choices for a cost proof, side by side: a mainland VAT invoice (专票 or 普票) verifiable on the State Taxation Administration's check site; an English commercial invoice from the supplier in the store's currency with the supplier's tax number; a commercial or pro forma invoice from the supplier or forwarder; a contract with payment record and stamped receipt; customs papers (one of which a Canada-store case saw refused as unclear). Sources: 贾科斯, 易销AI, 2025-08-07 (Canada and Germany cases); AMZ123 跨境小蚂蚁 2024-12-27. [opinion]

### Corrections to other packs

1. **Finance P-ref-40 (and E4a) — the 18-month method placed under post-order; the customer-return basis.**
   - P-ref-40 says post-order estimated proceeds are "an estimated sale price (from 18-month median prices and current list prices) minus referral fees and fulfillment fees". Rendered, the PDF it cites (`PC__Kiwi_Comms_redlined_policy_US_clean.pdf`, 2024-12-18) strikes the whole 18-month indicator block and the "Estimated proceeds" note, and the struck sentences apply that method to "a shipment to Amazon claim" and to "a fulfillment center operation claim or a removals claim": it was the *pre-2025 pre-order* method, not a post-order rule. The 2025-02-24 US, CA, UK and DE redlines and the 2025-02-19 JP texts show the same. Evidence: VR1, VR28.
   - The customer-return basis: P-ref-40 and the released skill's references/reimbursements.md quote "the refund amount or the sales price of the replacement item on the original order minus applicable fees". That string is the PDF's text layer, which keeps struck and inserted words together (VR28); rendered, the redlines read "the sales price on the original order minus applicable fees" (VR27). This file does **not** correct the finance pack's basis: the live page is unread by a permitted route, the JP Japanese redline keeps the refund amount beside the sales price (VR42), and the only live reading (customer-returns RT42) came through a barred route. The finance pack's owner may note that its quote mixes the redline's struck and inserted words. (This revises this file's earlier correction 1, which stated the sales price as the current basis.)
2. **Finance P-ref-40 / P-ref-16 / E4 — values and stores stated as if universal.**
   - The $5,000 cap is the US figure; each store has its own (*Values that move*: CAD 5,000, £2,000, €2,000, JPY 675,000).
   - The 60-day valuation-dispute window is the figure in every policy text read from 2024-12-18 on except the UK's earlier 90 days; P-ref-16's "Re-evaluation requests: Within 90 days of initial claim" comes from News d8f9a56c, which was issued for the **Australia** store (thread field A39IBJ37TRP1C6, canonical sellercentral.amazon.com.au), not a US or EU rule.
   - E4 calls a941ac02 the "EU copy" of the 2024-12-18 announcement; its store field and canonical link are the UK's. The thread this file cited as the US post, da761b17, is Canada's; the US post is 68864b6f.
   - Evidence: VR20, VR29, § A.
3. **Finance P-ref-14 — "a unit that was unsellable when lost is reimbursed at 'a reduced estimated cost'".** That holds for pre-order events only (in JP, for removal claims of unsellable items only). Post-order unsellable units are valued at the order's discounted sale price minus fees in the US, CA, UK and DE redlines; the JP texts state no post-order unsellable rule. Evidence: VR25, VR26.
4. **Stock pack P-inbound-29 (inbound.md F5) — "announced on the UK forum as effective March 10, 2025".** The effective date moved to 2025-03-31 (News ed8abc33, held as P-ref-15), and the UK redline of 2025-02-24 carries "After March 31, 2025". The UK text also now uses "sourcing cost", not "manufacturing cost". Evidence: VR2.
5. **Survey notes 04-job-money.md §4.4** ("Practitioners write 'March 31'; Amazon's posts say March 10"; "Manage Your Manufacturing Cost page"): outdated on both counts (P-ref-15 already holds this; restated for the survey's readers).

### Values that move

Each value is evidence of a rule stated in a position; it is read again for the seller's store at run time. All read 2026-11-13.

| Value (position) | Store | As read | Source and its date | Where read at run time |
|---|---|---|---|---|
| Per-unit cap (VR29) | US | $5,000 | R-US 2025-02-24; US PDF 2024-12-18; R-ZH | G200213130 as the store shows it |
| | CA | CAD 5,000 ("5,000 加元") | R-CA, R-CA-ZH 2025-02-24 | same |
| | UK | £2,000 | R-UK 2025-02-24; UK PDF 2024-12-11; staff 9d4ff2a6 2024-10-26 | same |
| | DE | €2,000 | R-DE 2025-02-24 | same |
| | FR, IT, ES | €2,000 | text layers of R-FR, R-IT, R-ES 2025-02-24 (not rendered) | same |
| | JP | JPY 675,000 ("675,000 円") | R-JP-EN, R-JP-JA 2025-02-19 | same |
| | AU, MX, IN, BR, others | not found | — | same |
| Valuation-dispute window (VR20) | US | 60 days after the reimbursement is issued | R-US 2025-02-24; US PDF 2024-12-18; staff 2025-04-30 to 2026-06-05; decline message 2026-02-22 | G200213130; the store's latest News post on claim windows |
| | CA | 60 days after issue | R-CA, R-CA-ZH 2025-02-24 | same |
| | UK | 90 days after issue | staff 9d4ff2a6 2024-10-26; UK PDF 2024-12-11 | same |
| | UK | 60 days after issue | R-UK 2025-02-24 | same |
| | DE, FR, IT, ES | 60 days after issue | R-DE; text layers of R-FR, R-IT, R-ES; 2025-02-24 | same |
| | JP | 60 days after issue ("返金が行われてから60 日以内") | R-JP-EN, R-JP-JA 2025-02-19 | same |
| | AU | "Within 90 days of initial claim" | News d8f9a56c, posted 2025-08-14, effective 2025-10-15 | same |
| Repeat period for a cost update or amount dispute without new information (VR9, VR22) | US, CA, UK, DE, FR, IT, ES, JP | 30 days | every redline read (2025-02-19 JP; 2025-02-24 others) | G200213130 |
| Cost updates per FNSKU per period (VR11) | CA | one per 30 days | Seller Support reply relayed in d23add81, 2025-03-19 | GN655EHATZUVWBC3; Update status column in MYSC |
| | US | two per 30 days; after both, wait 30 days from the first denial | Christine_Amazon 2025-11-25 (236be908), 2025-12-01 (acd6c179); Arish_Amazon 2026-02-24 (cd2909d2) | same |
| Maximum invoice age (VR14) | US | "within the last 365 days" | Nano_Amazon 2025-06-12 (b48840c1) | GN655EHATZUVWBC3 |
| | US | "less than 5 years old" | Christine_Amazon 2025-12-01 (acd6c179) | same |
| Sourcing-cost valuation starts; estimate refresh starts (VR2, VR5, VR41) | US, CA, UK, DE, FR, IT, ES | "After March 31, 2025" | 2025-02-24 redlines | G200213130 |
| | JP | refresh "After April 1, 2025" ("2025 年4 月1 日より"); no start date for the valuation itself in the text | R-JP-EN, R-JP-JA 2025-02-19 | same |

### Seat's own

These are this seat's readings and choices, not findings; none enters a skill as a rule.
- Using `approval-date` as the date that places a line before or after a cost's approval or the 2025 change (§ A(c), VR32): the nearest date the report carries; the policy does not name the governing date.
- Grouping reason values into pre-order and post-order bases (VR31) and the comparison that defines an "under-valued" line (§ H(c)).
- Reading the thread-level `marketplaceId` and canonical link as a post's store (method; homed in fc-lost-damaged).
- Which pack keeps valuation and reversals once the claims pack is published (finance `refunds-and-reimbursements`, this pack, or a shared reference): the office's call; this file only names where each fact now sits.


---

## 4. Open questions for a first run on a real account

1. What values does `condition` take on reimbursement lines for units reimbursed as unsellable, and does it mark the "sellable" condition the self-service dispute requires?
2. Which customer-return basis does the seller's store apply today (the redlines' sales price minus fees, or the refund or replacement price), and on a customer-return reimbursement after a partial refund, does `amount-per-unit` equal the order's sales price minus fees or the refund amount? (The live G200213130 is unread by a permitted route; VR27, VR42.)
3. Does the JP IDR portal show the 原価の管理 (MYSC) page today, and does the JP live policy keep the 2025-02-19 text? (The JP policy texts of 2025-02-19 answer the valuation part: VR41.)
4. Can the cost in force at a past date be read anywhere (a MYSC history or export), or only the current value and its last update?
5. On lines with `quantity-reimbursed-inventory` > 0, what do `amount-per-unit` and `amount-total` carry (zero, or a nominal value)?
6. Is a reversal's amount always the original `amount-total` (sign reversed), or is it ever revalued? Does every `Reimbursement_Reversal` row have a matching ledger F/N event on the same FNSKU, and within what lag?
7. Which window does the self-service "Dispute a reimbursement claim" workflow enforce for the seller's store, and does any store besides Australia count it from the initial claim?
8. Are the SKU Central / Revenue Calculator cost (Data Kiosk `cost.costOfGoodsSold`) and the MYSC sourcing cost one store or two on the same account?
9. Where do `Lost_Outbound` / `Damaged_Outbound` reimbursements sit (pre-order or post-order basis)?
10. Does the Support API's case read (sp-api-claims-surface) show valuation-dispute cases and their outcome, so a revaluation can be tied to its original line?
11. Does a revaluation arrive as a new reimbursement line (a new `reimbursement-id`) or as a change to the original?
12. On a Pan-European, EFN or NA unified account, which store and `currency-unit` does a reimbursement carry for a unit lost in a cross-border transfer, in another country's FC, or in US stock sold through Remote Fulfillment, and in which store is its value disputed (VR43; sp-api-claims-surface open question 2)?
13. Does Amazon accept a mainland Chinese VAT invoice, a Chinese-language invoice, a 1688 order receipt or a payment-platform receipt as proof of value, and an invoice whose buyer is a related company rather than the selling entity (VR44, VR45)? Settling sources: GN655EHATZUVWBC3's zh-CN layer if a permitted route opens; a gs.amazon.cn article on 采购成本; 知无不言 and AMZ123 threads on rejected 1688 invoices (not searched in this pass: the web search budget was spent).
14. What count of cost updates per FNSKU, and what maximum invoice age, does GN655EHATZUVWBC3 state today for the seller's store (VR11, VR14)?

---

## 5. Pages read

| Title | Address | Publisher | Page date | Read on | Used for |
|---|---|---|---|---|---|
| FBA inventory reimbursement policy (US redline, "R-US") | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_US.pdf | Amazon | PDF created 2025-02-24 | 2026-11-13 | VR1–6, 9, 22, 25–29, 34, 36; corrections 1–3 |
| FBA inventory reimbursement policy (US, "clean" redline) | https://m.media-amazon.com/images/G/01/rainier/help./PC__Kiwi_Comms_redlined_policy_US_clean.pdf | Amazon | PDF created 2024-12-18 | 2026-11-13 | A, F, VR20, VR27, VR28, correction 1 |
| FBA lost and damaged inventory reimbursement policy (UK, first redline) | https://m.media-amazon.com/images/G/01/rainier/help./_PC__Kiwi_Comms_redlined_policy_UK_clean_version.pdf | Amazon | PDF created 2024-12-11 | 2026-11-13 | VR3, VR20, VR29 |
| FBA lost and damaged inventory reimbursement policy (UK, "R-UK") | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_UK.pdf | Amazon | PDF created 2025-02-24 | 2026-11-13 | VR2, VR3, VR20, VR26, VR27, VR29 |
| FBA lost and damaged inventory reimbursement policy (DE, "R-DE") | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_DE.pdf | Amazon | PDF created 2025-02-24 | 2026-11-13 | VR2, VR20, VR26, VR27, VR29 |
| FBA inventory reimbursement policy (CA, "R-CA") | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_CA.pdf | Amazon | PDF created 2025-02-24 | 2026-11-13 | VR2, VR16, VR20, VR29 |
| FR / IT / ES redlines (English text; text layer read, not rendered) | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_FR.pdf (…_IT.pdf, …_ES.pdf) | Amazon | PDFs created 2025-02-24 | 2026-11-13 | VR2, VR16, VR29 |
| Report Type Values – FBA (`GET_FBA_REIMBURSEMENTS_DATA` columns and roles) | https://developer-docs.amazon.com/sp-api/docs/report-type-values-fba | Amazon (developer docs) | — | 2026-11-13 | H, VR30 |
| 亚马逊物流库存赔偿政策 (US policy, Chinese, "R-ZH") | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_US-zh_cn.pdf | Amazon | PDF created 2025-02-24 | 2026-11-13 | B, E, F, I, J, VR27 |
| 亚马逊物流库存赔偿政策 (CA policy, Chinese, "R-CA-ZH") | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_CA-zh_cn.pdf | Amazon | PDF created 2025-02-24 | 2026-11-13 (rendered) | A, F, VR2, VR20, VR27, values table |
| FBA lost and damaged inventory reimbursement policy (JP, English, "R-JP-EN") | https://m.media-amazon.com/images/G/09/rainier/help/redline_FBA_reimbursement_policy__EN_version.pdf | Amazon | "as of 02/19"; PDF created 2025-02-19 | 2026-11-13 (rendered) | A, E, F, VR1, VR3–6, VR9, VR25–27, VR41, VR42, values table |
| 破損・紛失商品の返金ポリシー (JP, Japanese, "R-JP-JA") | https://m.media-amazon.com/images/G/09/rainier/help/redline_FBA_reimbursement_policy__JP_version.pdf | Amazon | PDF created 2025-02-19 | 2026-11-13 (rendered) | A, E, F, VR36, VR41, VR42, values table |
| Update to the FBA inventory reimbursement policy (News, US store) | https://sellercentral.amazon.com/seller-forums/discussions/t/68864b6f-0ab8-41ef-be18-069c33df6336 | Amazon (News_Amazon) | 2024-12-18 | 2026-11-13 | A; correction 2 |
| Update to the FBA inventory reimbursement policy (News, UK store) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/a941ac02-d389-409a-9d62-00ab9db5bc4a | Amazon (News_Amazon) | 2024-12-18 | 2026-11-13 | A; correction 2 |
| FBA Lost and Damaged Inventory Reimbursement Policy (staff post, UK store) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/9d4ff2a6-8244-4ad9-bc8c-0d051600e817 | Seller Forums (Angie_Amazon) | 2024-10-26 | 2026-11-13 | D, VR20, VR29, values table |
| 你最关心的亚马逊库存管理问题，这次全解决！附案例 | https://gs.amazon.cn/zhishi/article-250305-3 | Amazon Global Selling | 2025-03 | 2026-11-13 | C (no proof-of-value content; inbound ownership only) |
| 亚马逊FBA货件状态怎么查？丢件能不能赔偿？一次讲清 | https://gs.amazon.cn/zhishi/article-250807-3 | Amazon Global Selling | 2025-08 | 2026-11-13 | C (no proof-of-value content) |
| Report Type Values – FBA, `.md` twin | https://developer-docs.amazon.com/sp-api/docs/report-type-values-fba.md | Amazon (developer docs) | — | 2026-11-13 | H, VR30, VR43 |
| Finances v0 model (`AdjustmentEvent`, `AdjustmentItem`, `Currency`, `FinancialEventGroup`) | amzn/selling-partner-api-models, `models/finances-api-model/financesV0.json` (commit db2936a) | Amazon (GitHub) | 2026-10-29 commit | 2026-11-13 | H, VR43 |
| Update to the FBA inventory reimbursement policy (News, Canada store) | https://sellercentral.amazon.com/seller-forums/discussions/t/da761b17-58cc-4734-98d2-5608e1d11419 (canonical .ca) | Amazon (News_Amazon) | 2024-12-18, updated 2024-12-19 | 2026-11-13 | A; seller reading of non-returns |
| Update to FBA inventory reimbursement claim windows (News) | https://sellercentral.amazon.com/seller-forums/discussions/t/d8f9a56c-882f-437c-ad34-cccd11cfa465 | Amazon (News_Amazon) | 2025-08-14 (eff. 2025-10-15) | 2026-11-13 | VR20 |
| New reimbursement policy - how are these values calculated | https://sellercentral.amazon.com/seller-forums/discussions/t/c7c767bc-9709-44ae-b8ee-a9e6c3268b27 | Seller Forums (KJ_Amazon reply) | 2025-03-21 / 2025-04-30 | 2026-11-13 | B, C, VR5–7, jewellery reports |
| illegal reimbursement | https://sellercentral.amazon.com/seller-forums/discussions/t/ca7ad06b-9c61-4127-9ea6-f190833409d0 | Seller Forums (KJ_Amazon) | 2025-04-26 / 2025-04-30 | 2026-11-13 | C, D |
| Reimbursement for lost and damaged goods | https://sellercentral.amazon.com/seller-forums/discussions/t/b0f2ffee-baec-4fd9-8562-6c185562ed2a | Seller Forums (KJ_Amazon) | 2025-06-03 | 2026-11-13 | C, D |
| Sourcing Cost - Hypothetical Question | https://sellercentral.amazon.com/seller-forums/discussions/t/f844fc37-b100-4980-8b98-2664d2d9cd6e | Seller Forums (Bryce_Amazon) | 2025-04-03 / 2025-04-04 | 2026-11-13 | VR12, VR21 |
| FBA reimbursement Re-evaluation and manage sourcing costs approval procedure??? | https://sellercentral.amazon.com/seller-forums/discussions/t/53eb4da7-c4f3-4059-9c9c-de87d80a4359 | Seller Forums (Christine_Amazon) | 2025-06-02 / 2025-06-04 | 2026-11-13 | VR10, VR21, VR32 |
| Managing Source Costs | https://sellercentral.amazon.com/seller-forums/discussions/t/236be908-148e-4b55-b6b2-3690e74c1acb | Seller Forums (Christine_Amazon) | 2025-11-18 / 2025-11-25 | 2026-11-13 | VR10, VR11, VR21 |
| Repeated Rejections of Valid Invoices for Sourcing Cost - Need Guidance | https://sellercentral.amazon.com/seller-forums/discussions/t/acd6c179-8504-4dfd-92ea-bb76a5557924 | Seller Forums (Christine_Amazon) | 2025-11-24 / 2025-12-01 | 2026-11-13 | VR11, VR13, VR14 |
| Mod Clarification - Manage sourcing cost … 60 days | https://sellercentral.amazon.com/seller-forums/discussions/t/cd2909d2-7dd0-4855-9f94-12051e13b8a3 | Seller Forums (decline message relayed; Arish_Amazon) | 2026-02-22 / 2026-02-24 | 2026-11-13 | VR8, VR11–13, VR20, VR21 |
| Sourcing cost approved, re-evaluation of reimbursement denied | https://sellercentral.amazon.com/seller-forums/discussions/t/32451dd6-651e-47f4-b3e4-dd642c86d7b9 | Seller Forums (Sofi_Amazon) | 2026-05-25 / 2026-06-05 | 2026-11-13 | VR8, VR21, VR23 |
| Amazon support exhausted my sourcing cost submission attempts | https://sellercentral.amazon.com/seller-forums/discussions/t/0ad71762-aee0-45a7-9ead-21541c3ba283 | Seller Forums | 2026-06-15 | 2026-11-13 | C (b) |
| Sourcing cost update failed - won't meet 60 day deadline | https://sellercentral.amazon.com/seller-forums/discussions/t/9d920446-76d9-4eaf-8296-0b4829847a15 | Seller Forums | 2025-10-23 | 2026-11-13 | VR24 |
| Question Regrading Re-Evaluation Reimbursement Request Denials | https://sellercentral.amazon.com/seller-forums/discussions/t/27d8463a-b74a-4bc1-ac71-fae1449c6f8c | Seller Forums (Josh_Amazon) | 2025-05-21 / 2025-05-30 | 2026-11-13 | D |
| Reimbursement Amount Far Below Actual Cost | https://sellercentral.amazon.com/seller-forums/discussions/t/d4d6c3dc-43ef-4a10-9724-a45fad531e8d | Seller Forums (Jameson_Amazon) | 2025-09-21 / 2025-09-22 | 2026-11-13 | C (decline reasons restated) |
| Proof of value document in Manage Your Sourcing Cost denied without explanation | https://sellercentral.amazon.ca/seller-forums/discussions/t/d23add81-e451-4c0c-abb3-515813658603 | Seller Forums, Canada store (GN655EHATZUVWBC3 list and Support reply relayed) | 2025-03-19 | 2026-11-13 | VR11, VR13 |
| Sourcing Cost - Proof of value document does not meet requirements Denied | https://sellercentral.amazon.com/seller-forums/discussions/t/b48840c1-3396-43ba-9731-b88f338e6aa8 | Seller Forums (Nano_Amazon) | 2025-06-12 | 2026-11-13 | VR14, VR15 |
| Proof of Value Documentation for Goods I Manufacture | https://sellercentral.amazon.com/seller-forums/discussions/t/5fb2d2f8-94fb-4494-853d-805a9c51016e | Seller Forums (Christine_Amazon) | 2026-03-02 / 2026-03-06 | 2026-11-13 | VR13, VR15 |
| New ASIN's not showing in Manage Your Sourcing Cost | https://sellercentral.amazon.com/seller-forums/discussions/t/270bbfe9-6291-448c-9ac8-4cb4bbccb82d | Seller Forums (Abbie_Amazon) | 2026-04-04 / 2026-04-10 | 2026-11-13 | VR7 |
| Manage Your Sourcing Cost (UK store) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/8033bd61-396b-4ed2-b40f-5bd71937e58b | Seller Forums, UK store (Glenn_Amazon) | 2025-12-14 / 2026-01-15 | 2026-11-13 | VR10, VR16 |
| New Manage Your Sourcing Cost board … | https://sellercentral.amazon.com/seller-forums/discussions/t/ec56a47b-c844-40c8-93bc-06c18960d96a | Seller Forums | 2025-03-04 | 2026-11-13 | B (b), bulk upload |
| Amazon's ridiculous sourcing costs … | https://sellercentral.amazon.com/seller-forums/discussions/t/1a833f18-a3cd-4dac-96f2-06c375718dd4 | Seller Forums | 2025-03-25 | 2026-11-13 | B (b) |
| Amazon's New Reimbursement Policy | https://sellercentral.amazon.com/seller-forums/discussions/t/11425b51-cf5f-4c25-a307-158f81399af6 | Seller Forums | 2025-03-10 | 2026-11-13 | B (b) |
| Buyer Returned a Different Item — What Happens Next? | https://sellercentral.amazon.com/seller-forums/discussions/t/a2c0b1c6-c0e8-46fa-9931-a4b651abbd85 | Seller Forums (Kris_Amazon post; seller reply) | 2026-08-05 | 2026-11-13 | VR33, E, F |
| Is there any way to dispute a reimbursement reversal? | https://sellercentral.amazon.com/seller-forums/discussions/t/c2302e97-e6ff-4d1c-a2d4-66090a91a097 | Seller Forums (Nano_Amazon) | 2025-03-03 / 2025-03-20 | 2026-11-13 | VR37, D |
| REIMBURSEMENT REVERSED WITHOUT REPLACEMENT | https://sellercentral.amazon.com/seller-forums/discussions/t/9742b13e-d2a7-4f5c-a4dc-b3a092adfc02 | Seller Forums (Micah_Amazon) | 2024-02-20 | 2026-11-13 | VR37, VR38 |
| TONS of reversed reimbursements … | https://sellercentral.amazon.com/seller-forums/discussions/t/353fbc51-4daf-4ccf-b864-3b9e88e568bf | Seller Forums (TaylorR_Amazon) | 2024-11-06 / 2024-11-29 | 2026-11-13 | VR37, VR38 |
| Invalid reversed reimbursement after six months | https://sellercentral.amazon.com/seller-forums/discussions/t/e23102e6-4f05-42a7-afa4-d69a53229adb | Seller Forums (TaylorR_Amazon) | 2024-02-11 / 2024-02-13 | 2026-11-13 | VR38 |
| Item was damaged in warehouse 16 MONTHS AGO. Now, Amazon reversed the reimbursement for that and supposedly added the inventory back. … | https://sellercentral.amazon.com/seller-forums/discussions/t/af89a498-9794-415a-bf6d-4cee39588d52 | Seller Forums, US store (Jameson_Amazon) | 2024-12-28 / 2025-01-17 | 2026-11-13 | VR37, VR38 |
| Need Assistance with an Ongoing issue with Lost Inventory Reimbursement being Reversed. | https://sellercentral.amazon.com/seller-forums/discussions/t/0f7ea6ce-c78e-4fe0-b33f-4830772b3904 | Seller Forums (Christine_Amazon) | 2024-12-17 / 2025-01-08 | 2026-11-13 | VR38 |
| Reimbursed from Inventory - Where do these units come from? | https://sellercentral.amazon.com/seller-forums/discussions/t/618623ce64ded0970d0d9e5a60f23e10 | Seller Forums | 2018-01-11 | 2026-11-13 | VR35 |
| Manage Your Sourcing Cost (help, GN655EHATZUVWBC3) — **unread** (JS shell by four routes); text relayed in d23add81, cd2909d2 | https://sellercentral.amazon.com/help/hub/reference/external/GN655EHATZUVWBC3 | Amazon | — | tried 2026-11-13 | VR11, VR13, VR14 (via relays) |
| FBA inventory reimbursement policy (help, G200213130) — **unread** by a permitted route (JS shell to a plain GET; the help hub's content call is barred) | https://sellercentral.amazon.com/help/hub/reference/external/G200213130 | Amazon | — | tried 2026-11-13 | run-time read named in VR20, VR29 |
| Reimbursement re-evaluation workflow (help-hub solution) — **unread** (signed-in page, named by staff) | https://sellercentral.amazon.com/help/hub/solution/WF_fba_reimbursement_revaluation | Amazon | — | not opened | VR21 |
| Data Kiosk schema analytics_economics_2024_03_15 | amzn/selling-partner-api-models, `schemas/data-kiosk/analytics_economics_2024_03_15.graphql` (commit db2936a; main b13d1d1 compared) | Amazon (GitHub) | 2026-10-29 commit; 2026-11-10 main | 2026-11-13 | VR19 |
| Finances v0 model (`AdjustmentType`) | amzn/selling-partner-api-models, `models/finances-api-model/financesV0.json` (commit db2936a) | Amazon (GitHub) | 2026-10-29 commit | 2026-11-13 | VR39 |
| Two Rejections Later, One Sourcing Cost Update Worth €805 | https://www.eagle-eye.software/blog/two-rejections-later-one-sourcing-cost-update-worth-805 | Eagle Eye (Ivan Raineri) | 2026-09-12 | 2026-11-13 | VR17, C, D |
| Amazon's 2025 Reimbursement Policy Change, Explained | https://clawbackfba.com/blog/amazon-reimbursement-policy-change-2025 | Clawback | 2026-07-05 | 2026-11-13 | D, H |
| Stop Revenue Loss: Handle Amazon Reversal Reimbursements Like a Pro | https://www.refunzo.com/blog/amazon-reversal-reimbursements-guide/ | Refunzo (Jimi Patel) | 2025-08-19 | 2026-11-13 | D, J |
| How to Make Sense of the FBA Reimbursement Report | https://getida.com/resources/blog/fba-reimbursements/fba-reimbursement-report/ | GETIDA | undated (2024 images) | 2026-11-13 | G |
| FBA Inventory Reimbursement Policy (third-party copy) | https://www.hopted.com/integrations/amazon-sp-api/amazon-help-articles/fba-inventory-reimbursement-policy | Hopted | undated | 2026-11-13 | VR20 (older 90-day text) |
| Lost Amazon Inventory Found Expired, Sellers Foot the Bill | https://myamazonguy.com/news/lost-amazon-inventory-found-expired/ | My Amazon Guy (Noah Wickham) | 2025-10-31 | 2026-11-13 | J (held as P-ref-18) |
| 亚马逊抢钱！新FBA赔偿政策只赔卖家成本！ | https://www.amz123.com/t/wwiRgOk7 | AMZ123 (跨境小蚂蚁) | 2024-12-27 | 2026-11-13 | A (b) |
| 为什么亚马逊总说你"发票无效"？2025年卖家合规指南+实战解法 | https://yixiaoai.com/post/amazon-invoice-compliance-guide-2025/ | 易销AI (贾科斯) | 2025-08-07 | 2026-11-13 | C (b) |
| Amazon FBA Bookkeeping (guide) | https://amzbase.com/guides/amazon-fba-bookkeeping/ | amzbase | undated | 2026-11-13 (search snippet) | I (b) |

Search-only (not opened): sellercentral.amazon.co.jp fee notices returned for a Japanese query on 調達コスト (earlier pass; superseded by the JP PDFs, which use 原価).

---

## Verification (2026-11-13)

An adversarial check of this file's load-bearing positions against their cited sources, from public pages only (no SP-API call, no login, no seller data).

**How checked.**
- Amazon's ten policy PDFs (R-US, R-CA, R-UK, R-DE, R-FR, R-IT, R-ES, R-ZH, the US 2024-12-18 PDF and the UK 2024-12-11 PDF) were downloaded again from m.media-amazon.com. Creation dates were read from the PDF metadata. Text was extracted, and struck and inserted text was told apart per character from the drawn strike lines and the text colour (red, underlined = inserted).
- Seller Forums threads cd2909d2, 236be908, 53eb4da7, acd6c179, 32451dd6, d23add81, b48840c1, 8033bd61 (.ca), 270bbfe9, d8f9a56c, da761b17, c7c767bc, f844fc37, 5fb2d2f8, 9d920446, 353fbc51, c2302e97 and af89a498 (.ca) were fetched again; quotes and `<time>` dates were matched.
- The SP-API models were grepped at db2936a, and main was compared at b13d1d1 (2026-11-10).
- Amazon's *Report Type Values – FBA* developer page was read for the report's columns.
- The Eagle Eye blog was read again.
- G200213130 is still a JavaScript shell (re-tried 2026-11-13).

**Confirmed.**
- PDF dates: 2024-12-11 (UK), 2024-12-18 (US), and 2025-02-24 for every R-*.
- "After March 31, 2025" and sourcing-cost wording in all eight R-* PDFs. "After March 10, 2025" and "manufacturing cost" in both 2024-12 PDFs. The UK 2024-12-11 definition "cost to acquire, purchase, or produce".
- The dispute line: 60 days in every 2025-02-24 redline and the US 2024-12-18 PDF; 90 days in the UK 2024-12-11 PDF.
- The cap per marketplace.
- The struck 18-month block and its UK "average" wording.
- The struck customer-return wording, and the post-order unsellable sentence as inserted text (red, underlined).
- The privacy, refresh and estimate sentences. The reversal sentence and the replace-or-reimburse sentence, English and Chinese.
- The News 2024-12-18/19 quotes, and the News 2025-08-14 "Within 90 days of initial claim".
- The staff quotes: VR8, VR10 (2025-11-25 and Glenn), VR11, VR12, VR13 (list as relayed, with the seller naming GN655EHATZUVWBC3), VR14, VR15, VR21 (routes 2 and 3), VR23, VR37.
- The dated cases in VR24 and VR17.
- The 18 report columns.
- `cost.costOfGoodsSold` and its stated SKU Central / Revenue Calculator source.
- `ReimbursementClawback` described as India-only Easy Ship.

**Changed.**
- § F: the pre-2025 customer-return sentence was misquoted. The word "sales" is an insertion, so the old text read "the refund amount or the price of the replacement item …". VR27 now names the insertion.
- § D: the DE dispute wording was misattributed (the UK reads "using the Get support page"; DE, FR, IT and ES read "on Get support").
- VR18: the grep result was misstated. `sourcing` also hits Inbound v0, the vendor-only Data Kiosk and report schemas, and a notification, none of them about sourcing cost. A newer upstream commit was checked.
- VR10: the 2025-06-04 staff post concerns the re-evaluation tool's denial, not the MYSC upload step. It is now separated.
- VR21: that the Get Help "Dispute a reimbursement claim" workflow and the `WF_fba_reimbursement_revaluation` tool are one workflow is now marked inferred.
- VR2, VR29, § A, § G: FR, IT and ES moved from "metadata only" to "text layer read" (English; March 31 date; €2,000 cap).
- § A(c): the use of `approval-date` to place a line before or after the change is marked inferred, since the policy does not say which date governs.
- Moving values: the repeat and attempt-lock period (VR9, VR22, VR24, § C(c), § D) and the dispute window (summary, VR23) are now stated as a rule read at run time, with the value kept as dated evidence.
- News d8f9a56c: noted as naming no marketplace.
- VR40: the matching instruction was rewritten as a fact about the N, O and F codes.
- § 5: two untitled thread rows now carry their titles, and the FBA report-type page was added.
- No path on this machine appears in the file.

**Forbidden positions found.**
- None of ours set a threshold, a sequence, a when-to-ask or a ceiling.
- VR40 carried a method instruction; it was rewritten.
- The practitioner advice kept in the file is quoted and tagged [opinion], with no position built on it: 易销AI on invoice language, currency and age; Clawback's "dispute candidate"; Christine_Amazon's view that the documented route "might be more successful", which was not carried.

**Remaining doubts.**
- The FR, IT and ES PDFs were not rendered, so whether any of their sentences are struck is unseen. Their caps and dates come from the text layer.
- G200213130 and GN655EHATZUVWBC3 remain unread at source. The live window, the attempt count and the invoice age rest on staff and relayed text.
- The marketplace scope of News d8f9a56c, and which window the self-service workflow enforces (open question 7), are unresolved.
- The Hopted copy paraphrases rather than quotes ("the replacement item price"). It is evidence of the older 90-day text only.
- Correction 4 (the UK forum's March 10 date) was not re-read against the UK thread. The UK 2024-12-11 PDF does carry "After March 10, 2025".

---

## Revision (2026-11-13)

Made after the completeness critic's round-1 review (items A1, A2, A3, A4, A6, A7, B, C, D, E, F, G, H; J and K have no item for this file beyond the relation to the finance skill, now stated). Public pages by plain GET only; no POST to any Amazon host, no help-hub content call, no SP-API host, no sign-in.

**Settled or narrowed.**
- *Store of each forum thread (A1).* Every thread cited was re-fetched; its thread-level `marketplaceId` and its canonical link agree on each, and two posts whose text names their store (amazon.ca, amazon.co.uk) calibrate the method. Results that change this file: News d8f9a56c (the "90 days of initial claim" post) is the **Australia** store's; da761b17, cited as the US announcement, is Canada's (the US one is 68864b6f; a941ac02 is the UK's); d23add81 (the "one cost update" reply and the relayed help-page list) is Canada's; 8033bd61 (Glenn_Amazon) is the UK's, not Canada's; af89a498 is the US store's, not Canada's.
- *Valuation-dispute window (A4; this file is its home).* Every policy text read counts it from the reimbursement's issue. The UK's 90 days (staff 2024-10-26, PDF 2024-12-11) became 60 in R-UK 2025-02-24; JP's texts read 60; the only from-claim window is Australia's. VR20 rewritten as a rule; values to the table. The customer-returns file's live US reading is not carried (barred route).
- *Per-unit cap (A7, D; home here).* JP's 675,000 yen added from R-JP-EN and R-JP-JA; CA-Chinese and the UK staff post added. The values left VR29 and § G for *Values that move*.
- *MYSC limits (A6; home here).* VR11: the "one per 30 days" statement is a Canada-store relay of 2025-03, the "two" are US-store staff posts of 2025-11 to 2026-02; stated with store and date, not settled. VR14: both invoice-age statements are US-store staff (2025-06-12: 365 days; 2025-12-01: under 5 years); stated with dates, not settled. Values to the table.
- *Japan (A7, C).* Amazon's JP policy redlines in English and Japanese (2025-02-19) were found and rendered: sourcing cost ("原価"), the "原価の管理" page on the IDR portal, refresh "After April 1, 2025", 30-day repeat rule, 60-day dispute window, JPY cap, the reduced estimate stated for unsellable removals only, no post-order unsellable sentence. Reconciled with removals-disposals RM18. The earlier search missed them because Amazon's Japanese word is 原価, not 調達コスト.
- *Customer-return value basis (A3).* VR27 now states the redlines' text and that the live page could not be read by a permitted route; the contrary live reading (customer-returns RT42) came through the barred route and is not used. Found by a permitted route: R-JP-JA keeps the refund amount and replacement price beside the sales price (VR42), so Amazon's own 2025 texts do not agree across languages. Correction 1 no longer corrects the finance pack's basis.

**Added.**
- Positions VR41 (JP policy), VR42 (JP English and Japanese texts differ on the customer-return basis), VR43 (store and currency of a reimbursement on Pan-EU, EFN and NA unified accounts: what the report and Finances v0 carry, and that no Amazon text read says more), VR44 (proof-of-value buyer entity and currency; no Amazon text on language, fapiao or 1688), VR45 (Chinese practitioners' choices for a cost proof, side by side) [B, C].
- § C: *Chinese cross-border evidence for a cost* (Amazon's relayed fields and staff words; gs.amazon.cn pages checked and found to cover inbound ownership only; 易销AI's mainland VAT-invoice, buyer-name, Chinese-invoice-refused and English-invoice-accepted cases; AMZ123).
- § H: currency and store fields in the report and in Finances v0 `AdjustmentEvent`.
- *Relation to the released finance skill* and *Homes inside this pack* paragraphs at the head (D).
- *Values that move* table; *Seat's own* list (F, E).
- Open questions 12 (currency on unified accounts), 13 (Chinese documents, 1688), 14 (current attempt count and invoice age); 2, 3 and 7 reworded.
- Pages read: R-CA-ZH, R-JP-EN, R-JP-JA, News 68864b6f and a941ac02, staff post 9d4ff2a6, two gs.amazon.cn articles, the developer-docs `.md` twin, the Finances v0 adjustment definitions.

**Changed.**
- VR1, VR2, VR3, VR4, VR5, VR6, VR9, VR22, VR25, VR26, VR34, VR36: JP texts added as sources; values (30 days, refresh date) moved out of VR9 and VR22.
- VR7, VR8, VR10, VR21, VR23, VR37, VR38: stores named; VR10 and VR38 store errors fixed.
- VR13: pro forma with proof of payment added; d23add81's store named.
- VR16: JP now evidenced by the JP policy texts.
- VR18: the "no operation" fact now points to sp-api-claims-surface SU12; only this file's term grep is kept (re-run at db2936a, no hits).
- VR19: role pointer to sp-api-claims-surface SU33.
- VR24, VR27, VR29, VR30, VR31: rewritten as rules with values in the table and the customer-return basis left to VR27.
- VR33: pointer to customer-returns RT17 for further reports (G: single-seller anecdote).
- Corrections: 1 revised (the 18-month method's placement stays; the basis correction is withdrawn); 2 extended (JP cap, d8f9a56c is Australia's, a941ac02 is the UK's); 3 extended (JP).
- § A: the 2024-12-18 announcement attributed to its three stores. § F: retitled; the live-page status and the JP and Chinese texts added. § G: the cap table replaced by a pointer to *Values that move*.

**Withdrawn.**
- VR35 (a single 2018 thread with no Amazon reply; the reports stay in § I(b)).

**Not done in this pass.**
- No Chinese web search on 1688 receipts or fapiao acceptance, and no further search for newer MYSC staff statements: the session's web search budget was spent. Only pages whose addresses were already known were fetched.
- G200213130 and GN655EHATZUVWBC3 remain unread: their plain GET returns a script shell, and the content call is barred.
