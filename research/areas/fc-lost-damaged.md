# Units lost or damaged inside Amazon's network (fc-lost-damaged)

**Summary.** A unit that an Amazon fulfilment centre (or a facility run on Amazon's behalf) loses or damages after receipt is reported as an adjustment in the Inventory Ledger, is researched for a while, and is then found, reimbursed, or left open. Amazon says it now reimburses "almost all" warehouse-lost and warehouse-damaged cases without a claim. It announced this store by store: each Seller Forums News post carries the store it was issued for in its own page data (`marketplaceId`), and this file holds the table of which post addresses which store (§ 2a). Read that way, the 2024-11-01 start is the US and Canada posts' date and the 2025-01-15 start is the UK post's; no automation post was found for any other store. A UK staff post of 2026-04-06 says UK warehouse-lost reimbursement is still manual, with a longer window, against Amazon's own UK News posts; both are stated. Where a manual claim exists, the window counts from the date Amazon reports the loss, not the date the seller finds it; its length is a per-store value (Values that move). The seller's own data is the ledger detail view (adjustment reason codes, reconciled and unreconciled quantity, `Country`, `Store`) matched against the Reimbursements report. The IDR portal, the claim tools and the sourcing-cost page exist only in Seller Central. Short sections cover units lost in cross-border transfers and NA Remote Fulfillment (§ 11), MCF units (§ 12), Vine units (§ 13), unreconciled rows older than the ledger's reach (§ 14) and the exclusions for expired, recalled and force-majeure cases (§ 15).

Date read for every page: **2026-11-13**, unless a row in Pages read says otherwise.

Neighbouring areas (one line each, not researched here): units short on an inbound shipment, including AWD-to-FBA replenishment shipments → **inbound-shortfalls**. Refunded-not-returned and returns damaged by Amazon → **customer-returns**. Removal orders and disposals Amazon made without a request → **removals-disposals**. How a reimbursement is valued, disputed and reversed → **value-and-reversals**. Roles, reports and what the API cannot do → **sp-api-claims-surface**. Case mechanics and conduct → **filing-and-conduct**. Services and their figures → **recovery-economics**.

Already held elsewhere, cited and not redone: the finance pack (cx-amazon-finance-playbook), research/areas/refunds-reimbursements-adjustments.md, P-ref-12 to P-ref-21, P-ref-35 to P-ref-38, P-ref-40 and P-ref-50; the stock pack (cx-amazon-stock-playbook), research/areas/stock-states.md, P-stock-states-12, -13, -28 to -36, -50 to -52 (its skill reference reports-and-ledger.md cites the same facts as W25 to W32). How a call or report is made is in the door (cx-amazon-sp-api, skills/amazon-sp-api/references/door.md) and is not repeated here.

---

## 1. What counts as a fulfilment-centre loss or damage

**(a) Amazon's rule.**

- Policy text, older version (a third-party mirror of Amazon's help article "FBA inventory reimbursement policy", hopted.com; the text gives an 18-month window and estimated-proceeds valuation, so it predates 2024-10-23): "This section applies to eligible items that are lost or damaged by an Amazon fulfillment center or a facility operated on behalf of Amazon, after Amazon receives them from you. These lost or damaged items are reported in your Inventory Ledger report." The general clause: "If an item you send through the Fulfillment by Amazon (FBA) service is lost or damaged at an Amazon facility or by a carrier operating on Amazon's behalf, we will replace the item with a new one of the same FNSKU or reimburse you for it." Read 2026-11-13.
- Amazon staff (Indy_Amazon, "🆘FBA Lost Your Inventory? Steps to File a Reimbursement Claim", sellercentral.amazon.com/seller-forums/discussions/t/0e07abc1-9026-4540-a005-153d9e78bf04, datePublished 2026-08-13, store US by its `marketplaceId`, § 2a): "Warehouse lost — Your inventory went missing while stored at a fulfillment center"; "Warehouse damaged — Your item was damaged by Amazon during storage or fulfillment operations". On valuation, the same post widens the scope: "For shipment to Amazon claims, removals claims, and fulfillment center operations claims that occur before fulfillment, we will reimburse you the sourcing cost of the item. This also covers lost and damage claims during inventory replenishment handled by Amazon or on behalf of Amazon to fulfillment centers or non-Amazon buildings in marketplaces where we provide the service." Read 2026-11-13.
- The general clause in Amazon's own 2025-02-24 policy PDFs (plain GET from m.media-amazon.com, read 2026-11-13): US, "If an item you send to us as part of the Fulfillment by Amazon (FBA) service is lost or damaged at a facility or by a carrier operated by Amazon or on behalf of Amazon, we replace that item with a new item of the same FNSKU or reimburse you for it" (Redlined_FBA_Reimbursement_policy_US.pdf, created 2025-02-24, text layer); UK, the same with "Fulfilment" and "we will replace … or we will reimburse you for it" (Redlined_FBA_Reimbursement_policy_UK.pdf, created 2025-02-24). These corroborate the mirror's general clause with Amazon-hosted text; the FC-operations section itself sits on a page the PDFs only link.
- Eligibility conditions (registered in FBA, exact shipping-plan quantities, not pending disposal, not customer-damaged, account status) are held in the finance pack as P-ref-12 and its § E1; the exclusions are in § 15 here. The UK staff post (§ 3) adds three conditions as UK requirements: "The ASIN must be active (not suppressed, prohibited, or restricted)", "You must have a standard FBA contract", and an account "in normal or pending status".
- The Reimbursements report's `reason` values that belong to this area, as seen in public files (finance pack P-ref-35): `Lost_Warehouse` and `Damaged_Warehouse`, plus `Lost_Outbound` and `Damaged_Outbound` for units lost or damaged on the way to a customer.

**(b) Practitioners.** 招单猫 (published in 卖家之家 / mjzj, dated 08/07/2024 on the page, read as 2024-08-07 because the post quotes the 2024-07-24 announcement) [opinion]: "问题的根源在于如何界定货物在哪里丢失" ("the root of the problem is how to define where the goods were lost"), followed by the worry that a seller who must prove the loss happened in the FBA warehouse will still have to submit POD and similar documents. Reading this as the inbound-versus-warehouse boundary is ours [inferred].

**(c) Into a skill:** a fulfilment-centre case begins only after Amazon has received the unit (the ledger shows a receipt), and it is reported in the ledger as an adjustment. Units that never got a receipt belong to inbound-shortfalls. A post-order loss is valued differently from a pre-order loss (finance pack P-ref-14). **Read at run time:** `GET_LEDGER_DETAIL_VIEW_DATA` with `eventType=Adjustments`, which needs the Amazon Fulfillment role (P-stock-states-50); and Amazon's page "FBA inventory reimbursement policy" (G200213130), https://sellercentral.amazon.com/help/hub/reference/G200213130, as the seller's store shows it.

---

## 2. Proactive (automatic) reimbursement: what Amazon announced, and when

**(a) Amazon's rule.** Each post below was re-read raw on 2026-11-13. Its posting date is the page's `datePublished`; its store is the post object's `marketplaceId` (method and checks in § 2a).

1. **US** (News_Amazon, "Update on Reimbursement Automation and Eligibility Window to file reimbursement claims", sellercentral.amazon.com/seller-forums/discussions/t/81c3235d-4c44-47ba-96c5-883cecab3244, posted 2024-07-24, store `ATVPDKIKX0DER`, 2.5K views, 17 replies): "Starting November 1, 2024, we'll proactively reimburse you for Fulfillment by Amazon (FBA) items that are lost in our fulfillment centers. We'll issue the reimbursement as soon as an item is reported as lost by the fulfillment center, which you can track in the Reimbursements report on Seller Central." "Almost all reimbursement claims related to warehouse lost and damaged and customer returns cases will now be proactively reimbursed. However, if you do not receive an automatic reimbursement and you believe that your inventory has been lost or damaged, you will need to file a manual claim. Additionally, all removal claims will still need to be filed manually." Its windows run from "October 23".
2. **Canada** (…/t/6605eede-df8e-4498-803f-cb612d95d7ce, posted 2024-07-24 less than a second after 1, store `A2EUQ1WTGCTBG2`, 132 views, 0 replies): the same text with "Fulfilment" and "fulfilment centres", and its own customer-return window.
3. **A seller relay on the Canada store** (Seller_xJx7vH6fvZFD9, "FINALLY GOOD NEWS?", …/t/3f3688d2-5949-4bd1-900b-d01b242955d3, posted 2024-07-25, store `A2EUQ1WTGCTBG2`) quotes the Amazon message, signed "The Fulfilment by Amazon team": "Starting on November 1, 2024, we'll proactively reimburse you … These updates go into effect on October 23." [official, relayed] The previous version of this file placed this relay on the UK forum because it was read on the .co.uk host; the post's own field says Canada.
4. **UK** (…/t/d0fc997e-de50-4100-9803-76b7993b66df, posted 2024-10-10, store `A1F83G8C2ARO7P`, 285 views): "Starting January 15, 2025, we'll proactively reimburse you…"; windows "Starting January 9, 2025". It refers to "Changes to programme policies".
5. **UK and Sweden follow-ups, 2025-01-15**: …/t/9a92846d-41f8-4ad7-b59a-f946efdcc2b4 (store UK, 155 views): "The Fulfilment by Amazon (FBA) reimbursement policy has been updated to reflect the new eligibility windows"; …/t/1101821c-7ff1-495a-b8a5-71ff01e3afc3 (store `A2NODRKZP88ZB9`, Sweden, 24 views): the same windows in US spelling. **Neither says anything about automatic reimbursement**; Sweden's post is a windows post only.
6. **Valuation posts of 2024-12-18 that restate the automation** (each a separate thread per store): US 68864b6f-0ab8-41ef-be18-069c33df6336 ("We now offer automatic reimbursements for items lost in our fulfillment centers"), UK a941ac02-d389-409a-9d62-00ab9db5bc4a and Canada da761b17-58cc-4734-98d2-5608e1d11419 ("We now offer automatic reimbursements for items lost in our fulfilment centres, saving you time and eliminating the need for you to submit a claim to receive reimbursement"). The UK post was published four weeks before the UK post's own 2025-01-15 start.

**Stores with no automation post found.** No News post announcing automatic reimbursement of warehouse-lost units was found for DE, FR, IT, ES, NL, PL, BE, IE, SE, JP, AU, IN, MX, BR, AE, SA, EG, TR or SG. The Sweden, Middle East (§ 3) and Australia (d8f9a56c) posts read change windows only. Chinese media assign 2025-01-15 to Europe: 速推站外 on AMZ123, 2024-10-23, "亚马逊最近宣布了对其欧洲站点的…赔偿政策的更新… 自2025年1月15日起" [opinion]; by the post's field the date is the UK's, and no EU-store post with that date was found. A Carbon6 article, now returning 404, had the URL slug "amazon-uk-changes-to-reimbursement-automation-and-claim-eligibility-windows-starting-january-2025" (seen in search results only); this agrees with the UK field of d0fc997e and is no longer needed as evidence.

**The 2026 UK contradiction.** Jameson_Amazon, "[April FBA Series]💰 Recover Your Lost FBA Inventory: UK Reimbursement Claims Explained", sellercentral.amazon.co.uk/seller-forums/discussions/t/2f44617d-9e1c-413e-94b0-d427524ceb82, posted 2026-04-06, store `A1F83G8C2ARO7P`, "updated by moderator". [official, staff]

- Warehouse Damage: "Automatically reimbursed within [a stated number of] days for sellable inventory" (value in Values that move); "Eligible for manual claims if source disposition is customer damaged, inbound carrier damaged, expired, or distributor damaged".
- Warehouse Lost Inventory: "Must be claimed within [a stated period] of the event"; "Currently requires manual claim submission (automatic reimbursement disabled since August 2022)".
- Valuation: "we reimburse you based on the estimated proceeds - your item's value minus applicable fees".
- "Key Timeframes for UK Sellers": damage claims "Available immediately after the damage event is visible", with a lost-inventory window and an automatic-damage period (values in Values that move).

This conflicts with three UK News posts (d0fc997e, 2024-10-10: automatic lost reimbursement from 2025-01-15; a941ac02, 2024-12-18: "We now offer automatic reimbursements"; 9a92846d, 2025-01-15: the shorter manual window) and with the UK policy PDF of 2025-02-24, which values pre-order losses at sourcing cost (value-and-reversals VR2). The staff post's "estimated proceeds - your item's value minus applicable fees" matches the wording the UK PDF strikes, so the staff post may restate the pre-2025 page [inferred]. In the same thread, a seller on the UK forum reports that for a lost item "they themselves sell for £75 and which the official manufacturer sells for £46 Amazon calculates at '£8.86 Amazon estimated'", while holding invoices for the exact cost (the invoice figure is not given) [opinion]. The "Amazon estimated" wording matches the label of an estimated sourcing cost rather than "estimated proceeds" [inferred; the post does not say which method was applied]. No Amazon announcement of an "August 2022" stop to automatic lost reimbursement was found. Neither side is picked here.

**History before 2024.** Amazon's 2021 researching text, as a seller quoted it on the forum (2021-04-07, store UK by its `marketplaceId`; held as P-stock-states-51 and stock-states § J1), reads: "For inventory adjustments occurring after March 19, 2021, you do not have to wait 30 days to file a claim because we are handling the 30-day researching duration for you". 雨果网 (王璧辉, 2019-06-12, republished on AMZ123 IgwBEtRX) describes the ledger's predecessor, the Inventory Adjustments report, and says rows showing both "Damaged at Amazon…" and "Transfer to holding…" "已自动赔偿" ("were already reimbursed automatically") [opinion, history]. Automatic handling of warehouse damage therefore predates 2024 in practitioners' accounts.

**(b) Practitioners.**

- Seller Labs (Nhan Dinh, 2026-03-18) [opinion]: auto-reimbursement does not remove the need to audit; it matches ledger events to reimbursements (§ 6).
- Spaghetti, Sellers Ask Sellers (2024-10-14, 2024-10-20) [opinion]: skips recent damage events because "Amazon often reimburses you for them", and prefers a provider that offers delayed claims so as not to file for "reimbursements Amazon would have automatically processed for you anyway".
- Refunds Manager (seller account Seller_MDD9UH4bX3QQQ, reply on 81c3235d, ≈2024-07) [opinion]: "Initially, there were no time restrictions on claims. In 2013 … Amazon changed to an 18-month window, and now it's just 60 days."
- 招单猫 (mjzj, 2024) [opinion] doubts the automation: "如果要让卖家去证明这个货件就是在FBA仓库丢失的，那最后也免不了还是要提交POD接收单等等资料" ("if the seller has to prove the shipment was lost in the FBA warehouse, they will still end up submitting POD receipts and similar documents").
- A vendor summary in search results says auto-reimbursement lands "within roughly 20 days" [opinion, uncorroborated]. The UK staff figure is 21 days for damage.

**(c) Into a skill:** Amazon states automatic reimbursement for warehouse-lost and warehouse-damaged units, with a manual claim for any unit not reimbursed. It announced the automation per store, each post with its own start date (the post-to-store table, § 2a; the dates in Values that move); no announcement was found for most stores, and a 2026 UK staff post contradicts the UK posts for lost units. Automatic reimbursements appear in `GET_FBA_REIMBURSEMENTS_DATA` with no `case-id` [inferred: the column holds the case of a manual claim; finance pack P-ref-20]. **Read at run time:** the seller's own Reimbursements report, to see whether automatic `Lost_Warehouse` / `Damaged_Warehouse` rows arrive at all for the store; the latest Seller Forums News post on reimbursement whose `marketplaceId` is that store (§ 2a); G200213130 as the store shows it.

---

## 2a. Which store each Amazon post addresses (the pack's post-to-store table)

This table is the pack's home for the store of each Seller Forums post the pack cites; the other files point here.

**How the store is read.** A forum thread id opens on every forum host (.com, .ca, .co.uk, sellercentral-europe, sellercentral-japan), so the host a thread is read on says nothing about its store. The page's embedded data carries two kinds of marketplace field:

- `selectedMarketplaceId` (and `ue_mid`) follow the host fetched from;
- the post object carries its own `"marketplaceId"`, immediately after `"contentMetadata":{"mentions":{}}` and before `"pinnedToCategory"`. That value stays the same whichever host serves the thread.

Amazon does not document the second field. Read 2026-11-13 by plain GET of each thread and a grep of the post object; marketplace ids decoded on Amazon's *Marketplace IDs* page (developer-docs.amazon.com/sp-api/docs/marketplace-ids, read 2026-11-13: `ATVPDKIKX0DER` US, `A2EUQ1WTGCTBG2` CA, `A1F83G8C2ARO7P` UK, `A1PA6795UKMFR9` DE, `A2NODRKZP88ZB9` SE, `A2VIGQ35RCS4UG` AE, `A17E79C6D8DWNP` SA, `ARBP9OOSHTCHU` EG, `A39IBJ37TRP1C6` AU, `A1VC38T7YXB528` JP).

**The check on posts whose store is certain without the field.** To settle the method's tag, the field was read on posts whose store is fixed by their own words:

| Thread | Why its store is certain | Field read | Hosts read |
|---|---|---|---|
| 2f44617d (Jameson_Amazon, 2026-04-06) | title "UK Reimbursement Claims Explained", "Key Timeframes for UK Sellers", £ figures | `A1F83G8C2ARO7P` (UK) | .co.uk, .com, sellercentral-europe, sellercentral-japan: the post field stayed UK while `selectedMarketplaceId` read UK, US, UK and JP |
| 2b01db4c (seller, 2025-03-25) | written in German; "nur Versand nach Deutschland" (shipping to Germany only) | `A1PA6795UKMFR9` (DE) | .com |
| 092c0c0b (seller, 2025-06-17) | reimbursements in £ ("£40 for 3 units") | `A1F83G8C2ARO7P` (UK) | .com |
| 9d4ff2a6 (Angie_Amazon, 2024-10-26) | "The max is £2,000 per unit" | `A1F83G8C2ARO7P` (UK) | .com |

All four agree. The tag is therefore **[command-verified]** for the field's value and for its agreement with the post's store on four posts of known store; that the field names the store a News post *governs* stays a reading, since Amazon documents neither the field nor its meaning. It settles the conflict between inbound-shortfalls ("command-verified") and removals-disposals ("inferred"): the value is command-verified; its use as "the store this rule is for" is now checked, not assumed.

**Two limits.** (1) For a seller's post the field is the store the seller posted under, not necessarily the store the post is about: c0d6d3da (2025-04-15), a complaint about Pan-EU stock sold in Italy, Spain and France, carries the UK field. (2) A News text is issued as a separate thread per store, sometimes within the same second (81c3235d and 6605eede are 0.66 s apart), and the copies differ in their values; a value read in one thread belongs to that thread's store only.

**The table** (every thread re-read 2026-11-13; date is `datePublished`, UTC):

| Thread id | Author | Posted | Store | What it carries for the pack |
|---|---|---|---|---|
| 81c3235d-4c44-47ba-96c5-883cecab3244 | News_Amazon | 2024-07-24 | US | automation from 2024-11-01; windows from 2024-10-23 (customer returns 60–120) |
| 6605eede-df8e-4498-803f-cb612d95d7ce | News_Amazon | 2024-07-24 | CA | same text; customer returns 45–105 |
| 3f3688d2-5949-4bd1-900b-d01b242955d3 | seller relay | 2024-07-25 | CA | the automation e-mail, "The Fulfilment by Amazon team" |
| 96a05f4a-537a-49d2-a918-703c47716bc0 | News_Amazon | 2024-08-06 | AE | the 2024-09-05 window set (held by inbound-shortfalls IN8) |
| c6da88ce-b14f-4ae1-95a5-1c6482b5c565 | News_Amazon | 2024-08-06 | SA | the 2024-09-05 window set, short form |
| e62a8ace-3875-433c-8ef1-bb27a29b17c4 | News_Amazon | 2024-08-06 | EG | the 2024-09-05 window set with carrier-damaged returns and lost customer returns |
| d0fc997e-de50-4100-9803-76b7993b66df | News_Amazon | 2024-10-10 | UK | automation from 2025-01-15; windows from 2025-01-09 |
| 2de1ef2f-e299-486c-9466-48a885c3faef | seller relay | 2024-10-16 | US | "updated from 18 months to 60 days" from 2024-10-23 |
| 9d4ff2a6-8244-4ad9-bc8c-0d051600e817 | Angie_Amazon (staff) | 2024-10-26 | UK | £2,000 cap; 90-day dispute (value-and-reversals VR20, VR29) |
| 68864b6f-0ab8-41ef-be18-069c33df6336 | News_Amazon | 2024-12-18 | US | manufacturing-cost valuation from 2025-03-10; "We now offer automatic reimbursements" |
| a941ac02-d389-409a-9d62-00ab9db5bc4a | News_Amazon | 2024-12-18 | UK | the same, British spelling |
| da761b17-58cc-4734-98d2-5608e1d11419 | News_Amazon | 2024-12-18 | CA | the same |
| 1101821c-7ff1-495a-b8a5-71ff01e3afc3 | News_Amazon | 2025-01-15 | SE | windows only |
| 9a92846d-41f8-4ad7-b59a-f946efdcc2b4 | News_Amazon | 2025-01-15 | UK | windows only |
| b175b700-09c4-4350-8a22-24f60a724042 | News_Amazon | 2025-01-21 | US | IDR portal launch |
| ed8abc33-a1d5-417d-b2e2-03b789099833 | News_Amazon | 2025-02-28 | US | valuation date moved to 2025-03-31 |
| 0252e05d-1b82-40e7-91d4-543dc22b907b | News_Amazon | 2025-02-28 | UK | the same move for the UK |
| d8f9a56c-882f-437c-ad34-cccd11cfa465 | News_Amazon | 2025-08-14 | AU | windows from 2025-10-15, including re-evaluation |
| 2f44617d-9e1c-413e-94b0-d427524ceb82 | Jameson_Amazon (staff) | 2026-04-06 | UK | UK lost "manual" since August 2022 (§ 2) |
| 0e07abc1-9026-4540-a005-153d9e78bf04 | Indy_Amazon (staff) | 2026-08-13 | US | routes, windows, "Don't file prematurely" |
| 5b46fd45c5a27980040dbe30d9a84637 | seller quoting Amazon | 2021-04-07 | UK | the 30-day researching text (P-stock-states-51) |
| 10da82b7, b738f397, 1d0a23e7, c0d7f362, d17dd798 | sellers; staff replies | 2024–2026 | US | AWD and transit threads (§ 9) |
| 66aa87b7-1f89-416a-aef8-ce72a552c00a | seller | 2025-07-18 | CA | sourcing cost $4.71 set by Amazon, paid $2.36 (value-and-reversals) |
| cfea683e-d5f4-48d8-b84e-d88d3b5eeb98 | seller | 2025-04-22 | US | pre-fulfilment lost-warehouse claims paid at half the approved sourcing cost (value-and-reversals) |
| 868caeba-f91e-488a-84b7-4d93a2212db4, a8d3c233-bba5-4928-b6b8-d70a835c9e17 | sellers | 2024-09-09, 2024-11-29 | US | MCF order losses (§ 12) |
| 63437a69-1d8a-4b47-bccb-42b89b77477f | seller | 2024-08-30 | UK | MCF order delivered to a wrong address (§ 12) |
| c0d6d3da-8e43-4903-8ca1-4927549ca9a5 | seller | 2025-04-15 | UK (field); content about IT, ES, FR | limit (1) above |

Removals-disposals and inbound-shortfalls read the same field for the posts they cite (removals RM5; inbound § B, IN8); their values agree with this table for every thread both read.

---

## 3. The claim window, and how it moved

**(a) Amazon's rule, page by page.** The rule is that the window is counted from Amazon's report of the loss, and that its length is set per store and changed by announcement. The table shows which page says what for which store (store from § 2a); the lengths themselves sit in Values that move.

| Source (Amazon) | Store | Posted / effective | Counted from |
|---|---|---|---|
| Policy text, older version (hopted.com mirror) | US text (US spelling; store not stated) | before 2024-10-23 | "the date the item was reported lost or damaged in your Inventory Ledger report" |
| News 81c3235d / 6605eede | US / CA | posted 2024-07-24, eff. 2024-10-23 | "after the item was reported lost or damaged" |
| News c6da88ce (16 views) / e62a8ace (49 views) / 96a05f4a (92 views); US spelling, "calendar days"; the texts differ (below) | SA / EG / AE | posted 2024-08-06, eff. 2024-09-05 | "the date the unit is marked as 'Damaged at Amazon fulfillment centers'" / "'Misplaced' in Inventory Adjustment report" |
| News d0fc997e | UK | posted 2024-10-10, eff. 2025-01-09 | "after the item was reported lost or damaged" |
| News 1101821c / 9a92846d | SE / UK | posted 2025-01-15 | as above |
| News d8f9a56c (British spelling; 95 views, 0 replies) | AU | posted 2025-08-14, eff. 2025-10-15 | "of reported loss or damage" |
| Staff Indy_Amazon 0e07abc1 | US | 2026-08-13 | "the date the loss or damage event appears in your reports" |
| Staff Jameson_Amazon 2f44617d | UK | 2026-04-06 | lost: "of the event"; damaged: "Available immediately after the damage event is visible" |
| Staff Angie_Amazon 9d4ff2a6 | UK | 2024-10-26 | no FC window stated |
| Supply Chain Portal reimbursements policy (a different programme; filing-and-conduct FL27) | US (Supply Chain Portal) | undated, © 2026 | "the loss or damage being reported in your Inventory Adjustment report" |

The 2024-09-05 post also gives windows of its own for other claim types (missing from inbound: inbound-shortfalls IN8; removals: removals-disposals RM6). Only the Egypt thread e62a8ace adds lines for carrier-damaged returns and for customer returns lost or not received (customer-returns); the Saudi Arabia thread c6da88ce has neither line (both re-read raw 2026-11-13; the UAE thread 96a05f4a is inbound-shortfalls' reading). It links a page titled "Summary of FBA reimbursement policies and requirements for lost and damaged inventory" (/gp/help/GVTRADRKAA3XXUJ3, unread: a JavaScript shell on the US, UK, IN, AE and AU hosts). Its wording ("calendar days", "Inventory Adjustment report") differs from the other posts because it is the Middle East stores' rule set (§ 2a); no US, UK or EU post carries it.

A seller on the US store (2de1ef2f, 2024-10-16; the previous version of this file called it the EU forum) quotes Amazon text: "Starting October 23, 2024, the FBA inventory reimbursement policy for the eligibility claim windows, except for shipment to Amazon claims, will be updated from 18 months to 60 days." [official, relayed]

**(b) Practitioners.**

- Chinese sources disagree on what the old window was. 招单猫 (mjzj) [opinion] says "索赔期限从原来的180天大幅缩短到了60天" (180 days down to 60) in its body but "18个月" in its introduction. 知无不言 question 50256 (2021-12-15) [opinion] works with "最近半年（180天）" (the last half-year). ZonGuru (Mansoor Ali, 2021-10-11) [opinion]: "Claims are not accepted past the 6-month mark."
- English vendors still printing 18 months in 2026 include GETIDA's undated blog ("within 18 months of loss identification") and some 2026 guides [opinion].
- Practitioners agree that the clock runs from Amazon's report date and not from discovery (search summaries of several 2025–2026 vendor guides) [opinion].

**(c) Into a skill:** the window is a dated rule counted from the date Amazon reports the loss or damage (the ledger event date), not from the seller's discovery. Its length is not stated in the skill. **Read at run time:** G200213130 as the store shows it, and the latest News post on claim windows whose `marketplaceId` is the store (§ 2a). No SP-API operation returns a window (finance pack P-ref-16). A ledger detail row whose event date is older than the window the store's page shows is outside Amazon's stated window; whether to file anyway is the seller's choice.

---

## 4. The Inventory Defect and Reimbursement (IDR) portal

**(a) Amazon's rule.** News_Amazon, "Inventory Defect and Reimbursement portal now available", datePublished **2025-01-21**, store US by its `marketplaceId` (§ 2a; readable on every host, sellercentral.amazon.com/seller-forums/discussions/t/b175b700-09c4-4350-8a22-24f60a724042). No launch post for another store was found. The portal's scope and exclusions are held for filing by filing-and-conduct FL5; the quotes stay here as the launch record:

- "Today, we launched a new Inventory Defect and Reimbursement (IDR) portal … manage all your inventory-related defects and reimbursements within warehouse lost, warehouse damage, and customer returns".
- It gives "Complete visibility into these defects and their status"; "Detailed information for each of these defects, including type, creation date, actions taken, reasons, and current status"; "A comprehensive view of these defects from multiple reports and policy checks to identify reimbursable opportunities"; "Insights into defect frequency and the resolution rationale".
- "Note that the portal doesn't include defects under missing from inbound, removals or warehouse disposals."
- The path is FBA dashboard → Inventory → Inventory Defect and Reimbursement, or through the Reimbursements report.

The help page it links is G66ZLS453YSE2Y4R (unread: a JavaScript shell on .com and sellercentral-europe). The page's own URL for sourcing cost, linked from the 2026 staff post, is `/inventory-reimbursement/cost-management`. Amazon's Chinese pages list three statuses (finance pack P-ref-37).

A seller in the launch thread [opinion]: "I just input a transaction ID for an eligible item into a reimbursement tool and it was immediately reimbursed."

**(b) Practitioners.**

- eComEngine (Becky Trowbridge, 2025-02-13, updated 2025-03-03) [opinion]:
  - Pages: Overview, Eligible for Claim ("You must review these before Amazon begins research and decides on the claim's outcome"), In Progress, Resolved ("Amazon's reasoning for the decisions") and Defect Status Trend.
  - Resolution types: Reimbursed, Reconcile and Ineligible.
  - The Eligible for Claim table carries FNSKU, ASIN, SKU, event date and type, defect type, Transaction ID, Order ID and quantity.
  - Defect types: "warehouse damage, warehouse lost, carrier damage, customer damage, sellable, in transit, defective, fulfiller damage", "not returnable (Amazon fault)" and "not returnable (not Amazon fault)".
  - It "combines information from the inventory ledger report, customer returns report, and Amazon's FBA reimbursement policy".
- My Amazon Guy (Francisco Valadez, 2025-01-24) [opinion]: the same three statuses; it suggests the Defect Status Trend to find defects near the end of their window.
- A seller in the launch thread [opinion] reports a "bulk upload" promised on the info page but missing from the portal.

**(c) Into a skill:** the IDR portal is a Seller Central view, announced 2025-01-21. It covers warehouse lost, warehouse damage and customer returns, and leaves out missing-from-inbound, removals and warehouse disposals. No SP-API operation or report in the models read returns its Eligible for Claim list or its statuses (see FC14). **Read at run time:** nothing through the API. cx can rebuild candidate cases from the ledger and the Reimbursements report (§ 6), and the seller can see Amazon's own list in the portal.

---

## 5. How the ledger shows a loss or damage

Held in the stock pack and not redone: the reason-code table with signs (P-stock-states-34, -35), the reconciliation outcomes (P-stock-states-36), the summary view's Lost, Damaged and Found columns (P-stock-states-29), the 18-month detail history (P-stock-states-30), units in transit between FCs (P-stock-states-31), signed quantities (P-stock-states-52), and the 30-day versus 60-day researching limit (P-stock-states-13).

**What this area adds.**

- **Which codes are loss and damage candidates.**
  - Lost: M and 5, "Inventory misplaced", "missing from a bin location in a fulfillment center".
  - Damaged at an Amazon FC: 6 (from carrier-damaged), 7 (from expired), E (from sellable), H (from customer-damaged), K (from defective) and U (from distributor-damaged), each followed by a P row.
  - Back in: F ("missing inventory has been found") and N ("incorrectly assigned … or because you received an Amazon reimbursement").
  - Out: O ("incorrectly received … or because Amazon has reimbursed you").
  - D is "Inventory disposed of", outside the IDR portal (§ 4).

  The codes are reproduced from Amazon's ledger help text by Openbridge (tspicer gists) and Reason Automation (help.reasonautomation.com/seller/inventory-ledger-details, "Updated: Daily"); Amazon's SP-API page lists none [official, via third parties].
- **Which of these Amazon pays without a claim, in its own words.** The UK staff post (§ 2) says sellable units damaged in the warehouse (code E, sellable → warehouse damaged) are "Automatically reimbursed within 21 days", and that damage whose "source disposition is customer damaged, inbound carrier damaged, expired, or distributor damaged" (codes H, 6, 7, U) is "Eligible for manual claims". It also tells sellers to "Verify the item disposition shows 'Sellable' and reason is 'Damaged at Warehouse'" before using the damaged-status tool. Amazon's Chinese FBA FAQ says warehouse-damaged units cannot be removed and are reimbursed and written off automatically (finance pack P-ref-37).
- **Transaction Item ID.** Amazon's staff posts send the seller to the ledger for a "Transaction Item ID" (UK: "Locate the Transaction Item ID in your Inventory Ledger Report"). The older policy text says "You can find the transaction item ID in the Inventory Ledger report". The ledger's column is named `Reference ID` ("Transaction ID, such as a shipment ID or adjustment ID", stock pack § F5). Spaghetti (Sellers Ask Sellers, 2024-10-14) [opinion] pastes ledger "Reference IDs" in batches of 25 into "Check warehouse damaged reimbursement status". So the Reference ID of an adjustment row is what Amazon's tools call the Transaction Item ID [inferred from practitioner use; Amazon's pages do not say so].
- **A code outside Amazon's table.** Spaghetti filters warehouse damage on "Reason Codes D and G" plus dispositions "Warehouse Damaged", "Carrier Damaged" and "Sellable" [opinion]. G does not appear in the table Openbridge and Reason Automation reproduce. A store's file may carry codes the reproduced table lacks [inferred].
- **A retired report in Amazon's own instructions.** The 2026-08-13 staff post tells sellers to "Go to Reports > Fulfillment > Inventory Adjustments" and to "Filter for 'Missing' (M) events", and lists "Inventory Adjustments Report — Track lost/damaged events" as a resource. The 2024-09-05 News post and the Supply Chain Portal policy count their windows from the "Inventory Adjustment report" (the Supply Chain Portal's own pre-claim check points to the Inventory Ledger). Amazon retired that report on 2023-01-31 in favour of the Inventory Ledger (P-stock-states-28). The ledger detail view's `Adjustments` events are its successor [official dates; the mapping is inferred].
- **Researching.** `getInventorySummaries` returns `researchingQuantity`, "The number of misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers" (fbaInventory.json; P-stock-states-12) [command-verified, grep of the model clone at db2936aa].

**(c) Into a skill:** the code-to-meaning table (cited to its third-party reproduction), the two-row pattern of a disposition change, N and O as reimbursement-driven moves, and "Transaction Item ID = the ledger row's reference" as a practitioner reading. **Read at run time:** `GET_LEDGER_DETAIL_VIEW_DATA` (`eventType=Adjustments`; columns `Date`, `FNSKU`, `Event Type`, `Reference ID`, `Quantity`, `Fulfillment Center`, `Disposition`, `Reason`, `Reconciled Quantity`, `Unreconciled Quantity`), `GET_LEDGER_SUMMARY_VIEW_DATA` (`Lost`, `Damaged`, `Found`, `In Transit Between Warehouses`), and `getInventorySummaries` (`researchingQuantity` with its age buckets). Each file's header row and code values are the truth for that store; codes outside the reproduced table are to be expected.

---

## 6. How found units net against lost ones, and the practitioners' detection recipe

**(a) Amazon's rule.**

- The ledger's reconciliation outcomes for a misplaced event are "Inventory found", "Reimbursed", "Damaged inventory misplaced" or "Remaining…"; for a damaged event, "Inspected and disposition corrected", "Reimbursed" or "Remaining…" (P-stock-states-36).
- A reimbursed unit later found may have its reimbursement reversed (finance pack P-ref-18).
- Amazon's own pre-claim checks, in the older policy text (hopted.com mirror): "Check your Manage FBA Inventory report to confirm that the lost or damaged item was not found or restored to your inventory in a sellable condition or in a damaged condition for which Amazon was not at fault (for example, the item was defective)." "Check your Inventory Ledger to confirm the date and adjustment code of the loss or damage to your items." "Check your Reimbursements report to see if you have already been reimbursed for the lost or damaged item. Search by FNSKU and date to filter the results."
- Staff 2026-08-13: "Don't file prematurely — Wait for shipments to finalize and reconciliation periods to pass"; "Don't submit duplicate claims — One claim per shipment or event"; "Check your Reimbursements report regularly — Amazon auto-reimburses many warehouse damage events."

**(b) Practitioners' recipes** [opinion, each]:

- **知无不言, question 50256** (2021-12-15). Download the reconciliation report over 180 days; "直接看最后一列unreconciled（未盘点）" (go straight to the last column, unreconciled); drop blanks and zeros; F "丢失库存已找到" (lost stock found); M "库存丢失，可能是货物在各个仓库调货的时候搞丢的" (stock lost, possibly during transfers between warehouses); check the M row's FNSKU in Amazon's eligibility tool and click "创建问题" (create a case); a payment email "不出三天" (within three days). The words "M可索赔" (M is claimable) appear only in the page's AI-generated summary, not in the author's text.
- **连连 LianLian Global** (2021-11-16). Sum the E and M rows (negative) and the F and N rows (positive); "两者之差若为负数，则表示有异常库存" (a negative difference means stock is missing) and can be claimed.
- **ZonGuru** (Mansoor Ali, 2021-10-11). "Adjustments made to inventory happen in pairs": M −1 then F +1 nets to 0; remove SKUs whose adjustments offset each other.
- **Spaghetti, Sellers Ask Sellers** (2024-10-14 to 2024-10-20). Lost: ledger detail, Adjustments, "Reason Codes M and 5", "Unreconciled Quantity greater than or equal to 1"; skip recent losses as "likely to be found"; open a case with 10–25 Reference IDs, or use "Investigate an Item Lost in Warehouse". Damaged: as in § 5. Tracking: "VLOOKUPs to update the Reconciled/Unreconciled columns by matching the Reference IDs". Reversals, on their own account: "our Reimbursement Reversals for 2023 reimbursements, have been adding up to $870, out of 10k reimbursed initially" (post of 2024-10-16).
- **Seller Labs** (Nhan Dinh, 2026-03-18). Ledger detail and Reimbursements report over "at least the last ninety days"; flag negative rows with reason "Inventory misplaced", "Damaged at Amazon fulfillment center" or "Inventory disposed of"; "Match on FNSKU and date range — not just FNSKU alone"; "Inventory found" and "Reimbursed" are "already resolved". It cites an unsourced 1–3 % of revenue unclaimed (recovery-economics owns this figure).
- **sellerboard** knowledge base (undated, © 2017–2026). Scans "Units were marked as lost in the FBA warehouse and not found" and "Units were damaged by Amazon and not reimbursed", over "Cases from the last 60 days"; files under "Fulfillment by Amazon → Inventory damaged or lost in warehouse", one case at a time.
- **GETIDA** (undated, ≈2024) lists "FNSKU Reconciliation" ("all transactions for an FNSKU" against the balance) as a claim type (survey notes) and asks for "FBA warehouse IDs" and "Date/period the inventory was unaccounted for".
- **Refunzo** (Jimi Patel, 2025-07-03): wait "30 to 45 days after spotting a discrepancy" and expect investigations of "30 to 45 days".

**Pitfalls the data carries** [inferred unless tagged]:

1. N and O are not only physical finds and losses: Amazon's own text says they also move units "because you received an Amazon reimbursement" or "because Amazon has reimbursed you" (P-stock-states-35). A net of (F + N) against (M + E) can therefore count a reimbursement as a find. 连连's recipe does exactly that.
2. A find can land at a different fulfilment centre, or in a different week, from the loss. The summary view aggregates by country by default and nets them, while the detail view carries each row with its own `Fulfillment Center` (P-stock-states-29, -30).
3. Codes 3 and 4 (product redefinition) move units between FNSKUs (P-stock-states-35), so a per-FNSKU net can show a loss on one FNSKU and a gain on another.
4. No identifier links a ledger adjustment to a Reimbursements report row (finance pack P-ref-36); matching is by FNSKU, quantity and date.
5. A reimbursement paid partly in inventory (`quantity-reimbursed-inventory`, finance pack P-ref-17) puts units back, likely as an N row [inferred].
6. Unknown Events in the summary shrink when the period is widened (P-stock-states-33).

**(c) Into a skill:** the disciplines Amazon itself names (confirm not found, confirm date and code, confirm not already reimbursed by FNSKU and date), and the pitfalls above. The practitioners' recipes are their opinion and are stated as choices, without picking one. **Read at run time:** the ledger detail view (Adjustments) and `GET_FBA_REIMBURSEMENTS_DATA` (`approval-date`, `reason`, `fnsku`, `quantity-reimbursed-*`, `original-reimbursement-id`). The Reimbursements report needs the Pricing or Amazon Fulfillment role, and the ledger needs Amazon Fulfillment (P-ref-19, P-stock-states-50).

---

## 7. Filing by hand: routes and the evidence Amazon asks for

**(a) Amazon's rule.**

- **Routes.** The entry point for each claim kind (warehouse damaged: the "Check warehouse damaged reimbursement status" tool by Transaction Item ID; warehouse lost: a Get Support case by FNSKU or Transaction Item ID), as the US staff post of 2026-08-13 gives them, is held by filing-and-conduct FL4 (see filing-and-conduct FL4). What this area adds: the UK staff post (2026-04-06, store UK) words the lost route as "Provide either the Transaction Item ID or FNSKU; Submit through Contact Us with relevant details", and the older policy text as "For damaged items, enter the transaction item ID in the following tool to check your eligibility and file a claim."
- **Evidence.**
  - Older policy text: "You may be asked to provide additional information such as the date or location (for example, the Amazon fulfillment center ID) of the loss or damage to your item."
  - UK staff list: "Transaction Item ID or FNSKU; Date and location of the loss or damage; Amazon shipment ID (for inbound issues); Proof of inventory ownership (invoice, receipt, or packing slip); Proof of delivery for inbound shipments".
  - Staff 2026-08-13, for units unsellable when lost: "we may request additional information or documentation to help us determine this adjusted value".
  - Supply Chain Portal policy (a different programme): for FC operations claims, "You must provide proof of the item's purchase value or manufacturing cost."
- **Outcome forms.** Replacement "with a new one of the same FNSKU" or reimbursement (older policy text; finance pack P-ref-40).
- **IDR.** Its Eligible for Claim page (§ 4), the launch-thread seller's "transaction ID" tool, and Manage Your Sourcing Cost.

**(b) Practitioners.**

- Spaghetti [opinion]: the results-page option of the damaged tool "never worked", so they open cases manually.
- 雨果网 2019 [opinion, history]: "Investigate Inventory Damaged in FBA Warehouse" form with a CSV attached.
- ZonGuru 2021 [opinion]: more than five requests at once, early requests or thin data "can delay a response".
- filing-and-conduct owns case limits and penalised conduct.

**(c) Into a skill:** that Amazon routes damaged units through a Transaction-Item-ID tool and lost units through a case or Contact Us with the FNSKU or Transaction Item ID, and the evidence fields Amazon names. **Read at run time:** the tool names and menu path as the store shows them (G200213130; G66ZLS453YSE2Y4R). No SP-API operation files a claim (sp-api-claims-surface).

---

## 8. Value, cap and dispute window as they bear on this area (pointer)

The valuation rules (sourcing cost before an order, sale price minus fees after an order, a reduced estimate for unsellable units) are held as finance pack P-ref-14, -15 and -40 and by value-and-reversals (VR1–VR5, VR25–VR27). The per-unit cap is value-and-reversals' (see value-and-reversals VR29), and so is the valuation-dispute window (see value-and-reversals VR20). Two store attributions from § 2a bear on them: the "£2,000 per unit" and "within 90 days" staff post 9d4ff2a6 is the **UK** store's, not an EU forum post; the "Re-evaluation requests: Within 90 days of initial claim" post d8f9a56c is the **Australia** store's, not a store-less or US post. The UK contradiction on valuation (staff "estimated proceeds" against the UK posts and PDF) is in § 2 and FC35.

---

## 9. Transfers between fulfilment centres, AWD, and outbound before delivery

**(a) Amazon's rule.**

- **Between FCs.** The ledger summary carries "In Transit Between Warehouses" separately from the ending balance (P-stock-states-31), and the detail view has a `WhseTransfers` event type (stock pack § F3). In pages read, Amazon names no separate claim type for a transfer loss. A unit lost in transfer is a warehouse-lost case in the 2026 staff post's scope ("handled by Amazon … to fulfillment centers") [inferred]. An Amazon moderator said of negative ledger rows on a shipment reference: "those units might be in transfer to another warehouse. It's hard to say without looking at the reason code in the inventory ledger" (TaylorR_Amazon, 2024-08-21; P-stock-states-52).
- **AWD, inside AWD.** The AWD service terms ("Dated: January 14, 2026", supplychain.amazon.com/legal/service-terms/warehouse-and-distribution) say: "we will replace that Unit with a new Unit of the same FNSKU or we will reimburse you for it". For facility losses, "the claim window starting on the date that the Unit was identified by Amazon as lost or damaged"; valuation is "according to the valuation methodology described in the" MCF inventory reimbursement policy. A seller (Seller_qHNihHIQx9ShU, sellercentral.amazon.com …/t/10da82b7-d167-419d-90d3-a35d6ec6af52, 2024-09-17) quotes AWD help page GHV89YC29VWN6SBM: "Under-the-roof reimbursement: During facility audit or replenishment of boxes to the FBA network, if Amazon Warehousing and Distribution operations identify a lesser number of boxes than originally reported as received because boxes were damaged or lost by Amazon, Amazon will reimburse the fair value of the inventory. Sellers are required to submit a case to Selling Partner Support…" [official, relayed]. Staff (Topher_Amazon) passed the case on.
- **AWD to FBA.** The 2026 staff post's replenishment sentence (§ 1) puts these losses at sourcing cost. Sellers report replenishment shipments "created by Amazon Distribution Program" under FBA shipment ids with "Replenishment Order ID: repl-…", with units never received (…/t/1d0a23e7-0e7b-4442-8438-0040624175aa, 2025-11-26). One seller was asked for carrier tracking they cannot hold because "the shipment was made completely within Amazon's system" (…/t/b738f397-d7d3-44f3-b511-823b60c97a8d, 2025-08-21) [opinion]. Staff (Glenn_Amazon, Topher_Amazon) asked for ids and gave no rule. These arrive as inbound shortfalls on an FBA shipment (inbound-shortfalls owns them). The stock pack notes AWD transfers arriving in the ledger as receipts, some negative (P-stock-states-52).
- **Outbound before delivery.** The Reimbursements report's `Lost_Outbound` and `Damaged_Outbound` values (P-ref-35) and the post-order valuation, "sales price on the original order minus applicable fees" (P-ref-14), are Amazon's side. Customer-facing refunds for damage in transit are customer-returns' area. An Amazon reply in "Why are sellers denied reimbursement for 'damaged in transit' on non-returnable FBA food items" (…/t/c0d7f362-b3ce-4f87-a458-64fd00723a9e, 2026-03-13) is cited there.

**(b) Practitioners.** 知无不言 50256 [opinion]: M can arise "during transfers between warehouses". A search summary cites a guide that names a common rejection: "inventory appears lost but is still in transit between Amazon warehouses" [opinion, unattributed].

**(c) Into a skill:** a transfer loss shows as an adjustment (M or 5) and not as a column of its own. AWD has its own terms and its own window start. AWD-to-FBA shortfalls are read through the FBA shipment. **Read at run time:** the ledger summary by `aggregateByLocation=FC` for `In Transit Between Warehouses`; the AWD terms page (supplychain.amazon.com/legal/service-terms/warehouse-and-distribution). The AWD API model carries no lost or damaged field (FC32). Cross-border moves: § 11.

---

## 10. What the SP-API carries for this area (command-verified against the model clone db2936aa, 2026-10-29)

- `fbaInventory.json`: `researchingQuantity` / `ResearchingQuantityEntry`, "The misplaced or warehouse damaged inventory that is actively being confirmed at our fulfillment centers", and `warehouseDamagedQuantity` under unfulfillable. These are the only hits for "misplaced" across the models.
- `financesV0.json`: `AdjustmentType` `FBAInventoryReimbursement`, "An FBA inventory reimbursement to a seller's account. This occurs if a seller's inventory is damaged" (the wording names damage only, though lost units post under the same type in practice, P-ref-21); `LostOrDamagedReimbursement` is "An Amazon Easy Ship reimbursement … for a package that we lost or damaged", which is not FBA.
- The AWD model (`awd_2024-05-09.json`) has no lost, damaged, discrepancy or reimbursement field; the only "damaged" hit is a packaging description.
- The Data Kiosk and notification schemas carry no reimbursement or misplaced field. `ShipmentTrackingMilestoneChangedNotification`'s `LOST` value is a carrier-shipment milestone, not an FBA unit.
- The Support API (`support-api-model`) reads cases (sp-api-claims-surface owns it).

- Finances v0 `AdjustmentEvent` carries `StoreName` ("The name of the store where the event occurred") and `AdjustmentAmount` as a `Currency` (`CurrencyCode`, "The three-digit currency code in ISO 4217 format"); Finances v2024-06-19 `Transaction` carries `marketplaceDetails.marketplaceId` ("The identifier of the marketplace where the transaction occurred") and `totalAmount`. These are where a reimbursement's store and currency are read (§ 11).

---

## 11. Units lost in cross-border transfers (Pan-EU, EFN, UK–EU) and NA Remote Fulfillment

**(a) Amazon's rule.**

- **Moving units is Amazon's right, and loss while stored is reimbursed under the guidelines.** Amazon's AU Business Solutions Agreement (PDF on m.media-amazon.com, "AmazonServicesBusinessSolutionsAgreement_2024edits1.pdf", created 2024-06-12, for "Amazon.com.au sellers"; read 2026-11-13), FBA Service Terms F-4: "We may move Units among facilities. If there is a loss of or damage to any Units while they are being stored, we will reimburse you in accordance with the FBA Guidelines … Except as provided in this Agreement, you and not Amazon will be responsible for any loss of, or damage to, any Units." The US agreement's FBA terms are read by customer-returns (G1791 v1 r31); its F-4 was not read by an open route in this pass.
- **Replenishment losses.** The 2025-02-24 policy PDFs (US, UK) put "lost and damage claims during inventory replenishment handled by Amazon or on behalf of Amazon to fulfillment centers or non-Amazon buildings in marketplaces where we provide the service" at sourcing cost (value-and-reversals VR4). No page read says whether a Pan-EU cross-border move is "replenishment" in this sense.
- **No claim type of its own.** No Amazon page read (policy PDFs US/UK/DE 2025-02-24, the News posts in § 2a, the staff posts) names a claim type, window or route for a unit lost while Amazon moves it between countries under Pan-EU, between the UK and the EU, or for an EFN order; nor does any say in which store such a loss is reported or reimbursed.
- **What the data carries.** The ledger detail view lists `WhseTransfers` as an event type and carries `Fulfillment Center`, `Country` and `Store` on each row (stock pack § F3, P-stock-states-30); the summary view keeps units moving between centres in "In Transit Between Warehouses" (P-stock-states-31). A unit lost during a move therefore appears as an `Adjustments` row (M or 5) at some centre and country, with the transfer itself as `WhseTransfers` rows [inferred from the column list; no Amazon text describes a cross-border loss row].
- **Store and currency of the money.** The Reimbursements report carries `currency-unit` per line (value-and-reversals; finance pack P-ref-19), Finances v0 `AdjustmentEvent` carries `StoreName` and a currency code, and Finances v2024-06-19 carries the transaction's `marketplaceId` (§ 10) [command-verified, db2936aa]. No Amazon page read states the rule (store of storage, of the account's home, or of sale). A developer reports that the Reimbursements report returns the same rows whatever `marketplaceIds` names within a region (see sp-api-claims-surface SU24). One ERP tells sellers to file in the Seller Central of the store where the event happened (see filing-and-conduct FL40) [opinion].
- **NA Remote Fulfillment.** Amazon's page (sell.amazon.com/fulfillment-by-amazon/remote-fulfillment, undated, read 2026-11-13): "Create offers on Amazon.ca, Amazon.com.mx, and Amazon.com.br, and we'll use your US FBA inventory to deliver orders across the border with Prime shipping"; sellers reach those stores "without sending inventory to those countries". The units stay in US centres, so a unit lost or damaged in a centre before an order is a US centre event [inferred]; one lost after a CA, MX or BR order is an outbound or customer-return case (customer-returns). No page read states the store or currency of a reimbursement for a Remote Fulfillment unit.
- **EFN.** The finance pack holds that EFN's cross-border fee is set by the store where the order is placed and the inventory pool it ships from (finance pack reconciliation.md, official via search snippets). Units under EFN stay in the home country's centres [inferred from the same]; nothing read addresses their loss.

