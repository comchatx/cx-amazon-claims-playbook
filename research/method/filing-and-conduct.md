# Filing and conduct: what a claim costs a seller, and what only Seller Central does

**Summary.** Every FBA claim is opened, evidenced, answered and reopened in Seller Central (an MCF account's claims under the Supply Chain Portal policy go through that portal's Contact Us); no SP-API operation does any of it (see sp-api-claims-surface SU12). Amazon publishes no cap on items per case or cases per day. It does publish a conduct rule that is unchanged in substance since at least April 2021: "insufficiently researched or premature requests" and "a large number of requests in a short time" (April 2021 policy PDF: "high volumes of requests"; Amazon's own denial and support messages already used "a large number of requests" in 2022 and 2024) interfere with support and can bring "delayed support", "monitoring, investigation, and account action". What Amazon's pages name as declined or as conduct is the claim that should not have been filed: one already reimbursed, a second claim for the same shipment, a premature request, a forged or tampered document (named for sourcing-cost submissions), or an issue re-raised after a "no further action" answer. Sellers report deactivations under Section 3 and the Seller Code of Conduct for "FBA credit reimbursement abuse". Since 2026-03-04 the Business Solutions Agreement also binds any automated agent acting on a seller's account, and the SP-API Acceptable Use Policy binds what an app submits to Amazon's support systems.

Date read for every page: 2026-11-13, unless a row says otherwise. Area code: FL.

**Routes and dates.** Every page here was read by a plain GET of a public page: Seller Forums threads, supplychain.amazon.com, Amazon's PDFs on m.media-amazon.com, developer-docs, GitHub and third-party sites. No POST went to any Amazon host, and the help hub's content call was not used (the office closed that route on 2026-11-10). A Seller Central help page answers a plain GET with a script shell, so it stays unread here; where its fact is carried, the route it came through is named. A forum post's date is its own `createdAt` (the thread's opening post also carries it as `datePublished`) in the page's embedded data, read 2026-11-13. The store a thread was posted to is the thread-level `marketplaceId`, not the host it was fetched from (the method and the post-to-store table are fc-lost-damaged's). Several threads below were posted to a different store than the host they were first read from: b175b700 and 807fb6a2 are US threads, 481080e4 and 8a2dfc1c are Canada threads.

**Scope and neighbours.** This file covers case mechanics, limits, penalised conduct, evidence formats, answers, reopening and escalation, and the policy texts that bear on an agent. The other areas of this research each own their part, and this file only points to them:
- what is owed per claim kind and its window: fc-lost-damaged, inbound-shortfalls, customer-returns, removals-disposals, fee-overcharges; the post-to-store table and the automation dates: fc-lost-damaged;
- how the amount is valued and when it is reversed, the per-unit cap, the valuation-dispute window and the Manage Your Sourcing Cost (MYSC) limits: value-and-reversals;
- roles, reports, the Support API's shape and that no operation files a claim: sp-api-claims-surface (its SU positions);
- what services charge and recover: recovery-economics.

**Already held elsewhere (not redone here).** The finance pack (cx-amazon-finance-playbook) research/areas/refunds-reimbursements-adjustments.md holds the claim windows as dated facts (P-ref-16) and the policy PDF of 2024-12-18 (P-ref-40). It also holds the SC-only list (P-ref-29, § What only Seller Central shows) and the services and their fees (P-ref-31, P-ref-32). The stock pack (cx-amazon-stock-playbook) research/areas/inbound.md holds the inbound reconciliation flow: `CLOSED` first, the Action required menu, the five-business-day reply, the 2–30/60-day research time and the invoice fields (§ F1–F3, P-inbound-26 to P-inbound-30). The door (cx-amazon-sp-api) holds how a call and a report are made.

---

## A. How a case is opened today, by claim kind

**(a) Amazon's words.** The policy text names four claim processes and makes following them a condition: "If your item is eligible under this policy, and we haven't already reimbursed you, you can file a reimbursement claim. The process to a file a claim varies depending on where in the fulfillment process your item is lost or damaged: Shipment to Amazon claims; Fulfillment center operations claim; Customer return claims; Removals claims. Important: You must follow the applicable process described on the pages above and provide all requested information when you file a claim. We may decline your claim if you do not." [read in official docs] (*FBA inventory reimbursement policy*, Amazon's redlined US PDF, https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_US.pdf, PDF created 2025-02-24, server last-modified 2025-02-27, read 2026-11-13.) The April 2021 text served under Amazon's UK path (G/02; its PDF title reads "EU FBA lost and damaged inventory reimbursement policy - ENG redline", created 2021-04-12) has the same sentences, with "Amazon has not already reimbursed you" and "Amazon may decline your claim if you do not" (…/G/02/rainier/help/legal/FBA_inventory_reimbursement_policy_April_2021_English_Redlined.pdf, read 2026-11-13).

