# Customer returns: what Amazon owes when a refund, a return and a unit do not line up

Research for brief 548 (the claims playbook), area *customer-returns*. Date read for every page: 2026-11-13, unless a row in *Pages read* says otherwise.

**Summary.** On an FBA order Amazon refunds or replaces on the seller's behalf and debits the seller. Amazon's staff and contract texts read through permitted routes say it then owes the seller when the unit never comes back within the store's set number of days, when it comes back unsellable through Amazon's fault, or when the unit is lost, damaged or wrong on its way to the buyer (BSA F-8.3). The customer-return claim window is counted from the refund or replacement date; Amazon's News posts give it per store (the US post 60–120 days; the Canada, UK, Sweden and Australia posts 45–105), and staff posts give other figures, so the window is read per store at run time. The FBA Returns report (`GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`) is the unit side of every join; it holds only units that reached a fulfilment centre, and its column names, disposition spellings and status names differ between Amazon's pages and practitioners' files. Units lost or damaged after an order and before delivery appear in the Reimbursements report as `Lost_Outbound` / `Damaged_Outbound` (finance pack P-ref-35); Amazon's policy text names no separate claim kind for them. Many store-specific rules this file once quoted (the US damage fee, Japan's and India's late-return rules, the 30-day removal rule, the fee credits on a return) rested on a route the office has closed; they are listed under *Held: read only through a barred route* and enter no skill.

**Tags.** [read in official docs] = Amazon's page, model or document, read on the date given, by the route named. [command-verified] = something run locally on this seat (a grep over the models clone at commit db2936aa of 2026-10-29, a parse of a forum page fetched by plain GET, or a render of an Amazon PDF). [opinion] = a named practitioner or vendor. [inferred] = this seat's reasoning from sources named. "seat's own" = no source; enters no skill. Route tags inside a source: (News) a Seller Forums News post; (staff) a Seller Forums reply by an Amazon moderator; (PDF) an Amazon PDF on m.media-amazon.com; (sell.amazon) a sell.amazon.com page; (SP-API docs) developer-docs.amazon.com; (listing pack's read) the listing pack's read of a help page on 2026-10-14, cited as that seat's read; (copy) a third party's verbatim copy of Amazon text.

**How pages were read (route).** On 2026-11-10 the office ruled (brief 307) that the help hub's content call stays off limits, and brief 548 allows no call to an Amazon host beyond public pages. This file's first round had read every Seller Central help page through that call; those reads are withdrawn. In this revision no help page was fetched and no POST was made to any Amazon host. Every fact that rested on a help page was re-sourced through a permitted route and tagged with it, or moved to *Held: read only through a barred route* by position id and page id. The permitted routes used: Seller Forums threads by plain GET (each post's date is its `createdAt` or `datePublished`; the store a post was issued for is the post object's `marketplaceId`, the field after `contentMetadata`, as the inbound-shortfalls and removals-disposals files read it [command-verified]; the post-to-store method and table are homed in fc-lost-damaged § 2a); Amazon PDFs on m.media-amazon.com (policy redlines and Business Solutions Agreements, rendered so that struck and inserted text are told apart, as value-and-reversals § F does); sell.amazon.com; developer-docs.amazon.com `.md` pages; the models clone at db2936aa; third-party pages by plain GET; and the listing pack's read of 2026-10-14 (cx-listing-playbook research/angles/returns.md), cited as that seat's read. Help-page ids named below as "read at run time" are pages the seller sees in Seller Central; their ids are carried by Amazon staff posts' own links (Veronica_Amazon links G9N934L7Y4SFWPJ4 and G200213130; Danny_Amazon links G9MAM9ELJTSSNYS5 and GX9GZV9UGAAL4C58). The amazon.com customer help pages (*Return Fees*, *Refunds*) answered HTTP 403 to a plain GET on 2026-11-13 and stay unread.

**Already held elsewhere (one fact, one home).** The finance pack (cx-amazon-finance-playbook) research/areas/refunds-reimbursements-adjustments.md holds refund money lines (P-ref-1..8), A-to-z, chargebacks and SAFE-T (P-ref-9..11), FBA reimbursement scope, automation and valuation (P-ref-12..15, P-ref-40), the claim-window table (P-ref-16), the Reimbursements report and its `reason` values (P-ref-17..20, P-ref-35) and reversals (P-ref-18). The stock pack (cx-amazon-stock-playbook) research/areas/stuck-stock.md holds the unfulfillable dispositions in `getInventorySummaries` (D1), "customer damaged" (D3), repackaging (D5), automated removal of unfulfillable stock (D6–D8); its stock-states.md holds the ledger (P-stock-states-29/30/35/36). The listing pack research/angles/returns.md holds the reason codes as a listing signal and the buyer's return windows. Within this pack: the post-to-store table and the automation dates → fc-lost-damaged § 2a; valuation, the per-unit cap, the valuation-dispute window and MYSC limits → value-and-reversals; the Support API, "no operation files a claim" and roles → sp-api-claims-surface; IDR and case routes, limits and conduct → filing-and-conduct; removal claims, including grading disputes → removals-disposals. This file cites those and adds only the customer-order side.

---

## 1. What Amazon owes on an FBA customer return: the three outcomes

**(a) Amazon's rule.**

Veronica_Amazon (staff), reply of 2023-10-13 in "Reimbursement for Customer-Damaged Returns" (thread 70760af8, store `ATVPDKIKX0DER` = US [command-verified]), read 2026-11-13. The reply links *FBA inventory reimbursement policy* and *FBA inventory reimbursement policy: Customer return claims* and restates them:
- "Sometimes a customer is refunded for your item, but the item isn't returned to a fulfillment center within 60 days of the refund. When this situation occurs, in most cases we'll charge the customer and reimburse you."
- "If a customer returns your item to a fulfillment center within 60 days of the refund, we'll first determine the condition of the returned item. If the returned item is sellable, we'll return the item to your inventory and will not reimburse you. If the returned item is unsellable, we'll determine who is responsible for the condition. If we find Amazon is responsible for an unsellable return, we'll reimburse you and will not add the item back to your inventory."
- "Amazon policy states that it does not accept responsibility and will not reimburse for returned items that are damaged by a customer, are subject to recall, are defective or in violation of Amazon policies, or for other similar reasons."

Indy_Amazon (staff), "FBA Lost Your Inventory? Steps to File a Reimbursement Claim" (thread 0e07abc1, US, posted 2026-08-13), read 2026-11-13, repeats the same three outcomes under "Customer return not received" and ends "Amazon will not reimburse you for returned items that are damaged by a customer".

Christine_Amazon (staff), "Refunds and Returns Policies" (thread 02bebf51, store `A2EUQ1WTGCTBG2` = Canada, posted 2025-03-24), read 2026-11-13: "Automatic Reimbursement: If an item is not returned within 60 days, you will automatically be reimbursed. Sellable Returns: If a return is in sellable condition, it is restocked in your inventory, and no reimbursement will be issued. Unsellable Returns: You will receive a reimbursement only if Amazon is responsible for the unsellable return". "Non-Reimbursable Scenarios: These include items damaged by customers, recalled products, defective items, policy violations, and refunds issued directly by the seller."

The buyer's reason does not decide. FBA customer returns policy (G200379860, v24 r2), as the listing pack read it on 2026-10-14 (listing pack's read): "our reimbursement decisions are based on the actual physical condition of the item when evaluated at our fulfillment center, not the buyer's selected reason."

UK conditions never paid. *FBA lost and damaged inventory reimbursement policy* (UK), Amazon redlines on m.media-amazon.com (PDF created 2024-12-11 and 2025-02-24), rendered, the sentence not struck [command-verified]: "Note: Amazon does not reimburse for customer returns with conditions such as, damaged box or packaging; missing factory seal; missing packaging, tape or shipping label over box; and different box." (PDF)

The contract, Business Solutions Agreement, FBA Service Terms. Two copies were read as Amazon PDFs: the North America redline (BSA_NA_English_redlined.pdf, created 2019-07-17) and the Australia agreement (Amazon_Services_Business_Solutions_Agreement_October_2023_LIVE.pdf, created 2023-10-16). The live US agreement is a help page and stays unread (see *Held*).
- F-8.2 (NA): "We will have the right to determine whether a customer will receive a refund, adjustment or replacement for any Amazon Fulfillment Unit and we will to require you to reimburse us where we determine you have responsibility … We will promptly notify you when you are responsible for a customer refund. You may appeal if you disagree with our finding within thirty (30) days after our notification". The appeal sentence is inserted text in the 2019 redline (blue, underlined) [command-verified]; "we will to require" is the redline's text layer, which keeps struck and inserted words together. AU 2023 adds: "Within thirty (30) days after our notification, you may request that we return to you any Unsuitable Unit for inspection and you may appeal if you disagree with our finding".
- F-8.3 (NA): "In situations relating to Amazon Fulfillment Units where the wrong item was delivered or the item was damaged or lost or is missing, unless we determine that the basis for such request is caused by you … we will, as your sole and exclusive remedy and at our option: (a) for any Amazon Fulfillment Unit, (i) ship a replacement Unit to the customer and reimburse you in accordance with the FBA Guidelines for the replacement Unit, or (ii) process a refund to the customer and reimburse you in accordance with the FBA Guidelines for the Unit". "we will be entitled to retain the applicable fees".
- F-8.4 (NA): "If we provide a replacement Unit or refund … and that customer returns the original Unit to us, … if it is a Sellable Unit, we may, at our option, place such Unit back into your inventory … If we do put a Unit back into your inventory, you will reimburse us for the applicable Replacement Value … of the returned Unit." This is the contract basis for taking back a reimbursement when the unit arrives after Amazon has paid (see § 8).

**(b) Practitioners.**
- GETIDA ("A Quick Guide to Amazon FBA Reimbursements Part 5", undated, re-read 2026-11-13) names these returns audit types: "Returns Reimbursement" ("A reimbursement was never actually paid out"), "Wrong Item Returned", "Returned Not Refunded after 45 Days", "Damaged Returns", "Return Overcharge" ("The customer was refunded more than they originally charged"), "Return after 60 Days", "Damaged Return by Carrier" and "Chargeback not Refunded". [opinion]
- My Amazon Guy (Steven Pope, "Types of Amazon FBA Refunds", 2024-07-26) names "Refund Overcharge", "Damaged Returns" and "Missing Refunds". [opinion]
- Refunzo (Jimi Patel, 2026-02-19) works from one matching rule: "Any refunded order with no corresponding return entry is a potential missing return reimbursement case". It says Amazon's automatic reimbursement "frequently misses cases", with no figure. [opinion]
- Seller 365 (help article "What types of reimbursements are included…", undated, read 2026-11-13) lists under "Orders Issues (Customer Returns)": "Refunded but Never Returned", "Returned Different FNSKU than Ordered", "Refunded and Replaced (with no replacement sent/received)", "Returned Outside of the Return Window". [opinion]
- In Chinese, the 邦阅网 guide (52by.com article 44020, read via search summary) lists "买家收到退款未退货；收到换货未退原产品；给买家退款金额多了；超过30天才退货". [opinion]