**(b) Practitioners.** One seller counted "the 1500 units Amazon lost on FC transfer" (Sellers Ask Sellers, packetfire, 2024-01-30; see recovery-economics EC16) [opinion; one account, no store stated]. 知无不言 50256 (2021) attributes M rows to transfers between warehouses (§ 9) [opinion]. No practitioner source read states which store or currency a Pan-EU or Remote Fulfillment reimbursement posts in; the web searches for one (English and Chinese) returned nothing citable, and the session's search budget ran out before a second round.

**(c) Into a skill:** a cross-border transfer loss is a fulfilment-centre loss in the ledger, read per row with its `Fulfillment Center`, `Country` and `Store`; Amazon states no separate rule for it. **Read at run time:** the ledger detail view (`Adjustments` and `WhseTransfers`); the Reimbursements report's `currency-unit`; the transaction's `marketplaceId` and currency in Finances. Which store a reimbursement lands in is read from those fields, not assumed.

---

## 12. MCF units lost or damaged in Amazon's hands

**(a) Amazon's rule.** Which page is the "MCF inventory reimbursement policy" that the AWD terms name, and whether the Supply Chain Portal page is it, belongs to inbound-shortfalls (see inbound-shortfalls IN26; filing-and-conduct FL27). What bears on this area:

- An MCF unit stored in an FBA centre and lost or damaged there before an order is FBA inventory, the same as any unit [inferred: the ledger and the FBA policy draw no line by sales channel]. The difference begins with the MCF order.
- **The Supply Chain Portal page** (supplychain.amazon.com/support/reimbursements, read 2026-11-13; for an active MCF account, filing-and-conduct FL27) has a section "MCF order related claims": "This section applies to eligible items in your MCF order that are lost, damaged in transit to the buyer, or have an incorrect item delivered. Orders that are marked as delivered by the carrier aren't eligible for lost order reimbursement. Additionally, Late deliveries beyond the promised date aren't eligible for any reimbursement." It sets an earliest day for a lost claim after the promised or estimated delivery date and a latest day after the estimated delivery date (values in Values that move), files "through the Contact Us page in Supply Chain Portal", and values "based on the refund or replacement given to the customer on your MCF order, up to a maximum of $300.00 per unit … with MCF fees subtracted from it".
- **Amazon India's MCF page** ("Reimbursements for your MCF orders", smartcommerce.amazon.in/blog/mcf-reimbursements-for-your-mcf-orders, dated Jan 24, 2023, read 2026-11-13): "You're eligible for reimbursements on your MCF orders if we determine that they have been lost or damaged due to reasons attributable to us"; ineligible if "You use MCF as a way to remove items from a fulfillment center" or "You use MCF as a way to fulfill Amazon orders"; "MCF fulfilment fee is ineligible for reimbursement"; valued at "estimated Fair Market Value" because "MCF orders occur outside Amazon.in, we don't have a record of the sale price"; "Orders that are marked as delivered by the carrier aren't eligible for reimbursement." Its windows differ from the Supply Chain Portal's (Values that move).
- **Contract.** MCF units are the seller's to refund and return (BSA F-6.1, F-6.4; see customer-returns RT44; the AU PDF of 2024-06-12 carries the same F-6.1 and F-6.4).