The entry points, as an Amazon moderator gave them (Indy_Amazon, *FBA Lost Your Inventory? Steps to File a Reimbursement Claim*, https://sellercentral.amazon.com/seller-forums/discussions/t/0e07abc1-9026-4540-a005-153d9e78bf04, US store, `createdAt` 2026-08-13T07:49:10Z, read 2026-11-13) [read in official docs, staff post]:

| Claim kind | Entry point (Amazon's words) | Identifier the form takes |
|---|---|---|
| Warehouse damaged | "Reports > Fulfillment > Inventory Adjustments", find "Warehouse Damaged", then on the Reimbursement Policy help page the "Check warehouse damaged reimbursement status" tool | "Transaction Item ID" |
| Warehouse lost | Same report, "Missing" (M) events; case via "Help > Get Support > Selling on Amazon > Fulfillment by Amazon > FBA Issue > Inventory Lost in Warehouse" | "FNSKU or Transaction Item ID" |
| Shipment to Amazon (missing from inbound) | "Inventory > Shipments > Shipping Queue", the shipment's "Reconcile" tab | Shipment ID |
| Inbound units received damaged | A case through "Help > Get Support" | Shipment ID, invoice, proof of delivery |
| Customer return | "Check FBA order reimbursement status" tool on the policy page (but see the second statement below) | Customer order ID |
| Removal | "Resolve a removal order issue" tool on the policy page | Removal order ID, Shipment ID, ASINs/FNSKUs, quantities, images |

**Customer returns: two Amazon statements of the route, neither picked.**
- Indy_Amazon, US store, 2026-08-13: three steps, "Go to Reimbursement Policy Help Page", "Use the Check FBA order reimbursement status tool", "Enter the customer Order ID to check eligibility and file" [read in official docs, staff post].
- *FBA inventory reimbursement policy: Customer return claims* (G9N934L7Y4SFWPJ4), US v14 and CA v5, with the GB companion G84Z6B8BTKVNV53S: the claim tool starts from the customer order id shown on the IDR portal's "Eligible for claim" tab, and a "Resolved" decision can be contested from that tab. This is customer-returns RT41's reading, made 2026-11-13 through the help hub's content call, a route the office closed on 2026-11-10; this file did not re-read it (see customer-returns RT41) [read in official docs, through a route now closed].

The two can describe one flow (the portal tab hands the order id to the tool) or two doors; neither page says which.

Other entry points written down elsewhere:
- The IDR portal (FBA dashboard → Inventory → Inventory Defect and Reimbursement, "You can also access the IDR portal through the Reimbursements report") covers warehouse lost, warehouse damage and customer returns. "Note that the portal doesn't include defects under missing from inbound, removals or warehouse disposals." (News_Amazon, *Inventory Defect and Reimbursement portal now available*, thread b175b700-09c4-4350-8a22-24f60a724042, US store by its `marketplaceId` though first read on the EU host, `createdAt` 2025-01-21, read 2026-11-13; the finance pack holds it as E3; fc-lost-damaged FC13 holds what the portal shows) [read in official docs]. Its help page, *Inventory Defect and Reimbursement (IDR) Portal* (G66ZLS453YSE2Y4R, linked from the launch post and from Indy_Amazon's post), is a script shell and unread.
- **Shipment to Amazon, as an Amazon denial put it** (Canada store, thread 481080e4, `createdAt` 2022-07-25, signed "Sincerely, Amazon Services", pasted by the seller): "To submit a claim for lost units, use the Reconcile tab. To submit a claim for damaged units, open a claim through the Contact Us page in Seller Central." [read in official docs, relayed]
- A valuation dispute has its own route and window (see value-and-reversals VR20, VR21).
- Weight and dimension fees go through a remeasurement request (NR_Amazon, *Importance of Accurate Product Measurements*, thread ca22eab2-3fbe-4826-ab22-74a842fac674, US store, `createdAt` 2025-04-30; conditions and limits: see fee-overcharges FE4) [read in official docs, staff post].
- **An MCF account's claims under the Supply Chain Portal policy.** *Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS)* (https://supplychain.amazon.com/support/reimbursements, no revision date, © 2026, read 2026-11-13) requires "Your Multichannel Fulfillment (MCF) account is in Active state" and makes a seller ineligible who uses "MCF as a way to fulfill any order placed on the Amazon.com website, including self-fulfilled orders, FBA orders". MCF order claims "can be filed through the Contact Us page in Supply Chain Portal", and valuation disputes go to "the Contact Us page in Supply Chain Portal". The AWD service terms ("Dated: January 14, 2026", https://supplychain.amazon.com/legal/service-terms/warehouse-and-distribution, read 2026-11-13) link their words "MCF inventory reimbursement policy" to this same address [read in official docs]. Its windows and values are other files' (inbound-shortfalls, fc-lost-damaged, value-and-reversals) and differ from FBA's.

Seller-fulfilled SAFE-T and A-to-z filing are held by the finance pack (P-ref-9, P-ref-11).

**A pitfall in Amazon's own instructions.** The 2026 staff post sends sellers to "Reports > Fulfillment > Inventory Adjustments" and asks for a "Transaction Item ID". The Inventory Adjustments report is one of the six reports the Inventory Ledger replaced. Its API type `GET_FBA_FULFILLMENT_INVENTORY_ADJUSTMENTS_DATA` was removed on 2023-01-31, a date moved from 2022-11-15, with `GET_LEDGER_SUMMARY_VIEW_DATA` and `GET_LEDGER_DETAIL_VIEW_DATA` as replacements (Amazon's *Deprecation Notice: Suppressed listings reports and FBA Inventory reports*, developer-docs.amazon changelog, text seen in search results on 2026-11-13; stock pack, stock-states.md F8 and P-stock-states-28) [read in official docs, via search text and the stock pack]. Amazon's FBA report-type page read on 2026-11-13 no longer lists the adjustments type. The same staff post links a Seller Central report page at `https://sellercentral.amazon.com/reportcentral/INVENTORY_ADJUSTMENT/0` and lists "Inventory Adjustments Report — Track lost/damaged events" among its resources, beside the Inventory Ledger. Whether that Seller Central page still serves the report is behind sign-in and unread; the API type's removal does not settle it. The ledger's detail report carries a `Reference ID`. Whether that is the Transaction Item ID the tools accept is not stated by Amazon:
- a Chinese ERP guide says "Reference ID = Transaction item ID" [opinion];
- a US forum thread asks how to match a reimbursement to a ledger `Reference ID` and gets no Amazon answer (https://sellercentral.amazon.com/seller-forums/discussions/t/bd311a5a-25f4-404b-a7e6-f1945b93ae25) [opinion].

**(b) What practitioners add.**
- **Paths drift by year.** Older or third-party menu paths read:
  - "Fulfillment by Amazon" → "Investigate Other FBA Issues" → "Other FBA Issues" (知无不言 Allen哥, 2020-10-28, https://www.wearesellers.com/question/26211) [opinion];
  - "Get support>Contact us >selling on Amazon issue >Fulfillment by Amazon>Other FBA Issue" (AMZ123 大姐夫站外推广, 2022-01-04, https://www.amz123.com/t/1PmAosGP; Jungle Scout China, 2022-04-08, https://www.junglescout.cn/blog/48329/) [opinion];
  - "Help > Contact Us > Selling on Amazon > Fulfillment by Amazon > 'FBA Inventory Reimbursement'" (Nova Data 2026 guide) [opinion];
  - the IDR portal's "Eligible for Claim" / "In Progress" / "Resolved" views (eComEngine, updated 2025-03-03; RiverBend) [opinion]. Amazon's announcement names no tabs. The finance pack (P-ref-37) holds Amazon's Chinese naming of three statuses.
- **The 知无不言 tutorial** (2020) tells sellers to write "English" and to choose English in the form's language list [opinion].
- **SellerSpace / 优麦云 索赔助手** (2025-03-20, https://www.sellerspace.com/en-US/help/doc/claim-indemnity-assistant-use-guide/). The seller copies the FNSKU into Seller Central's form, submits it by hand, then binds the returned Case ID in the tool. Claims must be filed "in the Seller Central of the matching store and marketplace" to avoid "account association issues". Loss and damage are "two separate appeal paths with different supporting materials" [opinion].

**(c) Into a skill:** a claim is filed only through the Seller Central process for its kind, with all requested information (an MCF account's claims under the SCP policy: through the Supply Chain Portal). The entry point and the identifier differ by kind, and the IDR portal excludes missing-from-inbound, removals and disposals. For customer returns Amazon has stated two starting points (the policy page's order tool, 2026-08-13; the IDR portal's "Eligible for claim" tab, help page US v14 as customer-returns read it); both are stated, neither picked. A seller named in the staff post's terms ("Transaction Item ID", "Inventory Adjustments") may need the ledger equivalent. **Read at run time:**
- Amazon's page *FBA inventory reimbursement policy*, https://sellercentral.amazon.com/gp/help/external/G200213130, and *Customer return claims* (G9N934L7Y4SFWPJ4), as the seller's store shows them (script shells to a plain GET; unread here). Its tools are linked from there.
- The IDR portal in Seller Central (no SP-API read; fc-lost-damaged FC14).
- The ledger `GET_LEDGER_DETAIL_VIEW_DATA` (Amazon Fulfillment) for the event, FNSKU, `Reference ID`, date and FC.
- The inbound shipment reads in Fulfillment Inbound (Amazon Fulfillment) for shipment IDs.
- The removal reports `GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA` / `…_REMOVAL_SHIPMENT_DETAIL_DATA` (Pricing or Amazon Fulfillment) for removal order IDs.
- The returns report `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` (Pricing or Amazon Fulfillment) for order IDs.

Roles as in sp-api-claims-surface.

---

## B. Limits on cases

**(a) Amazon's words.**
- **One claim per shipment (inbound).** "Please note, you may file only one claim per shipment. Additional claims for the same shipment will be declined." [read in official docs, an Amazon Services denial quoted by a seller] (*Missing Items from Inbound - Request to Investigate Denied*, https://sellercentral.amazon.com/seller-forums/discussions/t/481080e4a72836a40155169d3039fd25, Canada store, `createdAt` 2022-07-25). The Amazon Supply Chain page says the same for its programme: "You may file only one claim per shipment. Additional claims for the same shipment will be declined." [read in official docs] (https://supplychain.amazon.com/support/reimbursements, © 2026, no revision date; see the caution in § E). In 2026 the US moderator put it as "Don't submit duplicate claims — One claim per shipment or event" (Indy_Amazon, 2026-08-13) [read in official docs, staff post].
- **One issue per case; no parallel cases.** "One issue = one case (it helps our different teams work faster without confusion)." "If you already have a case open for an issue, please hang tight instead of creating another one." [read in official docs, staff post] (Connor_Amazon, *Contacting Seller Support*, https://sellercentral.amazon.com/seller-forums/discussions/t/460319ae-fb9b-426b-90c0-ff847a7d070a, US store, `createdAt` 2025-01-31.)
- **Volume.** No Amazon page read states a number of items per case or cases per day. The policy names volume only as conduct ("submitting a large number of requests in a short time", § C).
- **Remeasurement requests** have a per-FNSKU and a monthly per-account limit; the conditions, their source (NR_Amazon, 2025-04-30) and practitioners' numbers are fee-overcharges FE4's.
- **Sourcing-cost updates** are limited per FNSKU per period, and Amazon has stated the count differently; the statements and where the current value is read are value-and-reversals VR11's. The policy's repeat rule (a repeat within a stated period of a decision, without new information, may be declined) is VR22's.
- **Reading cases.** The Support API's three operations are reads with their own usage plan; that is a read limit, not a filing limit (see sp-api-claims-surface SU8, SU10; value in "Values that move").

**(b) What practitioners add** (each [opinion]; none cites an Amazon page for its number):
- **Units or FNSKUs per case.**
  - "Amazon once allowed only 5 units per case, but sellers can now add many FNSKUs in one request" (a 2026 vendor guide in search results).
  - "建议不要一个 case 開超過 5 個 FNSKU" (search snippet of a Chinese guide).
  - AMZ123 (2022-01-04): "每个case只查10个SKU，客服的效率会高一些", given as support staff's advice; the author adds that more makes replies slow and risks refusal. Jungle Scout China (2022-04-08): "以10个SKU为单位，向亚马逊开case".
  - SellerSpace (2025-03-20): "appeal for only one FNSKU per Case".
  - Vendors disagree on bundling. One guide says one case per issue, since bundled FNSKUs get one generic answer that is hard to appeal. Another says one case covering 15 lost ASINs from one shipment processes faster than 15 cases.
- **Cases per day.**
  - SellerSpace: "the number of appeals per store-marketplace should not exceed 10 per day".
  - 看点资讯 on Sina Finance (2021-04-16, https://t.cj.sina.com.cn/articles/view/6469010462/18195441e00100yy7s): one deactivated seller had opened "30+个case" in a day for FBA claims. An older seller it quotes advises "每天申请索赔最好不要超过10个", in batches, one after another.
  - RefundBest on Sohu (2024-06-12, credited "来源: 失眠物语", https://www.sohu.com/a/785386694_491696) says many claim cases in one day can get a store marked "高风险". It writes "亚马逊明确规定，卖家不能在短时间内频繁提交索赔申诉", which paraphrases Amazon's conduct paragraph.
- **The remeasurement number:** practitioners' figures are held in fee-overcharges FE4.
- **The SellerSpace wait.** "If no result is received within 30 days after submitting a claim, the application becomes invalid and can be resubmitted" (2025-03-20). This is a tool's rule, not Amazon's.

**(c) Into a skill:**
- Amazon's limits are one claim per shipment or event, one issue per case, and no second case while one is open.
- The remeasurement allowance (see fee-overcharges FE4) and the sourcing-cost update limit (see value-and-reversals VR11) are limits of their own tools, not of cases.
- Amazon publishes no per-case item cap and no per-day case cap. The practitioners' numbers (5, 10, 1 per case; 10 a day) are their own and conflict.

How to split a seller's candidates across cases is the seller's choice; neither shape is Amazon's rule:
- **Bundled cases:** fewer contacts, one answer for many items, harder to appeal per item (practitioners) [opinion].
- **One case per item or event:** more contacts, each answered alone; whether more contacts count toward "a large number of requests in a short time" (§ C) Amazon does not say [inferred].

**Read at run time:** the IDR portal's "Eligible for claim" view (Seller Central only); no SP-API read gives it. The remeasurement allowance is read as fee-overcharges FE4 says.

---

## C. The conduct Amazon penalises

**(a) Amazon's words.**

1. **The policy's conduct paragraph.** "Important: Our policies prohibit any activity that would interfere with our capacity to help other sellers. Examples of such activities include submitting insufficiently researched or premature requests, or submitting a large number of requests in a short time. Sellers who repeatedly engage in these activities may receive delayed support on their cases or be subject to monitoring, investigation, and account action." [read in official docs]
   - US PDF created 2025-02-24.
   - April 2021 UK-English PDF: "high volumes of requests in a short time", otherwise the same.
   - An Amazon Services denial of an inbound investigation, Canada store, pasted 2022-07-25 (thread 481080e4): "As a reminder, our policies prohibit any activity that would interfere with our capacity to help other sellers. Examples of such activities include submitting insufficiently researched or premature requests, submitting a large number of requests in a short time, or otherwise engaging in any other activity that interferes with our capacity to help other sellers." It sends the seller to "Selling Policies & Seller Code of Conduct" [read in official docs, relayed].
   - The Supply Chain Portal policy (MCF account, read 2026-11-13) has its own wording: "Merchants who repeatedly engage in these activities may receive delayed support or may be subject to further account monitoring and action, if necessary." Its *Shipment to Amazon claims* section adds: "Merchants who generate a high number of shipping problems affecting Amazon receiving operations may be subject to additional investigation and monitoring. These actions could result in delays to future reimbursements." [read in official docs]
   - Buy with Prime's reimbursement policy page (403 to a plain GET again on 2026-11-13; text seen in search results only) names "insufficiently researched, premature, or a high volume of claims for reimbursement" [search text only].
2. **Selling Partner Support's restatement.** A support message timed "09:50 PM 08/22/2024", pasted by a seller in a reply posted 2024-08-25 (`createdAt`) to the US thread *Amazon Seller Support* (https://sellercentral.amazon.com/seller-forums/discussions/t/6833e3db-02ca-49ae-8479-ff97ece6bc0a). The seller had been "pursuing a solution on lost merchandise and receiving a partial reimbursement" [read in official docs, relayed]:
   - "to protect sellers and customers, we decline requests that are not consistent with our policies";
   - "If we've informed you that no further action will be taken on an issue, … don't seek to obtain a different outcome by reopening the case or raising it again in other cases";
   - the policy's conduct paragraph verbatim, with "a large number of requests in a short time";
   - "Amazon may close cases or limit support if you don't follow these guidelines".

   It links Amazon's page *Guidelines for contacting Selling Partner Support*, …/help/hub/reference/GK3V2JYCN2P28BFX. That page is a script shell to a plain GET (again 2026-11-13) and is unread.
3. **Not already reimbursed.** A claim is open only "if … we haven't already reimbursed you" (US PDF 2025-02-24). The moderator: "Check Reports > Payments > Reimbursements before filing manually", and "Don't file too early. Amazon's systems need time to reconcile — filing prematurely is the #1 reason claims get denied." (Indy_Amazon, 2026-08-13) [read in official docs].
4. **Account status, widened.**
   - April 2021 UK PDF: "Your selling account is in normal status when you file a claim".
   - US PDF 2025-02-24: "When a lost or damaged item claim is filed, under review, and during any appeals, the seller's account must be in normal status".
   - Staff 2026: "Accounts in blocked, terminated, or fraud status aren't eligible".

   [read in official docs]
5. **Documents.** Amazon may decline a sourcing cost when "Any documentation is forged, tampered with, or illegible", or when "Your account is suspected of fraud, significant policy violations, or non-compliant selling activities" (US PDF 2025-02-24) [read in official docs].
6. **Seller Code of Conduct** (G1801). The page is a script shell to a plain GET (…/help/hub/reference/G1801 and …/gp/help/external/1801, again 2026-11-13), and no permitted primary copy was found: Amazon's BSA PDFs on m.media-amazon.com (AU 2021-07-29, English 2023-12-13, a 2024 edit of 2024-06-12, by last-modified) do not carry it, and the Chinese search found only third-party restatements (AMZ123). Its words here rest on a relay: Emet_Amazon, an `_Amazon` account, replying on 2024-11-23 (`createdAt`) in a US seller's thread *Pending suspension due to: Selling Policies and Seller Code of Conduct (attempting to damage or abuse another seller)* (https://sellercentral.amazon.com/seller-forums/discussions/t/a3c0c769-dab1-4c75-a5c0-43fceb67b581): "This policy requires that sellers act fairly and honestly…". Sellers must "Provide accurate information to Amazon and our customers at all times" and "Act fairly and not misuse Amazon's features or services" [read in official docs, staff relay of an unread page].
7. **Deactivation notices sellers have posted** [opinion: the seller's paste of Amazon's words; no Amazon reply affirms any of them]:
   - "Your Amazon Seller account has been deactivated in accordance with section 3 of Amazon's Business Solutions Agreement. … information available to us indicates that this account has misused Amazon's services in violation of our Seller Code of Conduct (https://sellercentral.amazon.com/help/hub/reference/1801) and involved in FBA credit reimbursement abuse." Thread 807fb6a2-374a-4f8a-bf9f-488eae597a1e, US store by its `marketplaceId` (first read on the EU host), `createdAt` 2024-07-01; Stevie_Amazon replied 2024-07-07. A notice with "has misused Amazon's services" and "FBA credit reimbursement abuse", but no Section 3 citation on the page, was posted 2023-03-27 to the US store, with a reinstatement denial citing "violations of our FBA Lost and Damaged Inventory Reimbursement policy" (https://sellercentral.amazon.com/seller-forums/discussions/t/e885be1d-8d49-45fa-b400-14af9aeb1b86).
   - "this account has repeatedly submitted improper claims for FBA reimbursement" (US store, `createdAt` 2021-05-04; the seller used "refunds manager", which the seller called "a service that they allow"; one reply: "Many many people have been suspended for using these services"; https://sellercentral.amazon.com/seller-forums/discussions/t/22eecf9e75a3ae1d6bae28c9e93d6b75).
   - Chinese, 2021: "该卖家在短时间内提交了不适当或者大量的重复请求，滥用了亚马逊的销售合作伙伴支持服务" (看点资讯 on Sina, 2021-04-16).
   - "apparently excessive contacts": a UK-store seller deactivated the day after joining (thread 83cf5f35bb680661131aeb7e01b33cd5, `createdAt` 2023-02-17). The seller later writes that Amazon said the account "violated the sellers code of conduct by misuses Amazon seller support service". The only `_Amazon` reply (Maja_Amazon, 2023-02-17) moves the thread to Account Health; a reply signed "Art from Amazon" names the Seller Code of Conduct but is posted from a seller-type account. The thread is not about claims.

**(b) What practitioners add.**
- **Responsibility.**
  - Sellers report that Amazon holds the seller responsible for claims a service files. "Amazon holds YOU responsible for what their 'partners' are doing" (seller reply in thread 807fb6a2, US store, 2024) [opinion].
  - In that thread the deactivated seller used Seller Investigators ("an Amazon partnered service", in the seller's words) for lost-inventory claims, and wrote "It appears that their service was submitting cases while I was deactivated". The thread does not say those cases caused the deactivation or that Amazon acted on them. Amazon's moderator (Stevie_Amazon) called the stated reason "almost conflicting" and asked for the notice. No outcome is posted [opinion; staff reply read in official docs].
  - Seller Labs: "Filing duplicate claims for already-reimbursed events is a violation of Amazon's seller policies and can result in account warnings or a reimbursement program restriction" (knowledge base, search result) [opinion]. No Amazon page read names a "reimbursement program restriction".
- **A found unit that is not the seller's.** 敏哥跨境记 on 跨境知道 (2024-09-24, https://www.ikjzd.com/articles/1810625995691812998) reports the case. A seller was paid for an inbound shortfall. About a month later Amazon "found" the units, "这些产品都不是卖家的产品", "平台就判定卖家违反了赔偿政策", and the account was closed [opinion; no notice text given].
- **Volume.** 看点资讯 (2021) puts the error rate of FBA at "大概在2.5~3%" and says a normal claim is legitimate; the trigger is frequency [opinion]. RefundBest (2024) says lawful claims carry no penalty, while forged evidence risks "永久封禁" [opinion]. 卖家之家 (跨境女子图鉴, 2022-04-08, https://mjzj.com/article/bhivfdlge0w6): "每个商品只能提出一项索赔" (the article's wider sentence on a second claim for the same shipment being refused is the researcher's reading, not re-read on 2026-11-13); "如果卖家多次向亚马逊索赔，可能会遭到封号处理" [opinion].
- **Law-firm and consultancy reading.**
  - RiverBend Consulting (Alex Landry, updated 2026-02-03, https://riverbendconsulting.com/blog/amazon-reimbursement/): "If it deems requests to be excessive, inaccurate or submitted in bad faith, your account is at risk for suspension." [opinion]
  - AMZ Sellers Attorney (pages 403 to a plain fetch; seen in search results) says falsified details or documents can bring immediate deactivation, and that continuous claims through outside companies can trigger suspension [opinion].
- **Older vendor practice.** The 2021 article advises turning off an ERP's "FBA发货数量差异" auto-claim option, waiting for "已完成" before an inbound investigation, and not claiming very small losses [opinion]. That last point is a seller's choice and is not stated here as a rule.

**(c) Into a skill:** these are Amazon's own rules and stand as such:
- a claim needs the event to have happened and not already been paid;
- a premature request is named conduct; that "premature" means before each kind's window opens is the reading of this file and of the staff post's "Don't file too early" [inferred];
- a second claim for the same shipment or event is declined;
- an issue answered "no further action" is not reopened or re-raised in another case;
- forged, tampered or illegible documents are a stated reason to decline a sourcing-cost submission (US PDF), and staff ask that a submitted value exactly match its document (Arish_Amazon);
- the account must be in normal status while a claim is filed, reviewed and appealed;
- repeated breaches can bring delayed support, monitoring, investigation and account action.

Sellers' posted notices name Section 3, the Seller Code of Conduct and "FBA credit reimbursement abuse". **Read at run time:**
- `GET_FBA_REIMBURSEMENTS_DATA` (Pricing or Amazon Fulfillment): what is already paid, with `case-id` and `original-reimbursement-id` (finance pack P-ref-19, P-ref-20).
- The ledger (Amazon Fulfillment): found (`F`) events after a reimbursement.
- Account status: `GET_V2_SELLER_PERFORMANCE_REPORT` `accountStatuses`, a status per marketplace (the schema's example shows `NORMAL`, `AT_RISK`, `SUSPENDED`; `accountHealthReport-2020-11-18.json`) (role per sp-api-claims-surface). That the policy's "normal status" is the report's `NORMAL` is not stated by Amazon [inferred].
- Amazon's pages *FBA inventory reimbursement policy* (G200213130) and *Guidelines for contacting Selling Partner Support* (GK3V2JYCN2P28BFX).

---

## D. Third-party filers, apps and agents

**(a) Amazon's words.**
- **No page read bars a third-party filer, and none endorses one.** The policy texts speak to "you" and to "Sellers who repeatedly engage" (§ C) [read in official docs; absence is inferred from the pages read].
- **SP-API Acceptable Use Policy** (undated page, https://sellercentral.amazon.com/mws/static/policy?documentType=AUP&locale=en_US) [read in official docs]:
  - 2.11: "Comply with all applicable Amazon policies, Program Policies, and Service Terms when acting on behalf of an Authorized User, and ensure all submissions and communications are accurate, policy-compliant, and do not result in frivolous or non-compliant contacts or degradation of Amazon support systems."
  - 1.1: "Use the Amazon Services API only to perform acceptable Amazon activities, and only for Authorized Users who have authorized you to perform these activities on their behalf."
  - 3.3: "Do not request or share Amazon Portal usernames or passwords from Authorized Users."
  - 3.7: "If Amazon Portal access is required to provide features or services that benefit Authorized Users, ask the Authorized User to grant access through secondary user permissions."
  - 3.6: "Do not ask Authorized Users to share information retrieved from Amazon Portals manually or programmatically to circumvent Amazon policies."

  When 2.11 entered the AUP was not established: the Wayback snapshot returned 502.
- **Business Solutions Agreement update and Agent Policy, effective 2026-03-04.** News_Amazon, *Business Solutions Agreement updates effective March 4, 2026*: US store thread https://sellercentral.amazon.com/seller-forums/discussions/t/84e3f6b1-42f7-4cf3-a189-a5cc8d78d838, `createdAt` 2026-02-17; the same post in the Canada store, thread 8a2dfc1c-2091-40d1-816b-457a68265b01 (first read on the .co.uk host; its `marketplaceId` is Canada's), `createdAt` 2026-02-19; both read 2026-11-13 [read in official docs]. Its words: "Agent restriction and new Agent Policy: We'll add requirements for the use of automated software or AI agents to access Amazon Services, and we may restrict their access in certain instances under the BSA and new Agent Policy. All AI agents must do the following: Clearly identify themselves as automated systems; Comply with the new Agent Policy at all times; Cease access if Amazon requests".
  - Automated software or AI agents accessing Amazon Services must identify themselves as automated systems, follow the new Agent Policy, and stop access when Amazon asks; Amazon may restrict their access.
  - It adds a definition of "Agent" (named, not quoted, in the announcement).
  - "Your continued use of Selling Services after the effective date constitutes acceptance of these changes."
  - It links the BSA (G1791), the changes page (G47071) and the Agent Policy (GS83KH2MA7HM69PH).

  The Agent Policy page (GS83KH2MA7HM69PH; the US post links …/help/hub/reference/GS83KH2MA7HM69PH) returned only a script shell to a plain GET again on 2026-11-13, by both the help-hub and the `gp/help/external` paths; its text is unread here. No permitted primary copy was found: the BSA PDFs Amazon serves on m.media-amazon.com (AU, last-modified 2021-07-29; English, 2023-12-13; a 2024 edit, 2024-06-12) predate the change and carry no agent clause, and developer-docs serves no Agent Policy page. What the policy itself says therefore rests on relays (§ D(b)). PPC Land (2026-02-22) reports a seller saying the announcement's Agent Policy link pointed to the wrong page [opinion].
- **Amazon's own plugin.** Amazon's `support-case-helper` skill calls no SP-API tool by default and leaves case creation to a connector tool only with the seller's explicit confirmation (see sp-api-claims-surface SU14). For conduct it adds one thing: it fills a "Reported From" field with "the name of the agent/assistant currently running this skill" [command-verified: read in the plugin's SKILL.md, the survey's copy].

**(b) What practitioners add.**
- **The Agent Policy's rules as relayed.** No Amazon page carrying them was readable (§ D(a)); these are a third party's relay. Ecomsellertool, 2026-09-25, updated 2026-11-04 (https://ecomsellertool.com/blog/amazon-agent-policy-ai-tools) [opinion: relayed text, unverified against Amazon's page]:
  - "Agent/[agent name]" in the user agent string of every HTTP(S) request;
  - agents must not hide that they are agents, including by "mimicking the speed or pattern of human keystrokes";
  - "Respond truthfully" when asked whether a person or a computer is acting;
  - do not get around measures that "block, limit, modify, or control" use;
  - the definition: "any software or service that takes autonomous or semi-autonomous action on behalf of, or at the instruction of," (truncated);
  - BSA Section 19 requires agents to follow the Agent Policy "at all times" (the words "Clearly identify themselves as automated systems" are the announcement's, above).

  Other writers say the policy names no technical mechanism (search summaries). DAM Law Firm (Mark Nathaniel Toledo, 2026-09-03): "After March 4, however, the seller is responsible for ensuring every Agent on their account complies at all times"; it lists "VA-operated scripts run using the seller's credentials" and "reimbursement tracking services" among tools the Agent Policy covers [opinion].
- **How services file.**
  - SPS Commerce: "Our team then manages claim preparation, submission, and follow-up directly within Amazon Seller Central".
  - Jarvio: its agent "prepares complete claim documentation … but you submit the case through Seller Central".
  - Seller 365 / Threecolts (2026-08-19) asks for Seller Central user permissions including "Manage FBA Inventory Shipments" and "Fulfillment by Amazon" and "Manage Your Cases" at View & Edit.
  - Helium 10's managed service says it files as "an official member of the exclusive Amazon Emerald Program" (finance pack P-ref-31). No Amazon page read describes that programme.

  [all opinion]

**(c) Into a skill:**
- An app acting through the SP-API is bound by AUP 2.11: submissions accurate and policy-compliant, and no "frivolous or non-compliant contacts or degradation of Amazon support systems".
- An SP-API developer that needs Amazon Portal (Seller Central) access asks the seller to grant it through secondary user permissions and does not request or share portal usernames or passwords (AUP 3.3, 3.7). The AUP binds SP-API developers; a service that never uses the SP-API is not named by it [inferred].
- From 2026-03-04 any automated agent on the account must identify itself as automated, comply with the Agent Policy and stop when Amazon asks (BSA announcement).
- Amazon's own support skill leaves submission to the seller unless a connector tool exists and the seller confirms (see sp-api-claims-surface SU14).

Who files is the seller's choice, and each option changes something:
- **The seller files by hand:** no access granted; the seller's own time.
- **A service as a secondary user:** permissions the seller grants and can revoke, a fee on recoveries (recovery-economics), and in practice the seller answering for what the service files.
- **A tool or agent that prepares the claim and leaves submission to the seller:** no Seller Central access; the seller still submits.

**Read at run time:** Amazon's pages *Agent Policy* (…/help/hub/reference/GS83KH2MA7HM69PH) and *Amazon Services Business Solutions Agreement* (G1791), as the seller's store shows them (script shells to a plain GET; read in the seller's own Seller Central), and the AUP page above.

---

## E. Evidence Amazon accepts

**(a) Amazon's words.**
- **Shipment to Amazon.** "proof of inventory ownership (itemized invoice, receipt from another seller, or packing slip)"; "proof of delivery (amazon stamped delivery document for LTL & FTL shipments or active tracking ID for SPD shipments)" (Amazon Services denial text signed "Sincerely, Amazon Services", Canada store, pasted 2022-07-25, thread 481080e4) [read in official docs, relayed]. The moderator (2026-08-13): "Itemized invoices or receipts", "Tracking IDs and proof of delivery for inbound shipments", "Amazon-stamped delivery documents for LTL/FTL shipments", screenshots, photos [read in official docs, staff post]. Invoice fields (date, quantity, issuer and purchaser name and address), or a signed packing slip for a manufacturer, are held by the stock pack (inbound.md F2, Christine_Amazon 2025-11-14).
- **The Amazon Supply Chain page's version.**
  - The ownership document "must show date of purchase, product names matching the items, and quantity".
  - LTL/FTL proof of delivery shows "the number of boxes in the shipment and the total weight", stamped by Amazon.
  - Small parcel needs an active tracking ID per package, added before reimbursement if it was not entered.
  - Removals: removal order ID, shipment and tracking ID or proof of delivery, ASINs/FNSKUs and quantities, "LPN number", images of units, packaging and box, proof of cost.

  [read in official docs] **Caution:** this page is titled *Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS)* and requires an active Multichannel Fulfillment account. It is also the page Amazon's AWD service terms (dated 2026-01-14) link as the "MCF inventory reimbursement policy", so both names fit it: the ASCS programme's SCP policy (its title) and the MCF inventory reimbursement policy (the AWD terms' link text). Its valuation disputes and MCF order claims go through "the Contact Us page in Supply Chain Portal". Its per-unit cap and fallback valuation are its own and differ from the FBA policy's (values in "Values that move"; the FBA cap is value-and-reversals VR29's). Its evidence lists match the FBA staff post, but its windows and caps are not FBA's.
- **Removal claims (FBA).** "Provide the Shipment ID, ASINs/FNSKUs, affected quantities, and images of affected units if applicable" (Indy_Amazon 2026-08-13) [read in official docs, staff post].
- **Sourcing cost (proof of value).**
  - "Visit the Manage Your Sourcing cost help page for accepted proof-of-value documentation details" (US PDF 2025-02-24); that page is unread. A forum post gives its id as GN655EHATZUVWBC3 [opinion: relayed id].
  - Amazon moderators [read in official docs, staff posts]:
    - Nano_Amazon (US store, 2025-06-12 by `createdAt`, *Sourcing Cost - Proof of value document does not meet requirements Denied*, https://sellercentral.amazon.com/seller-forums/discussions/t/b48840c1-3396-43ba-9731-b88f338e6aa8): "Ensure your invoice is recent (within the last 365 days)"; "clearly shows your company name, supplier details, product information, and unit costs"; "Highlight the relevant information"; "If using a pro forma invoice, include proof of payment"; "For products manufactured in-house, provide a detailed cost breakdown".
    - Arish_Amazon (US store, reply of 2026-02-24 by `createdAt`, thread cd2909d2): "Accepted documents include manufacturer invoices, wholesaler invoices, purchase invoices, and commercial invoices"; "Please ensure the value in your submission exactly matches what is shown in your documentation".

**(b) What practitioners add** [all opinion]:
- **跨境风暴 on AMZ123** (2024-08-01, https://www.amz123.com/t/vcGmSDYD), for an inbound loss of 5,000+ units:
  - the invoice date "必须早于发货日期";
  - "增值税发票", supplier-signed packing lists or seller-signed receipts;
  - LTL/FTL: an Amazon-stamped pickup slip with box count and total weight;
  - everything in English, product names matching the listing, quantities matching the shipment, matching consignee and address.

  Its result was one case, "合计赔偿了10个产品，费用是92美金". The article still cites an 18-month window (stale).
- **卖家之家** (2022): "正规的机打的发票"; the invoice quantity equal to the shipped quantity.
- **Search-result vendor guides:** supplier name, address, phone and website on invoices, and the buyer matching the Seller Central entity (several; unverified). One forum seller was denied with the official supplier's invoice (thread 267c908a, search result).
- **A Chinese tax invoice ("fapiao")** is named as accepted proof of value by a third-party guide (search result).

**(c) Into a skill:**
- Each claim kind has its own evidence. Inbound: ownership (itemized invoice, receipt from another seller, packing slip or signed packing slip) plus proof of delivery (Amazon-stamped for LTL/FTL; an active tracking ID for small parcel, "SPD" in the denial text). Removals: IDs, quantities and images. Sourcing cost: a proof-of-value document whose value matches the submission; its fields, accepted types and the invoice age Amazon has stated two ways are value-and-reversals VR12–VR14's.
- Forged, tampered or illegible documents are a stated reason to decline a sourcing-cost submission.

**Read at run time:**
- The inbound shipment's ID, quantities and carrier type from Fulfillment Inbound (Amazon Fulfillment).
- Removal shipments' carrier and tracking from `GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA`.
- The seller's own invoices, which no Amazon read holds.
- Amazon's *Manage Your Sourcing Cost* help page (GN655EHATZUVWBC3) as the seller's store shows it (see value-and-reversals VR13, VR14).

---

## F. How answers come back, and how long they take

**(a) Amazon's words.**
- **Case states.** The moderator names the states sellers see as "Pending Amazon Action" and "Pending Merchant Action" (Connor_Amazon, 2025-01-31) [read in official docs]. The Support API model's states, channels, dates, role and limits are sp-api-claims-surface SU8–SU11's.
- **Staying open.** "Need more time to get back to us? Just let us know by responding to the case, and we'll keep it open." (Connor_Amazon) [read in official docs].
- **Inbound research** has a stated research time and a stated time for the seller to answer a request for more information (stock pack inbound.md F1, F2; values in "Values that move") [read in official docs, via the stock pack].
- **Remeasurement** has a stated completion time (NR_Amazon, 2025-04-30; see fee-overcharges FE4; value in "Values that move") [read in official docs].
- **Supply Chain Portal MCF order claims** have their own stated claim timing (SCP page; values in "Values that move") [read in official docs].
- **The outcome lands in the Reimbursements report.** Its `case-id` is filled for manual claims (finance pack P-ref-20).
- **Help channels.** "Professional sellers can e-mail, request a call or chat with support." Individual-plan sellers e-mail only (Connor_Amazon) [read in official docs].

**(b) What practitioners add** [opinion]:
- **Auto-"Answered".** A seller's case "remained pending for 14 full days and was automatically marked as 'Answered' on August 11, 2026" with no reply (forum, search result). Sellers read "Answered" or "Closed" as transferred to another team (EU forum, search result).
- **Automated denials.** "We're denying your reimbursement claim for the following units because we didn't receive all expected quantities" (a seller on thread 0e07abc1, 2026).
- **Timing claims by vendors.** GETIDA: "Amazon aims to process reimbursement claims within 90 days" (blog, undated). SellerSpace's 30-day resubmit rule (§ B).
- **Delays and receiving backlogs.** A US seller reports "they can't do any investigation not until 90 days after the removal order was made" for missing removal units (thread 8e91e62f, 2024). My Amazon Guy reports a wait instruction during receiving backlogs (stock pack I26).

**(c) Into a skill:**
- A case is in one of four states, and the seller's reply moves `PENDING_MERCHANT_ACTION` back to Amazon.
- An answer arrives in the Case Log, by email and, when paid, as a row of the Reimbursements report with the `case-id`.
- Amazon states a review or reply time only for inbound research, for remeasurement, and for the seller's reply to an inbound information request; the values are read on those pages ("Values that move"). No page read states one for other FBA claims.

**Read at run time:**
- `GET_FBA_REIMBURSEMENTS_DATA` rows whose `case-id` matches the seller's Case ID.
- The case itself only through the Support API, under Selling Partner Support (Restricted), outside GL's roles. Otherwise the seller reads the Case Log.

---

## G. Reopening, re-evaluation and escalation

**(a) Amazon's words.**
- **Reopen a closed case.** "If you have questions about a closed case simply reopen it instead of creating a new one." (Connor_Amazon, 2025-01-31) [read in official docs].
- **Do not re-raise a final answer.** "If we've informed you that no further action will be taken on an issue, … don't seek to obtain a different outcome by reopening the case or raising it again in other cases" (support message of 2024-08-22, pasted 2024-08-25, thread 6833e3db) [read in official docs, relayed].
- **Re-evaluation and valuation disputes** each have their own route and a window whose start and length Amazon has stated more than one way; all of it is value-and-reversals VR20–VR24's (see also customer-returns RT42 for the US help page's wording as customer-returns read it).
- **Deactivation.** Reinstatement goes through Account Health: "you will need to reinstate your account by working with the Account Health team" (TaylorR_Amazon, US store, 2024-11-26, thread 8e91e62f) [read in official docs, staff post].

**(b) What practitioners add** [opinion]:
- **Reopen window.** A 2024 seller blog says cases reopen only within five days of closure (search result).
- **New case citing the old one.** One vendor describes, where reopening is not offered, a new case opened after the old one closes that cites the old ID (salesduo, search result). Reopening the closed case (Connor_Amazon) and a new case citing it are two shapes practitioners describe; Amazon's word above is for reopening.
- **Higher escalation.** GETIDA: "If repeats fail, reach out to Executive Customer Relations", and "you can appeal a denied reimbursement request within 90 days of the decision".
- **Forum staff.** Sellers post case IDs on the Seller Forums for Amazon staff to pick up; in thread 8e91e62f (2024) a "Live Channel Specialist" wrote "I have reopened that check and we are waiting for a response with more detailed images".

**(c) Into a skill:**
- Amazon distinguishes a question on a closed case (reopen it) from a decision of "no further action" (do not reopen or re-raise).
- Re-evaluation and valuation disputes have their own routes and dated windows (see value-and-reversals VR20, VR21).
- An account in deactivation goes to Account Health, and claims are ineligible while it is not in normal status (§ C4).

**Read at run time:** the case's state and last update (Support API, SPS(R), or the Case Log), and the reimbursement's `approval-date` (Reimbursements report) to date the re-evaluation and valuation windows.

---

## H. What filing costs a seller

**(a) Amazon's words.** No Amazon page read charges a fee to file a claim [inferred from the pages read]. The costs Amazon's pages name are not money:
- a declined claim when information is missing (§ A);
- delayed support, monitoring, investigation and account action for repeated insufficiently researched, premature or high-volume requests (§ C);
- a reversal of a reimbursement made in error or for a unit later found (finance pack P-ref-18, P-ref-40).

**(b) What practitioners add:** services charge 15–30% of recoveries (finance pack P-ref-31; recovery-economics). Refunzo: "Amazon does not charge to file a claim in Seller Central, so Amazon FBA reimbursement fees come only from third-party providers" [opinion]. Vendors warn of a fee charged on money Amazon would have paid by itself (GETIDA's day-64 warning, finance pack P-ref-31) [opinion].

**(c) Into a skill:** filing has no Amazon fee. What it risks is conduct (§ C) and reversal. Which candidates to file, and when, is the seller's choice, and each choice changes something:
- **Filing as soon as a window opens:** keeps the most time left in the window; whether Amazon then counts it as premature is not stated beyond the window itself [inferred].
- **Filing late in a window:** gives Amazon's automatic reimbursement more time, which may pay first (finance pack P-ref-13; automation dates are fc-lost-damaged's); where a re-evaluation window runs from the initial claim (value-and-reversals VR20), its length is unchanged by when the claim is filed [inferred].
- **Not filing small candidates:** forgoes the money and avoids the contacts.
- **Using a service:** costs a share and hands the filing to someone the seller answers for.

---

## I. Chinese sellers' guidance in one place

Chinese sources on 索赔 conduct share three warnings. All are [opinion], dated 2020–2025:
- one claim per goods or shipment (卖家之家 2022);
- not many cases in one day, with "≤10" per day a common figure (看点资讯 2021; SellerSpace 2025; RefundBest 2024);
- deactivation for "多次恶意提交不合理的物流理赔" or "滥用了亚马逊的销售合作伙伴支持服务" (看点资讯 2021), and for a found unit that was not the seller's (跨境知道 2024).

Per-case batching guidance ranges from 1 FNSKU (SellerSpace) to 10 SKUs (AMZ123, Jungle Scout China 2022). Several still cite superseded windows: 18 months (AMZ123 2024-08) and "180天→60天" (招单猫 on 卖家之家, 2024-08-07, https://m.mjzj.com/article/du2ckgmjnthc). The ERPs (领星, 赛狐, 积加, 优麦云) track the Case ID the seller enters and none files (finance pack P-ref-39; SellerSpace page read here).

---

## Positions

- **FL1.** No SP-API operation opens an FBA case or claim, attaches evidence, replies to a case or reopens one; each is done in Seller Central by the seller or a user the seller authorises (see sp-api-claims-surface SU8, SU10, SU12, SU13 for the Support API's reads and the one carrier-claim operation). [command-verified there]
- **FL2.** Amazon's policy makes following the process for the claim kind, and giving all requested information, a condition: "We may decline your claim if you do not." The Supply Chain Portal policy states the same for its programme. Sources: FBA inventory reimbursement policy PDF (US, created 2025-02-24); April 2021 UK-path PDF; SCP page (read 2026-11-13) [read in official docs].
- **FL3.** A claim is open only for an item Amazon has not already reimbursed. The moderator's instruction is to check the Reimbursements report before filing manually. Sources: US PDF 2025-02-24; Indy_Amazon, US, 2026-08-13 [read in official docs].
- **FL4.** Entry points differ by kind. As Amazon's US moderator gave them on 2026-08-13:
  - warehouse damaged: the "Check warehouse damaged reimbursement status" tool on the policy page, by Transaction Item ID;
  - warehouse lost: a Get Support case ("FBA Issue > Inventory Lost in Warehouse"), by FNSKU or Transaction Item ID;
  - missing from inbound: the shipment's Reconcile tab;
  - damaged inbound: a Get Support case (an Amazon denial in the Canada store, 2022-07-25: "open a claim through the Contact Us page");
  - customer returns: the "Check FBA order reimbursement status" tool on the policy page, by order ID;
  - removals: the "Resolve a removal order issue" tool, by removal order ID.

  For customer returns Amazon has a second statement: the help page *Customer return claims* (G9N934L7Y4SFWPJ4, US v14, CA v5; GB G84Z6B8BTKVNV53S) starts the claim tool from the order id on the IDR portal's "Eligible for claim" tab, and lets a "Resolved" decision be contested there (customer-returns RT41, read 2026-11-13 through the help hub's content call, a route the office closed on 2026-11-10). Both are stated with their dates; neither is picked, and neither page says whether they are one flow. Sources: Indy_Amazon, thread 0e07abc1, US, 2026-08-13 [read in official docs, staff post]; thread 481080e4, Canada, 2022-07-25 [read in official docs, relayed]; customer-returns RT41 [read in official docs, through a route now closed].
- **FL5.** The IDR portal, announced 2025-01-21 for the US store, covers warehouse lost, warehouse damage and customer returns and "doesn't include defects under missing from inbound, removals or warehouse disposals". It is reached from the FBA dashboard's Inventory menu or from the Reimbursements report. Its help page (G66ZLS453YSE2Y4R) is unread. Source: News_Amazon, thread b175b700 (`createdAt` 2025-01-21; `marketplaceId` US) [read in official docs]. (Finance pack E3; what the portal shows is fc-lost-damaged FC13–FC15.)
- **FL6.** Pitfall: Amazon's 2026 staff instructions name the "Inventory Adjustments" report and a "Transaction Item ID", and link a Seller Central report page `reportcentral/INVENTORY_ADJUSTMENT/0`. The report's API type (`GET_FBA_FULFILLMENT_INVENTORY_ADJUSTMENTS_DATA`) was removed on 2023-01-31 in favour of the Inventory Ledger, and Amazon's FBA report-type page no longer lists it; whether the Seller Central page still serves the report is unread (sign-in). Amazon does not state that the ledger's `Reference ID` is the Transaction Item ID. Sources: Indy_Amazon 2026-08-13 [read in official docs]; Amazon's deprecation notice (search text only; the developer-docs changelog page returned no notice text on a plain GET) and stock pack P-stock-states-28 [read in official docs, via search text and the stock pack]; Amazon's FBA report-type page (`Reference ID` column of `GET_LEDGER_DETAIL_VIEW_DATA`, read 2026-11-13) [read in official docs]; a Chinese ERP guide [opinion].
- **FL7.** Amazon declines a second claim for the same inbound shipment: "you may file only one claim per shipment. Additional claims for the same shipment will be declined." In 2026 the US moderator put it as one claim per shipment or event. Sources: Amazon Services denial text relayed (Canada store, 2022-07-25, thread 481080e4); SCP page (its programme); Indy_Amazon, US, 2026-08-13 [read in official docs]. (inbound-shortfalls IN17 holds the same rule for its area.)
- **FL8.** Amazon's support rule is one issue per case, and no new case while one is open for the same issue. Source: Connor_Amazon, US, 2025-01-31 (thread 460319ae) [read in official docs].
- **FL9.** No Amazon page read states a maximum of items per case or of cases per day. Volume enters only as conduct (FL11). Sources: the pages in § B [inferred from the pages read].
- **FL10.** Practitioners' per-case and per-day figures conflict and cite no Amazon page:
  - 5 FNSKUs per case (older guides);
  - 10 SKUs per case (AMZ123 2022, Jungle Scout China 2022);
  - 1 FNSKU per case and at most 10 per store-marketplace per day (SellerSpace 2025);
  - a deactivation after "30+个case" in a day (看点资讯 2021).

  [opinion]
- **FL11.** Amazon prohibits activity that interferes with its capacity to help other sellers. Its examples are "submitting insufficiently researched or premature requests" and "submitting a large number of requests in a short time" ("high volumes" in the April 2021 policy PDF). Sellers who repeat them "may receive delayed support on their cases or be subject to monitoring, investigation, and account action". The paragraph stands in the April 2021 UK-path policy PDF and the 2025-02-24 US PDF, and Amazon's own messages quote it: a denial in the Canada store (2022-07-25) and a Selling Partner Support message (US, 2024-08-22). The Supply Chain Portal policy carries its own version for MCF accounts ("delayed support or … further account monitoring and action"). Sources: those PDFs; threads 481080e4 and 6833e3db [read in official docs, relayed]; SCP page [read in official docs]; Buy with Prime reimbursement policy [search text only; 403 to a plain GET].
- **FL12.** Selling Partner Support's restatement: "we decline requests that are not consistent with our policies". After "no further action", a seller is not to seek a different outcome "by reopening the case or raising it again in other cases", and "Amazon may close cases or limit support if you don't follow these guidelines." The message was sent to a seller pursuing a partial reimbursement for lost merchandise and links *Guidelines for contacting Selling Partner Support* (GK3V2JYCN2P28BFX, unread). Source: support message timed 08/22/2024, pasted in a reply of 2024-08-25, thread 6833e3db, US [read in official docs, relayed].
- **FL13.** Dated change: the account-status condition widened. April 2021 (UK path) required normal status "when you file a claim". The 2025-02-24 US text requires it "When a lost or damaged item claim is filed, under review, and during any appeals". The US moderator in 2026 excludes "blocked, terminated, or fraud status" accounts. The SCP policy requires an MCF account "in Active state and not under review or suspension". Sources: the two PDFs; Indy_Amazon 2026-08-13; SCP page [read in official docs].
- **FL14.** Amazon may decline a submitted sourcing cost for documents "forged, tampered with, or illegible", or when the account is suspected of fraud or significant policy violations. Source: US PDF 2025-02-24 [read in official docs]. (The policy's repeat rule on the same item is value-and-reversals VR22's.)
- **FL15.** The Seller Code of Conduct requires sellers to "Provide accurate information to Amazon … at all times" and to "Act fairly and not misuse Amazon's features or services". These words rest on a relay: Amazon's page (G1801) is a script shell to a plain GET and no permitted primary copy was found (m.media-amazon.com BSA PDFs, gs.amazon.cn search); they are an Amazon staff member's quotation of it. Source: Emet_Amazon, US, 2024-11-23 (thread a3c0c769) [read in official docs, staff relay of an unread page].
- **FL16.** Deactivation notices sellers have posted for claims name Section 3 of the BSA (807fb6a2 only), the Seller Code of Conduct, "FBA credit reimbursement abuse" (807fb6a2, e885be1d), "repeatedly submitted improper claims for FBA reimbursement" and (Chinese, 2021) "短时间内提交了不适当或者大量的重复请求，滥用了亚马逊的销售合作伙伴支持服务". Sources: threads 807fb6a2 (US, 2024-07-01), e885be1d (US, 2023-03-27), 22eecf9e (US, 2021-05-04); 看点资讯 2021-04-16 [opinion: sellers' pastes of Amazon's words].
- **FL17.** Sellers deactivated for claims report having used a third-party claims service (807fb6a2, 2024; 22eecf9e, 2021), and a seller reply says "Amazon holds YOU responsible" for such partners; one deactivated seller found the service still filing cases while the account was deactivated, with no outcome posted. DAM Law Firm writes that from 2026-03-04 the seller answers for every Agent on the account. No Amazon page read states that the seller answers for a service's claims. Sources: threads 807fb6a2, 22eecf9e; DAM Law Firm 2026-09-03 [opinion].
- **FL18.** Practitioners report a deactivation after an inbound shortfall was paid and the "found" units proved not to be the seller's. Source: 敏哥跨境记, 跨境知道, 2024-09-24 [opinion].
- **FL19.** No Amazon page read bars or endorses third-party reimbursement services. Sources: § D pages [inferred from the pages read].
- **FL20.** SP-API AUP 2.11 binds an app acting for a seller to "ensure all submissions and communications are accurate, policy-compliant, and do not result in frivolous or non-compliant contacts or degradation of Amazon support systems". AUP 1.1 limits it to activities the seller has authorised. Source: Acceptable Use Policy (undated page) [read in official docs].
- **FL21.** An SP-API developer that needs Amazon Portal access asks the seller to grant it through secondary user permissions, and must not request or share Amazon Portal usernames or passwords. Source: AUP 3.3, 3.7 [read in official docs]. That a third party outside the SP-API is bound the same way is not stated there [inferred].
- **FL22.** Dated change: from 2026-03-04 the BSA requires any automated software or AI agent accessing Amazon Services to identify itself as automated, comply with the Agent Policy and cease access when Amazon asks; Amazon may restrict its access. Continued use after that date is acceptance. Source: News_Amazon, US thread 84e3f6b1 (2026-02-17) and Canada thread 8a2dfc1c (2026-02-19) [read in official docs]. The Agent Policy's own text (GS83KH2MA7HM69PH) is unread: a script shell to a plain GET, with no permitted primary copy found. Every rule beyond the announcement's three duties rests on relays: the "Agent/[agent name]" user-agent string, no mimicking of human keystrokes, and truthful answers come from ecomsellertool (2026-09-25, updated 2026-11-04) [opinion: relayed, unverified against Amazon's page].
- **FL23.** (Narrowed: the skill's SP-API and case-creation behaviour is homed in sp-api-claims-surface; see sp-api-claims-surface SU14.) Kept here for conduct: the skill fills a "Reported From" field with the running agent's name. Source: `support-case-helper` SKILL.md v1.0.0 [command-verified].
- **FL24.** Shipment-to-Amazon evidence is proof of ownership (itemized invoice, receipt from another seller, or packing slip; a signed packing slip for a manufacturer) and proof of delivery. For LTL/FTL that is an Amazon-stamped delivery document; for small parcel, an active tracking ID ("SPD shipments" in the denial text; per package on the SCP page). Sources: Amazon Services denial text (Canada, 2022-07-25); Indy_Amazon, US, 2026-08-13; stock pack inbound.md F2 for the invoice fields [read in official docs].
- **FL25.** Removal-claim evidence is the removal order ID, shipment ID, ASINs/FNSKUs, affected quantities and images of affected units. The SCP page adds tracking or proof of delivery, the LPN and proof of cost. Sources: Indy_Amazon 2026-08-13; supplychain.amazon.com *Reimbursements* [read in official docs].
- **FL26.** (Narrowed: the proof-of-value fields, accepted documents, the exact-match rule and the invoice age Amazon has stated two ways are value-and-reversals VR12–VR14's; Nano_Amazon's post is dated 2025-06-12 and Arish_Amazon's 2026-02-24.) Kept here: a sourcing-cost document is submitted in Seller Central's Manage Your Sourcing Cost, not in a case. Source: US PDF 2025-02-24 ("Visit the Manage Your Sourcing cost help page") [read in official docs].
- **FL27.** Pitfall of sources: the page at supplychain.amazon.com/support/reimbursements has two names. Its own title is *Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS)*, and it requires an active MCF account and excludes MCF used to fulfil Amazon.com orders. Amazon's AWD service terms (dated 2026-01-14) link their words "MCF inventory reimbursement policy" to that same address. So inbound-shortfalls' reading (the MCF policy the AWD terms name, IN26) and this file's (the ASCS programme's, for an active MCF account) describe one page. Its claims and disputes are filed through the Supply Chain Portal's Contact Us. Its windows, per-unit cap and fallback valuation are its own, not FBA's, though its evidence lists agree with FBA's; each is read on its own page (values in "Values that move"). Sources: SCP page; AWD service terms; US PDF 2025-02-24 [read in official docs].
- **FL28.** Sellers see a case as "Pending Amazon Action" or "Pending Merchant Action", and a reply from the seller hands it back to Amazon. Source: Connor_Amazon, US, 2025-01-31 [read in official docs]. (The Support API's four states are sp-api-claims-surface SU10's.)
- **FL29.** A paid manual claim appears in `GET_FBA_REIMBURSEMENTS_DATA` with its `case-id` (finance pack P-ref-20); that is the API's only link from a case to money. Reading the case itself needs the role in sp-api-claims-surface SU8. [read in official docs]
- **FL30.** Amazon states review or reply times only for inbound research, remeasurement and the seller's reply to an inbound information request; each is read on its page (values in "Values that move"). No page read states a review time for other FBA claims. The SCP policy states its own timing for MCF order claims. Sources: stock pack inbound.md F1–F2; NR_Amazon, US, 2025-04-30 (see fee-overcharges FE4); SCP page [read in official docs].
- **FL31.** Sellers report cases auto-marked "Answered" with no reply, for example after 14 days pending (2026-08-11). Sources: forum posts (search results) [opinion].
- **FL32.** Amazon tells sellers to reopen a closed case for questions rather than open a new one, and not to reopen or re-raise an issue after a "no further action" decision. Sources: Connor_Amazon, US, 2025-01-31; support message of 2024-08-22 (thread 6833e3db) [read in official docs].
- **FL33.** A seller can extend a case by replying that more time is needed. Source: Connor_Amazon, US, 2025-01-31 [read in official docs].
- **FL34.** A deactivated account is reinstated through Account Health, and claims are ineligible while the account is not in normal status. Sources: TaylorR_Amazon, US, 2024-11-26 (thread 8e91e62f); US PDF 2025-02-24 [read in official docs].
- **FL35.** (withdrawn: the remeasurement limits are homed in fee-overcharges FE4; see fee-overcharges FE4. NR_Amazon's post ca22eab2 is dated 2025-04-30.)
- **FL36.** (withdrawn: the MYSC update limit and the repeat rule are homed in value-and-reversals; see value-and-reversals VR11, VR22.)
- **FL37.** No Amazon page read charges a fee to file a claim. The costs Amazon names are declined claims, conduct consequences (FL11) and reversals. Sources: § H [inferred from the pages read].
- **FL38.** Professional sellers can e-mail, request a call or chat with support; Individual-plan sellers can only e-mail. Source: Connor_Amazon, US, 2025-01-31 (G64491 linked) [read in official docs].
- **FL39.** Practitioners' menu paths and windows go stale: 2020–2024 Chinese and English guides cite "Other FBA Issue" paths and 18-month or 180-day windows superseded by the 2024–2025 changes. Sources: 知无不言 2020, AMZ123 2022 and 2024, 卖家之家 2024 [opinion]; finance pack P-ref-16 for the dated windows [read in official docs].
- **FL40.** One ERP tells sellers to file each claim in the Seller Central of the store and marketplace where the event happened, warning of "account association issues" otherwise; no Amazon page read states this. Source: SellerSpace 2025-03-20 [opinion].
- **FL41.** The SCP policy adds a conduct sentence of its own for inbound: "Merchants who generate a high number of shipping problems affecting Amazon receiving operations may be subject to additional investigation and monitoring. These actions could result in delays to future reimbursements." No FBA page read carries it. Source: SCP page, *Shipment to Amazon claims* (read 2026-11-13) [read in official docs].
- **FL42.** Amazon's 2022 inbound denial in the Canada store already used the policy's later wording ("a large number of requests in a short time") and added a catch-all ("or otherwise engaging in any other activity that interferes with our capacity to help other sellers"), so the 2021 PDF's "high volumes" is not the only wording Amazon applied before 2025. Source: thread 481080e4 (2022-07-25) [read in official docs, relayed].

## Values that move

A value that differs by store, programme or date sits here, not in a position. Each is read at run time on the page named.

| Value | Store / programme | Value as read | Source | Read on |
|---|---|---|---|---|
| Inbound research time | US, FBA | "anywhere from 2 to 30 days … up to 60 days" | stock pack inbound.md F1 (Amazon pages via the stock pack) | 2026-11-13 |
| Seller's reply to an inbound information request | US, FBA | "within five business days" | stock pack inbound.md F2 | 2026-11-13 |
| Remeasurement completion | US, FBA | "typically within 10 days of request" | NR_Amazon, ca22eab2, 2025-04-30 (see fee-overcharges FE4) | 2026-11-13 |
| Per-unit cap | SCP / MCF account | "$300.00" | supplychain.amazon.com/support/reimbursements | 2026-11-13 |
| Fallback valuation without proof of cost | SCP / MCF account | "40% of the retail price" (valuation section); "40% of the estimated sale price" (Shipment to Amazon section) | same page | 2026-11-13 |
| Valuation-dispute window | SCP / MCF account | "within 90 days after we issue the reimbursement" | same page | 2026-11-13 |
| MCF order claim timing | SCP / MCF account | lost claim once "not delivered within 7 days after the promised delivery date"; "up to 90 days after the estimated delivery date" | same page | 2026-11-13 |
| Per-unit cap, FBA | each store | see value-and-reversals VR29 | — | — |
| Valuation-dispute and re-evaluation windows, FBA | each store | see value-and-reversals VR20 | — | — |
| MYSC update attempts and invoice age | US | see value-and-reversals VR11, VR14 | — | — |
| Support API usage plan | all | see sp-api-claims-surface SU8, SU10 (evidence there: 0.1 requests per second, burst 10, `support_2025-02-01.json`, commit db2936aa) | — | 2026-11-13 |

## Seat's own

These are this file's readings, not Amazon's rules, and enter no skill as findings:
- that "premature" in the conduct paragraph means before a kind's window opens (§ C(c)) [inferred];
- that the policy's "normal status" is the account-health report's `NORMAL` (§ C) [inferred];
- that more, smaller cases may or may not count toward "a large number of requests" (§ B(c)) [inferred];
- that the Indy_Amazon tool route and the IDR "Eligible for claim" tab may be one flow (FL4) [inferred, left open].

## Corrections to other packs

Named, not changed:
- **Finance pack P-ref-40 / E4a** reads the US policy PDF created 2024-12-18 (`PC__Kiwi_Comms_redlined_policy_US_clean.pdf`). A later US PDF exists (`Redlined_FBA_Reimbursement_policy_US.pdf`, created 2025-02-24, last-modified 2025-02-27). It:
  - says "Sourcing cost" and "Manage Your Sourcing cost";
  - refers to "After March 31, 2025";
  - widens the account-status condition (FL13);
  - carries the conduct paragraph (FL11), which P-ref-40 does not quote.

  P-ref-40's claim that the PDF "still says March 10, 2025" holds for the 2024-12-18 file only. (Its valuation wording against the live US help page is value-and-reversals' and customer-returns' to settle.)
- **Stock pack P-inbound-27** cites Amazon Supply Chain's *Reimbursements* page as the US FBA source of the nine-month inbound window. That page is the SCP policy for MCF accounts, the one the AWD terms call the "MCF inventory reimbursement policy" (FL27). The stock pack's own shortages.md already calls it MCF's. The nine months for FBA still stands on the 2026-08-13 staff post and Amazon's Chinese pages (finance pack P-ref-37), so the position's source list needs that page moved out, not its value.
- **Finance pack P-ref-29 and "What only Seller Central shows"** list the SC-only filing tools. FL4 adds the second customer-return statement (IDR tab), FL6 the staff post's report naming, FL22 the BSA agent duties.
- **Finance pack E3** (IDR portal): the launch post b175b700 is a US-store post dated 2025-01-21 (`createdAt`), though served on the EU host too.

## Open questions for a first run on a real account

1. Does the "Check warehouse damaged reimbursement status" tool accept the ledger detail report's `Reference ID` as the Transaction Item ID (FL6), and does Seller Central still serve the Inventory Adjustments report page the 2026 staff post links?
2. (withdrawn: the remeasurement allowance is fee-overcharges FE4's question.)
3. Does the IDR portal show an "Eligible for claim" view with an in-portal submit action, and does it say whether a candidate was already filed?
4. Does a case filed through a tool or the Reconcile tab return a Case ID that later appears as `case-id` in `GET_FBA_REIMBURSEMENTS_DATA`, and for every claim kind (FL29)?
5. Do the Agent Policy (GS83KH2MA7HM69PH) and the *Guidelines for contacting Selling Partner Support* (GK3V2JYCN2P28BFX) pages, as the seller's store shows them, state anything on volume, automation or third-party filers beyond FL11, FL12 and FL22, and do they confirm the relayed rules in FL22?
6. What text does the seller's store show on G200213130 today, and does it still carry the conduct paragraph?
7. (withdrawn: the Manage Your Sourcing Cost page's fields are value-and-reversals' question; see VR13, VR14.)
8. Which of the seller's existing cases (Case Log) are open, and in which state (FL8)? Through the Support API this needs the role in sp-api-claims-surface SU8; otherwise the seller reads the Case Log.
9. Does a case in "Pending Merchant Action" close by itself after a set time? No Amazon page read says so.
10. On a customer-return candidate, does the "Check FBA order reimbursement status" tool on the policy page and the IDR portal's "Eligible for claim" tab lead to the same claim (FL4)?
11. What does the IDR help page (G66ZLS453YSE2Y4R) say about filing from the portal, as the seller's store shows it?

## Pages read

| Title | Address | Publisher | Page date | Read on | Used for |
|---|---|---|---|---|---|
| FBA inventory reimbursement policy (redlined, US) | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_US.pdf | Amazon | PDF created 2025-02-24; last-modified 2025-02-27 | 2026-11-13 | § A, C, E, G; FL2, FL3, FL11, FL13, FL14, FL27 |
| FBA lost and damaged inventory reimbursement policy (April 2021, English, redlined; PDF title "EU FBA lost and damaged inventory reimbursement policy - ENG redline", served under the UK path G/02) | https://m.media-amazon.com/images/G/02/rainier/help/legal/FBA_inventory_reimbursement_policy_April_2021_English_Redlined.pdf | Amazon | PDF created 2021-04-12; last-modified 2021-04-12 | 2026-11-13 | FL2, FL11, FL13; 90-day valuation dispute |
| FBA reimbursement policy (redlined, UK) and (EN, EU) | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_UK.pdf ; https://m.media-amazon.com/images/G/09/rainier/help/redline_FBA_reimbursement_policy__EN_version.pdf | Amazon | created 2025-02-24 / 2025-02-19 | 2026-11-13 (downloaded; dates read, text not extracted) | existence and dates only |
| FBA inventory reimbursement policy (redlined, US, Dec 2024) | https://m.media-amazon.com/images/G/01/rainier/help./PC__Kiwi_Comms_redlined_policy_US_clean.pdf | Amazon | created 2024-12-18 | 2026-11-13 (dates only) | correction to finance P-ref-40 |
| FBA inventory reimbursement policy (help page G200213130) | https://sellercentral.amazon.com/help/hub/reference/external/G200213130 (also .co.uk) | Amazon | — | 2026-11-13: script shell, **unread** | open question 6 |
| FBA inventory reimbursement policy: Customer return claims (G9N934L7Y4SFWPJ4) | https://sellercentral.amazon.com/help/hub/reference/external/G9N934L7Y4SFWPJ4 | Amazon | US v14 (as customer-returns read it) | not read here; carried from customer-returns RT41, read through the help hub's content call (closed 2026-11-10) | FL4 |
| FBA Lost Your Inventory? Steps to File a Reimbursement Claim | https://sellercentral.amazon.com/seller-forums/discussions/t/0e07abc1-9026-4540-a005-153d9e78bf04 | Amazon (Indy_Amazon), US store | `createdAt` 2026-08-13 | 2026-11-13 | § A, B, C, E; FL3, FL4, FL6, FL7, FL13, FL24, FL25 |
| Inventory Defect and Reimbursement portal now available | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/b175b700-09c4-4350-8a22-24f60a724042 | Amazon (News_Amazon), US store by `marketplaceId` | `createdAt` 2025-01-21 | 2026-11-13 | FL5 |
| Missing Items from Inbound - Request to Investigate Denied | https://sellercentral.amazon.com/seller-forums/discussions/t/481080e4a72836a40155169d3039fd25 | seller, quoting Amazon Services; Canada store | `createdAt` 2022-07-25 | 2026-11-13 | FL7, FL11, FL24 |
| Amazon Seller Support (support message of 2024-08-22) | https://sellercentral.amazon.com/seller-forums/discussions/t/6833e3db-02ca-49ae-8479-ff97ece6bc0a | seller, quoting Selling Partner Support; US store | thread 2024-08-21; the reply pasting the message 2024-08-25; message dated 08/22/2024 | 2026-11-13 | FL12, FL32 |
| Contacting Seller Support (staff post) | https://sellercentral.amazon.com/seller-forums/discussions/t/460319ae-fb9b-426b-90c0-ff847a7d070a | Amazon (Connor_Amazon), US store | `createdAt` 2025-01-31 | 2026-11-13 | FL8, FL28, FL32, FL33, FL38 |
| Guidelines for contacting Selling Partner Support | https://sellercentral.amazon.com/help/hub/reference/GK3V2JYCN2P28BFX (address as linked in thread 6833e3db) | Amazon | — | **unread** | open question 5 |
| Importance of Accurate Product Measurements | https://sellercentral.amazon.com/seller-forums/discussions/t/ca22eab2-3fbe-4826-ab22-74a842fac674 | Amazon (NR_Amazon), US store | `createdAt` 2025-04-30 | 2026-11-13 | § A, F; FL30 |
| Mod Clarification - Manage sourcing cost | https://sellercentral.amazon.com/seller-forums/discussions/t/cd2909d2-7dd0-4855-9f94-12051e13b8a3 | Amazon (Arish_Amazon) and seller, US store | thread 2026-02-22; Arish_Amazon's reply 2026-02-24 | 2026-11-13 | § E (pointer to value-and-reversals) |
| Sourcing Cost - Proof of value document does not meet requirements | https://sellercentral.amazon.com/seller-forums/discussions/t/b48840c1-3396-43ba-9731-b88f338e6aa8 | Amazon (Nano_Amazon), US store | `createdAt` 2025-06-12 | 2026-11-13 | § E (pointer to value-and-reversals) |
| Seller code of conduct (staff relay of G1801) | https://sellercentral.amazon.com/seller-forums/discussions/t/a3c0c769-dab1-4c75-a5c0-43fceb67b581 | Amazon (Emet_Amazon), US store | thread 2024-11-20; Emet_Amazon's reply 2024-11-23 | 2026-11-13 | FL15 |
| Seller Code of Conduct G1801 | https://sellercentral.amazon.com/help/hub/reference/G1801 (also …/gp/help/external/1801) | Amazon | — | 2026-11-13: script shell, **unread** (relayed above) | FL15 |
| Section 3 for FBA credit reimbursement abuse? | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/807fb6a2-374a-4f8a-bf9f-488eae597a1e | seller; Stevie_Amazon reply; US store by `marketplaceId` | `createdAt` 2024-07-01; reply 2024-07-07 | 2026-11-13 | FL16, FL17 |
| Account Suspension for Violation of Lost and Damaged Reimbursement Policy | https://sellercentral.amazon.com/seller-forums/discussions/t/e885be1d-8d49-45fa-b400-14af9aeb1b86 | seller, US store | `createdAt` 2023-03-27 | 2026-11-13 | FL16 |
| Amazon deactivated for fba reimbursement abuse | https://sellercentral.amazon.com/seller-forums/discussions/t/22eecf9e75a3ae1d6bae28c9e93d6b75 | seller, US store | `createdAt` 2021-05-04 | 2026-11-13 | FL16, FL17 |
| Excessive contacts issue | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/83cf5f35bb680661131aeb7e01b33cd5 | seller; Maja_Amazon reply; UK store | `createdAt` 2023-02-17 | 2026-11-13 | § C7 |
| No Reimbursements on my missing units and deactivated my account instead | https://sellercentral.amazon.com/seller-forums/discussions/t/8e91e62f-297e-4828-a41c-871bda710238 | seller; TaylorR_Amazon; US store | thread 2024-11-08; TaylorR_Amazon's reply 2024-11-26 | 2026-11-13 | FL34; § F |
| Business Solutions Agreement updates effective March 4, 2026 (US) | https://sellercentral.amazon.com/seller-forums/discussions/t/84e3f6b1-42f7-4cf3-a189-a5cc8d78d838 | Amazon (News_Amazon), US store | `createdAt` 2026-02-17 | 2026-11-13 | FL22 |
| Business Solutions Agreement updates effective March 4, 2026 (Canada) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/8a2dfc1c-2091-40d1-816b-457a68265b01 | Amazon (News_Amazon), Canada store by `marketplaceId` | `createdAt` 2026-02-19 | 2026-11-13 | FL22 |
| Agent policy (GS83KH2MA7HM69PH) | https://sellercentral.amazon.com/help/hub/reference/external/GS83KH2MA7HM69PH (also …/gp/help/external/GS83KH2MA7HM69PH) | Amazon | — | 2026-11-13: script shell, **unread** | FL22, open question 5 |
| Inventory Defect and Reimbursement (IDR) Portal (G66ZLS453YSE2Y4R) | https://sellercentral.amazon.com/gp/help/external/G66ZLS453YSE2Y4R | Amazon | — | 2026-11-13: script shell, **unread** | FL5, open question 11 |
| Amazon Services Business Solutions Agreement PDFs (AU; English; 2024 edit) | https://m.media-amazon.com/images/G/35/rainier/help/AU_EN_BSA_PDF.pdf ; https://m.media-amazon.com/images/G/01/rainier/help./1.1_BSA_PDF_English.pdf ; https://m.media-amazon.com/images/G/31/rainer/AmazonServicesBusinessSolutionsAgreement_2024edits1.pdf | Amazon | last-modified 2021-07-29 / 2023-12-13 / 2024-06-12 | 2026-11-13 (text extracted) | no agent clause, no Code of Conduct text; FL15, FL22 |
| Amazon Warehousing and Distribution service terms | https://supplychain.amazon.com/legal/service-terms/warehouse-and-distribution | Amazon | "Dated: January 14, 2026" | 2026-11-13 | FL27 (the "MCF inventory reimbursement policy" link) |
| Acceptable Use Policy (SP-API) | https://sellercentral.amazon.com/mws/static/policy?documentType=AUP&locale=en_US | Amazon | undated | 2026-11-13 | FL20, FL21 |
| Reimbursements (Amazon Supply Chain): *Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS)* | https://supplychain.amazon.com/support/reimbursements | Amazon | © 2026, no revision date | 2026-11-13 | § A, C, E; FL2, FL7, FL11, FL13, FL25, FL27, FL41; Values that move |
| Reimbursement policy for Buy with Prime orders | https://buywithprime.amazon.com/knowledge-center/reimbursement-policy-for-buy-with-prime-orders | Amazon | — | 2026-11-13: 403 again; text from search results | FL11 |
| Support API model `support_2025-02-01.json` | amzn/selling-partner-api-models, commit db2936aa (2026-10-29); main b13d1d10 (2026-11-11) checked | Amazon | first in the public repo 2026-09-30; rate limits added 2026-10-28 | 2026-11-13 | pointer to sp-api-claims-surface |
| Amazon plugin skill `support-case-helper` SKILL.md | Amazon's Claude plugin (the survey's copy) | Amazon | v1.0.0 | 2026-11-13 | FL23 (pointer to SU14) |
| Amazon's new AI agent rules shake up sellers before March 4 deadline | https://ppc.land/amazons-new-ai-agent-rules-shake-up-sellers-before-march-4-deadline/ | PPC Land (Luís Rijo) | 2026-02-22 | 2026-11-13 | FL22 (US thread id, dates) |
| Amazon's Agent Policy: what AI tools and agents may do | https://ecomsellertool.com/blog/amazon-agent-policy-ai-tools | Ecomsellertool | 2026-09-25, upd. 2026-11-04 | 2026-11-13 | FL22 relayed rules |
| Amazon BSA Update 2026 | https://damlawfirm.com/blog/amazon-bsa-update-august-2026/ | DAM Law Firm (M. N. Toledo) | 2026-09-03 | 2026-11-13 | FL17 |
| Amazon BSA agent policy 2026 | https://sellersprite.ai/en/blog/amazon-bsa-agent-policy-2026 | SellerSprite | 2026-06-27 | 2026-11-13 | FL22 (announcement quote) |
| Amazon Just Wrote the First Rules for AI Agents | https://getsliq.com/blog/amazon-ai-agent-rules | Sliq | undated | 2026-11-13 | § D (no verbatim text) |
| How to provide Seller Central access for the Seller 365 reimbursements service | https://intercom.help/seller-365/en/articles/10514319-how-to-provide-seller-central-access-for-the-seller-365-reimbursements-service | Seller 365 / Threecolts | 2026-08-19 | 2026-11-13 | § D permissions |
| Amazon Reimbursement Policy – Decoded for Faster Claims | https://getida.com/resources/blog/fba-reimbursements/amazon-reimbursement-policy/ | GETIDA | undated (images 2024-07) | 2026-11-13 | § F, G |
| Can you get your money back from Amazon FBA? | https://riverbendconsulting.com/blog/amazon-reimbursement/ | RiverBend Consulting (Alex Landry) | upd. 2026-02-03 | 2026-11-13 | § C |
| 索赔助手 - 图文教程 (Claim assistant guide) | https://www.sellerspace.com/en-US/help/doc/claim-indemnity-assistant-use-guide/ | SellerSpace / 优麦云 | 2025-03-20 | 2026-11-13 | FL10, FL40; § B, F |
| 亚马逊FBA索赔开Case步骤截图详细教程 | https://www.wearesellers.com/question/26211 | 知无不言 (Allen哥) | 2020-10-28 | 2026-11-13 | § A; FL39 |
| 让你的店铺增加1%净利润---向亚马逊索赔的正确姿势 | https://www.amz123.com/t/1PmAosGP | AMZ123 (大姐夫站外推广) | 2022-01-04 | 2026-11-13 | FL10, FL39 |
| 学会亚马逊FBA索赔，轻松增加1%店铺净利润 | https://www.junglescout.cn/blog/48329/ | Jungle Scout China | 2022-04-08 | 2026-11-13 | FL10 |
| 如何对亚马逊FBA进行索赔 | https://mjzj.com/article/bhivfdlge0w6 | 卖家之家 (跨境女子图鉴) | 2022-04-08 | 2026-11-13 | § C, E |
| 亚马逊FBA索赔时限缩短，卖家有解决方案了！ | https://m.mjzj.com/article/du2ckgmjnthc | 卖家之家 (招单猫) | 2024-08-07 | 2026-11-13 | FL39 |
| 亚马逊卖家丢货超5000件！申诉索赔实操分享！ | https://www.amz123.com/t/vcGmSDYD | AMZ123 (跨境风暴) | 2024-08-01 | 2026-11-13 | § E; FL39 |
| FBA丢件索赔却惨遭封号！ | https://www.ikjzd.com/articles/1810625995691812998 | 跨境知道 (敏哥跨境记) | 2024-09-24 | 2026-11-13 | FL18 |
| 正常索赔竟遭封店！亚马逊"耍流氓"？还是另有隐情？ | https://t.cj.sina.com.cn/articles/view/6469010462/18195441e00100yy7s | 新浪财经 (看点资讯) | 2021-04-16 | 2026-11-13 | FL10, FL16 |
| 亚马逊索赔对店铺会不会有影响？FBA卖家如何合规进行索赔？ | https://www.sohu.com/a/785386694_491696 | 搜狐 (RefundBest) | 2024-06-12 | 2026-11-13 | § B, C |
| Search-result-only pages (snippets, not fetched) | myamazonguy.com reimbursement guide; refunzo.com service-cost and FBA pages; nventory.io; sellerlabs.com knowledge base; lumian.ai; jarvio.io; spscommerce.com 3P revenue recovery; ecomengine.com IDR portal; salesduo.com escalation; seller forum threads 8696d6e3, bd311a5a, 267c908a, 851515e5, and the "Answered" thread of 2026-08-11 | various | various | 2026-11-13 (search results only) | opinions marked [opinion] in § B, C, D, F, G |

## Verification (2026-11-13)

An adversarial check re-opened the sources behind the positions on 2026-11-13: public pages only, no SP-API call, no login, no seller data.

**Checked and confirmed** (source re-read):
- FL1: the Support API model at commit db2936aa has three operations, all reads (`listCases`, `getCase`, `listContacts`); upstream main b13d1d10 (2026-11-11) changes neither the Support model nor any claim operation; Amazon's tutorial covers retrieval only; the role is *Selling Partner Support (Restricted)* on Amazon's roles page.
- FL2, FL3, FL11, FL13, FL14: the sentences quoted, in the US PDF (created 2025-02-24) and the April 2021 PDF (created 2021-04-12), both text-extracted; the $5,000 cap and the 60-day (US 2025) / 90-day (2021) valuation-dispute windows.
- FL4: the six entry points, tool names and identifiers in Indy_Amazon's post; "Don't file too early", "Check Reports > Payments > Reimbursements before filing manually", "One claim per shipment or event", "blocked, terminated, or fraud".
- FL5: the IDR portal's coverage and exclusion sentence.
- FL6: `GET_LEDGER_DETAIL_VIEW_DATA` carries `Reference ID` (Amazon Fulfillment role); the adjustments type is gone from Amazon's FBA report-type page; its removal date 2023-01-31 (moved from 2022-11-15) per the deprecation notice's search text.
- FL7, FL24: the Amazon Services denial text (signed "Sincerely, Amazon Services").
- FL8, FL28, FL32, FL33, FL38: Connor_Amazon's sentences; the four states, channels and date fields in the model.
- FL12: the support message dated 08/22/2024 and its sentences.
- FL15: Emet_Amazon's relay of G1801.
- FL20, FL21: AUP 1.1, 2.11, 3.3, 3.6, 3.7, verbatim; the page carries no date.
- FL22: the announcement's three agent duties, the effective date, "continued use" and the linked page ids; the Agent Policy page is still a shell.
- FL23: the SKILL.md text.
- FL25, FL27: the Supply Chain page's evidence lists, cap, fallback, filing route and title.
- FL26, FL36: Nano_Amazon's and Arish_Amazon's sentences; the 60-day re-evaluation line is a decline notice a seller relayed, not a staff post.
- FL34, FL35, FL30: TaylorR_Amazon's Account Health sentence; NR_Amazon's remeasurement sentences, with no number for the monthly limit.
- Report columns and roles named in "Read at run time": `GET_FBA_REIMBURSEMENTS_DATA` (`case-id`, `original-reimbursement-id`, `approval-date`; Pricing or Amazon Fulfillment), the removal and returns reports' roles, `accountStatuses` in the account-health schema.
- Practitioner sources (SellerSpace, AMZ123, Jungle Scout China, 知无不言, 卖家之家 2022, 跨境知道, RiverBend, Sohu, Seller 365, ecomsellertool, DAM Law Firm, PPC Land): dates and attributed words.

**Changed:**
- Summary: the 2025 US wording "a large number of requests" now leads; "forged document" is tied to sourcing-cost submissions; "penalises" narrowed to what the pages name as declined or as conduct.
- FL1: added that the only claim-creating SP-API operation, Shipping v2 `createClaim`, is for Amazon Shipping labels, not FBA inventory.
- FL6: the removal date was attached to the Ledger by the sentence's grammar; it belongs to the adjustments report's API type. The deprecation notice was added as a source.
- FL16: Section 3 appears only in thread 807fb6a2; thread e885be1d's notice carries no Section 3 citation.
- FL17: rewritten. The cases filed while the account was deactivated were the seller's finding, with no Amazon action on them shown; "Amazon holds YOU responsible" is a seller's reply; DAM Law Firm speaks of Agents, not claim services.
- FL21 and § D(c): the AUP binds SP-API developers, and the words are "Amazon Portal". That a non-SP-API service is bound the same way is now marked [inferred].
- FL23 and § D: "by default", "current state", `apis: []` and the skill's scope (connector/plugin support, not FBA claims) were added; § D(c) no longer says the skill always leaves submission to the seller.
- § A(b) menu paths: 知无不言 (2020) and AMZ123/Jungle Scout China (2022) give different paths. They are now listed apart, with the words each source uses.
- § B(b), FL10, § C(b): Chinese quotes corrected to the source ("30+个case", "每天申请索赔最好不要超过10个", "大概在2.5~3%"); the AMZ123 per-case advice is attributed to support staff, as the article does.
- § C(a): the GK3V2JYCN2P28BFX address is linked in thread 6833e3db itself, not taken from search results; Emet_Amazon's thread title added.
- § C(c): "premature = before the window opens" marked [inferred]; the forged-document rule tied to sourcing cost; the "exact match" rule attributed to Arish_Amazon.
- § G(b): the reopened check in thread 8e91e62f was a "Live Channel Specialist's", not a moderator's.
- § H(c): "filing late leaves less room for re-evaluation" removed. The re-evaluation window runs from the initial claim, so filing later does not shorten it. "Not premature" if filed at window opening downgraded to [inferred].
- § B(c): the claim that more contacts carry "more weight" under the conduct rule is downgraded to [inferred].
- Moving values: FL26 (365-day invoice recency), FL27 ($300 / 40% / $5,000), FL30 (2–30/60 days, 10 days, five business days), FL36 and § B(c) (two per FNSKU per 30 days), § B(a) (0.1 rps, burst 10) are restated as a rule plus where it is read, with the value kept as dated, marketplace-tagged evidence.
- Open question 8: dropped "before anything new is prepared", a sequence.
- Dates: relative page dates ("3 months ago", "9 months ago", "2 years ago", "4 years ago", "a year ago") recorded beside the absolute dates the file uses; the April 2021 PDF's own title ("EU … ENG redline", served under the UK path) recorded; Support API model history (first public 2026-09-30, rate limits 2026-10-28) added.
- No file path on this machine was found in the file.

**Remaining doubts:**
- The 2026-08-13 date of Indy_Amazon's post and the 2026-02-17 date of the BSA announcement rest on the finance pack and PPC Land; the forum pages show only relative dates, which agree.
- The 2023-01-31 removal date was read from search text of Amazon's deprecation notice; a direct fetch of the notice returned an index page.
- The Agent Policy (GS83KH2MA7HM69PH), *Guidelines for contacting Selling Partner Support* (GK3V2JYCN2P28BFX), G200213130, G1801 and *Manage Your Sourcing Cost* are still unread (JavaScript shells or sign-in).
- Buy with Prime's wording (FL11) is still search text only (403).
- News d8f9a56c (re-evaluation within 90 days of initial claim, effective 2025-10-15) was confirmed only through search text and the finance pack.
- Sources seen only as search snippets (Seller Labs, lumian.ai, Refunzo, GETIDA's appeal window, salesduo, the "Answered" thread of 2026-08-11, threads 8696d6e3, bd311a5a, 267c908a) were not re-opened.
- Emet_Amazon is read as Amazon staff by the `_Amazon` suffix; the page gives no title.
- 卖家之家 (2022): only "每个商品只能提出一项索赔" was re-confirmed; the wider sentence about a second claim on the same shipment was not.

## Revision (2026-11-13)

After the completeness review. Routes: public pages by plain GET only; no POST to an Amazon host; the help hub's content call not used. The web search budget ran out partway through, so the Agent Policy and G1801 search for a primary copy stopped at the sources listed.

**Dates pinned from page data** (`createdAt` / `datePublished`, read 2026-11-13), replacing every "≈" date:
- Connor_Amazon 460319ae: 2025-01-31 (was ≈2024). NR_Amazon ca22eab2: 2025-04-30 (was ≈2024; agrees with fee-overcharges). Nano_Amazon b48840c1: 2025-06-12. Arish_Amazon cd2909d2: 2026-02-24 (thread 2026-02-22). Emet_Amazon a3c0c769: 2024-11-23. TaylorR_Amazon 8e91e62f: 2024-11-26. Indy_Amazon 0e07abc1: 2026-08-13 (now read directly, no longer via the finance pack).
- b175b700 (IDR portal): 2025-01-21, US store (was ≈2024, "EU forum"). 481080e4: 2022-07-25, Canada store (was ≈2022, read as US). e885be1d: 2023-03-27 (was ≈2022). 22eecf9e: 2021-05-04 (was ≈2020). 807fb6a2: 2024-07-01, US store (was "EU forum ≈2024"). 83cf5f35: 2023-02-17, UK store (was undated).
- 6833e3db: the support message dated 08/22/2024 was pasted in a reply of 2024-08-25; it also quotes the conduct paragraph in full.
- BSA announcement: US thread 84e3f6b1, 2026-02-17, now read directly; thread 8a2dfc1c is the Canada store's post of 2026-02-19 (was "UK thread", dated through PPC Land).

**Changed:**
- FL4: customer returns now carry both Amazon statements with their dates (Indy_Amazon's policy-page tool, 2026-08-13; the help page's IDR "Eligible for claim" tab, customer-returns RT41, through a route now closed); neither is picked. Damaged inbound adds the 2022 Canada denial's "Contact Us" wording.
- FL5: date, store and the Reimbursements-report access path; help page G66ZLS453YSE2Y4R recorded as unread.
- FL6: the staff post's link to a Seller Central `reportcentral/INVENTORY_ADJUSTMENT/0` page added; the removal date stays on search text and the stock pack (the changelog page gave no notice text to a plain GET).
- FL11, FL12: Amazon's own 2022 and 2024 messages quoting the conduct paragraph; the SCP wording; Buy with Prime still 403 and tagged search text only.
- FL13: the SCP account condition added.
- FL14: the repeat rule moved to value-and-reversals VR22.
- FL15, FL22: the position now says the Code of Conduct words and the Agent Policy's rules rest on relays; the search for a permitted primary copy (help paths by plain GET, Amazon's BSA PDFs on m.media-amazon.com, developer-docs, gs.amazon.cn by search) found none.
- FL27: reconciled with inbound-shortfalls IN26. The AWD terms link "MCF inventory reimbursement policy" to supplychain.amazon.com/support/reimbursements, the same page titled *SCP Reimbursements policy - ASCS*, so the two files describe one page by two names.
- FL1, FL23, FL28, FL29: the Support API and the support skill are pointed to sp-api-claims-surface (SU8, SU10, SU12–SU14).
- FL26: narrowed to a pointer to value-and-reversals VR12–VR14.
- FL30: values moved to "Values that move"; SCP timing added.
- § C7: 83cf5f35 corrected. The reply naming the Code of Conduct ("Art from Amazon") is posted from a seller-type account, and the only `_Amazon` reply transfers the thread.
- § G(b): the salesduo practice is now stated beside Amazon's reopen instruction as a choice, not a step.
- § A, § B, § E, § F, § G: valuation dispute, MYSC limits, remeasurement limits and Support API limits are replaced by pointers (value-and-reversals VR11–VR14, VR20–VR22; fee-overcharges FE4; sp-api-claims-surface SU8, SU10).
- Added the "Values that move", "Seat's own" and "Corrections to other packs" sections; added a routes-and-dates note at the head.

**Withdrawn:** FL35 (homed in fee-overcharges FE4); FL36 (homed in value-and-reversals VR11, VR22); open questions 2 and 7 (same homes).

**Added:** FL41 (the SCP policy's inbound monitoring sentence); FL42 (the 2022 Canada denial already used "a large number of requests" plus a catch-all); open questions 10 (are the two customer-return routes one flow?) and 11 (the IDR help page).