**(c) Into a skill:** the three outcomes (not back within the store's days → reimbursed in most cases without a claim; back sellable → restocked, no money; back unsellable → fault decides). The fault decision rests on the unit's physical condition, not the buyer's reason. Customer-damaged, recalled, defective or policy-violating units and seller-issued refunds are not reimbursed. The contract lets Amazon take back a reimbursement when the unit later returns sellable (F-8.4), and gives the seller an appeal against a finding of responsibility within a period after Amazon's notice (F-8.2; value in *Values that move*).
**Read at run time:** the store's *FBA inventory reimbursement policy: Customer return claims* (G9N934L7Y4SFWPJ4) as the seller sees it in Seller Central; the store's BSA, FBA Service Terms F-8. The seller's own outcomes come from `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`, `GET_FBA_REIMBURSEMENTS_DATA`, and the refunds in Finances (`listTransactions`; the settlement V2 flat file was removed on 2026-11-11, sp-api-claims-surface SU38).

---

## 2. The claim window and the "not returned" clock: dated, and different per store

**(a) Amazon's rule.** No source is picked; each carries its date and store. The values are in *Values that move*; the store of each News post is its `marketplaceId` (fc-lost-damaged § 2a holds the post-to-store table for the pack).

- US News post 81c3235d (2024-07-24): "An FBA customer returns claim can be submitted between 60-120 days after the customer refund or replacement date. Claims must not be submitted before 60 days to ensure the customer has time to return the item to us for processing." Effective "October 23". (News)
- Canada News post 6605eede (posted 0.7 s later, same title, British spelling): the same sentence with "between 45-105 days" and "before 45 days". (News)
- UK News d0fc997e (2024-10-10) and 9a92846d (2025-01-15), Sweden News 1101821c (2025-01-15), Australia News d8f9a56c (2025-08-14, effective 2025-10-15): 45–105 days after the customer refund or replacement. (News)
- US staff: Veronica_Amazon (2023-10-13) and Indy_Amazon (2026-08-13) give 60 days as the "not returned" clock; Indy_Amazon gives the claim window as "no sooner than 60 days after the customer refund … and within 18 months". (staff)
- Canada staff: Christine_Amazon (2025-03-24) gives "between 60–120 days after a customer receives a refund or replacement" and "not returned within 60 days", against the Canada News post's 45–105. (staff)

Read by store, the two posts of 2024-07-24 are the US (60–120) and Canada (45–105) issues of one announcement [command-verified: post `marketplaceId`; that the field names the store a post governs is the reading the pack shares, see fc-lost-damaged § 2a]. The US staff post of 2026-08-13 agrees on the 60-day start and gives an 18-month end that no News post carries. The Canada staff post contradicts the Canada News post.

**(b) Practitioners.**
- 卖家之家 (小牛站外, "重大调整！亚马逊FBA索赔申请期限又缩短了！", 2025-01-24) and AMZ123 (跨境小蚂蚁, "两大新政！亚马逊FBA索赔资格申请期限更新", 2025-01-19) report that the 美国站 window moved from "60-120天，缩短至45-105天", on an announcement dated "1月16日". The posts dated 2025-01-15 that carry 45–105 are the Sweden and UK issues (1101821c on the EU forum; 9a92846d), not a US one; that the articles read one of those is [inferred]. [opinion]
- Refunzo (2026-02-19), AMZBase ("Amazon FBA Returns: Where the Money and the Unit Actually Go", 2026-09-07) and most 2026 English vendor pages give 60–120 for the US. Eva.guru and SellerSprite give 45–105 "since October 15, 2025", the Australia post's date. [opinion]
- SPS Commerce ("Amazon Reversed Reimbursements", updated 2025-07-24) still says 45 days. [opinion]

**(c) Into a skill:** the claim window is counted from the customer refund or replacement date, never from the return-received date. A claim filed before the window opens is refused ("Claims must not be submitted before …"), and one filed after it closes is ineligible. The figures differ by store and Amazon's own posts disagree, so the skill states the rule and where to read the value; it never states a day count of its own.
**Read at run time:** the store's *Customer return claims* page (G9N934L7Y4SFWPJ4) as the seller sees it; the latest Seller Forums News post on claim windows whose `marketplaceId` is the seller's store (fc-lost-damaged § 2a). No SP-API operation gives the window [command-verified: no model in the clone names a reimbursement window]. The refund date comes from Finances (finance pack P-ref-25).

---

## 3. Returned, but in a different state: dispositions, fault, ownership

**(a) Amazon's rule.**

*FBA Customer Returns report (overview)* (G200453320, v16 r0), as the listing pack read it on 2026-10-14 (listing pack's read): dispositions `SELLABLE`, `DAMAGED`, `CUSTOMER DAMAGED`, `DEFECTIVE`, `CARRIER DAMAGED`, `EXPIRED`; "`DAMAGED` and `CARRIER DAMAGED` read 'We take responsibility for the damage.' `DEFECTIVE` reads 'The unit is either obviously damaged, or the customer stated that it's faulty.'"

Gorilla ROI ("Amazon FBA Returns: What Every Condition Code Means", last updated 2026-05-07, read 2026-11-13) reproduces the table "Per the FBA Customer Returns report" in close paraphrase (copy, not verbatim): `DAMAGED` and `CARRIER_DAMAGED` "Amazon takes responsibility for the damage. Ownership transfers to Amazon. Amazon compensates you per the FBA inventory reimbursement policy"; `CUSTOMER_DAMAGED` "This does not mean the item itself is damaged. Opened packaging qualifies. Customer is refunded. Unit stays in your inventory as unsellable"; `DEFECTIVE` "Customer is refunded. Unit stays in your inventory as unsellable"; `EXPIRED` "within approximately 50 days of its expiration date". [opinion, as a copy of Amazon's table]

FBA Damaged Inventory Ownership (G9MAM9ELJTSSNYS5). PPC Land (Luís Rijo, 2025-08-18, read 2026-11-13) quotes Amazon's documentation (copy): the program "allows you to opt out of Amazon's damage-fault ownership evaluation process so that Amazon does not take ownership of and sell or remove your Amazon-fault damaged inventory through Amazon Resale (previously Amazon Warehouse), Liquidations, or other recovery or removal channels per the FBA inventory reimbursement policy"; "By participating in this program, you will retain ownership of enrolled Amazon-fault damaged inventory and determine the final removal decision as it is added to your unfulfillable inventory"; "Enrolled inventory will not be eligible for damage reimbursements per the FBA inventory reimbursement policy." The article adds, in its own words, that enrolled units are "marked as 'defective'", that the choice is per ASIN by CSV or for all ASINs, that recovered lost items stay outside the program, and that Amazon announced it on 2024-12-10 with effect from 2025-03-31. [copy for the three quotes; opinion for the rest]
- A seller (thread bf1c7ab1, US, 2025-03-17) quotes Selling Partner Support: "By enrolling in Damaged Inventory Ownership, you agree to be the damage-fault owner for enrolled damaged inventory; hence you will not be reimbursed for this inventory." Danny_Amazon (staff, 2025-03-21) answers that for an enrolled FBA account "the details from that page, and these terms and conditions would apply", linking G9MAM9ELJTSSNYS5 and GX9GZV9UGAAL4C58, and points seller-fulfilled orders to SAFE-T. (staff; support relayed)

Disputing a grade: the dispute needs the unit removed to the seller and is a removal claim (see removals-disposals RM11, RM12). The Australia News post d8f9a56c (2025-08-14, effective 2025-10-15) gives "Removal orders grading : 120 days from date item was removed from our fulfilment network". (News)

**(b) Practitioners.**
- Gorilla ROI spells the codes with underscores (`CUSTOMER_DAMAGED`, `CARRIER_DAMAGED`). For `DAMAGED` and `CARRIER_DAMAGED` it says: "If it is missing, you have an open claim", meaning no matching reimbursement row. [opinion]
- Lingxing's profit-report formula page (领星 "利润报表（新）公式核对", undated, read 2026-11-13) filters "DAMAGED、CARRIER_DAMAGED" for JP. [opinion; spelling evidence]
- PPC Land (above) dates Damaged Inventory Ownership to an announcement of 2024-12-10, effective 2025-03-31. [opinion]
- The seller who opened thread 70760af8 (US, 2023-10-06) describes Amazon labelling the retail box itself, which makes an unopened unit unsellable once the label is cut off. The staff reply restates policy and does not address it. [opinion]

**(c) Into a skill:** `DAMAGED` and `CARRIER DAMAGED` are graded as Amazon's responsibility and owed under the reimbursement policy. `CUSTOMER DAMAGED` and `DEFECTIVE` stay in the seller's unsellable inventory with no reimbursement, except where a grade is disputed, and a grade dispute needs the unit physically removed to the seller (removals-disposals). A seller enrolled in Damaged Inventory Ownership has given up damage reimbursement for the ASINs enrolled; cx cannot see the enrolment through the API.
**Read at run time:** `detailed-disposition` and `status` per row of `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`. The unfulfillable split from `getInventorySummaries` (`details=true`), held by the stock pack. Damaged Inventory Ownership enrolment cannot be read (Seller Central only; G9MAM9ELJTSSNYS5 as the seller sees it). The grading window from the store's removals-claims page (removals-disposals RM12).

---

## 4. Returned as something else: wrong item, empty box, swapped unit

**(a) Amazon's rule.**
- The contract covers a wrong item delivered (F-8.3, § 1). Amazon's evidence list for a removal claim, including a different product received in a removal, is homed in removals-disposals (RM14).
- Reason code `SWITCHEROO` is the buyer's "Amazon sent me the wrong item" (G200453320, listing pack's read). It is not a finding that the buyer swapped the unit.
- The policy redlines put the customer-return claim under "Post-Order Lost or Damaged Events" (PDF; § 12); its value is homed in value-and-reversals (VR27).

**(b) Practitioners.**
- Sellers on the US forum ("switcheroo FBA order return reimbursement claim", thread cd49634e, US, opened 2025-04-18) report switcheroo claims paid at sourcing cost, not refund minus fees. Seller_7oRqSa2nEp4id: "Every switcheroo claim I have done since April 1st has been reimbursed at the sourcing cost"; Seller_pAiS7b4evCQoa: "Every switcheroo claim is being reimbursed at sourcing cost". Support called it "the lost and damaged policy for pre order events". [opinion; two of the thread's five posters]
- Seller_iobipI6xASRkh (thread 76efc391, US, 2025-07-30) lists the photos as shipping label, packing slip, LPN sticker and the item at several angles; the LPN is matched to the order id through the returns report, and the reimbursement is "Cost of Goods not the retail price anymore". [opinion]
- A seller (thread bd2e5bba, US, 2023-07-25) reports support asking for an "LPN number image" on emptied-box returns; another seller shows the LPN sticker; Tatiana_Amazon (staff, 2023-09-07) only asks whether that answered it. [opinion; staff gave no rule]
- An older US thread (588390408669ce78defa82c839402b2c, 2020-02-03) gives a seller's recipe: find the order id through the LPN, file through the order-reimbursement path, attach images of the returned item, the LPN sticker and the return label. [opinion]
- Xander_Amazon (staff, reply of 2026-04-23 in "Large Scale FBA Returns Fraud", thread d781984a, US, opened 2026-04-14) told an FBA seller to "file SAFE-T claims" and use the Guided Refund Workflow "within the first 4 days of receiving the return". Both are seller-fulfilled mechanisms (finance pack P-ref-5, P-ref-11). [read in official docs, staff; contradicts the FBA terms]
- 百运网 ("买家恶意退货，亚马逊FBA卖家如何维权？", 2025-11-07) gives "退货发起后 30 天内" as the appeal limit, a figure on no Amazon page read. [opinion]
- Refunds Manager, SellerApp and other vendor pages list "wrong item returned" as a standard returns audit category. [opinion]

**(c) Into a skill:** on a wrong-item or empty-box return the unit is the evidence, so the claim follows the removal of that unit (removals-disposals RM14 for the evidence list). The order ↔ unit link is the LPN in the returns report. The value basis is value-and-reversals' (VR27, VR33); two US sellers report switcheroo claims paid at sourcing cost (one since 2025-04-01).
**Read at run time:** for the order ↔ LPN join, the LPN column and the order column in `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` (names from the file's header, § 9). For the removal's delivery date, `GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA` and `GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA` (removals area).

---

## 5. Replacements whose original was not returned

**(a) Amazon's rule.**
- The contract: Amazon may "ship a replacement Unit to the customer and reimburse you in accordance with the FBA Guidelines for the replacement Unit" (F-8.3), and "Any replacement Unit shipped by us under these FBA Service Terms will be deemed to be, and will be treated in the same manner as, an order and sale of such Unit from you to the customer" (F-8.4). (PDF, NA BSA)
- The claim clock counts from "the customer refund or replacement date" (News posts, § 2).
- The value is value-and-reversals' (VR27).

SP-API *FBA Reports* (updatedAt 2026-10-13, read 2026-11-13): `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA`, "Contains replacements that have been issued to customers for completed orders", "Amazon store availability: NA and Amazon IN stores", role Amazon Fulfillment only; attributes `shipment-date`, `sku`, `asin`, `fulfillment-center-id`, `original-fulfillment-center-id`, `quantity`, `replacement-reason-code`, `replacement-amazon-order-id`, `original-amazon-order-id`. (SP-API docs) Outside NA and IN, the orders read gives the link: Orders v0 `IsReplacementOrder` ("When true, this is a replacement order") and `ReplacedOrderId`; Orders v2026-01-01 `associatedOrders[].associationType` = `REPLACEMENT_ORIGINAL_ID` or `EXCHANGE_ORIGINAL_ID` [command-verified, ordersV0.json and orders_2026-01-01.json]. Orders v0 is deprecated and removed on 2027-03-27 (sp-api-claims-surface SU37).

The Chinese FBA FAQ says the original of a free replacement must reach the warehouse within 45 days (finance pack P-ref-37). Joey_Amazon says an unreturned replacement original is reimbursed under the customer-return policy (finance pack A9).

**(b) Practitioners.** Settlement and transaction files carry `FREE_REPLACEMENT_REFUND_ITEMS` as a reimbursement description (finance pack P-ref-33; Lingxing's formula page lists it among 35 FBA库存赔偿 descriptions). [opinion; value command-verified by the finance pack] Seller 365 lists "Refunded and Replaced (with no replacement sent/received)" as a claim type. [opinion]

**(c) Into a skill:** a replacement is a shipment the contract deems a sale; what is owed when the original is not returned runs on the customer-return clock counted from the replacement, valued as value-and-reversals states. The meaning of each `replacement-reason-code` value is not read here (see *Held*).
**Read at run time:** `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA` (NA, IN), or the orders read elsewhere. Matched against `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` by `original-amazon-order-id` = the returns report's order column, and against `GET_FBA_REIMBURSEMENTS_DATA` by `amazon-order-id`.

---

## 6. Refund above the sale, partial quantity, fees on a return

**(a) Amazon's rule.**
- Over-refund: no Amazon page read addresses a refund larger than the sale. The contract leaves the refund to Amazon and makes the seller pay "where we determine you have responsibility" (BSA F-8.2), with an appeal after notification. (PDF)
- The contract lets Amazon keep its fees on a replaced or refunded unit: "we will be entitled to retain the applicable fees" (F-8.3). (PDF)
- Seller-fulfilled restocking fees, the Guided Refund Workflow and the four-day automatic refund belong to the finance pack (P-ref-5, P-ref-7). The finance model's `RestockingFee` is "The charge that is applied to the buyer when returning a product in certain categories" (finance pack P-ref-7).

**(b) Practitioners.**
- Sellers on the EU forum report FBA refunds many times the order value, explained by support as a "goodwill gesture" or "concession from our customer service team", with no reimbursement: £94.98 on £9.99 (thread 9c7a8fe0, 2025-02-26), £52.50 on £2.99 (thread aad3a1bd, 2025-05-29), £150 on £16 (same thread 9c7a8fe0). [opinion]
- A US seller (thread 446cc0c9, 2025-03-26) reports a three-unit order refunded in full, one cent above the charge, with one unit returned "damaged" and reimbursed $0.00 and two units "non reimburse-able". [opinion]
- GETIDA, My Amazon Guy and others list "Return/Refund Overcharge" as a claim type. AMZBase (2026-09-07) states that a restocking fee charged to the buyer is credited to the seller. [opinion]
- Lingxing reads refunds from the transaction report's `Refund` rows (product sales, shipping credits, gift wrap credits, promotional rebates, selling fees, fba fees, other transaction fees), and the FBA returns-processing fee as `FBACustomerReturnPerUnitFee`. [opinion]

**(c) Into a skill:** the refund lines of an order are compared with its charge lines, item by item (finance pack P-ref-1, P-ref-22). Amazon's pages read give no rule that a refund above the charge is paid back; practitioners file it as a claim type and sellers report goodwill refunds refused, so whether one is owed stays open. The refund's quantity is compared with the returned quantity per order and SKU.
**Read at run time:** the refund lines from `listTransactions` (v2024-06-19) (finance pack P-ref-23; the settlement V2 flat file is removed, SU38). Returned quantity from `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`. For seller-fulfilled orders, `Order Amount` and `Refunded Amount` in `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE`, which needs a role outside the five (§ 10).

---

## 7. Returns accepted late, returnless refunds, and items that cannot be returned

**(a) Amazon's rule.**
- The buyer's windows: "In most cases, buyers can request to return an item within 30 days of receiving it. We may make case-by-case exceptions and accept return requests beyond 30 days of receipt" (G200379860 v24 r2, listing pack's read). No page read by a permitted route says what the seller gets when Amazon accepts a late return.
- Returnless refunds are absent from the FBA returns report: "At our discretion, we may give a refund without requiring that the customer return the item. These refunds don't appear in the FBA Customer Returns report" (G200453320, listing pack's read). FBA Returnless Resolutions refunds are the seller's choice and are not reimbursed (finance pack P-ref-8).
- The store-specific late-return and returnless-refund rules this file once quoted (JP, IN, GB, DE, US) are held (see *Held*).

**(b) Practitioners.** GETIDA's "Return after 60 Days" (a return granted outside the window) and Seller 365's "Returned Outside of the Return Window" are claim types. [opinion] Refunzo: sellers who opted into Returnless Resolutions "cannot claim … you agreed to that outcome". [opinion]

**(c) Into a skill:** a returnless refund leaves no row in the returns report. A returnless refund set by the seller's own rule is not owed. Whether a late-accepted return or an Amazon-granted returnless refund is owed is a store rule read at run time; this file holds no permitted read of it.
**Read at run time:** the store's *FBA customer returns policy* (G200379860) as the seller sees it. The buyer's return window per order cannot be read: no SP-API operation gives it. Whether the seller has Returnless Resolutions rules cannot be read either (finance pack P-ref-29).

---

## 8. Reimbursed, then the unit arrives: reversals and clawbacks on returns

**(a) Amazon's rule.** BSA F-8.4 (§ 1). The policy redlines: "If a reimbursement was made in error, or if a reimbursed item is later found and returned to your inventory, we reserve the right to reverse the reimbursement credit that was applied to your account" (PDF, US 2024-12-18 and 2025-02-24, not struck). The Reimbursements report's reversal columns and the dispute window are homed elsewhere (finance pack P-ref-18, P-ref-35; value-and-reversals VR20).

**(b) Practitioners.**
- Synder and Carbon6 read the settlement description `COMPENSATED_CLAWBACK` ("Reversal of previous refunds") as the take-back when a reimbursed unit is found or a refunded-not-returned unit arrives sellable. [opinion]
- SPS Commerce (2025-07-24): "be prepared for the possibility that returns could end up coming in late". [opinion]
- Lingxing lists `COMPENSATED_CLAWBACK` under 调整费用, separate from `REVERSAL_REIMBURSEMENT`. [opinion]

**(c) Into a skill:** a reimbursement for an unreturned unit is provisional. If the unit later returns sellable, Amazon may take it back (F-8.4; the policy's reversal sentence). Two names have been seen for the take-back, a reversal row in the Reimbursements report and `COMPENSATED_CLAWBACK` in transactions. Whether the seller's files show a return row (or ledger `CustomerReturns` event) for the order behind a take-back is a fact read from those files.
**Read at run time:** `GET_FBA_REIMBURSEMENTS_DATA` (`original-reimbursement-id`, `original-reimbursement-type`); `listTransactions` descriptions; `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` and `GET_LEDGER_DETAIL_VIEW_DATA` with `eventType` = `CustomerReturns` for the arrival.

---

## 9. The FBA Returns report: columns, values and pitfalls

**(a) Amazon's rule.**

SP-API *Fulfillment by Amazon (FBA) Reports* (https://developer-docs.amazon.com/sp-api/docs/report-type-values-fba.md, updatedAt 2026-10-13, read 2026-11-13), "FBA Returns Report", `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`. Roles: Pricing, Amazon Fulfillment. "Availability: FBA sellers". "This report can only be requested." "Tab-delimited flat file". "Contains customer returned items received at an Amazon fulfillment center, including Return Reason and Disposition. Content updated daily." Attributes: `return-date`, `order-id`, `sku`, `asin`, `fnsku`, `product-name`, `quantity`, `fulfillment-center-id`, `detailed-disposition`, `reason`, `status`, `license-plate-number`, `customer-comments`. (SP-API docs)

Help page G200453320 v16 r0, as the listing pack read it on 2026-10-14 (listing pack's read): `return-date` "Date returned merchandise was processed at the fulfillment center"; `reason` "Short description of reason for return as indicated by the customer"; `customer-comments`; "The disposition column ('Condition of the returned item')"; `status`; `lpn`. The 33 reason codes with Amazon's descriptions are in the listing pack (returns.md).

Return status values. Gorilla ROI (2026-05-07) gives "the exact status values from Amazon's documentation" (copy): "Unit returned to inventory" ("Unit has been returned to your sellable or unsellable inventory"); "Reimbursed" ("A reimbursement has been approved for the unit. The unit has not been returned to your inventory. Allow 5 days for the reimbursement to post."); "Pending repackaging"; "Repackaged successfully"; "To be autoremoved"; "Immediate disposal"; "Immediate donation"; "Immediate liquidation"; "Policy-related disposal" ("Unit was disposed per product health, safety, or regulatory policies"). Openbridge (FBA Customer Returns Report, 2024-02-15, re-read 2026-11-13) gives the first four as "Unit Returned to Inventory", "Reimbursed" ("please allow 5 days for reimbursements to post"), "Pending Repackaging", "Repackaged Successfully". [copy; the two copies differ in capitalisation]

The SP-API removal shipment report lists no LPN column (`request-date`, `order-id`, `shipment-date`, `sku`, `fnsku`, `disposition`, `shipped-quantity`, `carrier`, `tracking-number`, `shipment-status (IN store only)`, `removal-order-type`). (SP-API docs, FBA Reports 2026-10-13)

**(b) Practitioners.**
- Openbridge (2024-02-15) gives the download header as `amazon-order-id` and `lpn`. [opinion; listing pack]
- Gorilla ROI (2026-05-07) gives dispositions with underscores and spells one status two ways ("To be autoremoved" / "To be auto-removed"). [opinion]
- Lingxing counts returns by `return-date`, filters status per store: "IN、AE、SG、SA、BR：不过滤状态", JP excludes `DAMAGED、CARRIER_DAMAGED`, and other stores keep "Unit returned to inventory、Repackaged Successfully、IMMEDIATE_DISPOSAL、IMMEDIATE_DONATION、IMMEDIATE_LIQUIDATION". So some files carry status values in UPPER_SNAKE form. [opinion]

**(c) Into a skill:** the report is a list of units received. A refund that has no row is a unit not yet received, a returnless refund, or a unit lost. `return-date` is the processing date at the FC, not the refund date and not the claim clock. Column names, disposition spellings and status names are read from the header and values of the seller's own file; the SP-API page, the help page as read by the listing pack and practitioners' files disagree on them.
**Read at run time:** the header line and distinct `detailed-disposition` / `status` values of the seller's own `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` file. How a report is requested belongs to the door (cx-amazon-sp-api skills/amazon-sp-api/references/door.md); the maximum date range per request is not stated on the SP-API page (sp-api-claims-surface SU16).

---

## 10. Seller-fulfilled returns: what a claims skill adds to the finance pack

SAFE-T, A-to-z and chargebacks belong to the finance pack (P-ref-5, P-ref-9..11, P-ref-41). This area adds two things.

**(a) Amazon's rule.** SP-API *Returns Reports* (https://developer-docs.amazon.com/sp-api/docs/report-type-values-returns.md, updatedAt 2026-10-28, read 2026-11-13) lists for `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE`: "Order ID, Order date, Return request date, Return request status, Amazon RMA ID, Merchant RMA ID, Label type, Label cost, Currency code, Return carrier, Tracking ID, Label to be paid by, A-to-Z Claim, Is prime, ASIN, Merchant SKU, Item Name, Return quantity, Return Reason, In policy, Return type, Resolution, Invoice number, Return delivery date, Order Amount, Order quantity, SafeT Action reason, SafeT claim id, SafeT claim state, SafeT claim creation time, SafeT claim reimbursement amount, Refunded Amount, Order Item ID". It caps a request's date range (value in *Values that move*). Roles: Inventory and Order Tracking, Direct to Consumer Shipping (Restricted). (SP-API docs) Neither role is among the five roles of the seller's app, so this report is not readable through it (see sp-api-claims-surface § 2.1, the report table's row for this type).

**(b) Practitioners.** None beyond the finance pack.

**(c) Into a skill:** the SAFE-T clock runs from the later of the return delivery scan and the refund (P-ref-11). `Return delivery date` and the refund date sit in the seller's own files, and `Refunded Amount` against `Order Amount` shows a refund above the sale; whether a claim was filed and how it stands is in the `SafeT claim …` columns. Through the seller's app these columns are out of reach: the refund lines come from `listTransactions` instead (finance pack). MCF orders are the seller's to refund (BSA F-6.1, F-6.4), so they fall outside the FBA customer-return claim.
**Read at run time:** whether the seller's app holds Inventory and Order Tracking (sp-api-claims-surface); without it, `listTransactions` refund lines. Amazon's page *Reimbursement for seller-fulfilled orders* (G202188810) for the window, as the seller sees it.

---

## 11. Automatic reimbursement of returns: what it covers and when it posts

**(a) Amazon's rule.** The automation announcements and their dates per store are homed in fc-lost-damaged § 2a; the finance pack holds the programme (P-ref-13). This area adds:
- The 2024 announcements name customer returns: "Almost all reimbursement claims related to warehouse lost and damaged and customer returns cases will now be proactively reimbursed. However, if you do not receive an automatic reimbursement … you will need to file a manual claim." (News 81c3235d US; 6605eede CA; d0fc997e UK)
- Automatic reimbursement of unreturned refunds is older than that programme: Veronica_Amazon (US, 2023-10-13) states "in most cases we'll charge the customer and reimburse you".
- The status "Reimbursed" means "allow 5 days for the reimbursement to post" (Gorilla and Openbridge copies of G200453320, § 9). The Reimbursements report's own posting delay is the finance pack's (P-ref-17).
- Where a claim starts: the route is homed in filing-and-conduct (FL4). The two staff statements, dated: Christine_Amazon (Canada, 2025-03-24): "If customer-related defects show up in the Eligible for claim tab of the portal, you can file a claim by entering the required information, such as the order ID, FNSKU, and quantity. If you disagree with the resolution decision, you can appeal by submitting a claim via the Resolved tab"; Indy_Amazon (US, 2026-08-13): "Use the Check FBA order reimbursement status tool. Enter the customer Order ID to check eligibility and file". (staff)

**(b) Practitioners.** GETIDA reports, from its own sample, that Amazon pays almost all FBA customer-return issues within about two months (finance pack P-ref-31). [opinion] Refunzo says the automation "frequently misses cases". [opinion]

**(c) Into a skill:** the claim starts from the customer order id. Amazon's stated rule reimburses a refunded unit not returned within the store's days "in most cases"; an order whose refund has no return row and no reimbursement row after those days is one that rule describes. The IDR portal's tabs and the order-reimbursement tool are Seller Central only (filing-and-conduct FL4).
**Read at run time:** `GET_FBA_REIMBURSEMENTS_DATA` (`amazon-order-id`, `reason` `CustomerReturn` / `CustomerServiceIssue`, finance pack P-ref-35).

---

## 12. Units lost or damaged outbound: after the order, before delivery

**(a) Amazon's rule.**
- The contract. F-8.3: "where the wrong item was delivered or the item was damaged or lost or is missing", unless caused by the seller, Amazon at its option ships a replacement "and reimburse[s] you in accordance with the FBA Guidelines for the replacement Unit", or processes a refund "and reimburse[s] you in accordance with the FBA Guidelines for the Unit"; it keeps "the applicable fees". (PDF, NA BSA 2019, not struck [command-verified]; AU BSA 2023 has the same clause with "wrong item was shipped")
- The policy. The redlines insert (red, underlined, so live from 2025) "We calculate reimbursement value based on whether the item was lost or damaged before or after it was ordered by the end customer", with two headings, "Pre-Order Lost or Damaged Events" and "Post-Order Lost or Damaged Events" [command-verified: rendered US 2024-12-18 and 2025-02-24]. Under the post-order heading the only claim named is "a customer return claim", and the policy's list of claim kinds is "Shipment to Amazon claims", "Fulfillment center operations claim", "Customer return claims", "Removals claims". (PDF) No Amazon text read names a separate claim kind for a unit lost or damaged on its way to the buyer; that such a unit is handled as a customer-return case (the buyer is refunded or replaced and the unit is not returned) is [inferred] from the post-order heading and F-8.3.
- The value of a post-order loss is homed in value-and-reversals (VR27, VR31; finance pack P-ref-14).
- The report. `Lost_Outbound` and `Damaged_Outbound` are `reason` values seen in public Reimbursements reports (finance pack P-ref-35). No SP-API model in the clone names them [command-verified: grep of the models at db2936aa]; no Amazon page read defines them.
- Automation: the 2024 posts name "customer returns cases" as proactively reimbursed (§ 11); none names outbound losses.

**(b) Practitioners.**
- Seller 365 (undated, read 2026-11-13) defines "Lost Outbound": "situations where a shipment, after leaving an Amazon fulfillment center, goes missing and is never delivered to its intended recipient. This applies to direct customer orders, as well as lost removal orders where inventory is supposed to be shipped back to the seller." It counts lost removal shipments in the same class; the pack homes those in removals-disposals. [opinion]
- Sellers of non-returnable FBA food items (thread c0d7f362, US, opened 2026-03-13) report that buyers who select "damaged during transit" are refunded with no proof and keep the item, that frontline support denies reimbursement because the item is non-returnable, and that "whenever I ask for the case to be escalated to a specialist team, the reimbursement is approved". A second seller reports the same for a Handmade item. No Amazon reply appears in the thread [command-verified: no `_Amazon` poster among its posts]. [opinion]
- Lingxing and others treat outbound reasons as FBA库存赔偿 lines (finance pack P-ref-33). [opinion]

**(c) Into a skill:** a unit lost, damaged or wrong on its way to the buyer is Amazon's under F-8.3 unless the seller caused it, and Amazon reimburses "in accordance with the FBA Guidelines". The policy text read files it under post-order events; no separate outbound claim kind is named. On the seller's files it shows as a refund or replacement with no return row and, when paid, a reimbursement row whose `reason` is an outbound value. Practitioners report that a non-returnable item refunded for transit damage is denied at first contact and paid on escalation; that is a report, not a rule.
**Read at run time:** `GET_FBA_REIMBURSEMENTS_DATA` rows with an outbound `reason` (the values from the seller's file, not from a list held here); refunds and replacements from `listTransactions` and the replacements report or orders read (§ 5); `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` for the absence of a return row. Shipping API `createClaim` files a carrier claim, not an FBA reimbursement (sp-api-claims-surface SU13).

---

## 13. Wrong-FNSKU and commingled returns; returns credited to another seller

**(a) Amazon's rule.**
- Commingling and its end are homed in inbound-shortfalls (§ I, IN24). The definition, from the News post (UK thread 06778c12, store `A1F83G8C2ARO7P`; Canada thread cd352647, `A2EUQ1WTGCTBG2`; both posted 2025-12-08): "Commingling is when we fulfil customer orders using exact product matches from the closest available inventory in the Amazon fulfilment network, even if that inventory belonged to a different seller". (News)
- No Amazon page read says to whose inventory a returned commingled unit is credited, or names a claim kind for a return received under another FNSKU or credited to another seller.
- The returns report carries `sku` and `fnsku` per row beside the order column (SP-API docs, § 9).

**(b) Practitioners.**
- GETIDA lists "Wrong FNSKU Returns" among its claim types (finance pack, sellers-tools-and-research, GETIDA row). Helium 10 lists "incorrect FNSKU returns" (finance pack research/areas/refunds-reimbursements-adjustments.md, vendor table, Helium 10 row). Seller 365 lists "Returned Different FNSKU than Ordered" (read 2026-11-13). [opinion] The finance pack sums the vendors' view that automation misses "returned units of the wrong FNSKU or empty boxes". [opinion]
- A US seller (thread 588390408669ce78defa82c839402b2c, 2020-02-03) holds that "The fulfillment center can mix up products on accident" or the buyer may mix two items, and files these as wrong-item returns with the LPN. [opinion]
- PPC Land (2026-03-24, cited by inbound-shortfalls IN25) holds that ending commingling improves seller-specific traceability. [opinion]

**(c) Into a skill:** a return row whose `sku` or `fnsku` differs from what the order shipped is the case vendors file as a wrong-FNSKU return [inferred: Amazon names no such kind]. Before 2026-03-31 a stickerless unit could have been another seller's on the outbound side, and Amazon states no rule for the return side. A return credited to another seller has no Amazon rule read and no field that shows it in the seller's own files; it would appear only as a refund with no return row (§ 9, § 11).
**Read at run time:** the returns report's `sku`, `fnsku` and order column against the order's items (Orders read) and the seller's label choice per SKU (inbound-shortfalls § I, `labelOwner`).

---

## 14. Cross-border returns: Remote Fulfillment (NA) and EFN (Europe)

**(a) Amazon's rule.**
- Remote Fulfillment with FBA (sell.amazon.com, "Remote Fulfillment with FBA", read 2026-11-13): "As we do with FBA in the US, we'll handle returns and customer service for Remote Fulfilment with FBA orders. Returns will be sent back to the US and are subject to the FBA customer returns policy". (sell.amazon)
- Return-fee credits (News c61a5494, store US, posted 2025-03-10): "Starting March 25, 2025, we'll provide you with credits to cover return fees for items that are sold and returned through Remote Fulfillment with FBA in the Mexico and Brazil stores. … We'll automatically issue credits within 30 days after a return. To view your credit, go to your Transaction view. If you receive a credit, you'll see 'Refund' in 'Transaction type' and 'Remote Fulfillment credit' in 'Transaction details'." TaylorR_Amazon restated it (thread 076624df, 2025-03-27). (News; staff) The post links a *Customer returns* page (G5P3CDUHZWSZLXLB), unread.
- A seller (thread ce526b12, US, 2025-02-17) quotes the Remote Fulfillment policy: "The FBA return processing fees on the US FBA policy don't apply to Remote Fulfillment. Remote Fulfillment with FBA doesn't charge FBA return fees in any category", and reports being charged the fee; Bryce_Amazon (staff, 2025-03-06) asked for the case. [opinion, relayed policy]
- EFN between the UK and the EU (Amazon PDF *The European Fulfilment Network between the UK and the EU*, "Updated as of January 2022", created 2022-05-19), FAQ 4: "Where are the items going to be returned? The items will be sent to the source store." The same FAQ: the network "is only available for the arcs between UK and Germany, France, Italy and Spain". (PDF)
- No Amazon page read states the store or currency in which a customer-return reimbursement on a cross-border order posts. Currency is homed in value-and-reversals.

**(b) Practitioners.**
- Sellers on the UK forum report EFN and Remote Fulfilment returns landing in other EU fulfilment centres instead of the source store: thread e4406a7a (2024-08-19, 2024-08-22), thread 9fe56ee3 (2023-02-15: "They are supposed to return to the home marketplace, but will likely pass through an EU Amazon location. Sometimes they get stuck there"), and a reply of 2025-05-30 in thread 40c2c288 reporting storage fees charged on returns stranded in EU sites "that we have no access to". [opinion]

**(c) Into a skill:** a Remote Fulfillment return goes back to the US and is governed by the US FBA customer-returns policy, so its claim follows the US rules of §§ 1–2. Amazon credits the return fee on Remote Fulfillment returns in Mexico and Brazil from 2025-03-25, posting a "Remote Fulfillment credit" line; a charged fee with no credit is a fee question (fee-overcharges). EFN returns are meant to go to the source store; sellers report otherwise. Which store's claim rules and currency apply to a cross-border return's reimbursement is not stated in any page read.
**Read at run time:** `listTransactions` lines with transaction details "Remote Fulfillment credit" against the order's return fee; the order's `marketplaceId` and the return row's `fulfillment-center-id`; the reimbursement row's `currency-unit` (value-and-reversals).

---

## Values that move

A value that differs by store or year is not part of a position. Each row gives the store, the date read and the source.

| Value | Store | Value as read | Source and route | Date read |
|---|---|---|---|---|
| Customer-return claim window | US | 60–120 days after refund or replacement; not before 60; effective 2024-10-23 | News 81c3235d (`ATVPDKIKX0DER`), posted 2024-07-24 | 2026-11-13 |
| Same | US | no sooner than 60 days after the refund, within 18 months | Indy_Amazon 0e07abc1 (US), 2026-08-13 (staff) | 2026-11-13 |
| Same | Canada | 45–105 days; not before 45; effective 2024-10-23 | News 6605eede (`A2EUQ1WTGCTBG2`), posted 2024-07-24 | 2026-11-13 |
| Same | Canada | 60–120 days | Christine_Amazon 02bebf51 (Canada), 2025-03-24 (staff) | 2026-11-13 |
| Same | UK | 45–105 days, from 2025-01-09 | News d0fc997e (`A1F83G8C2ARO7P`), 2024-10-10; News 9a92846d (UK), 2025-01-15 | 2026-11-13 |
| Same | Sweden | 45–105 days | News 1101821c (`A2NODRKZP88ZB9`), 2025-01-15 | 2026-11-13 |
| Same | Australia | 45–105 days, from 2025-10-15 | News d8f9a56c (`A39IBJ37TRP1C6`), 2025-08-14 | 2026-11-13 |
| "Not returned" days before Amazon charges the buyer and reimburses | US | 60 days of the refund | Veronica_Amazon 70760af8 (US), 2023-10-13; Indy_Amazon 2026-08-13 (staff) | 2026-11-13 |
| Same | Canada | 60 days | Christine_Amazon 2025-03-24 (staff) | 2026-11-13 |
| Appeal against a finding of seller responsibility | NA (2019 text); AU (2023) | within thirty (30) days after Amazon's notification | BSA F-8.2 (PDF) | 2026-11-13 |
| Removal grading-dispute window | Australia | 120 days from the date the item was removed | News d8f9a56c; other stores in removals-disposals RM12 | 2026-11-13 |
| "Reimbursed" status posting allowance | — | 5 days | Gorilla ROI and Openbridge copies of G200453320 | 2026-11-13 |
| Seller-fulfilled returns report, date range per request | all | "up to 60 days of data in a single report" | SP-API *Returns Reports*, updatedAt 2026-10-28 | 2026-11-13 |
| Damaged Inventory Ownership, ASINs per CSV | US | 10,000 | PPC Land (copy), 2025-08-18 | 2026-11-13 |
| Remote Fulfillment return-fee credit | Mexico, Brazil (US sellers) | from 2025-03-25; issued within 30 days of a return | News c61a5494 (US), 2025-03-10 | 2026-11-13 |
| Commingling end | UK, Canada posts | inventory shipped on or after 2026-03-31 | News 06778c12, cd352647 (inbound-shortfalls IN24) | 2026-11-13 |
| Seller-fulfilled restocking window (staff advice to an FBA seller) | US | "within the first 4 days of receiving the return" | Xander_Amazon d781984a, 2026-04-23 (staff) | 2026-11-13 |

---

## Corrections to other packs

1. **Finance pack P-ref-16 / § F (windows): incomplete.** It omits the News post 81c3235d (posted 2024-07-24T19:49:56.298Z, "between 60-120 days … Claims must not be submitted before 60 days"), posted beside 6605eede. Read by the post's `marketplaceId`, 81c3235d is the US issue and 6605eede the Canada issue [command-verified]; the 45–105 posts read are Canada, UK, Sweden and Australia. P-ref-16's 45–105 stands for those stores, not for the US. Evidence: the posts' `marketplaceId` fields, read 2026-11-13; fc-lost-damaged § 2a.
2. *(withdrawn: rested on a barred route.)* The earlier correction to finance pack P-ref-3 (fulfilment fee on a return) quoted G200379860 through the help hub's content call. P-ref-3 stands as the finance pack has it.
3. *(withdrawn: rested on a barred route; the home is value-and-reversals.)* The earlier correction to finance pack P-ref-37 / P-ref-40 quoted G200213130 v47 through the content call. The permitted-route correction to P-ref-40 is value-and-reversals' correction 1 (rendered redlines).
4. **Finance pack E1, "If a customer returns … within 60 days" (staff) vs "45 days" (relayed).** Re-sourced: the staff 60 days is a US post (Veronica_Amazon's thread 70760af8 carries `marketplaceId` `ATVPDKIKX0DER`, though it is served on the EU forum host too), and a Canada staff post also says 60 while the Canada News post opens the claim window at 45. The figures belong to different posts and stores; neither is "relayed" against "staff". Evidence: thread 70760af8, 02bebf51, 6605eede.
5. **Stock pack stuck-stock.md D4 ("The page lists no values for `detailed-disposition`, `reason` or `status`").** The listing pack's read of G200453320 v16 (2026-10-14) lists the dispositions and reasons, and the status values are carried by two third-party copies of that page (Gorilla ROI 2026-05-07; Openbridge 2024-02-15). The D8 part of the earlier correction (the 30-day removal rule) is withdrawn: it rested on a barred route.
6. *(withdrawn: rested on a barred route.)* The earlier correction to stock pack D12 quoted G9MAM9ELJTSSNYS5 through the content call; D12 stands as the stock pack has it.
7. **Finance pack E5 (Ezra_Amazon: disabling returns evaluation marks all returns defective).** Consistent with Amazon's text as PPC Land copies it (enrolled Amazon-fault damaged units stay with the seller and "will not be eligible for damage reimbursements"), with Selling Partner Support's reply relayed in thread bf1c7ab1 (2025-03-17) and Danny_Amazon's reply (2025-03-21). The per-ASIN CSV and its size are PPC Land's wording, not a read of Amazon's page.

Note to a sibling file in this pack (not edited here): fc-lost-damaged § 9 says thread c0d7f362 holds "An Amazon reply"; the thread as fetched on 2026-11-13 has no post by an Amazon account (§ 12).

---

## Positions

- **RT1.** On an FBA order Amazon refunds or replaces on the seller's behalf and debits the seller. It reimburses when the unit is not returned within the store's set number of days of the refund ("in most cases"), or returns unsellable through Amazon's fault. A unit back sellable is restocked with no money. Sources: Veronica_Amazon 70760af8 (US, 2023-10-13), Indy_Amazon 0e07abc1 (US, 2026-08-13), Christine_Amazon 02bebf51 (Canada, 2025-03-24) [read in official docs, staff]; BSA F-8.2–F-8.4 (PDF) [read in official docs].
- **RT2.** Reimbursement decisions follow the unit's physical condition as evaluated at the fulfilment centre, not the buyer's chosen reason. Source: G200379860 v24 r2 (listing pack's read, 2026-10-14) [read in official docs].
- **RT3.** Not reimbursed on a customer return: units damaged by the customer, recalled, defective or in violation of Amazon policies, and refunds the seller issued directly. The UK policy adds conditions it does not reimburse: damaged box or packaging, missing factory seal, missing packaging, tape or shipping label over the box, and a different box. Sources: Veronica_Amazon (US, 2023-10-13), Christine_Amazon (Canada, 2025-03-24) [read in official docs, staff]; UK policy redlines 2024-12-11 and 2025-02-24, sentence not struck (PDF) [read in official docs; render command-verified].
- **RT4.** The customer-return claim window is counted from the customer refund or replacement date. Amazon refuses a claim filed before the window opens or after it closes. The day counts differ by store and Amazon's posts disagree, so the window is read per store at run time on the store's *Customer return claims* page (G9N934L7Y4SFWPJ4) as the seller sees it and in the latest News post for that store. The values read on 2026-11-13 are in *Values that move*. Sources: News 81c3235d, 6605eede, d0fc997e, 9a92846d, 1101821c, d8f9a56c [read in official docs].
- **RT5.** On 2024-07-24 Amazon posted the same announcement twice, 0.7 seconds apart: the US issue (81c3235d) gives customer-return claims one window and the Canada issue (6605eede) another, both effective 2024-10-23. Sources: both posts' `datePublished` and `marketplaceId` [read in official docs; store command-verified; the field-equals-store reading is shared with fc-lost-damaged § 2a].
- **RT6.** Amazon's statements of the window conflict with one another: in Canada the News post and a staff post give different windows; in the US the News post gives a fixed end and a 2026 staff post an 18-month end. Which one a claim form enforces is open. Sources: 6605eede, 02bebf51, 81c3235d, 0e07abc1 [read in official docs].
- **RT7.** Chinese media (卖家之家 2025-01-24; AMZ123 2025-01-19) reported a US move to the 45–105 window announced about 2025-01-16. No US post read carries it; the posts of 2025-01-15 with that window are the Sweden and UK issues. Sources: those articles [opinion]; 1101821c, 9a92846d, 81c3235d [read in official docs]; that the articles read a non-US post is [inferred].
- **RT8.** The "not returned" days (after which Amazon in most cases charges the buyer and reimburses the seller) are set per store and read at run time on the store's *Customer return claims* page as the seller sees it. US and Canada staff posts state a value (in *Values that move*); no permitted read gives the other stores'. Sources: Veronica_Amazon (thread 70760af8, store US), Indy_Amazon, Christine_Amazon [read in official docs, staff; store command-verified].
- **RT9.** `DAMAGED` and `CARRIER DAMAGED` are graded as Amazon's responsibility ("We take responsibility for the damage"; ownership passes to Amazon and the unit is compensated under the reimbursement policy). `CUSTOMER DAMAGED` and `DEFECTIVE` leave the unit in the seller's unsellable inventory. `CUSTOMER DAMAGED` can mean only opened packaging. Sources: G200453320 v16 (listing pack's read) [read in official docs]; Gorilla ROI 2026-05-07 [copy of Amazon's table; opinion].
- **RT10.** *(withdrawn: rested only on a barred route; see Held.)*
- **RT11.** A seller enrolled in FBA Damaged Inventory Ownership keeps enrolled Amazon-fault damaged inventory in its unfulfillable stock and decides its removal, and that inventory "will not be eligible for damage reimbursements". The enrolment's scope (all ASINs or a list) is read on G9MAM9ELJTSSNYS5 as the seller sees it. No SP-API read shows the enrolment. Sources: PPC Land 2025-08-18 [copy of Amazon's text]; Selling Partner Support relayed in thread bf1c7ab1 (2025-03-17) [opinion, relayed]; Danny_Amazon 2025-03-21 [read in official docs, staff]; models clone [command-verified: no operation names the setting].
- **RT12.** *(withdrawn: rested only on a barred route; see Held.)*
- **RT13.** A grade dispute on a customer return (customer damaged or defective) needs the unit removed to the seller and is a removal claim; its window is removals-disposals' (see removals-disposals RM11, RM12). The Australia post's value is in *Values that move*. Source: News d8f9a56c [read in official docs].
- **RT14.** *(withdrawn: rested only on a barred route; see Held.)*
- **RT15.** *(withdrawn: rested only on a barred route; see Held.)*
- **RT16.** For a wrong item or empty box returned, the unit is the evidence and the claim follows its removal; Amazon's evidence list for a removal claim is removals-disposals' (see removals-disposals RM14). Sellers report support asking for an image of the LPN label. Sources: RM14; threads bd2e5bba (2023-07-25), 588390408669ce78defa82c839402b2c (2020), 76efc391 (2025-07-30) [opinion].
- **RT17.** Sellers report US wrong-item ("switcheroo") claims paid at sourcing cost (one dates it from 2025-04-01), although Amazon's policy puts the customer-return claim under "Post-Order Lost or Damaged Events", whose value is value-and-reversals' (VR27). Sources: threads cd49634e (2025-04-18; two of five posters), 76efc391 (2025-07-30) [opinion]; US policy redlines 2024-12-18 and 2025-02-24, heading inserted (PDF) [read in official docs; render command-verified].
- **RT18.** The reason code `SWITCHEROO` is the buyer's claim "Amazon sent me the wrong item", not Amazon's finding that the buyer swapped the unit. Source: G200453320 v16 (listing pack's read) [read in official docs].
- **RT19.** Amazon may settle a lost, damaged, missing or wrong unit by shipping a replacement and reimbursing the seller "for the replacement Unit"; the replacement is deemed a sale from the seller to the customer. A claim for an unreturned original runs on the customer-return clock counted from the replacement date; its value is value-and-reversals' (VR27). Sources: BSA F-8.3, F-8.4 (PDF); News 81c3235d ("customer refund or replacement date") [read in official docs].
- **RT20.** `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA` covers only NA and IN stores and needs the Amazon Fulfillment role. Elsewhere the link from a replacement to its original is Orders v0 `IsReplacementOrder` / `ReplacedOrderId` (deprecated; sp-api-claims-surface SU37) or Orders v2026-01-01 `associatedOrders` with `REPLACEMENT_ORIGINAL_ID`. Sources: FBA Reports (2026-10-13) [read in official docs]; ordersV0.json, orders_2026-01-01.json [command-verified].
- **RT21.** The SP-API names the replacements report's columns, including `replacement-reason-code`, `replacement-amazon-order-id` and `original-amazon-order-id`. The meaning of each reason code is not read by a permitted route (see Held). Source: FBA Reports (2026-10-13) [read in official docs].
- **RT22.** *(withdrawn: rested only on a barred route; see Held.)*
- **RT23.** *(withdrawn: rested only on a barred route; see Held. The restocking fee's posting line is finance pack P-ref-7.)*
- **RT24.** No Amazon page read provides for repaying a refund above the order's charge. The contract leaves refunds to Amazon and makes the seller pay where Amazon finds the seller responsible. Sellers report FBA refunds of several times the order value called "goodwill" or a "concession" and refused for reimbursement (EU forum 2025); recovery services list "refund overcharge" as a claim type. Sources: BSA F-8.2 (PDF) [read in official docs]; threads 9c7a8fe0, aad3a1bd [opinion]; GETIDA, My Amazon Guy [opinion].
- **RT25.** *(withdrawn: rested only on a barred route; see Held.)*
- **RT26.** *(withdrawn: rested only on a barred route; see Held.)*
- **RT27.** *(withdrawn: rested only on a barred route; see Held. The returnless-refund facts that stand are RT32 and finance pack P-ref-8.)*
- **RT28.** *(withdrawn: rested only on a barred route; see Held.)*
- **RT29.** Under the FBA Service Terms Amazon decides refunds on FBA units and notifies the seller when it holds the seller responsible; the seller may appeal within a period counted from that notification (in Australia also ask for the unsuitable unit back for inspection). The period is set in F-8.2 of the store's BSA (value in *Values that move*). Sources: NA BSA redline (2019) and AU BSA (2023), F-8.2 (PDF) [read in official docs; appeal sentence inserted in the 2019 redline, render command-verified].
- **RT30.** Under the FBA Service Terms, if a refunded or replaced unit comes back sellable and Amazon restocks it, the seller repays its Replacement Value. With the policy's reversal sentence, this is the basis for taking back a returns reimbursement. Sources: BSA F-8.4 (PDF); US policy redlines, reversal sentence not struck (PDF) [read in official docs].
- **RT31.** Practitioners name the transaction description `COMPENSATED_CLAWBACK` ("Reversal of previous refunds") as Amazon taking back a reimbursement when a unit is found or a return arrives sellable. Amazon publishes no definition read here. Sources: Synder, Carbon6, SPS Commerce, Lingxing [opinion].
- **RT32.** `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` lists only units received at an FC, updated daily, request-only, tab-delimited, roles Pricing or Amazon Fulfillment. A refund given without a return is never in it. Sources: FBA Reports (2026-10-13) [read in official docs]; G200453320 v16 (listing pack's read) [read in official docs].
- **RT33.** `return-date` in the returns report is "Date returned merchandise was processed at the fulfillment center", not the refund date; the claim clock counts from the refund or replacement. Sources: G200453320 v16 (listing pack's read); News 81c3235d [read in official docs].
- **RT34.** The returns report's column names differ by source: the SP-API page has `order-id` and `license-plate-number`; the help page as the listing pack read it and Openbridge's copy have `lpn`, and Openbridge has `amazon-order-id`. cx reads the header of the seller's file. Sources: FBA Reports; G200453320 (listing pack's read) [read in official docs]; Openbridge [opinion].
- **RT35.** Disposition values are written with a space on Amazon's help page as the listing pack read it (`CUSTOMER DAMAGED`) and with an underscore in a practitioner's copy (`CUSTOMER_DAMAGED`). Status values appear in sentence case in two copies of Amazon's page, with different capitalisation, and partly UPPER_SNAKE in one ERP's filters (`IMMEDIATE_DISPOSAL`). cx reads the values from the file. Sources: G200453320 (listing pack's read) [read in official docs]; Gorilla ROI, Openbridge, Lingxing [opinion].
- **RT36.** Return status "Reimbursed" means a reimbursement was approved and the unit was not added to inventory, with a stated posting allowance (value in *Values that move*). The Reimbursements report's own delay is finance pack P-ref-17's. Sources: Gorilla ROI and Openbridge copies of G200453320 [copy; opinion].
- **RT37.** The returns report carries the LPN of each returned unit, which ties a unit later removed to the seller back to its row and order. The SP-API removal shipment report has no LPN column. Sources: FBA Reports; G200453320 (listing pack's read) [read in official docs]; Openbridge [opinion].
- **RT38.** The returns report's `reason` is chosen by the buyer from a list; Amazon's 33 codes and descriptions are held by the listing pack. Source: G200453320 (listing pack's read) [read in official docs].
- **RT39.** The seller-fulfilled `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE` carries `Order Amount`, `Refunded Amount`, `Return delivery date`, `A-to-Z Claim` and five `SafeT …` columns, with a capped date range per request (value in *Values that move*). Its roles, Inventory and Order Tracking or Direct to Consumer Shipping (Restricted), are both outside the five roles of the seller's app (see sp-api-claims-surface § 2.1). Source: Returns Reports (updatedAt 2026-10-28) [read in official docs].
- **RT40.** No SP-API notification announces an FBA customer return's receipt or grading. Source: notification schemas in the models clone at db2936aa (26 schema files; none names an FBA customer return or a disposition) [command-verified]. `SHIPMENT_TRACKING_MILESTONE_CHANGED` carries a milestone `RETURN_RECEIVED` ("The returns facility received the return shipment"), a carrier-tracking milestone whose scope its schema does not tie to FBA customer returns; that it does not cover them is [inferred].
- **RT41.** *(withdrawn: the claim route is homed in filing-and-conduct; see filing-and-conduct FL4. The two dated staff statements are in § 11 as evidence.)*
- **RT42.** *(withdrawn: the valuation and its dispute window are homed in value-and-reversals; see value-and-reversals VR27, VR20. The live-page wording it quoted rested on a barred route; see Held.)*
- **RT43.** An Amazon moderator told an FBA seller to use SAFE-T and the Guided Refund Workflow for materially different returns (reply of 2026-04-23). Both are seller-fulfilled programmes, so this staff reply is not a rule source for FBA. Sources: Xander_Amazon, thread d781984a [read in official docs, staff]; finance pack P-ref-5, P-ref-11.
- **RT44.** MCF units are the seller's to refund and return. If Amazon receives an MCF return, the seller directs return or disposal at its own cost, so MCF returns are outside the FBA customer-return claim. Source: NA BSA F-6.1, F-6.4 (PDF; AU BSA the same) [read in official docs].
- **RT45.** *(withdrawn: rested only on a barred route; see Held.)*
- **RT46.** Where an FBA unit is lost, damaged, missing or the wrong item is delivered to the buyer, Amazon, unless the seller caused it, replaces or refunds at its option and reimburses the seller "in accordance with the FBA Guidelines", keeping its fees. Sources: NA BSA F-8.3 (PDF, not struck) and AU BSA F-8.3 [read in official docs; render command-verified].
- **RT47.** Amazon's policy values a loss by whether it happened before or after the end customer's order, and under its post-order heading names only the customer-return claim; its list of claim kinds has no separate outbound kind. That a unit lost or damaged after the order and before delivery is handled as a customer-return case is [inferred]. Sources: US policy redlines 2024-12-18 and 2025-02-24, sentences inserted (PDF) [read in official docs; render command-verified].
- **RT48.** `Lost_Outbound` and `Damaged_Outbound` are Reimbursements report `reason` values seen in public files (see finance pack P-ref-35). No Amazon page read defines them and no SP-API model names them. Sources: P-ref-35; models clone db2936aa [command-verified].
- **RT49.** Sellers of non-returnable FBA items report that refunds for buyer-reported transit damage are denied at first contact for being non-returnable and approved on escalation; no Amazon reply in the thread states a rule. Source: thread c0d7f362 (US, 2026-03-13 onward) [opinion; absence of an Amazon reply command-verified].
- **RT50.** A recovery vendor defines "Lost Outbound" as a shipment that leaves an FC and is never delivered, counting both customer orders and lost removal orders in it. Source: Seller 365 help article [opinion].
- **RT51.** Amazon defined commingling as fulfilling orders from the closest exact-match inventory "even if that inventory belonged to a different seller", and ended it for inventory shipped on or after a cut-off (see inbound-shortfalls IN24; value in *Values that move*). No Amazon page read says to whose inventory a returned commingled unit is credited. Sources: News 06778c12 (UK), cd352647 (Canada), 2025-12-08 [read in official docs].
- **RT52.** Recovery vendors list returns received under a different FNSKU than ordered as a claim type; Amazon names no such kind in pages read. The returns report row carries `sku` and `fnsku` beside the order, which is where such a return is seen [inferred]. Sources: GETIDA, Helium 10 (finance pack vendor rows), Seller 365 [opinion]; FBA Reports [read in official docs].
- **RT53.** A Remote Fulfillment with FBA return is sent back to the US and is subject to the FBA customer-returns policy. Source: sell.amazon.com, *Remote Fulfillment with FBA* (read 2026-11-13) [read in official docs].
- **RT54.** Amazon credits the return fees on Remote Fulfillment returns in the Mexico and Brazil stores, automatically and within a stated period, as a "Refund" transaction with details "Remote Fulfillment credit" (start date and period in *Values that move*). Sources: News c61a5494 (US, 2025-03-10); TaylorR_Amazon 076624df (2025-03-27) [read in official docs].
- **RT55.** Under EFN between the UK and the EU, returned items are sent to the source store; sellers report returns landing in other EU fulfilment centres and storage charged there. No page read states the store or currency of a cross-border return's reimbursement. Sources: Amazon PDF *The European Fulfilment Network between the UK and the EU* (January 2022) [read in official docs]; threads 9fe56ee3, e4406a7a, 40c2c288 [opinion].

---

## Held: read only through a barred route

Each fact below was read only through the help hub's content call, which the office closed on 2026-11-10. No permitted route found on 2026-11-13 carries it. It is listed by position id and the page id it rested on, without its text, and enters no skill.

| Position | Page id it rested on (store layer) | What part |
|---|---|---|
| RT3 (part) | G9N934L7Y4SFWPJ4 (US) | the clause on refunded items buyers cannot return |
| RT6 (parts) | G9N934L7Y4SFWPJ4 (CA); G200379860 (GB, DE) | the CA page's internal contradiction; the GB/DE clock and returnless-refund window |
| RT8 (part) | G9N934L7Y4SFWPJ4 (GB, DE, FR, MX, JP, AU); G200379860 (CA, IN, JP) | other stores' "not returned" days |
| RT10 | G9MAM9ELJTSSNYS5 (US) | the seller-fault / Amazon-fault list of dispositions |
| RT12 | G9N934L7Y4SFWPJ4 (US) | the damage fee and the seller's credit (the buyer-side *Return Fees* page, amazon.com nodeId 15015721, answered 403 on re-read) |
| RT14 | G200379860 (US, CA, JP, AU) | the removal deadline for defective and customer-damaged returns |
| RT15 | G9N934L7Y4SFWPJ4 (GB) | the automatic cases |
| RT16 (part) | G9N934L7Y4SFWPJ4 (JP); G9ZB3H4DP4H72U6R (US, GB) | the JP wrong-item evidence and value; the removal page's "Different Product" list (removals-disposals holds a permitted copy in RM14) |
| RT19 (part) | G200379860 (US) | fees and payment on a replacement order; the buyer's duty to return the original |
| RT21 (part) | G200453300 (US) | the replacement reason-code labels and the help page's column name |
| RT22 | G200379860 (US, JP) | fee credits on a return |
| RT23 | G200379860 (US, CA) | the restocking-fee credit rule |
| RT25 | G200379860 (IN) | India's automated reimbursement and partial refunds |
| RT26 | G200379860 (JP, IN, US) | late-accepted returns |
| RT27 | G200379860 (JP); G9N934L7Y4SFWPJ4 (US) | returnless refunds claimable in JP; the US clause |
| RT28 | G200379860 (GB, DE) | the two-year warranty returns and the notice period |
| RT36 (part) | G200732720 (US) | the business-day delay and combining of same-day reimbursements |
| RT37 (part) | G200379860 (US, GB) | the policy's LPN sentence and the manufacturer-barcode caveat |
| RT42 | G200213130 (US) | the live US wording of the customer-return value and the dispute route; it conflicts with the redlines read in value-and-reversals VR27 and cannot be settled by a permitted route |
| RT45 | G9N934L7Y4SFWPJ4 (IN, AE, BR, SG) | the pages not served in those layers |
| body only | G84Z6B8BTKVNV53S (GB) | the UK claim window and grading text |
| body only | G200453320 (US) | the report-scheduling maximum, the Manage Returns note, the `EXPIRED` wording beyond the copy |
| body only | G202191620, G1791 (US v1 r31), G64LS955WNFT6EDP, GN655EHATZUVWBC3, GX9GZV9UGAAL4C58 | page versions and texts once cited; the US BSA is cited here from Amazon's NA PDF instead |

---

## Open questions for a first run on a real account

1. Which window does the claim tool enforce for the seller's store: the store's News post, a staff post's figure (for the US, an 18-month end), or the help page the seller sees? The answer comes from the claim tool's own reply on a live order.
2. Does any reimbursement row or transaction line carry a credit for a customer-damaged return, and under which `reason` or description?
3. The returns report's real header (`order-id` or `amazon-order-id`; `license-plate-number` or `lpn`), the `return-date` format, and the exact spellings of `detailed-disposition` and `status` values in the seller's file.
4. Does a ledger `CustomerReturns` row carry the order id in `Reference ID`, so ledger and returns report join without the LPN?
5. How does a reversal of a customer-return reimbursement appear in the Reimbursements report against `COMPENSATED_CLAWBACK` in transactions? Is it one event seen twice, or two different events?
6. Are switcheroo and wrong-item claims on the seller's store paid at the order basis or at sourcing cost (RT17)? The answer comes from `amount-per-unit` on reimbursement rows with a `case-id`, compared with the order.
7. Does the seller's store reimburse returns accepted late, and under which `reason`?
8. Outside NA and IN, does the orders read show every replacement, including FBA replacements created by customer service?
9. Is the seller enrolled in Damaged Inventory Ownership, or has it disabled returns evaluation for some ASINs? Only the seller can say.
10. For multi-unit orders, does the returns report write one row per LPN (quantity 1) or one row per line?
11. Do `Lost_Outbound` / `Damaged_Outbound` rows arrive without a `case-id` (automatic), and are they valued at the order basis (value-and-reversals VR31)?
12. Does the seller's file show returns whose `fnsku` differs from the order's, and did any commingled-era refund lack a return row because the unit was credited elsewhere?
13. For a Remote Fulfillment or EFN return reimbursed, in which store's report and currency does the row post?
14. Where, for stores other than the US and Canada, does the seller see the "not returned" days (the store's *Customer return claims* page as served in Seller Central)?

---

## Pages read

| Title | Address | Publisher | Page date | Read on | Used for |
|---|---|---|---|---|---|
| Update on Reimbursement Automation and Eligibility Window… (81c3235d) | https://sellercentral.amazon.com/seller-forums/discussions/t/81c3235d-4c44-47ba-96c5-883cecab3244 | Amazon (News_Amazon), store US | 2024-07-24 | 2026-11-13 | §2, 11; RT4, 5, 6, 19, 33; Values; Corrections 1 |
| Same title (6605eede) | https://sellercentral.amazon.com/seller-forums/discussions/t/6605eede-df8e-4498-803f-cb612d95d7ce | Amazon (News_Amazon), store Canada | 2024-07-24 | 2026-11-13 | §2; RT4–6; Values |
| Same title (d0fc997e) | https://sellercentral.amazon.com/seller-forums/discussions/t/d0fc997e-de50-4100-9803-76b7993b66df | Amazon (News_Amazon), store UK | 2024-10-10 | 2026-11-13 | §2, 11; RT4; Values |
| FBA reimbursement policy updated (9a92846d) | https://sellercentral.amazon.com/seller-forums/discussions/t/9a92846d-41f8-4ad7-b59a-f946efdcc2b4 | Amazon (News_Amazon), store UK | 2025-01-15 | 2026-11-13 | §2; RT4, 7; Values |
| FBA reimbursement policy updated (1101821c) | https://sellercentral.amazon.com/seller-forums/discussions/t/1101821c-7ff1-495a-b8a5-71ff01e3afc3 | Amazon (News_Amazon), store Sweden | 2025-01-15 | 2026-11-13 | §2; RT4, 7; Values |
| Update to FBA inventory reimbursement claim windows (d8f9a56c) | https://sellercentral.amazon.com/seller-forums/discussions/t/d8f9a56c-882f-437c-ad34-cccd11cfa465 | Amazon (News_Amazon), store Australia | 2025-08-14 | 2026-11-13 | §2–3; RT4, 13; Values |
| FBA Lost Your Inventory? Steps to File a Reimbursement Claim (0e07abc1) | https://sellercentral.amazon.com/seller-forums/discussions/t/0e07abc1-9026-4540-a005-153d9e78bf04 | Amazon staff (Indy_Amazon), store US | 2026-08-13 | 2026-11-13 | §1–2, 11; RT1, 6, 8 |
| Reimbursement for Customer-Damaged Returns (70760af8) | https://sellercentral.amazon.com/seller-forums/discussions/t/70760af8-280a-4988-a04d-56ec518a3a88 | Seller (2023-10-06) + Amazon staff (Veronica_Amazon, 2023-10-13), store US | 2023-10-06 | 2026-11-13 | §1–3, 11; RT1, 3, 8; Corrections 4 |
| Refunds and Returns Policies (02bebf51) | https://sellercentral.amazon.ca/seller-forums/discussions/t/02bebf51-816e-4585-a7e7-8b6aa61fcd5f | Amazon staff (Christine_Amazon), store Canada | 2025-03-24 | 2026-11-13 | §1–2, 11; RT1, 3, 6, 8 |
| Large Scale FBA Returns Fraud (d781984a) | https://sellercentral.amazon.com/seller-forums/discussions/t/d781984a-96ad-4842-9069-ad16709bb1a1 | Seller (2026-04-14) + Amazon staff (Xander_Amazon, 2026-04-23) | 2026-04-14 | 2026-11-13 | §4; RT43 |
| Damaged inventory ownership? (bf1c7ab1) | https://sellercentral.amazon.com/seller-forums/discussions/t/bf1c7ab1-1985-472b-91b0-f5916359665e | Seller + Amazon staff (Danny_Amazon) | 2025-03-17 | 2026-11-13 | §3; RT11; Corrections 7 |
| switcheroo FBA order return reimbursement claim (cd49634e) | https://sellercentral.amazon.com/seller-forums/discussions/t/cd49634e-576b-4b3c-af7c-95c68fd2b175 | Sellers | 2025-04-18 | 2026-11-13 | §4; RT17 |
| Reimbursement for customer returning item that isn't what I sold them (76efc391) | https://sellercentral.amazon.com/seller-forums/discussions/t/76efc391-04de-4126-90e2-0fec94097a72 | Sellers | 2025-07-30 | 2026-11-13 | §4; RT16, 17 |
| Return Items with Emptied Boxes!? What is LPN Number image? (bd2e5bba) | https://sellercentral.amazon.com/seller-forums/discussions/t/bd2e5bba-a6af-4ee4-8736-598578e2699f | Seller + staff (Tatiana_Amazon, 2023-09-07) | 2023-07-25 | 2026-11-13 | §4; RT16 |
| FBA customer returned a totally different and much cheaper item | https://sellercentral.amazon.com/seller-forums/discussions/t/588390408669ce78defa82c839402b2c | Sellers | 2020-02-03 | 2026-11-13 | §4, 13; RT16 |
| Why are sellers denied reimbursement for "damaged in transit" on non-returnable FBA food items (c0d7f362) | https://sellercentral.amazon.com/seller-forums/discussions/t/c0d7f362-b3ce-4f87-a458-64fd00723a9e | Sellers | 2026-03-13 | 2026-11-13 | §12; RT49 |
| High refund amount (9c7a8fe0) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/9c7a8fe0-28fe-4f0b-8eeb-b2c81fb90e09 | Sellers | 2025-02-26 | first round, 2026-11-13 | §6; RT24 |
| Excessive FBA refunds (aad3a1bd) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/aad3a1bd-fa99-49ea-8ae4-9334b5b5e6dd | Sellers | 2025-05-29 | first round, 2026-11-13 | §6; RT24 |
| $0.00 reimbursement for FBA Return (446cc0c9) | https://sellercentral.amazon.com/seller-forums/discussions/t/446cc0c9-c551-4eef-9d8f-9d52f9db9f3a | Seller | 2025-03-26 | first round, 2026-11-13 | §6 |
| Commingling practices will end effective March 31, 2026 (06778c12) | https://sellercentral.amazon.com/seller-forums/discussions/t/06778c12-539e-478a-8f67-00592c4c5cca | Amazon (News_Amazon), store UK | 2025-12-08 | 2026-11-13 | §13; RT51 |
| Same (cd352647) | https://sellercentral.amazon.com/seller-forums/discussions/t/cd352647-7a0d-426f-83e7-e3dd4add6c5c | Amazon (News_Amazon), store Canada | 2025-12-08 | 2026-11-13 | §13; RT51 |
| New return credits for Remote Fulfillment with FBA (c61a5494) | https://sellercentral.amazon.com/seller-forums/discussions/t/c61a5494-45a3-4715-8291-943feac1ee74 | Amazon (News_Amazon), store US | 2025-03-10 | 2026-11-13 | §14; RT54 |
| ICYMI: New return credits for Remote Fulfillment with FBA (076624df) | https://sellercentral.amazon.com/seller-forums/discussions/t/076624df-7998-486a-8d2e-3fe15757c237 | Amazon staff (TaylorR_Amazon) | 2025-03-27 | 2026-11-13 | §14; RT54 |
| Need Mod Help - FBA Customer Return Fee for a remote fulfillment order (ce526b12) | https://sellercentral.amazon.com/seller-forums/discussions/t/ce526b12-40d5-4657-bff2-dc1322490485 | Seller + staff (Bryce_Amazon) | 2025-02-17 | 2026-11-13 | §14 |
| EFN - where do returns end up? (9fe56ee3) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/9fe56ee37a3e41ceb47a13ee1059297c | Sellers, store UK | 2023-02-15 | 2026-11-13 | §14; RT55 |
| Remote fulfillment/EFN returns (e4406a7a) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/e4406a7a-9994-46fc-811b-78e730db3dc8 | Sellers, store UK | 2024-08-19 | 2026-11-13 | §14; RT55 |
| Customs Clearance and Shipping Services (40c2c288), seller reply of 2025-05-30 | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/40c2c288-394a-4428-a467-266a39ec9d1d | Amazon (News_Amazon) + seller | 2025-05-28 | 2026-11-13 | §14; RT55 |
| FBA inventory reimbursement policy (US, "clean" redline) | https://m.media-amazon.com/images/G/01/rainier/help./PC__Kiwi_Comms_redlined_policy_US_clean.pdf | Amazon (PDF) | created 2024-12-18 | 2026-11-13 (rendered) | §8, 12; RT17, 30, 47 |
| FBA inventory reimbursement policy (US redline, R-US) | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_US.pdf | Amazon (PDF) | created 2025-02-24 | 2026-11-13 (rendered) | §8, 12; RT17, 30, 47 |
| FBA lost and damaged inventory reimbursement policy (UK, clean and R-UK) | https://m.media-amazon.com/images/G/01/rainier/help./_PC__Kiwi_Comms_redlined_policy_UK_clean_version.pdf ; https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_UK.pdf | Amazon (PDF) | created 2024-12-11; 2025-02-24 | 2026-11-13 (rendered) | §1; RT3 |
| Amazon Services Business Solutions Agreement (NA, redlined) | https://m.media-amazon.com/images/G/01/rainier/help/legal/BSA_NA_English_redlined.pdf (also on images-na.ssl-images-amazon.com) | Amazon (PDF) | created 2019-07-17 | 2026-11-13 (rendered) | §1, 5, 6, 10, 12; RT1, 19, 24, 29, 30, 44, 46 |
| Amazon Services Business Solutions Agreement (Australia) | https://m.media-amazon.com/images/G/35/01/Amazon_Services_Business_Solutions_Agreement_October_2023_LIVE.pdf | Amazon (PDF) | created 2023-10-16 | 2026-11-13 | §1, 12; RT29, 44, 46 |
| The European Fulfilment Network between the UK and the EU | https://m.media-amazon.com/images/G/02/fba/Handbook_EFN_between_the_UK_and_the_EU_EN.pdf | Amazon (PDF) | "Updated as of January 2022"; created 2022-05-19 | 2026-11-13 | §14; RT55 |
| Pan-European FBA guide | https://m.media-amazon.com/images/G/02/FBA_SSR_Contents/Pan-EU_EN.pdf | Amazon (PDF) | — | 2026-11-13 | §14 (no return rule found) |
| Remote Fulfillment with FBA | https://sell.amazon.com/fulfillment-by-amazon/remote-fulfillment | Amazon (sell.amazon.com) | — | 2026-11-13 | §14; RT53 |
| Fulfillment by Amazon (FBA) Reports | https://developer-docs.amazon.com/sp-api/docs/report-type-values-fba.md | Amazon (SP-API docs) | updatedAt 2026-10-13 | 2026-11-13 | §5, 9, 13; RT20, 21, 32, 34, 37, 52 |
| Returns Reports | https://developer-docs.amazon.com/sp-api/docs/report-type-values-returns.md | Amazon (SP-API docs) | updatedAt 2026-10-28 | 2026-11-13 | §10; RT39 |
| selling-partner-api-models (ordersV0.json, orders_2026-01-01.json, notification schemas; grep for outbound reasons) | https://github.com/amzn/selling-partner-api-models (commit db2936aa) | Amazon | 2026-10-29 | 2026-11-13 | RT11, 20, 40, 48 |
| Listing pack, research/angles/returns.md (its read of G200453320 v16 r0 and G200379860 v24 r2) | cx-listing-playbook research/angles/returns.md | this office (listing seat) | read 2026-10-14 | cited 2026-11-13 | §1, 3, 7, 9; RT2, 9, 18, 32–35, 37, 38 |
| Amazon FBA Returns: What Every Condition Code Means | https://www.gorillaroi.com/blog/amazon-fba-returns | Gorilla ROI | updated 2026-05-07 | 2026-11-13 | §3, 9; RT9, 35, 36 |
| FBA Customer Returns Report | https://docs.openbridge.com/en/articles/8135664-fba-customer-returns-report | Openbridge | 2024-02-15 | 2026-11-13 | §9; RT34–37 |
| Amazon shifts liability to sellers with new FBA inventory policy | https://ppc.land/amazon-shifts-liability-to-sellers-with-new-fba-inventory-policy/ | PPC Land (Luís Rijo) | 2025-08-18 | 2026-11-13 | §3; RT11; Values |
| What types of reimbursements are included with my Seller 365 reimbursements service | https://intercom.help/seller-365/en/articles/10638659-what-types-of-reimbursements-are-included-with-my-seller-365-pro-reimbursements-service | Seller 365 | undated | 2026-11-13 | §1, 5, 7, 12, 13; RT50, 52 |
| A Quick Guide to Amazon FBA Reimbursements Part 5 | https://getida.com/quick-guide-to-fba-auditing-reimbursements/ | GETIDA | undated | 2026-11-13 | §1, 6, 7; RT24 |
| Types of Amazon FBA Refunds | https://myamazonguy.com/amazon-reimbursement/types-of-amazon-fba-refunds/ | My Amazon Guy (Steven Pope) | 2024-07-26 | first round | §1, 6 |
| Refunded But Never Returned | https://www.refunzo.com/blog/amazon-missing-return-reimbursement-guide/ | Refunzo (Jimi Patel) | 2026-02-19 | first round | §1, 2, 7, 11 |
| Amazon FBA Returns: Where the Money and the Unit Actually Go | https://amzbase.com/guides/amazon-fba-returns/ | AMZBase | 2026-09-07 | first round | §2, 6 |
| Amazon Reversed Reimbursements | https://www.spscommerce.com/community/articles/amazon-reversed-reimbursements | SPS Commerce | updated 2025-07-24 | first round | §2, 8; RT31 |
| COMPENSATED_CLAWBACK (search summaries of Synder and Carbon6 pages) | https://synder.com/fees-amazon/compensated-clawback-reversal-of-previous-refunds/ ; https://www.carbon6.io/?p=11323 | Synder; Carbon6 | — | first round (search summary only) | §8; RT31 |
| 重大调整！亚马逊FBA索赔申请期限又缩短了！ | https://m.mjzj.com/article/eawxbluj5am8 | 卖家之家 (小牛站外) | 2025-01-24 | first round | §2; RT7 |
| 两大新政！亚马逊FBA索赔资格申请期限更新 | https://www.amz123.com/t/LFOykLna | AMZ123 (跨境小蚂蚁) | 2025-01-19 | first round | §2; RT7 |
| 利润报表（新）公式核对 | https://www.lingxing.com/help/article/Formulacheck | 领星 Lingxing | undated | first round | §3, 5, 6, 8, 9; RT31, 35 |
| 买家恶意退货，亚马逊FBA卖家如何维权？ | https://m.by56.com/news/54008.html | 百运网 | 2025-11-07 | first round | §4 |
| FBA卖家哪些情况可以向亚马逊索赔？ | https://www.52by.com/article/44020 | 邦阅网 | undated | first round (search summary only) | §1 |
| Eva.guru / SellerSprite reimbursement guides | https://eva.guru/answers/how-to-file-an-amazon-fba-reimbursement-claim/ ; https://www.sellersprite.com/en/blog/amazon-reimbursement-services | Eva; SellerSprite | 2026 | first round (search summary only) | §2 |
| Return Fees; Refunds (amazon.com customer help) | https://www.amazon.com/gp/help/customer/display.html?nodeId=15015721 ; …nodeId=GKQNFKFK5CF3C54B | Amazon | — | 2026-11-13: HTTP 403 to a plain GET; unread | Held (RT12) |
| Reimbursement policy for Buy with Prime orders | https://buywithprime.amazon.com/knowledge-center/reimbursement-policy-for-buy-with-prime-orders | Amazon | — | first round: HTTP 403; unread | — |

Seller Central help pages are not rows here: none was fetched in this revision, and the first round's reads of them are withdrawn (see *Held*).

---

## Seat's own (no source; enters no skill)

- Whether a first run on a real account only observes the claim tool's reply and files nothing is a decision for the seat and the seller, not a fact about Amazon.
- Reading column names and values from the header of the seller's own file (RT34, RT35) is this seat's method for the disagreement Amazon's pages and copies show; the disagreement itself is the sourced fact.
- Grouping outbound losses, wrong-FNSKU returns and cross-border returns with customer returns (§§ 12–14) follows the order id as the key they share; it is this seat's arrangement, not Amazon's.

## Verification (2026-11-13, first round; superseded in part)

The first round's adversarial check re-read the help pages through the help hub's content call; those checks are withdrawn with the reads they confirmed (see *Held*). What it checked by other routes stands: forum `datePublished` and authors by plain GET, the SP-API report-type pages, and the models clone at db2936aa compared with GitHub main (one commit ahead, b13d1d1, 2026-11-11, Data Kiosk analytics economics schema only). This revision re-read every forum thread it cites by plain GET (post text, author, `createdAt`, `marketplaceId`), rendered the Amazon PDFs it cites to tell struck from inserted text, and re-read the SP-API pages and third-party copies it cites.

**Remaining doubts:**
- That a News post's `marketplaceId` is the store it governs is the pack's shared reading; Amazon does not document the field (fc-lost-damaged § 2a).
- The NA BSA read here is a 2019 redline; the live US agreement is a help page and was not read. Its F-8 text may have changed since.
- The listing pack's reads of G200453320 and G200379860 (2026-10-14) were themselves made through the content call; they are cited as that seat's read, a route the brief names as permitted, and carry that seat's date.
- Practitioner pages not re-read in this revision keep the first round's tags.
- Whether `RETURN_RECEIVED` ever fires for an FBA customer return is not stated by Amazon.

## Revision (2026-11-13)

After the completeness critic's review (round 1) and the office's ruling of 2026-11-10 closing the help hub's content call:
- Route paragraph rewritten: no help page fetched, no POST to any Amazon host; every help-page fact re-sourced through a permitted route (News and staff posts by plain GET with `marketplaceId`, Amazon PDFs rendered, sell.amazon.com, SP-API docs, third-party copies, the listing pack's read) or moved to the new section *Held: read only through a barred route* by position id and page id.
- Withdrawn to *Held*: RT10, RT12, RT14, RT15, RT22, RT23, RT25, RT26, RT27, RT28, RT45; parts of RT3, RT6, RT8, RT16, RT19, RT21, RT36, RT37. Withdrawn to a pointer: RT41 (filing-and-conduct FL4), RT42 (value-and-reversals VR27, VR20; its live-page wording held).
- Re-sourced and rewritten: RT1–RT9, RT11, RT13, RT16–RT21, RT24, RT29, RT30, RT32–RT39, RT43, RT44. RT5 now names the stores of the two 2024-07-24 posts (US, Canada) by `marketplaceId` (critic A1), pointing to fc-lost-damaged § 2a for the post-to-store table; RT7 names the Sweden and UK posts of 2025-01-15 as the likely source of the Chinese reports.
- Self-corrections: Veronica_Amazon's thread 70760af8 carries the US `marketplaceId` (it was called an EU-host post that names no store), and her reply is dated 2023-10-13, not 2023-10-06 (the thread's opening). Xander_Amazon's reply is dated 2026-04-23.
- New sections: § 12 units lost or damaged outbound (`Lost_Outbound` / `Damaged_Outbound`; BSA F-8.3; the policy's pre/post-order split; RT46–RT50); § 13 wrong-FNSKU and commingled returns and returns credited to another seller (RT51, RT52); § 14 cross-border returns, Remote Fulfillment and EFN (RT53–RT55).
- `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE` is stated to need roles outside the five, pointing to sp-api-claims-surface § 2.1 (critic B; §§ 6, 10, RT39).
- Homes applied (critic D): automation dates and the post-to-store table → fc-lost-damaged § 2a; valuation and the dispute window → value-and-reversals; claim routes → filing-and-conduct FL4; grading disputes and the removal evidence list → removals-disposals RM11, RM12, RM14; roles → sp-api-claims-surface. The settlement V2 flat file is replaced by `listTransactions` as a run-time read (SU38); Orders v0's deprecation noted (SU37).
- A *Values that move* table added; the § 2 per-store table's values moved into it.
- Corrections to other packs: 1 and 4 re-sourced; 2, 3 and 6 withdrawn (barred route); 5 narrowed; 7 re-sourced. A note added for fc-lost-damaged § 9 (thread c0d7f362 has no Amazon reply).
- Open questions 11–14 added; questions 1, 2 and 6 reworded so as not to rest on held facts.
- Not done for want of a route on the day: the store layers of G200213130, G200379860 and G9N934L7Y4SFWPJ4 outside the US, UK, Canada, Sweden and Australia News posts; Japanese practitioner sources. The session's web-search allowance ran out during this revision, so no further search for third-party copies of the held texts was possible.