**(b) Practitioners and sellers** [opinion, each]:

- US seller (868caeba, 2024-09-09): an MCF order for an Etsy sale "marked as LOST" was paid at "HALF of what the item was worth"; Seller Support quoted "MCF fulfillment fees and items in orders that are marked as delivered by the carrier aren't eligible for reimbursement" and "estimated proceeds of sale".
- US seller (a8d3c233, 2024-11-29): an MCF order used to fulfil an Amazon FBM order and delivered to a wrong address was refused because MCF was used "as a means to fulfill your Amazon order".
- UK seller (63437a69, 2024-08-30): an MCF order for eBay delivered to the wrong house was refused under "a policy that doesn't cover MCF orders once they've been delivered".

**(c) Into a skill:** an MCF unit lost in a centre is an FBA centre loss; an MCF order lost or damaged on the way to the buyer is an MCF claim with its own window, value basis, cap and route, and an order marked delivered by the carrier is outside it by Amazon's pages. **Read at run time:** the MCF page for the seller's store (inbound-shortfalls holds which page that is); `FULFILLMENT_ORDER_STATUS` / `FBA_OUTBOUND_SHIPMENT_STATUS` for the order's state (see sp-api-claims-surface).

---

## 13. Vine units

**(a) Amazon's rule.** Amazon's Vine page (sell.amazon.com/tools/vine, undated, read 2026-11-13): enrolled products need "a listing with FBA selected as the fulfillment method"; "FBA inventory must be sent to Amazon fulfillment centers for products to be shipped to Vine Voices"; the seller specifies "the number of units you'd like to make available" and tracks "claimed quantity" on the Vine dashboard; the enrolment fee is not charged "If you don't receive a Vine review within 90 days from the date of enrollment" (the fee and its posting are the finance pack's, selling-fees H1; a fee charged wrongly is fee-overcharges'). The page says nothing about a Vine unit lost or damaged in a centre or on its way to the reviewer, and no Amazon page read does.

**(b) Practitioners.** None found. A seller reply relayed in search results says a Vine reviewer who receives a damaged item can ask for a replacement [opinion, snippet; damage after delivery, not before].

**(c) Into a skill:** a Vine unit is FBA inventory until it ships, so a unit lost in a centre before it ships to a Vine Voice is a centre loss like any other [inferred]; nothing read says how a unit lost on its way to a reviewer is treated. **Read at run time:** the ledger detail view for the unit's movements; the Vine dashboard's claimed quantity is in Seller Central only.

---

## 14. Unreconciled loss rows older than the ledger's reach

**(a) Amazon's rule.**

- The ledger detail view lists "all historical movements of your inventory for 18 months" (*FBA Reports*; see sp-api-claims-surface SU15; P-stock-states-30). A row older than that is no longer in a file requested now.
- Every FC-operations window read is counted from the date Amazon reported the loss (§ 3), and none read is longer than the ledger's reach (Values that move). A loss row that has left the ledger is therefore outside every window Amazon has stated, in every store with a stated window [read, by comparing the stated values].
- No Amazon page read says what becomes of an `Unreconciled Quantity` that never reconciles: whether Amazon reimburses it, writes it off, or leaves it open. The reconciliation outcomes Amazon lists are held as P-stock-states-36.
- A report's look-back and a claim's window are different facts (see sp-api-claims-surface SU18).

**(b) Practitioners.** Seller Labs (2026-03-18) audits at least the last 90 days; 知无不言 (2021) read 180 days of the older report (§ 6) [opinion]. None read addresses rows past 18 months.

**(c) Into a skill:** an unreconciled loss older than the ledger's reach can only be seen in a copy the seller or cx kept earlier; Amazon states no rule for it beyond the windows. **Read at run time:** the ledger detail view as far back as it reaches; any earlier copy the seller holds.

---

## 15. Exclusions: expired, recalled, disposed, opted-out and force-majeure cases

**(a) Amazon's rule.**

- **Eligibility, in Amazon's PDFs** (US and UK, created 2025-02-24, read 2026-11-13; US text layer, which can merge struck text, value-and-reversals VR28): "The item is registered in FBA at the time it is lost or damaged"; "The item complies with FBA product restrictions and with FBA inventory requirements"; "The item is not pending disposal or was not disposed of at your request or because we have exercised a right to do so"; "The item is not defective and was not damaged by a customer"; account status (filing-and-conduct FL13, FL34). The US text adds "The shipment for the item is not in canceled or deleted status." Neither PDF names expiry, recall or force majeure.
- **Expired stock damaged at the centre (code 7).** The UK staff post (2026-04-06) lists "expired" among the source dispositions whose damage is "Eligible for manual claims" (§ 2). Amazon's *FBA Damaged Inventory Ownership* page classes "expired" with customer-damaged, defective and distributor-damaged as seller-fault for its damage-fault evaluation (see customer-returns RT10; that page was read by customer-returns through the help hub's content call, a route since closed, and is carried here by pointer only). The two are stated; no page read reconciles them.
- **Recalled stock.** The returns sections exclude returned items "subject to recall" (customer-returns RT3; the Supply Chain Portal page has the same sentence). The AU agreement (2024-06-12 PDF, S-3.1) makes the seller "responsible for … any public or private recall of or safety alert for any of Your Products … and will reimburse us for any costs we may incur". No page read excludes a recalled unit lost in a centre, or includes one.
- **Damaged-inventory ownership opt-out.** A seller who opts an ASIN out has eligible damaged units "always marked 'defective'", and they "will not be eligible for damage reimbursements"; enrolment covers "Amazon-fault warehouse damaged inventory" (see customer-returns § 3, G9MAM9ELJTSSNYS5 v4, carried by pointer).
- **Force majeure.** The AU agreement, General Terms 12: "We will not be liable for any delay or failure to perform any of our obligations under this Agreement by reasons, events or other matters beyond our reasonable control." No reimbursement page read applies or disapplies it to units destroyed by fire, flood or similar events, and no Amazon post read addresses such an event.

**(b) Practitioners.** Refunzo lists "natural disasters" among what removal reimbursement does not cover (see removals-disposals § A) [opinion; removals, not FC losses]. My Amazon Guy (2025-10-31) reports found units coming back expired and charged for removal or disposal (FC28) [opinion].

**(c) Into a skill:** the exclusions Amazon states are the eligibility list above; expiry is stated both ways by Amazon's own pages; recall and force majeure have no FC-loss rule in any page read. **Read at run time:** G200213130 as the store shows it; the ledger row's disposition and reason code (7 = from expired, § 5).


---

## Only in Seller Central

- The IDR portal: Overview, Eligible for Claim, In Progress, Resolved, Defect Status Trend.
- Manage Your Sourcing Cost (`/inventory-reimbursement/cost-management`).
- "Check warehouse damaged reimbursement status" (Transaction Item ID).
- The "Inventory Lost in Warehouse" case route and "Investigate an Item Lost in Warehouse".
- Contact Us for valuation disputes and re-evaluation.
- The policy pages G200213130, G66ZLS453YSE2Y4R, GVTRADRKAA3XXUJ3, G4FKT5KQWFFJ7LDN (ledger help) and GHV89YC29VWN6SBM (AWD).
- The Vine dashboard's claimed quantity per enrolment (§ 13).
- The FBA settings for damaged-inventory ownership (opt-out per ASIN, § 15).
- MCF order claims: the Supply Chain Portal's Contact Us page (for a Supply Chain Portal account) or Selling Partner Support (§ 12).

---

## The seller's choices (stated, none picked)

- **Wait for Amazon's automatic reimbursement, or file as soon as an event appears.** Waiting relies on Amazon's stated automation and keeps clear of "Don't file prematurely" (staff 2026). Filing early can meet "Don't submit duplicate claims" against an automatic payment. The window keeps running in either case (§ 3).
- **Enter sourcing costs on Manage Your Sourcing Cost, or leave Amazon's estimate.** This changes the value of pre-order losses (P-ref-14); the UK-forum seller's "£8.86 Amazon estimated" for an item the manufacturer sells at £46 is one reported outcome.
- **Audit alone, with software, or with a service.** recovery-economics owns the figures. The service's filing and conduct are filing-and-conduct's.
- **For a UK store, read the 2026 UK staff post's longer lost window as the operative one, or the UK News posts' shorter window** (FC5). Each side is Amazon's; the seller decides which to act on, and the store's G200213130 and the claim form's own reply are where it is tested.

---

## Positions

FC1. A fulfilment-centre operations claim covers eligible units "lost or damaged by an Amazon fulfillment center or a facility operated on behalf of Amazon, after Amazon receives them from you", and such losses "are reported in your Inventory Ledger report". Amazon's own policy PDFs (US and UK, created 2025-02-24) carry the general clause that an item "lost or damaged at a facility or by a carrier operated by Amazon or on behalf of Amazon" is replaced with a new item of the same FNSKU or reimbursed. Sources: Amazon's help article "FBA inventory reimbursement policy", older version, via the hopted.com mirror (FC-operations wording); Redlined_FBA_Reimbursement_policy_US.pdf and _UK.pdf on m.media-amazon.com (general clause). [read in official docs; the FC-operations wording via a third-party mirror]

FC2. Amazon staff on the US store (2026-08-13) extend sourcing-cost valuation to "lost and damage claims during inventory replenishment handled by Amazon or on behalf of Amazon to fulfillment centers or non-Amazon buildings in marketplaces where we provide the service"; the US and UK policy PDFs of 2025-02-24 carry the same sentence (value-and-reversals VR4). Source: Indy_Amazon, 0e07abc1 (store US, § 2a). [read in official docs, staff]

FC3. News_Amazon posted on 2024-07-24, in the thread whose store is the US (81c3235d, `ATVPDKIKX0DER`), that from a stated date Amazon would "proactively reimburse you for … items that are lost in our fulfillment centers … as soon as an item is reported as lost". It said "almost all" warehouse-lost, warehouse-damaged and customer-return cases would be reimbursed proactively, that a manual claim remains for any not reimbursed, and that all removal claims stay manual. Source: 81c3235d. [read in official docs; store command-verified, § 2a] Extends finance pack P-ref-13 with the US thread.

FC4. Amazon announced proactive reimbursement of FC-lost units store by store, each in its own News thread with its own start date: the US (81c3235d) and Canada (6605eede) posts of 2024-07-24 and the UK post of 2024-10-10 (d0fc997e); the US, UK and Canada valuation posts of 2024-12-18 (68864b6f, a941ac02, da761b17) each restate "We now offer automatic reimbursements for items lost in our fulfil(l)ment cent(re|er)s". No such announcement was found for any other store; Sweden's, the Middle East stores' and Australia's posts change windows only. A store's date is read from the post whose `marketplaceId` is that store (§ 2a); the dates are in Values that move. Sources: the posts named; AMZ123 wW7n3WJP assigns the 2025 date to "欧洲站点" [opinion], which the post's field narrows to the UK. [read in official docs; store command-verified on the post field, § 2a; absence for other stores is a search result]

FC5. Contradiction in the UK: a UK staff post (Jameson_Amazon, 2f44617d, 2026-04-06, store UK) says UK warehouse-lost inventory "Currently requires manual claim submission (automatic reimbursement disabled since August 2022)", with a window counted from "the event", and that warehouse damage to sellable units is reimbursed automatically within a stated period. Amazon's UK News posts state automatic lost reimbursement (d0fc997e, 2024-10-10, with a start date; a941ac02, 2024-12-18, "We now offer") and a shorter manual window (d0fc997e; 9a92846d, 2025-01-15). Both are stated; neither is picked. The values on each side are in Values that move. Sources: 2f44617d; d0fc997e; a941ac02; 9a92846d (all store UK by `marketplaceId`). [read in official docs]

FC6. Amazon's 2021 text says that for adjustments after 2021-03-19 Amazon handles the 30-day researching duration, so sellers need not wait 30 days to file. Source: held as P-stock-states-51 (forum thread 5b46fd45, 2021-04-07, store UK by its field, official via seller). [read in official docs, relayed] History; cited, not redone.

FC7. Before the 2024 change, Amazon's policy text set the FC operations claim window at a length counted from "the date the item was reported lost or damaged in your Inventory Ledger report" (value in Values that move). A seller on the US store relays Amazon text: "Starting October 23, 2024, the FBA inventory reimbursement policy for the eligibility claim windows, except for shipment to Amazon claims, will be updated from 18 months to 60 days." Sources: hopted.com mirror; 2de1ef2f (2024-10-16, store US; earlier called an EU-forum post here). [read in official docs, via mirror and relay]

FC8. Chinese practitioner sources give the pre-2024 window as 180 days (招单猫 on mjzj; 知无不言 50256, 2021), against Amazon's 18 months. The 180-day figure is not supported by any Amazon text read. Sources: as named. [opinion]

FC9. The FC lost or damaged claim window is set per store and changed by announcement; its length for a store is read at run time from G200213130 as that store's host shows it and from the latest News post on claim windows whose `marketplaceId` is that store (§ 2a), and no SP-API operation returns it. Posts read carry windows for US (81c3235d; staff 0e07abc1), CA (6605eede), UK (d0fc997e, 9a92846d; staff 2f44617d, which disagrees, FC5), SE (1101821c), SA, EG and AE (c6da88ce, e62a8ace, 96a05f4a), and AU (d8f9a56c). None was found for DE, FR, IT, ES, NL, PL, BE, IE, JP, IN, MX, BR, TR or SG. Values: Values that move. [read in official docs; stores command-verified, § 2a]

FC10. The FC window starts from Amazon's report of the event ("after the item was reported lost or damaged"; "the date the loss or damage event appears in your reports"; "the date the unit is marked as … 'Misplaced'"), not from the seller's discovery. Sources: 81c3235d; 0e07abc1; c6da88ce. [read in official docs]

FC11. The 2024-08-06 window set (effective 2024-09-05; "calendar days"; counted from the "Inventory Adjustment report") was issued for the Saudi Arabia (c6da88ce), Egypt (e62a8ace) and UAE (96a05f4a) stores, not for the US, the UK or the EU. The copies differ: only the Egypt thread lists carrier-damaged returns and lost customer returns. It links "Summary of FBA reimbursement policies and requirements for lost and damaged inventory" (GVTRADRKAA3XXUJ3, unread). Source: the three threads, `marketplaceId` read 2026-11-13. [read in official docs; stores command-verified, § 2a]

FC12. Pitfall: Amazon's staff post of 2026-08-13 directs sellers to "Reports > Fulfillment > Inventory Adjustments", and the 2024-09-05 News posts of the Saudi Arabia, Egypt and UAE stores and the Supply Chain Portal policy count their windows from the "Inventory Adjustment report", which Amazon retired on 2023-01-31 in favour of the Inventory Ledger. Sources: 0e07abc1; c6da88ce; supplychain.amazon.com/support/reimbursements; P-stock-states-28. [read in official docs; the ledger-as-successor mapping is inferred]

FC13. The IDR portal was announced by News_Amazon on 2025-01-21 in a thread whose store is the US (b175b700); no launch post for another store was found. Its scope and exclusions are held for filing by filing-and-conduct FL5 (see filing-and-conduct FL5). Source: b175b700 (datePublished 2025-01-21, read raw). [read in official docs] Adds the date and store to finance pack P-ref-13 / § E3.

FC14. No operation or schema in the SP-API model clone returns the IDR portal's Eligible-for-Claim list, its statuses or its resolution reasons. Source: grep of models and schemas for "misplaced", "reimburs", "defect" (db2936aa); the "defect" hits are account-health, tracking and the Finances invoices model's `defectTypes` (invoice discrepancies such as `PRODUCT_COST_NOT_ACTIVE`), none of them IDR. Upstream main at b13d1d1 (2026-11-10) adds only an Analytics Economics schema change with no relevant field. [command-verified for models; for report types, inferred from the FBA Reports page as read by the finance pack]

FC15. Practitioners describe the IDR pages as Overview, Eligible for Claim, In Progress, Resolved and Defect Status Trend, with resolutions Reimbursed, Reconcile and Ineligible, built from the ledger, the customer returns report and the policy. Sources: eComEngine (2025-02-13); My Amazon Guy (2025-01-24). [opinion]

FC16. (withdrawn: the entry points by claim kind are homed in filing-and-conduct; see filing-and-conduct FL4. This file keeps only the UK staff wording of the lost route, § 7.)

FC17. Amazon locates the Transaction Item ID in the Inventory Ledger. Practitioners paste the ledger's `Reference ID` into the damaged-status tool, so the Reference ID of an adjustment row serves as the Transaction Item ID. Sources: 2f44617d; older policy text; Spaghetti, Sellers Ask Sellers (2024-10-14) [opinion]. [inferred]

FC18. The evidence Amazon names for a fulfilment-centre claim is the date or location of the loss (for example the FC ID), the Transaction Item ID or FNSKU, and proof of ownership. For a unit unsellable when lost, Amazon "may request additional information or documentation" to set a reduced value. Sources: older policy text (mirror); 2f44617d; 0e07abc1. [read in official docs]

FC19. In Amazon's UK staff wording, warehouse damage to sellable units is reimbursed automatically within a stated period (Values that move), and damage whose source disposition was customer damaged, inbound carrier damaged, expired or distributor damaged is "Eligible for manual claims". Source: 2f44617d (store UK). [read in official docs, staff, UK only]

FC20. Amazon's older policy text names three pre-claim checks: confirm in Manage FBA Inventory that the unit was not found or restored, confirm the date and adjustment code in the Inventory Ledger, and confirm in the Reimbursements report, "by FNSKU and date", that it was not already reimbursed. Source: hopted.com mirror of the policy. [read in official docs, via mirror]

FC21. (withdrawn: premature and duplicate filing as conduct are homed in filing-and-conduct; see filing-and-conduct FL7 and FL11. The US staff post's "Don't file prematurely" and "Don't submit duplicate claims" stay quoted in § 6 as Amazon's pre-claim discipline.)

FC22. The ledger codes that mark an FC loss are M and 5 (misplaced). Damage at an FC is 6, 7, E, H, K and U, each followed by P. Found is F and N, correction is O, and disposed is D. N and O also move units because of a reimbursement. Source: held as P-stock-states-34 and -35 (Openbridge and Reason Automation reproductions of Amazon's ledger help). [read in official docs, via third parties] Cited, not redone.

FC23. Practitioners select open losses in different ways, stated here as choices side by side, none Amazon's and none picked: Spaghetti (2024-10-14) filters the ledger detail view's Adjustments on reason codes M and 5 with an unreconciled quantity of at least one; 知无不言 50256 (2021-12-15) drops blank and zero unreconciled rows of the older reconciliation report and reads the M rows; Seller Labs (2026-03-18) flags negative rows with the reasons for misplaced, damaged and disposed. [opinion]

FC24. Practitioners who net losses against finds do it in different ways, stated as choices, none picked: per pair of rows, M −1 then F +1 nets to 0 (ZonGuru, 2021-10-11); per FNSKU, (E + M) against (F + N), a negative difference read as missing stock (连连, 2021-11-16). FC25 and FC26 are the pitfalls each choice meets. [opinion]

FC25. Pitfall: because N and O also record reimbursement-driven moves, a net that counts N as a find can treat a reimbursement as a recovered unit. Sources: P-stock-states-35; 连连 recipe. [inferred]

FC26. Pitfall: a found unit can appear at a different fulfilment centre, on a different date or under a different FNSKU (codes 3 and 4) from the loss. A net computed on the summary view by country hides this, while the detail view carries each row's `Fulfillment Center`. Sources: P-stock-states-29, -30, -35. [inferred]

FC27. Practitioners match a ledger loss to a Reimbursements report row by FNSKU and date range, not by FNSKU alone, because no identifier links the two. Sources: Seller Labs (2026-03-18) [opinion]; finance pack P-ref-36. [opinion]

FC28. Found units can come back months after a reimbursement, with the reimbursement reversed and the units sometimes expired and charged for removal or disposal. Source: My Amazon Guy (Noah Wickham, 2025-10-31), relaying seller reports. A seller reply on 0e07abc1 ("Then a year later their inventor was 'found' and they were billed for storage and disposal fees") describes an inbound shortfall that was never paid, not a reversal, and supports only the late find and the fees. [opinion] Reversal mechanics: finance pack P-ref-18.

FC29. Practitioner Spaghetti reports reversals of $870 on $10,000 reimbursed in 2023 on one account. Source: Sellers Ask Sellers 4875 (post of 2024-10-16, datePublished 2024-10-16T14:02Z; corrected from 2024-10-17). [opinion; one account]

FC30. `getInventorySummaries` returns `researchingQuantity`, "the misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers". It is the only SP-API field that names misplaced units. Source: fbaInventory.json (db2936aa), grep. [command-verified] Extends P-stock-states-12.

FC31. The Finances v0 model describes `FBAInventoryReimbursement` as occurring "if a seller's inventory is damaged". `LostOrDamagedReimbursement` is an Easy Ship type, not FBA. Source: financesV0.json (db2936aa). [command-verified]

FC32. The AWD API model, the Data Kiosk schemas and the notification schemas carry no field for lost, damaged or reimbursed units. Source: grep of the model clone (db2936aa). [command-verified]

FC33. (withdrawn: the per-unit cap is homed in value-and-reversals; see value-and-reversals VR29. The store of the "£2,000" staff post 9d4ff2a6 is the UK, § 2a.)

FC34. (withdrawn: the valuation-dispute window is homed in value-and-reversals; see value-and-reversals VR20. Its evidence posts are the UK staff post 9d4ff2a6 and the Australia post d8f9a56c, § 2a.)

FC35. Contradiction on valuation in the UK: UK staff (2f44617d, 2026-04-06) describe reimbursement on "estimated proceeds - your item's value minus applicable fees", while Amazon's UK News post a941ac02 (2024-12-18, store UK, previously read here as an EU post) and its postponement 0252e05d (2025-02-28, store UK) move pre-order losses to sourcing cost, as does the UK policy PDF of 2025-02-24 (value-and-reversals VR2). A seller in the UK staff thread reports an "£8.86 Amazon estimated" value for an item Amazon sells at £75 and the manufacturer at £46 (the invoice figure is not given). Sources: 2f44617d; a941ac02; 0252e05d; R-UK. [read in official docs; seller report opinion]

FC36. Units lost in a transfer between fulfilment centres have no claim type of their own in Amazon's pages read. The ledger shows them as adjustments, with units in transit kept in "In Transit Between Warehouses". Sources: P-stock-states-31; 0e07abc1; 知无不言 50256 [opinion]. [inferred]

FC37. Amazon's AWD terms (dated 2026-01-14) replace or reimburse units lost or damaged at an AWD facility or by an Amazon-operated carrier. The facility claim window starts "on the date that the Unit was identified by Amazon as lost or damaged", and valuation follows the MCF reimbursement methodology. Source: supplychain.amazon.com/legal/service-terms/warehouse-and-distribution. [read in official docs]

FC38. Amazon's AWD help text, as a seller quoted it on 2024-09-17, promises "fair value" reimbursement when AWD finds fewer boxes than received "during facility audit or replenishment of boxes to the FBA network", on a case to Selling Partner Support. Source: 10da82b7, quoting GHV89YC29VWN6SBM. [read in official docs, relayed]

FC39. AWD-to-FBA replenishment shipments carry FBA shipment ids and replenishment order ids, and their shortfalls are pursued as inbound shortfalls. Sellers report Amazon asking for carrier tracking that the seller cannot hold. Sources: 1d0a23e7 (2025-11-26); b738f397 (2025-08-21) [opinion]; inbound-shortfalls owns the claim. [opinion]

FC40. The Supply Chain Portal reimbursements policy (counted from the Inventory Adjustment report; its own cap and its fallback percentages of the retail or estimated sale price, values in Values that move) is a different programme from Seller Central FBA, for an active MCF account (filing-and-conduct FL27), and its figures are not FBA's. Source: supplychain.amazon.com/support/reimbursements. [read in official docs]

FC41. Correction to the finance pack: the two News posts of 2024-07-24 that carry the 2024-11-01 automation are two stores' posts: 81c3235d is the US store's (customer-return claims "between 60-120 days") and 6605eede, which P-ref-13, P-ref-16 and § F cite, is Canada's ("between 45-105 days"). Source: both pages read raw, `marketplaceId` read 2026-11-13. [read in official docs; stores command-verified, § 2a]

FC42. The 2025-10-15 claim-windows post (d8f9a56c, British spelling, 95 views, 0 replies) is the Australia store's (`A39IBJ37TRP1C6`). Treating it as the US rule, as the earlier survey notes did, or as store-less, as value-and-reversals VR20 does, is not supported by the page. Source: d8f9a56c read raw. [read in official docs; store command-verified, § 2a]

FC43. Practitioners report pre-2024 automatic reimbursement of warehouse damage: rows showing "Damaged at Amazon" with "Transfer to holding" were already reimbursed. Source: 雨果网 (王璧辉, 2019-06-12). [opinion, history]

FC44. Amazon's Chinese FBA FAQ says warehouse-damaged units cannot be removed and are reimbursed automatically and written off. Source: held as finance pack P-ref-37. [read in official docs] Cited, not redone.

FC45. A Seller Forums post's store is the `marketplaceId` in its own post object (after `contentMetadata`, before `pinnedToCategory`), which stays the same on every forum host, while `selectedMarketplaceId` follows the host. On four posts whose store is fixed by their own words (UK title and £ figures; German text shipping only to Germany; £ reimbursements; a £ cap) the field named that store. Source: plain GET of 2f44617d from four hosts, 2b01db4c, 092c0c0b, 9d4ff2a6; Amazon's *Marketplace IDs* page. [command-verified; that the field names the store a rule governs is checked on these four, Amazon does not document it]

FC46. Amazon issues one News text as separate threads per store, with values that differ between the copies (the 2024-07-24 US and Canada posts, 0.66 s apart, differ on the customer-return window; the 2024-08-06 Saudi Arabia and Egypt posts differ on two lines). A value read in one thread is that store's value only. Sources: 81c3235d, 6605eede, c6da88ce, e62a8ace (§ 2a). [command-verified]

FC47. On a seller's post the field is the store the seller posted under, which can differ from the store the post discusses (c0d6d3da, about Pan-EU sales in IT, ES and FR, carries the UK field). Source: c0d6d3da read raw. [command-verified for the value; the reading is inferred]

FC48. No Amazon page read names a claim type, window, route or reimbursing store for a unit lost while Amazon moves it across borders (Pan-EU, UK–EU) or for EFN stock; the ledger records such a loss as an adjustment at a centre, with `Country` and `Store` on each row and the move as `WhseTransfers`. Amazon's agreement lets it "move Units among facilities" and reimburses loss "while they are being stored" under the FBA Guidelines (AU agreement F-4). Sources: the 2025-02-24 policy PDFs; the News posts of § 2a; stock pack § F3; AU agreement PDF (2024-06-12). [read in official docs; the ledger reading is inferred]

FC49. The store and currency in which a reimbursement posts are read from the Reimbursements report's `currency-unit`, Finances v0 `AdjustmentEvent.StoreName` and `AdjustmentAmount.CurrencyCode`, and Finances v2024-06-19 `marketplaceDetails.marketplaceId`; no Amazon page read states the rule for a unit stored in one country and sold or reported in another. Sources: financesV0.json and finances_2024-06-19.json (db2936aa); value-and-reversals on `currency-unit`. [command-verified for the fields; the rule is open]

FC50. Under NA Remote Fulfillment the units stay in US fulfilment centres while offers sell on Amazon.ca, Amazon.com.mx and Amazon.com.br; a pre-order loss of such a unit is a US centre loss, and no page read states the store or currency of its reimbursement. Source: sell.amazon.com/fulfillment-by-amazon/remote-fulfillment (read 2026-11-13). [read in official docs; the US-centre reading is inferred]

FC51. An MCF order lost or damaged on the way to the buyer is claimed under Amazon's MCF terms, not as an FC-operations claim: Amazon's MCF pages exclude orders "marked as delivered by the carrier", exclude MCF fees, exclude MCF used to fulfil Amazon orders or to remove stock (India page), and set their own window, value basis and cap (values in Values that move). Which page is the MCF policy for a store is inbound-shortfalls' (see inbound-shortfalls IN26). Sources: supplychain.amazon.com/support/reimbursements ("MCF order related claims"); smartcommerce.amazon.in MCF reimbursements page (2023-01-24); sellers 868caeba, a8d3c233 (US), 63437a69 (UK) [opinion]. [read in official docs]

FC52. No Amazon page read addresses a Vine unit lost or damaged before it reaches the Vine Voice. Vine units are FBA inventory ("FBA inventory must be sent to Amazon fulfillment centers for products to be shipped to Vine Voices"). Source: sell.amazon.com/tools/vine (read 2026-11-13). [read in official docs; the absence is a search result]

FC53. The ledger detail reaches back 18 months, and every FC-operations window read is no longer than that reach and counts from the loss report; no Amazon page read says what becomes of a loss row that stays unreconciled past the reach. Sources: *FBA Reports* (see sp-api-claims-surface SU15); § 3; Values that move. [read in official docs; the comparison is ours, the fate of the row is open]

FC54. Amazon's eligibility list excludes units pending disposal or disposed of, defective or customer-damaged units, units outside FBA product restrictions, and (US) units on cancelled or deleted shipments; it names no exclusion for expiry, recall or force majeure. On expired stock damaged at a centre, the UK staff post lists it as "Eligible for manual claims". [held, § 11 of the README: the clause that Amazon's damaged-inventory ownership page classes "expired" as seller-fault came only through customer-returns RT10's read of G9MAM9ELJTSSNYS5 by the closed route, and enters no skill.] Sources: R-US and R-UK (2025-02-24); 2f44617d. [read in official docs]

FC55. Amazon's agreement disclaims liability for failure to perform "by reasons, events or other matters beyond our reasonable control" (AU agreement, General Terms 12) and makes the seller responsible for recall costs (S-3.1); no reimbursement page or post read applies either to a unit lost or destroyed in a fulfilment centre. Source: AmazonServicesBusinessSolutionsAgreement_2024edits1.pdf (AU, created 2024-06-12), m.media-amazon.com. [read in official docs; AU text, the US agreement's clauses not re-read by an open route]

FC56. (withdrawn: held, § 11 of the README; its only source is customer-returns' read of G9MAM9ELJTSSNYS5 through a route since closed. What a permitted route establishes on the setting is customer-returns RT11.) As read: a seller who opts an ASIN out of damaged-inventory ownership has its eligible damaged units marked "defective", and they "will not be eligible for damage reimbursements"; enrolment covers Amazon-fault warehouse-damaged inventory. Source: customer-returns § 3 (G9MAM9ELJTSSNYS5 v4, US), carried by pointer. [read in official docs, by another file through a route since closed]


---

## Open questions for a first run on a real account

1. Does the store's Reimbursements report carry `Lost_Warehouse` rows with no `case-id` (automatic) after the store's start date (Values that move)? How many days after the ledger's M row do they arrive? For a UK store, does this confirm or refute "automatic reimbursement disabled since August 2022" (FC5)?
2. What window does G200213130 show on the store's host today? Does the Contact Us form refuse a lost-unit claim outside it?
3. Does the store's ledger file use reason codes outside the reproduced table (for example G)? Is the detail view's `Reference ID` accepted by "Check warehouse damaged reimbursement status" as the Transaction Item ID?
4. For a reimbursed unit, does an N row (or an O row) appear in the ledger, and on what date relative to the Reimbursements report's `approval-date`?
5. How do `researchingQuantity` age buckets line up with the M rows, and does a unit leave researching at 30 or at 60 days?
6. Do the IDR portal's Eligible-for-Claim rows match the candidates rebuilt from the ledger and Reimbursements report? Which events does the portal show that the rebuild misses, and which does the rebuild show that the portal omits? Does the portal exist outside the US?
7. (moved: cap and dispute window are value-and-reversals' open questions.)
8. For a store using AWD, do AWD-to-FBA shortfalls appear as negative receipts in the FBA ledger or as adjustments, and under which reimbursement `reason`?
9. For a DE, FR, IT, ES, JP, AU, IN, MX or other store with no automation post (FC4): do automatic `Lost_Warehouse` rows arrive at all? Was there an announcement that the search did not reach (for example in the store's language)?
10. (answered: the 2024-09-05 window set is the Saudi Arabia, Egypt and UAE stores', FC11.)
11. For a Pan-EU or EFN seller: in which store's Reimbursements report and settlement, and in which `currency-unit`, does a reimbursement for a unit lost in another country's centre appear? Does the ledger show the loss under the storage country's `Country` and which `Store`?
12. For a Remote Fulfillment seller: does a reimbursement for a US-stored unit ever post in CAD, MXN or BRL?
13. For a Vine enrolment: how do Vine shipments appear in the ledger (event type, reason), and does a unit lost on its way to a reviewer get a `Lost_Outbound` row?
14. Does any `Unreconciled Quantity` on an M row persist to the edge of the ledger's 18 months, and is it later reimbursed, found or dropped?
15. Does the store's G200213130 name expiry, recall or force majeure among its exclusions?

---

## Values that move

Each value is read 2026-11-13 from the source named; store from § 2a. A position states the rule and where the value is read; the value sits here.

| What | Store | Value | Date of the value | Source |
|---|---|---|---|---|
| Automatic reimbursement of FC-lost units, start | US | 2024-11-01 | posted 2024-07-24 | News 81c3235d |
| Automatic reimbursement of FC-lost units, start | CA | 2024-11-01 | posted 2024-07-24 | News 6605eede; relay 3f3688d2 |
| Automatic reimbursement of FC-lost units, start | UK | 2025-01-15 | posted 2024-10-10 | News d0fc997e |
| "We now offer automatic reimbursements" (no date) | US, UK, CA | stated | posted 2024-12-18 | News 68864b6f, a941ac02, da761b17 |
| UK lost units: automatic reimbursement | UK | "disabled since August 2022", manual | posted 2026-04-06 | staff 2f44617d |
| Automatic reimbursement start, any other store | DE, FR, IT, ES, NL, PL, BE, IE, SE, JP, AU, IN, MX, BR, AE, SA, EG, TR, SG | none found | — | search of forums and media, 2026-11-13 |
| UK sellable warehouse damage reimbursed automatically within | UK | 21 days | posted 2026-04-06 | staff 2f44617d |
| FC-operations window | US (text of the older page) | 18 months from the ledger report date | before 2024-10-23 | hopted.com mirror; relay 2de1ef2f ("from 18 months to 60 days") |
| FC-operations window | US | 60 days after reported lost or damaged | eff. 2024-10-23 | News 81c3235d |
| FC-operations window | US | 60 days from the event appearing in reports | posted 2026-08-13 | staff 0e07abc1 |
| FC-operations window | CA | 60 days | eff. 2024-10-23 | News 6605eede |
| FC-operations window | UK | 60 days | eff. 2025-01-09 | News d0fc997e; 9a92846d (2025-01-15) |
| FC-operations window, lost | UK | 18 months of the event | posted 2026-04-06 | staff 2f44617d |
| FC-operations window, damaged | UK | "Available immediately after the damage event is visible" (no end stated) | posted 2026-04-06 | staff 2f44617d |
| FC-operations window | SE | 60 days | posted 2025-01-15 | News 1101821c |
| FC-operations window | SA, EG, AE | 60 calendar days from marking as damaged or misplaced | eff. 2024-09-05 | News c6da88ce, e62a8ace, 96a05f4a |
| FC-operations window | AU | 60 days of reported loss or damage | eff. 2025-10-15 | News d8f9a56c |
| FC-operations window | other stores | not read | — | G200213130 layers unread by an open route |
| Supply Chain Portal FC-operations window (not FBA) | US (SCP) | 60 days from the Inventory Adjustment report | undated, © 2026 | supplychain.amazon.com/support/reimbursements |
| Supply Chain Portal per-unit cap (not FBA) | US (SCP) | $300.00 | undated | same |
| Supply Chain Portal fallback without proof of cost (not FBA) | US (SCP) | "40% of the retail price" / "40% of the estimated sale price" (two clauses) | undated | same |
| MCF order: lost claim earliest | US (SCP) | 7 days after the promised or estimated delivery date | undated | same, "MCF order related claims" |
| MCF order: claim latest | US (SCP) | 90 days after the estimated delivery date | undated | same |
| MCF order: lost claim earliest | IN | 15 days after the estimated delivery date | 2023-01-24 | smartcommerce.amazon.in MCF reimbursements |
| MCF order: claim latest | IN | 30 days after the estimated delivery date | 2023-01-24 | same |
| MCF re-evaluation request | IN | 60 days from the original reimbursement | 2023-01-24 | same |
| Ledger detail look-back | all (page names none) | 18 months | page updatedAt 2026-10-13 | *FBA Reports* (sp-api-claims-surface SU15) |
| Per-unit cap; valuation-dispute window | by store | — | — | value-and-reversals VR29, VR20 |

---

## Seat's own

- The choice of the four posts used to check the `marketplaceId` reading (§ 2a) is this seat's; another set of posts of known store would test the same thing.
- The reading that a cross-border transfer loss, a Remote Fulfillment unit's loss and a Vine unit's pre-shipment loss are ordinary centre losses (§§ 11–13, FC48, FC50, FC52) is inferred from the ledger's columns and Amazon's descriptions of the programmes; no Amazon page says it.
- The comparison in FC53 (every window read is within the ledger's reach) is this seat's arithmetic over the values above.
- Which homes hold which facts (the post-to-store table and automation dates here; cap and dispute window in value-and-reversals; routes and conduct in filing-and-conduct) follows the office's brief, not a finding.

---

## Corrections to other packs

1. **Finance pack P-ref-13, P-ref-16 and § E2 ("no page names the store each post addresses").** Each post names its store in its own `marketplaceId` (§ 2a, FC45): 6605eede is Canada's (`A2EUQ1WTGCTBG2`), d0fc997e is the UK's (`A1F83G8C2ARO7P`), 1101821c is Sweden's (`A2NODRKZP88ZB9`), and 81c3235d, which the finance pack does not cite, is the US store's. So P-ref-13's 2024-11-01 is the US and Canada date and 2025-01-15 the UK date; P-ref-16's "between 45-105 days" for customer returns is the Canada, UK and Sweden value, the US post giving "between 60-120 days"; and § E2's "per-store rollout (US first, Europe later) … [seat]" is no longer a seat reading for the US and UK. Evidence: the threads read raw 2026-11-13, post object `marketplaceId`.
2. **Finance pack research/areas/refunds-reimbursements-adjustments.md, Pages read ("Update to the FBA inventory reimbursement policy … EU https://sellercentral-europe…/a941ac02") and P-ref-14.** a941ac02 is the **UK** store's post (`A1F83G8C2ARO7P`), not an EU one; the EU host only serves it. P-ref-14's "Since 2025-03-31" rests on the US postponement ed8abc33 (`ATVPDKIKX0DER`); the UK has its own postponement to the same date, 0252e05d (2025-02-28, `A1F83G8C2ARO7P`), and Canada its own 2024-12-18 post, da761b17 (`A2EUQ1WTGCTBG2`). Evidence: the threads read raw 2026-11-13.
3. **Stock pack skills/stock-inbound/references/shortages.md, line "Proactive reimbursement (US from 2024-11-01; UK from 2025-01-15)".** The store attribution is right by the posts' fields, but the UK date is stated as fact without Amazon's own UK staff post of 2026-04-06, which says UK lost-unit reimbursement "Currently requires manual claim submission (automatic reimbursement disabled since August 2022)" (FC5). Evidence: 2f44617d, store UK, read 2026-11-13.
4. **Stock pack P-stock-states-51 / stock-states § J1 ("EU forum 5b46fd45").** The 2021 researching thread's post field is the UK store's (`A1F83G8C2ARO7P`), posted 2021-04-07. Evidence: 5b46fd45c5a27980040dbe30d9a84637 read raw 2026-11-13.

---

## Pages read

| Title | Address | Publisher | Page date | Read on | Used for |
|---|---|---|---|---|---|
| Update on Reimbursement Automation and Eligibility Window to file reimbursement claims (store US) | https://sellercentral.amazon.com/seller-forums/discussions/t/81c3235d-4c44-47ba-96c5-883cecab3244 | Amazon (News_Amazon) | 2024-07-24 | 2026-11-13 | FC3, FC9, FC41; Refunds Manager reply |
| Update on Reimbursement Automation and Eligibility Window… (store CA) | https://sellercentral.amazon.com/seller-forums/discussions/t/6605eede-df8e-4498-803f-cb612d95d7ce | Amazon (News_Amazon) | 2024-07-24 | 2026-11-13 | FC9, FC41 |
| FINALLY GOOD NEWS? (seller relay, store CA) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/3f3688d2-5949-4bd1-900b-d01b242955d3 | Seller (Canada store by field) | 2024-07-25 | 2026-11-13 | FC4 |
| Update on Reimbursement Automation… (2025-01-15 start; store UK) | https://sellercentral.amazon.com/seller-forums/discussions/t/d0fc997e-de50-4100-9803-76b7993b66df | Amazon (News_Amazon) | 2024-10-10 | 2026-11-13 | FC4, FC9 |
| Update on eligibility window to file reimbursement claims (store UK) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/9a92846d-41f8-4ad7-b59a-f946efdcc2b4 | Amazon (News_Amazon) | 2025-01-15 | 2026-11-13 | § 2, FC5, FC9 |
| Update on eligibility window to file reimbursement claims (store SE) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/1101821c-7ff1-495a-b8a5-71ff01e3afc3 | Amazon (News_Amazon) | 2025-01-15 | 2026-11-13 | § 2, FC9 |
| Update on reimbursement claim window eligibility on FBA (stores SA and EG) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/c6da88ce-b14f-4ae1-95a5-1c6482b5c565 and https://sellercentral.amazon.co.uk/seller-forums/discussions/t/e62a8ace-3875-433c-8ef1-bb27a29b17c4 | Amazon (News_Amazon) | 2024-08-06 | 2026-11-13 | FC9, FC10, FC11, FC12 |
| Update to FBA inventory reimbursement claim windows (store AU) | https://sellercentral.amazon.com/seller-forums/discussions/t/d8f9a56c-882f-437c-ad34-cccd11cfa465 | Amazon (News_Amazon) | 2025-08-14 (eff. 2025-10-15) | 2026-11-13 | FC9, FC34, FC42 |
| Inventory Defect and Reimbursement portal now available (store US) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/b175b700-09c4-4350-8a22-24f60a724042 (same id on .com) | Amazon (News_Amazon) | 2025-01-21 | 2026-11-13 | FC13, § 4 |
| 🆘FBA Lost Your Inventory? Steps to File a Reimbursement Claim (store US) | https://sellercentral.amazon.com/seller-forums/discussions/t/0e07abc1-9026-4540-a005-153d9e78bf04 | Amazon staff (Indy_Amazon) | 2026-08-13 | 2026-11-13 | FC2, FC9, FC10, FC12, FC16, FC18, FC21, FC28 |
| [April FBA Series] Recover Your Lost FBA Inventory: UK Reimbursement Claims Explained (store UK; read from four hosts) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/2f44617d-9e1c-413e-94b0-d427524ceb82 | Amazon staff (Jameson_Amazon); seller replies | 2026-04-06 | 2026-11-13 | FC5, FC16–FC19, FC35 |
| FBA Lost and Damaged Inventory Reimbursement Policy 📜 (store UK) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/9d4ff2a6-8244-4ad9-bc8c-0d051600e817 | Amazon staff (Angie_Amazon) | 2024-10-26 | 2026-11-13 | FC33, FC34 |
| FBA inventory reimbursement policy changes from 23th of october (seller relay, store US) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/2de1ef2f-e299-486c-9466-48a885c3faef | Seller (US store by field) | 2024-10-16 | 2026-11-13 | FC7 |
| Update to the FBA lost and damage inventory reimbursement policy (store UK) | https://sellercentral.amazon.com/seller-forums/discussions/t/a941ac02-d389-409a-9d62-00ab9db5bc4a | Amazon (News_Amazon) | 2024-12-18 | 2026-11-13 | § 2, FC4, FC35; correction 2 |
| FBA inventory reimbursement policy (G200213130) | https://sellercentral.amazon.com/help/hub/reference/external/G200213130 (also .co.uk, .co.jp) | Amazon | — | 2026-11-13: JavaScript shell; Wayback captures 2026-05-20, 2026-08-07, 2026-09-01 answered 502 | unread; run-time read |
| IDR portal help (G66ZLS453YSE2Y4R) | https://sellercentral.amazon.com/help/hub/reference/external/G66ZLS453YSE2Y4R | Amazon | — | 2026-11-13: JavaScript shell (.com, -europe) | unread |
| Summary of FBA reimbursement policies and requirements for lost and damaged inventory (GVTRADRKAA3XXUJ3) | /help/hub/reference/external/GVTRADRKAA3XXUJ3 on .in, .ae, .co.uk, .com.au | Amazon | — | 2026-11-13: JavaScript shell | unread; FC11 |
| FBA inventory reimbursement policy (third-party mirror of Amazon's help text, older version) | https://www.hopted.com/integrations/amazon-sp-api/amazon-help-articles/fba-inventory-reimbursement-policy | Hopted (mirror of Amazon text) | undated; content pre-2024-10-23 | 2026-11-13 | FC1, FC7, FC16–FC18, FC20, FC33, FC34 |
| Supply Chain Portal: Reimbursements | https://supplychain.amazon.com/support/reimbursements | Amazon | © 2026 | 2026-11-13 | FC12, FC33, FC34, FC40 |
| AWD service terms | https://supplychain.amazon.com/legal/service-terms/warehouse-and-distribution | Amazon | 2026-01-14 | 2026-11-13 | FC37 |
| AWD Lost Inventory, Amazon refuses to Reimburse (quotes GHV89YC29VWN6SBM) | https://sellercentral.amazon.com/seller-forums/discussions/t/10da82b7-d167-419d-90d3-a35d6ec6af52 | Seller; Amazon staff (Topher_Amazon) | 2024-09-17 | 2026-11-13 | FC38 |
| Amazon not reimbursing me for lost inventory on AWD-FBA shipment | https://sellercentral.amazon.com/seller-forums/discussions/t/b738f397-d7d3-44f3-b511-823b60c97a8d | Seller; staff | 2025-08-21 | 2026-11-13 | FC39 |
| Be aware: My AWD to FBA shipment "Closed" — inventory lost | https://sellercentral.amazon.com/seller-forums/discussions/t/1d0a23e7-0e7b-4442-8438-0040624175aa | Seller; staff (Glenn_Amazon) | 2025-11-26 | 2026-11-13 | FC39 |
| Why are sellers denied reimbursement for "damaged in transit" on non-returnable FBA food items | https://sellercentral.amazon.com/seller-forums/discussions/t/c0d7f362-b3ce-4f87-a458-64fd00723a9e | Seller | 2026-03-13 | 2026-11-13 | § 9 pointer |
| Damaged During Transit - Reimbursement FBA | https://sellercentral.amazon.com/seller-forums/discussions/t/d17dd798-738e-4018-84c5-e79de60a245b | Seller | 2024-04-22 | 2026-11-13 | § 9 pointer |
| IDR Portal guide | https://www.ecomengine.com/blog/idr-portal | eComEngine (Becky Trowbridge) | 2025-02-13, upd. 2025-03-03 | 2026-11-13 | FC15 |
| Amazon Launched New Inventory Defect and Reimbursement Portal | https://myamazonguy.com/news/amazon-launched-new-inventory-defect-and-reimbursement-portal/ | My Amazon Guy (Francisco Valadez) | 2025-01-24 | 2026-11-13 | FC13, FC15 |
| Lost Amazon Inventory Found Expired, Sellers Foot the Bill | https://myamazonguy.com/news/lost-amazon-inventory-found-expired/ | My Amazon Guy (Noah Wickham) | 2025-10-31 | 2026-11-13 | FC28 |
| Which third party reimbursement service… | https://sellersasksellers.com/t/which-third-party-reimbursement-service-for-damage-and-lost-items-in-amazon-warehouse-do-you-guys-use/4875 | Sellers Ask Sellers (Spaghetti, HumbleWarrior) | 2024-10-14 to 2024-10-21 | 2026-11-13 | FC17, FC23, FC29, § 5, § 6 |
| FBA Reimbursement Audit: Find Money Amazon Owes You | https://www.sellerlabs.com/blog/fba-reimbursement-audit-amazon-owes-you-2026/ | Seller Labs (Nhan Dinh) | 2026-03-18 | 2026-11-13 | FC27, § 6 |
| Lost & damaged inventory (knowledge base) | https://help.sellerboard.com/?p=3402 | sellerboard | undated | 2026-11-13 | § 6 |
| [5 Steps] Claim Reimbursement for Amazon FBA Lost Inventory | https://getida.com/resources/blog/fba-reimbursements/amazon-fba-lost-inventory/ | GETIDA | undated (≈2024) | 2026-11-13 | § 3, § 6 |
| How Amazon Tracks Inventory Adjustments | https://www.refunzo.com/insights/how-amazon-tracks-inventory-adjustments | Refunzo (Jimi Patel) | 2025-07-03 | 2026-11-13 | § 6 |
| How to Check for Damaged or Lost FBA Inventory | https://www.zonguru.com/blog/how-to-check-for-damaged-or-lost-fba-inventory | ZonGuru (Mansoor Ali) | 2021-10-11 | 2026-11-13 | FC8, FC24 |
| Inventory Ledger Details | https://help.reasonautomation.com/seller/inventory-ledger-details | Reason Automation | undated | 2026-11-13 | FC22 (code table; held) |
| 运营中心运营索赔 (FC operations claim method) | https://www.wearesellers.com/question/50256 | 知无不言 (seller) | 2021-12-15 | 2026-11-13 | FC8, FC23, FC36 |
| 怎么用库存盘点来找到亚马逊丢失的货件 (using inventory reconciliation to find lost units) | https://global.lianlianpay.com/article_train/16-39676.html | 连连 LianLian Global | 2021-11-16 | 2026-11-13 | FC24, FC25 |
| 亚马逊FBA索赔时限缩短 (Amazon shortens FBA claim windows) | https://m.mjzj.com/article/du2ckgmjnthc | 卖家之家 (招单猫) | 2024-08-07 (as listed) | 2026-11-13 | FC8, § 1, § 2 |
| 从 2025 年开始，亚马逊丢件能够自动获得赔偿 (from 2025, lost units reimbursed automatically) | https://www.amz123.com/t/wW7n3WJP | AMZ123 (速推站外) | 2024-10-23 | 2026-11-13 | FC4 |
| 亚马逊FBA仓库损坏库存索赔 (claiming for warehouse-damaged FBA stock; 雨果网 article) | https://www.amz123.com/t/IgwBEtRX | AMZ123 / 雨果网 (王璧辉) | 2019-06-12 | 2026-11-13 | FC43 |
| Amazon have announced two policy updates for Amazon FBA sellers | https://avask.com/blog/amazon-fba-reimbursement-update/ | Avask (Georgina Copeland) | 2024-10-03, upd. 2024-11-07 | 2026-11-13 | § 2 (US dates restated) |
| Shortened reimbursement claim windows | https://shopkeeper.com/blog/shortened-reimbursement-claim-windows | Shopkeeper | 2026-02-09 | 2026-11-13 | § 3 (no transition rule found) |
| UK changes to reimbursement automation… January 2025 | https://carbon6.io/blog/amazon-uk-changes-to-reimbursement-automation-and-claim-eligibility-windows-starting-january-2025 | Carbon6 | — | 2026-11-13: 404; slug seen in search results only | FC4 |
| 2025年亚马逊推出库存缺陷和赔偿新板块 (Amazon's new Inventory Defect and Reimbursement section, 2025) | https://zhuanlan.zhihu.com/p/20029130181 | 知乎 | — | 2026-11-13: 403, unread | — |
| selling-partner-api-models (fbaInventory.json, financesV0.json, awd_2024-05-09.json, schemas) | https://github.com/amzn/selling-partner-api-models (local clone at commit db2936aa, 2026-10-29) | Amazon | 2026-10-29 | 2026-11-13 (grep) | FC14, FC30–FC32 |
| Update to the FBA inventory reimbursement policy (store US) | https://sellercentral.amazon.com/seller-forums/discussions/t/68864b6f-0ab8-41ef-be18-069c33df6336 | Amazon (News_Amazon) | 2024-12-18 (updated 2024-12-19) | 2026-11-13 | § 2, FC4; correction 2 |
| Update to the FBA inventory reimbursement policy (store CA) | https://sellercentral.amazon.ca/seller-forums/discussions/t/da761b17-58cc-4734-98d2-5608e1d11419 | Amazon (News_Amazon) | 2024-12-18 | 2026-11-13 | § 2, FC4 |
| New effective date (store US) | https://sellercentral.amazon.com/seller-forums/discussions/t/ed8abc33-a1d5-417d-b2e2-03b789099833 | Amazon (News_Amazon) | 2025-02-28 | 2026-11-13 | § 2a; correction 2 |
| New effective date for FBA lost and damaged inventory reimbursement policy (store UK) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/0252e05d-1b82-40e7-91d4-543dc22b907b | Amazon (News_Amazon) | 2025-02-28 | 2026-11-13 | § 2a, FC35; correction 2 |
| Update on reimbursement claim window eligibility on FBA (store AE) | https://sellercentral.amazon.com/seller-forums/discussions/t/96a05f4a-537a-49d2-a918-703c47716bc0 | Amazon (News_Amazon) | 2024-08-06 | 2026-11-13 (field only; text is inbound-shortfalls') | § 2a, FC11 |
| Rechnungen - Easybill (German; check post, store DE) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/2b01db4c-a016-4291-a407-69f4f2c25fde | Seller | 2025-03-25 | 2026-11-13 | § 2a, FC45 |
| Reimbursement for lost items (£; check post, store UK) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/092c0c0b-448b-4a89-b170-64fbb6e61901 | Seller | 2025-06-17 | 2026-11-13 | § 2a, FC45 |
| Amazon's Fatal Mistake: Over €60,000 Lost Due to Unnotified Change from PAN-EU to EFN (store UK by field) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/c0d6d3da-8e43-4903-8ca1-4927549ca9a5 | Seller | 2025-04-15 | 2026-11-13 | § 2a limit (1), FC47 |
| Amazon Violating Their Own Policy for Sourcing Cost (store CA) | https://sellercentral.amazon.ca/seller-forums/discussions/t/66aa87b7-1f89-416a-aef8-ce72a552c00a | Seller | 2025-07-18 | 2026-11-13 | § 2a (for value-and-reversals) |
| "…reimbursements that are exactly HALF…" (store US) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/cfea683e-d5f4-48d8-b84e-d88d3b5eeb98 | Seller | 2025-04-22 | 2026-11-13 | § 2a (for value-and-reversals) |
| MCF IS A COMPLETE SCAM! (store US) | https://sellercentral.amazon.com/seller-forums/discussions/t/868caeba-f91e-488a-84b7-4d93a2212db4 | Seller | 2024-09-09 | 2026-11-13 | § 12, FC51 |
| I did MCF on FBM order … Now refused reimbursement (store US) | https://sellercentral.amazon.com/seller-forums/discussions/t/a8d3c233-bba5-4928-b6b8-d70a835c9e17 | Seller | 2024-11-29 | 2026-11-13 | § 12, FC51 |
| FBA delivered to the wrong house? (MCF for eBay; store UK) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/63437a69-1d8a-4b47-bccb-42b89b77477f | Seller | 2024-08-30 | 2026-11-13 | § 12, FC51 |
| Marketplace IDs | https://developer-docs.amazon.com/sp-api/docs/marketplace-ids | Amazon | undated | 2026-11-13 | § 2a id decoding |
| FBA inventory reimbursement policy, US redline ("R-US") | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_US.pdf | Amazon | PDF created 2025-02-24 | 2026-11-13 (text layer) | § 1, § 15, FC1, FC54 |
| FBA lost and damaged inventory reimbursement policy, UK redline ("R-UK") | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_UK.pdf | Amazon | PDF created 2025-02-24 | 2026-11-13 (text layer) | § 1, § 2, § 15, FC1, FC35, FC54 |
| Amazon Services Business Solutions Agreement (AU, "2024edits1") | https://m.media-amazon.com/images/G/31/rainer/AmazonServicesBusinessSolutionsAgreement_2024edits1.pdf | Amazon | PDF created 2024-06-12 | 2026-11-13 | § 11, § 12, § 15, FC48, FC55 |
| Remote Fulfillment with FBA | https://sell.amazon.com/fulfillment-by-amazon/remote-fulfillment | Amazon | undated | 2026-11-13 | § 11, FC50 |
| Get customer reviews with Amazon Vine | https://sell.amazon.com/tools/vine | Amazon | undated | 2026-11-13 | § 13, FC52 |
| Reimbursements for your MCF orders | https://smartcommerce.amazon.in/blog/mcf-reimbursements-for-your-mcf-orders | Amazon (Smart Commerce India) | 2023-01-24 | 2026-11-13 | § 12, FC51 |
| Supply Chain Portal: Reimbursements, "MCF order related claims" section | https://supplychain.amazon.com/support/reimbursements | Amazon | © 2026 | 2026-11-13 | § 12, FC51 |
| selling-partner-api-models, finances_2024-06-19.json and financesV0.json (`AdjustmentEvent`, `Currency`, `MarketplaceDetails`) | https://github.com/amzn/selling-partner-api-models (local clone at db2936aa, 2026-10-29) | Amazon | 2026-10-29 | 2026-11-13 (grep) | § 10, § 11, FC49 |
| Pages tried and not found (404): sell.amazon.com/tools/amazon-vine, …/programs/amazon-vine, sell.amazon.co.uk/tools/amazon-vine, sell.amazon.com/global-selling/remote-fulfillment, sell.amazon.co.uk/fulfilment-by-amazon/pan-european-fba, …/european-fulfilment-network | — | Amazon | — | 2026-11-13 | — |
| (held) Researching - FBA Inv (store UK by field) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/5b46fd45c5a27980040dbe30d9a84637 | Seller quoting Amazon | 2021-04-07 | via stock pack; field read 2026-11-13 | FC6; correction 4 |
| (held) FBA Reports; Role Mappings | https://developer-docs.amazon.com/sp-api/ | Amazon | 2026-10-13 / 2026-10-28 | via finance and stock packs | § 5, § 6 run-time reads |

---

## Verification (2026-11-13)

An adversarial check re-read each cited public page raw (forum `datePublished` from the page's JSON-LD) and grepped the SP-API model clone at db2936aa against upstream main.

**Checked and confirmed (dates, quotes, counts):** FC1 and FC20 (mirror text, including "no later than 18 months after the date the item was reported lost or damaged in your Inventory Ledger report", the three pre-claim checks and "Search by FNSKU and date"); FC2, FC10, FC16, FC18, FC21 (0e07abc1, 2026-08-13: the scope, the sourcing-cost and replenishment sentence, "within 60 days of the date the loss or damage event appears in your reports", both routes, "#1 reason", "One claim per shipment or event"; the `/inventory-reimbursement/cost-management` link is in the post's resource list); FC3 and FC41 (81c3235d and 6605eede, both 2024-07-24, 2.5K/17 and 132/0, 60–120 against 45–105); FC4 (d0fc997e 2024-10-10, 2025-01-15 and 2025-01-09, "Changes to programme policies"; 3f3688d2 2024-07-25 with "The Fulfilment by Amazon team"; AMZ123 wW7n3WJP 2024-10-23 assigns 2025-01-15 to "欧洲站点"; the Carbon6 URL answers 404); FC5, FC19 (2f44617d 2026-04-06, "updated by moderator", every quoted line, the UK eligibility conditions); FC7 (2de1ef2f 2024-10-16); FC13 (b175b700 2025-01-21, scope, exclusions, path); FC15 (eComEngine 2025-02-13; My Amazon Guy 2025-01-24); FC22 and FC25 (Reason Automation's table: N "because you received an Amazon reimbursement", O "because Amazon has reimbursed you"); FC24 (连连 2021-11-16: EM against FN); FC27 (Seller Labs 2026-03-18, read through a fetch tool as the page refuses plain requests); FC30–FC32 (`researchingQuantity`, `warehouseDamagedQuantity`, `FBAInventoryReimbursement` "if a seller's inventory is damaged", `LostOrDamagedReimbursement` as Easy Ship, AWD model's only "damaged" hit a packaging description, `LOST` as "The carrier lost the shipment."); FC37 (AWD terms dated January 14, 2026, window start and MCF valuation); FC38 (10da82b7 2024-09-17, the "Under-the-roof reimbursement" quote, Topher_Amazon passing the case on); FC42 (d8f9a56c 2025-08-14, British spelling, 95 views, 0 replies); FC8 (招单猫: "18个月" in the introduction, "180天" in the body).

**Changed:**

- FC29: the $870 reversal post is dated 2024-10-16, not 2024-10-17; the § 6 quote was paraphrased and is now verbatim.
- FC11 and § 3: c6da88ce (EU host) and e62a8ace (UK host) are not the same text; only the UK-host thread carries carrier-damaged returns and lost customer returns.
- FC12 and § 5: only the staff post directs sellers to the retired report; the 2024-09-05 post and the Supply Chain Portal count their windows from it.
- FC23 and § 6: the 知无不言 recipe does not use codes M and 5 or "≥ 1"; its "可以索赔" quote came from the page's AI-generated summary, not the author, and is now marked so.
- FC28: the 0e07abc1 seller reply concerns an unpaid inbound shortfall, not a reversal; it no longer supports the reversal half.
- FC35, § 2 and the seller's choices: £46 is the manufacturer's selling price as the seller states it, not an invoice cost; the sourcing-cost reading of "£8.86 Amazon estimated" is now marked [inferred].
- § 7: the Supply Chain Portal evidence line is now its exact wording; FC40's "40 % of retail" now gives both of the page's 40 % clauses.
- § 1(b): the inbound-versus-warehouse reading of 招单猫 is now marked [inferred].
- FC9, FC33, FC34 (moving values): each position now states the rule and where its value is read; the 60-day, 18-month, $5,000, £2,000, $300, 60/90-day figures stay as evidence with host, source and date read.
- § 3(c): "a row older than the window is history and not a claim", a threshold of ours tied to a "US 60-day rule" that no page establishes for the US, is now a fact about Amazon's stated window plus the seller's choice.
- FC14: the "defect" hits are named (none is IDR), and upstream main b13d1d1 (2026-11-10) adds nothing relevant.

**Remaining doubts:**

- G200213130, G66ZLS453YSE2Y4R and GVTRADRKAA3XXUJ3 still return a JavaScript shell, so no current policy page was read. Every window, cap and valuation in this file comes from News posts, staff posts, a third-party mirror or another programme.
- The US policy PDF (2024-12-18, $5,000, 60-day dispute), a941ac02, 1101821c, P-stock-states and the other held rows were not re-read in this pass.
- Amazon names no store for the 2024-11-01 and 2025-01-15 dates, and the UK staff post's "disabled since August 2022" contradicts both. None of these is resolved.
- The Reference ID = Transaction Item ID equivalence (FC17) rests on one practitioner's use.
- Not re-read in this pass: ZonGuru, GETIDA, Refunzo, sellerboard, the 雨果网 article, the AWD-to-FBA threads (1d0a23e7, b738f397) and the 2021 EU researching thread.

---

## Revision (2026-11-13)

Done after the completeness critic's first round. Every forum thread named below was re-read raw on 2026-11-13 by plain GET; no help-hub content call, no POST, no sign-in.

**What changed.**

- **Post-to-store table (critic A1, D).** New § 2a holds the pack's table of which store each cited Seller Forums post addresses, read from the post object's `marketplaceId`. The method's tag is settled: the field was read on four posts whose store is fixed by their own words (2f44617d from four hosts, 2b01db4c in German, 092c0c0b and 9d4ff2a6 in £); all four agree, so the field's value and its agreement with the store are [command-verified], while the field's meaning remains undocumented by Amazon. The two limits (seller posts carry the poster's store; per-store copies differ in values) are stated.
- **Store attributions corrected in this file.** 3f3688d2 is a Canada-store relay, not UK; 2de1ef2f is a US-store relay, not EU; 9d4ff2a6 is the UK store's staff post, not EU; a941ac02 is the UK store's valuation post, not EU; c6da88ce and e62a8ace are the Saudi Arabia and Egypt stores', not "EU host" and "UK host"; d8f9a56c is Australia's; 5b46fd45 is the UK store's.
- **Automation dates by store (A1, A8).** § 2 rewritten: US and Canada 2024-11-01, UK 2025-01-15, "We now offer" restated for US, UK and CA on 2024-12-18; none found for any other store. The Carbon6 slug and AMZ123 now agree with the UK field and no longer carry the attribution. The UK staff post FC5 is stated against three UK News posts; neither is picked.
- **Positions restated:** FC1 (adds Amazon's own 2025-02-24 PDFs beside the mirror), FC2, FC3, FC4, FC5, FC7, FC9, FC11, FC13, FC19, FC23 and FC24 (practitioner recipes now stated as choices side by side, critic E), FC35 (a941ac02 and 0252e05d are UK), FC40, FC41 (6605eede is Canada), FC42 (d8f9a56c is Australia).
- **Withdrawn (homed elsewhere):** FC16 (routes → filing-and-conduct FL4), FC21 (premature and duplicate filing → filing-and-conduct FL7, FL11), FC33 (cap → value-and-reversals VR29), FC34 (dispute window → value-and-reversals VR20). § 7 routes and § 8 are now pointers.
- **Moving values out of positions (critic F).** FC5, FC9, FC19 and FC40 state the rule; the values sit in the new "Values that move" table with store, date and source. § 3's table now carries store and anchor, not length.
- **Pointers for other kinds' windows.** § 3's inbound, removal and returns values from the 2024-09-05 posts are replaced by pointers to inbound-shortfalls IN8, removals-disposals RM6 and customer-returns.
- **New sections (critic B):** § 11 cross-border transfers (Pan-EU, UK–EU, EFN) and NA Remote Fulfillment, with the fields where a reimbursement's store and currency are read; § 12 MCF units (MCF policy page pointed to inbound-shortfalls IN26); § 13 Vine units; § 14 unreconciled rows older than the ledger's 18 months; § 15 exclusions for expired, recalled, disposed, opted-out and force-majeure cases. § 10 adds the Finances `AdjustmentEvent` and `marketplaceDetails` fields (grep of the model clone at db2936aa).
- **New positions:** FC45 (the method), FC46 (per-store copies differ), FC47 (seller posts), FC48 (cross-border transfer loss), FC49 (store and currency fields), FC50 (Remote Fulfillment), FC51 (MCF orders), FC52 (Vine), FC53 (rows past the ledger's reach), FC54 (exclusions), FC55 (force majeure and recall in the agreement), FC56 (damaged-inventory ownership opt-out).
- **Small fixes:** § 9 (c) pointed to FC39 for the AWD model; it is FC32. § 4 gives the IDR launch post's store (US) and points to FL5 for its scope.
- **Added sections required by the file's form:** Values that move; Seat's own; Corrections to other packs (four entries: finance P-ref-13/-16/§ E2, finance a941ac02 and P-ref-14, stock shortages.md UK date, stock § J1 store label).
- **Open questions:** 7 moved to value-and-reversals; 10 answered by FC11; 11–15 added.

**Not done, and why.**

- G200213130, G66ZLS453YSE2Y4R and GVTRADRKAA3XXUJ3 stay unread: the help hub serves a script shell and its content call is closed. Facts that customer-returns read by that route (G9MAM9ELJTSSNYS5, RT10, the opt-out) are carried here by pointer and tagged.
- The web search budget for the session ran out after the first searches for Pan-EU/EFN currency, Remote Fulfillment reimbursements and Vine losses; the English and Chinese searches made before that returned nothing citable on those points, and the gaps stand as open questions 11–13.
- The US agreement's F-4 and General Terms 12 were not read by an open route; the AU PDF stands in, labelled as AU.
- The § "Verification (2026-11-13)" block above records the earlier pass and is left as it was; its "Remaining doubts" line on store attribution is superseded by § 2a.
