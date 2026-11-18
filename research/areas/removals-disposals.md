# Removals and disposals: what Amazon owes when stock leaves FBA

Date read for every page below: 2026-11-13, unless a row says otherwise.

**Summary.** A removal claim is the one FBA inventory claim Amazon has never automated. Every Amazon text from 2024 to 2026 says "all removal claims will still need to be filed manually", and the IDR portal leaves removals and warehouse disposals out. What a removal claim covers is narrow: units lost or damaged by Amazon, or by a carrier Amazon used, after they left the facility on the way to the seller's return address, plus grading disputes on customer returns that came back through a removal. Amazon has issued at least four dated window changes since 2024, each in a post whose marketplace field names one store, so the window is a per-store value read at run time; the 2025-10-15 change appears only on a post marked for Australia. The data that finds a claim is in two reports cx can read (Removal Order Detail, Removal Shipment Detail) and in the ledger and Finances. Filing, attaching photos and reading the answer happen in Seller Central, except that the restricted Support API can read a case. Three edges of removal and disposal are covered in § J, § L and § M: units Amazon disposes of after classing them unfulfillable dangerous goods, for which no Amazon text read offers a claim and Amazon's agreement and staff describe disposal without reimbursement; removals of stranded units, which are ordinary removals once they leave; and liquidation shortfalls, which Amazon's removals page does not cover by its wording and which only a join of removal-order quantities to liquidation events can see. Amazon's Seller Central help pages for removals claims are not read here: they serve a script shell to a plain GET, and the route that once read them was closed by the office on 2026-11-10.

**One fact, one home.** Already held, and cited, not repeated:

- The finance pack (cx-amazon-finance-playbook) holds:
  - the policy scope and the automation (P-ref-12, P-ref-13);
  - sourcing-cost valuation (P-ref-14, P-ref-15);
  - the window conflict (P-ref-16);
  - reversals (P-ref-18) and the Reimbursements report (P-ref-19);
  - removal and disposal fees as money (research/areas/fulfilment-charges.md § H, P-ful-*);
  - liquidation as money (fulfilment-charges.md § H4);
  - Grade and Resell, Donations and the liquidation default (refunds-reimbursements-adjustments.md § J, P-ref-43, P-ref-48, P-ref-49).
- The stock pack (cx-amazon-stock-playbook) holds:
  - removal mechanics, status words, processing times, cancelling, the removal feed and the three removal reports' columns (research/areas/stuck-stock.md E-R1 to E-R8, R3, R4);
  - automatic disposals and required removals (stuck-stock.md D6 to D8, C4);
  - per-unit fee timing (holding-costs.md G1, P-holding-costs-30);
  - the ledger (stock-states.md F2, F3, P-stock-states-29, P-stock-states-30).
- The door (cx-amazon-sp-api, references/door.md) is how a report is requested. It is not repeated here.
- The stock pack also holds stranding itself (research/README.md S1 to S8; skills/stuck-stock/references/stranded.md), the automated settings (S15), cancelling (S17), FBA Liquidations' rule, eligibility and events (S19 to S22) and dangerous goods as a stock state (G18; research/beyond/programs-and-regions.md H1, J9).
- The finance pack holds liquidation proceeds and fees as money (P-ful-11).
- Inside this pack:
  - the News posts on automation and windows, and which store each post is for: fc-lost-damaged (post-to-store table);
  - the per-unit cap, the valuation-dispute window and Manage Your Sourcing Cost: value-and-reversals (VR20, VR29, VR11, VR14, VR16);
  - the Support API, the roles and "no operation files a claim": sp-api-claims-surface (SU5, SU8, SU10, SU12, SU13);
  - entry points by claim kind, the IDR portal's scope and conduct: filing-and-conduct (FL4, FL5, FL11).

This file adds:

- the claim rules and their dated history, store by store;
- the evidence Amazon lists;
- grading disputes;
- the pitfalls that hide a removal claim in the data;
- what liquidation and disposal events mean for a claim;
- corrections to the two packs (see *Corrections*).

---

## A. What a removal claim covers, in Amazon's words

**(a) Amazon's rule.**

- **Scope.** The removals-claims section of Amazon's policy: "This section applies to eligible items lost or damaged by Amazon or a carrier used by Amazon while removing your inventory from a fulfillment center to your returns shipping address. The item must not have been returned to you because you violated a program policy or other terms and conditions that apply to your use of any Amazon selling service. The damage or loss must have occurred after the item left an Amazon facility." [official]
  - The same text appears in two places. One is Amazon's EU redline of the help pages, *FBA inventory reimbursement policy: Removals claims* (https://m.media-amazon.com/images/G/02/rainier/help/EU_Policy_Redline.pdf, PDF created 2024-08-20, "ESAS help page template version 23.01"). The other is an undated third-party copy of the US help page (Hopted, https://www.hopted.com/integrations/amazon-sp-api/amazon-help-articles/fba-inventory-reimbursement-policy, Wayback capture 2026-07-13).
  - The Seller Central page itself is a JavaScript shell to a plain GET (see *Pages read*), and no permitted route read its live text on 2026-11-13.
  - The same scope sentences, word for word, stand on Amazon Supply Chain's *Supply Chain Portal (SCP) Reimbursements policy* (https://supplychain.amazon.com/support/reimbursements, undated, © 2026, read 2026-11-13). That page is the Amazon Supply Chain Services programme's, not FBA's (filing-and-conduct FL27), so it corroborates the wording and is not the FBA rule. [official, another programme's page]
- **Eligibility, for every inventory claim, removals included** (US policy PDF, created 2024-12-18):
  - "The item is registered in FBA at the time it is lost or damaged."
  - "The item complies with FBA product restrictions and with FBA inventory requirements."
  - "The item is not pending disposal or was not disposed of at your request or because we have exercised a right to do so."
  - "The item is not defective and was not damaged by a customer."
  - "When a lost or damaged item claim is filed, under review, and during any appeals, the seller's account must be in normal status." [official] (https://m.media-amazon.com/images/G/01/rainier/help./PC__Kiwi_Comms_redlined_policy_US_clean.pdf)
  - Bryce_Amazon restated the same list in reply to a removal-reimbursement thread on 2024-09-28 (https://sellercentral.amazon.com/seller-forums/discussions/t/b3bb247e-1d58-45c7-bd84-a9196edd6fbf). [official, staff]
- **Manual filing.** "Additionally, all removal claims will still need to be filed manually." [official] This sentence is in every automation post (81c3235d, 6605eede, d0fc997e, read 2026-11-13). The posts, their dates and their stores are fc-lost-damaged's (post-to-store table); the finance pack's P-ref-13 holds the automation.
- **The IDR portal** leaves out removals and warehouse disposals (see filing-and-conduct FL5; finance pack E3).
- **The filing route** for a removal claim is the "Resolve a removal order issue" tool, by removal order ID (see filing-and-conduct FL4, from Indy_Amazon 0e07abc1, 2026-08-13, US field). The same staff post lists "Photos of damaged items received in removal orders" among the records to keep. [official, staff] (https://sellercentral.amazon.com/seller-forums/discussions/t/0e07abc1-9026-4540-a005-153d9e78bf04, read 2026-11-13)
  - The Hopted copy of the help page links the tool as https://sellercentral.amazon.com/help/hub/reference/G9ZB3H4DP4H72U6R.
  - The staff "April FBA Series" post of 2026-04-09 lists "FBA Inventory Reimbursement Policy: Removals Claims - Removal-related reimbursements" as its own help page (https://sellercentral.amazon.com/seller-forums/discussions/t/969ce6b1-2baf-445a-830a-9ebcbdecf14e). [official, staff]
- **Kinds of removal claim in Amazon's texts.** These are the ones Amazon's texts name: lost in transit; damaged in transit; "Damaged, Different or Incomplete (missing accessory or main item) units from a removal shipment received" (UAE post, 96a05f4a, 2024-08-06); and grading disputes (§ C). [official]

**(b) What practitioners add.**

- **Mr Prime** (Robert Prime, UK, "checked 1 October 2026") groups "Damaged, wrong item or short delivery" under one 60-day removal window in the UK. He reports that the UK removals page's text says 74 days where its table says 75. [opinion] (https://mrprime.com/insights/fba-reimbursements/)
- **Refunzo** (Jimi Patel, 2025-06-23) lists what is not covered: "customer-damaged or defective items, restricted inventory, self-canceled removal orders, suspended accounts, natural disasters, and seller packaging or address errors". [opinion] (https://www.refunzo.com/insights/amazon-removal-order-reimbursements-explained)
- **环至美物流** (2025-06-04) names the Chinese Seller Central case path: "FBA 库存问题" → "已移除库存未收到或收到数量不符" (FBA inventory issue → removed inventory not received, or received in a different quantity). [opinion] (https://www.huanzhimei.net/news/1550.html)

**(c) Into a skill.** The scope sentence; the eligibility list; that removal claims are manual and outside the IDR portal; the four kinds of claim; the name of the Seller Central tool.

**Read at run time.**

- The policy as the seller's store shows it: *FBA inventory reimbursement policy: Removals claims* and the "Resolve a removal order issue" tool (https://sellercentral.amazon.com/help/hub/reference/G9ZB3H4DP4H72U6R). Both are behind sign-in or JavaScript, so the seller opens them.
- No SP-API operation returns eligibility.

---

## B. The windows: a dated history, store by store

**How the store was read.** Which store each News post is for, the `marketplaceId` field it is read from, and the tag of that reading are fc-lost-damaged's (post-to-store table); the "Store (field)" column below follows it. Two observations from this file's own reads of 2026-11-13 go to that home: the field after `contentMetadata` is the post's, while the page's first `marketplaceId` hits are the host's store list; and no removal-related post read names its store in its body text (862f270b, UK field, says "Fulfilment" and "May 1, 2026" but no country; d8f9a56c, Australia field, names none), so no post read here could test the field against a store named in the text.

**(a) Amazon's rule, post by post.** Each quote was read from the raw page on 2026-11-13. Each date posted is the page's `datePublished`.

| Post | Store (field) | Posted | Effective | Lost in transit | Damaged / other | Grading |
|---|---|---|---|---|---|---|
| Removals-claims help page, pre-2024 text (Hopted copy; EU redline's struck text) | page US / EU | undated | — | "no sooner than 14 days from the last confirmed movement of your removal shipment"; all "within 18 months of the date the item was removed from the Amazon fulfillment network" | "as soon as you receive the items"; 18 months | "within 30 days of delivery of the removal order to the return address" |
| News 81c3235d "Update on Reimbursement Automation and Eligibility Window…" | US (ATVPDKIKX0DER) | 2024-07-24 | 2024-10-23 | "15-75 days from the shipment-creation date. Claims must not be submitted before 15 days" | "All other removal claims must be filed within 60 days of the shipment being delivered back to you" | (inside "all other") |
| News 6605eede (same title, British spelling) | Canada (A2EUQ1WTGCTBG2) | 2024-07-24 | 2024-10-23 | same | same | same |
| EU redline of the removals page | EU help template | PDF 2024-08-20 | — | added: "must be submitted within 75 days from the shipment creation date"; kept: "no sooner than 14 days from the last confirmed movement" | struck "18 months", added "60 days of the date the item was delivered back to you" | "30" struck, "60" added (days of delivery) |
| News 96a05f4a "Update on reimbursement claim window eligibility on FBA" | UAE (A2VIGQ35RCS4UG) | 2024-08-06 | 2024-09-05 | "No sooner than 15 calendar days from the shipment ship date but no later than 75 calendar days" | "Damaged, Different or Incomplete (missing accessory or main item) units from a removal shipment received: Within 30 calendar days from the shipment delivery date" | — |
| News d0fc997e (same title as 81c3235d) | UK (A1F83G8C2ARO7P) | 2024-10-10 | 2025-01-09 | 15–75 days from shipment creation | 60 days of delivery back | — |
| News 1101821c "Update on eligibility window to file reimbursement claims" | Sweden (A2NODRKZP88ZB9), EU host | 2025-01-15 | (in force) | 15–75 days from shipment creation | 60 days | — |
| News d8f9a56c "Update to FBA inventory reimbursement claim windows" | Australia (A39IBJ37TRP1C6) | 2025-08-14 | 2025-10-15 | "Removal orders lost : Between 15-135 days from shipment creation" | "Removal orders damaged : 120 days from shipment delivery date" | "Removal orders grading : 120 days from date item was removed from our fulfilment network"; "Re-evaluation requests : Within 90 days of initial claim" |
| Staff post 0e07abc1, Indy_Amazon | US (ATVPDKIKX0DER) | 2026-08-13 | — | "Removal claims: File within 18 months of the shipment being delivered or lost" | (same) | — |

[official, every row] The d8f9a56c thread renders on the .com, .co.uk, -europe and .ca hosts with the same text.

**Where the pages disagree** (stated; none resolved):

- **The lower bound has three anchors.** "15 days from the shipment-creation date" (News posts, 2024–2025); "14 days from the last confirmed movement of your removal shipment" (the help page text, kept in the 2024-08-20 redline); "15 calendar days from the shipment ship date" (UAE). A removal order's shipments are created, shipped and last scanned on different days.
- **The upper bound for lost units:**
  - 75 days from creation (US/CA 2024-10-23, UK 2025-01-09, SE 2025-01-15);
  - 75 days from ship date (UAE 2024-09-05);
  - 135 days from creation (AU 2025-10-15);
  - 18 months from delivery or loss (US staff post 2026-08-13).
- **The US staff post** of 2026-08-13 matches the pre-2024 help page in length (18 months), not any News post. The anchors differ: the old page counts 18 months from "the date the item was removed from the Amazon fulfillment network"; the staff post counts from "the shipment being delivered or lost". This is evidence for the finance pack's surmise (§ F there) that the staff post restates an older page, not proof.
- **The help page and the posts disagree within themselves.** The UK removals page says 74 days in its text and 75 in its table (Mr Prime, 2026-10-01). No US News post after 2024-07-24 was found that restates removal windows for the US. Whether the 2025-10-15 windows apply to the US is not established [inferred from absence; SellerSprite (2026-10-23) applies them to the US, opinion].

**The US grading-dispute window, by permitted sources only.** What each says, with its date:

- The pre-2024 US help-page text: "within 30 days of delivery of the removal order to the return address" (Hopted copy, undated, Wayback capture 2026-07-13; read 2026-11-13). This is the oldest text and the one RM12 used to lean on.
- News 81c3235d (US field, posted 2024-07-24, effective 2024-10-23): "All other removal claims must be filed within 60 days of the shipment being delivered back to you" (read 2026-11-13). It names lost-in-transit claims and "all other"; it does not name grading. That grading falls under "all other" is [inferred].
- The EU redline of the removals page (PDF created 2024-08-20): "30" struck and "60" added for grading, counted from delivery of the removal order (read 2026-11-13). EU, not US; it shows the direction of the 2024 change.
- Amazon Supply Chain's SCP page (undated, © 2026, read 2026-11-13) repeats 81c3235d's "All other removal claims must be filed within 60 days of the shipment being delivered back to you". It is another programme's page (filing-and-conduct FL27).
- News d8f9a56c (Australia field, effective 2025-10-15): "Removal orders grading : 120 days from date item was removed from our fulfilment network" (read 2026-11-13). Australia's, not the US's.
- Mr Prime (UK, checked 2026-10-01): grading disputes within 60 days of the removal's delivery. [opinion]

A reading of the live US removals-claims page newer than these was recorded elsewhere in this pack through a route the office closed on 2026-11-10. It is not used here, and no permitted route confirmed or refuted it on 2026-11-13: the Seller Central page serves a script shell to a plain GET, and no third-party copy of it newer than the Hopted capture was found. On permitted sources, the US grading window is 60 days from the removal's delivery if grading sits under "all other" in 81c3235d [inferred], and 30 days in the older page text; which the US tool enforces today is unread.

**(b) What practitioners add.**

- **15–135 / 120 / 120 days, applied to the US:** SellerSprite Content Team (2026-10-23, https://www.sellersprite.com/en/blog/amazon-reimbursement-services), Olifant Digital, Marketplace Officer and Refunzo's "2027 guide". [opinion]
- **Still cite 15–75 / 60:** PrepVia (Bernardo Campelo, 2026-08-25, modified 2026-11-01, https://www.prepvia.com/blogs/amazon-removal-orders-2026-guide), Mr Prime (UK, 2026-10-01) and ReclaimHQ (UK, "74 days"). [opinion]
- Several services tell the seller to "verify the current numbers in Seller Central … because Amazon has revised these windows more than once" (PrepVia). [opinion]
- **Chinese.** AMZ123 and 卖家之家 (both 2025-01) report 15–75 / 60 (finance pack, What practitioners add). 百运网 (2025-04-05, https://m.by56.com/news/46973.html) gives the older help-page text. It renders "no sooner than 14 days" as "丢失需在移除货件最后一次确认转移后14天内提交" ("within 14 days"), which reverses its meaning. [opinion; the misreading is command-verified against the English text]
- **ReclaimHQ** (UK, undated, © 2026): filing before the lower bound "will result in an automatic rejection with a “too early” response". It gives the UK lost-in-transit window as "74 days from shipment creation". [opinion] (https://reclaimhq.uk/weekly-removal-order-reconciliation-sop)

**(c) Into a skill.**

- Facts that stand:
  - the claim types and the event each window counts from (creation, last movement, ship date, delivery, removal);
  - that Amazon's posts are per store and carry a marketplace field;
  - that a lower bound exists ("too early" is a rejection);
  - the dated history above, as history.
- The figures themselves are values that move (see *Values that move*).

**Read at run time.**

- The window for the seller's store and claim: Amazon's page *FBA inventory reimbursement policy: Removals claims* (US policy hub https://sellercentral.amazon.com/help/hub/reference/external/G200213130, a JavaScript page) and the "Resolve a removal order issue" tool (G9ZB3H4DP4H72U6R), which shows eligibility per removal order.
- The latest News post whose marketplace field matches the seller's store (Seller Forums, News and Announcements).
- The event dates come from the seller's data: `request-date` (Removal Order Detail); `shipment-date` (Removal Shipment Detail); the carrier's delivery date (the tracking number on the carrier's site; no SP-API field).
- No SP-API operation gives a window.

---

## C. Grading disputes, and how Grade and Resell bears on a removal claim

**(a) Amazon's rule.**

- **The text.** "Disputing Amazon grading post customer return. If you disagree with Amazon's grading of items returned by customers as customer damaged or defective, you can file your claim according to the 'Submit your claim' section below. In order to file a claim, the disputed item must have been physically returned to you by means of a removal order." [official] (EU redline, 2024-08-20)
- **The customer-returns page points here.** "For grading disputes, create a removal order and file all claims within 30 days of delivery of the removal order to the return address. To learn more, go to the FBA removal orders claims section 'Disputing Amazon grading post customer return'." [official] (same PDF, customer-return claims page)
  - Its 30 days is unredlined text, while the removals page in the same PDF strikes 30 and adds 60. The PDF disagrees with itself.
- **What is not reimbursed.** "Note: Amazon does not reimburse for customer returns with following conditions: Damaged box or packaging, missing factory seal, missing packaging, tape or shipping label over box, different box." [official] (same)
- **The 2025-10-15 Australia post** words it "Removal orders grading : 120 days from date item was removed from our fulfilment network". It counts from removal, not from delivery. [official]
- **The US window** on permitted sources, with dates, is in § B (*The US grading-dispute window*).
- **Evidence.** For a grading dispute, the claim adds an "Explanation as to why you disagree with Amazon's grading of the disputed item (Amazon grading disputes only)". [official] (EU redline; Hopted copy)
- **Grade and Resell is a different thing.** It is Amazon grading an unfulfillable return for resale as Used, under an `amzn.gr.` SKU. It is tracked in Removal Order Detail ("Requested Qty", "Completed Qty"). "Standard removal fees do not apply to submitted FBA Grade and Resell items. If you dispatch to an address or dispose of the inventory after an item is graded and relisted, removal fees will apply." [official] (finance pack § J1, P-ref-43)
  - No Amazon text read ties Grade and Resell's own grading to the removal-grading claim window [inferred from absence].

**(b) What practitioners add.**

- **Disposal ends the dispute.** Mr Prime: "you must first get the unit back with a removal order, then claim within 60 days of that delivery" (UK). [opinion] A disposal (automatic or chosen) destroys the unit and with it the dispute. A seller reports units marked "defective products" and then disposed of by an automatic order that "couldn't be stopped", and Glenn_Amazon asked for the case id without promising a reimbursement (thread posted 2025-09-09, https://sellercentral.amazon.com/seller-forums/discussions/t/8299f3f0-45c5-43a7-add2-e189180eb29f). [opinion; staff reply official]
- **Misgrading.** PrepVia: "a material share of what comes back marked unsellable is recoverable after real inspection". [opinion]
- **"Customer damaged" does not mean broken** (stock pack D3). [official, staff]

**(c) Into a skill.**

- A grading dispute needs the unit physically returned through a removal order.
- It concerns customer returns graded customer-damaged or defective.
- Its window counts from delivery of the removal (EU text) or from the date of removal (Australia post).
- A disposed unit cannot be disputed.
- Grade and Resell is a separate programme, whose money is the finance pack's.

**Read at run time.**

- Which units were graded customer-damaged or defective: `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` (`detailed-disposition`, `license-plate-number`, `status`), Pricing or Amazon Fulfillment (customer-returns area).
- Whether they were removed or disposed: `GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA` (`order-type`, `disposition`, `disposed-quantity`, `shipped-quantity`), Pricing or Amazon Fulfillment.
- The seller's automated unfulfillable settings, which decide whether such units are disposed before they can come back, are read only in Seller Central (stock pack S1).

---

## D. Evidence Amazon asks for

**(a) Amazon's rule.**

- **The list.** "When filing a claim for lost units, you must provide the following information and documents":
  - "Amazon removal order ID";
  - "Shipment ID and active tracking ID or proof of delivery, which the carrier can confirm from the packing slip";
  - "ASINs/FNSKUs and quantities affected";
  - "Licence plate number (LPN)";
  - "Images of the affected units";
  - "Images of the affected units' product packaging";
  - "Images of the shipping box";
  - "Images of shipping label";
  - the grading explanation (grading disputes only). [official]
- **The note.** "When filing a claim for lost units, you must provide Shipment ID and active tracking ID or proof of delivery." [official] (EU redline 2024-08-20)
  - The Hopted copy of the US page has the same list without "Images of shipping label".
- **Staff, US, 2026-08-13.** "Shipment ID, ASINs/FNSKUs, quantities affected, and images of affected units if applicable"; keep "Photos of damaged items received in removal orders". [official, staff]
- **Following the process.** "You must follow the applicable process described on the pages above and provide all requested information when you file a claim. We may decline your claim if you do not." [official] (US policy PDF 2024-12-18)
- **Wrong or missing items.** For a wrong item received, an experienced seller's advice (photos of "all sides of the box, the address label, packing slip and multiple product photos") was endorsed by Jameson_Amazon: "I'm happy to see that @… provided great advice on next steps" (thread posted 2024-08-21, https://sellercentral.amazon.com/seller-forums/discussions/t/aa7d890f-a9ac-457b-a160-4dc8e2346342). [official, staff endorsement of a seller's list]

**(b) What practitioners add.**

- **Mr Prime:** "Photograph every removal delivery as you open it; most of the evidence Amazon asks for can only be captured on that day." [opinion]
- **A seller's case (thread posted 2026-06-25).** The seller received eight wrong units across two removal orders. Seller Support first paid on a product photo plus a tracking-label photo. It then asked for "Unboxed product photos and LPN stickers" for each unit. The case was resolved only after escalation by forum staff (Angie_Amazon, Manny_Amazon) and Executive Seller Relations (https://sellercentral.amazon.com/seller-forums/discussions/t/da0a8dbe-487f-47f2-9207-5ad59d77d531). [opinion, a seller's account; staff replies official]
- **Chinese practitioners treat the unboxing video (开箱视频) as the core evidence.**
  - 环至美物流 (2025-06-04): 海外仓的开箱视频、显示标签与实物数量不符的照片 (the warehouse's unboxing video, photos showing label versus count). It also names the test that places a shortfall: "如果海外仓入库数量 < 亚马逊移除订单数量：问题发生在亚马逊移除环节或物流运输环节" (if the warehouse received fewer than the removal order states, the loss was in Amazon's removal or in transit).
  - 搜狐 (2025, https://www.sohu.com/a/909477311_122014422): film from the sealed parcel, all six faces and the waybill, in one take. [opinion]
- **No Amazon text read names a video as accepted or required** [inferred from absence].

**(c) Into a skill.** Amazon's evidence list as dated text. The LPN and the shipment ID are on Amazon's list. Photos of the box, the label and the units can only be taken at receipt.

**Read at run time.** The fields are listed below.

- From the SP-API (Pricing or Amazon Fulfillment):
  - the removal order id (`order-id`);
  - FNSKU, quantities, carrier and tracking (Removal Shipment Detail);
  - LPNs, for returned units (customer returns report `license-plate-number`).
- Not in any SP-API report read:
  - the "Shipment ID": Removal Shipment Detail has no shipment-id column ([official] FBA Reports page, updatedAt 2026-10-13). It is read in Seller Central's removal order page or on the packing slip [inferred];
  - photos, box and label, which are the seller's own.

---

## E. How a removal claim is valued

**(a) Amazon's rule.**

- **Before 2025: estimated proceeds.** "If we elect to reimburse you for a removal claim, we will reimburse you for the estimated proceeds of the sale of that item, unless the item was in an unsellable condition when removed from the Amazon fulfilment network. For unsellable removal items, Amazon will reimburse you at a valuation consistent with the estimated proceeds of the discounted sale of the unit." [official] (EU policy redline, PDF created 2021-04-12, https://m.media-amazon.com/images/G/02/rainier/help/legal/FBA_inventory_reimbursement_policy_April_2021_English_Redlined.pdf)
- **Since the 2025 change: sourcing cost.** "For shipment to Amazon claims, removals claims, and fulfillment center operations claims that occur before fulfillment, we will reimburse you the manufacturing cost of the item … For items that were in unsellable condition when lost, damaged or removed from the Amazon fulfillment network, we will reimburse at a reduced estimated cost of the unit". The old "estimated proceeds" sentence for removal claims is struck through in each redline. [official; strikeouts command-verified by reading line drawings over the text spans with PyMuPDF]
  - US: created 2024-12-18 (`PC__Kiwi_Comms_redlined_policy_US_clean.pdf`) and 2025-02-24 (`Redlined_FBA_Reimbursement_policy_US.pdf`).
  - UK: created 2024-12-11 (`_PC__Kiwi_Comms_redlined_policy_UK_clean_version.pdf`).
  - Japan: page "as of 02/19" (2025), JPY cap (`redline_FBA_reimbursement_policy__EN_version.pdf`).
  - Wording: the US 2024-12-18 and UK 2024-12-11 redlines say "manufacturing cost"; the US 2025-02-24 and JP 2025-02-19 redlines say "sourcing cost" for the same sentence. The quote above is the 2024-12-18 US text. [command-verified, text extraction]
  - Canada, Chinese: created 2025-02-24 (`Redlined_FBA_Reimbursement_policy_CA-zh_cn.pdf`): "对于在配送之前发生的发往亚马逊的货件索赔、移除索赔和运营中心操作索赔，我们将向您赔偿商品的采购成本" (for shipment-to-Amazon, removal and FC claims occurring before fulfilment, we reimburse the sourcing cost).
  - The effective date is the finance pack's (P-ref-14, P-ref-15: 2025-03-31 in the US).
- **The per-unit cap and the valuation-dispute window** are value-and-reversals' (VR29, VR20). This file's reads that VR29 and VR20 do not yet carry are handed there (see *Notes for other files of this pack*): the JP redline's cap and dispute window.
- **Japan.** The JP redline (English, `redline_FBA_reimbursement_policy__EN_version.pdf` on Amazon's JP image path G/09, PDF created 2025-02-19, "※This Help page is as of 02/19", re-read 2026-11-13) says: "For shipment to Amazon claims, removal claims, and fulfillment center operations claims, we will reimburse you the sourcing cost of the item"; "For removal claim of unsellable items, we will reimburse at a reduced estimated cost of the unit"; "You can provide your sourcing cost for an item on the “Manage Your Sourcing cost” page on the Inventory Defect & Reimbursement (IDR) portal"; and "Note: After April 1, 2025, we will periodically refresh our cost estimates". The old "estimated proceeds" sentence for removal claims is still in its text layer, struck in the rendering (strike command-verified in the earlier pass). The PDF names no store; Japan is read from the JPY amount, the "consumption tax" wording and the G/09 path [inferred]. [official]

**(b) What practitioners add.**

- **Packaging-only damage, 2019.** A seller received a damaged removal unit and was paid 20% for "only packaging damage and there is no damage to the unit". Seller Support's re-evaluation reply called it "the final decision" (thread posted 2019-07-30, https://sellercentral.amazon.com/seller-forums/discussions/t/45e6c264964867c1d0629bca469a97cb). [opinion; Amazon's reply quoted by the seller; predates sourcing-cost valuation]
- **Sourcing cost lowers payouts.** Seller Labs (Nhan Dinh, 2026-03-18): a $50 product costing $15 "went from roughly $50 to roughly $15 per unit". AMZ123 (2026-11-02, finance pack): reported payouts "下降了50%到75%" (down 50% to 75%). [opinion]

**(c) Into a skill.**

- Removal claims are valued like other pre-order events: sourcing cost, reduced for units already unsellable when removed.
- The cap and the dispute window: see value-and-reversals VR29, VR20.

**Read at run time.**

- The seller's entered sourcing cost and how it is read: see value-and-reversals (VR11, VR18).
- What was paid: `GET_FBA_REIMBURSEMENTS_DATA` (`amount-per-unit`, `reason`, `case-id`), Pricing or Amazon Fulfillment (finance pack P-ref-19).

---

## F. The data: reports, ledger and Finances, with their pitfalls

**(a) Amazon's rule** [official] (*Fulfillment by Amazon (FBA) Reports*, https://developer-docs.amazon.com/sp-api/docs/report-type-values-fba.md, updatedAt 2026-10-13).

- **`GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA`.**
  - Roles: Pricing, Amazon Fulfillment. "This report can only be requested."
  - "Contains all the removal orders, including the items in each removal order, placed during any given time period. This can be used to help reconcile the total number of items requested to be removed from an Amazon fulfillment center with the actual number of items removed, along with the status of each item in the removal order. Content updated in near real-time."
  - Columns: `request-date`, `order-id`, `order-source`, `order-type`, `service-speed`, `order-status`, `last-updated-date`, `sku`, `fnsku`, `disposition`, `requested-quantity`, `cancelled-quantity`, `disposed-quantity`, `shipped-quantity`, `in-process-quantity`, `removal-fee`, `currency`.
  - The stock pack holds these columns (E-R6, R3). They are restated here only as the join keys.
- **`GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA`.**
  - Roles: Pricing, Amazon Fulfillment.
  - "Provides shipment tracking information for all removal orders and includes the items that have been removed from an Amazon fulfillment center for either a single removal order or for a date range. This report will not include canceled returns or disposed items; it is only for shipment information."
  - Columns: `request-date`, `order-id`, `shipment-date`, `sku`, `fnsku`, `disposition`, `shipped-quantity`, `carrier`, `tracking-number`, `shipment-status` (IN store only), `removal-order-type`.
  - **There is no shipment id, no delivery date and no carrier status outside India.**
- **`GET_LEDGER_DETAIL_VIEW_DATA`.** Role: Amazon Fulfillment only. It has the `eventType` value `VendorReturns` beside `Adjustments` and the rest. The summary view has a `Vendor Returns` column and a `Disposed` column. The page names "removals" among the ledger's movements, and the detail view's description says it covers products "removed/disposed". The pack's reading that `VendorReturns` is where removals and disposals post is [inferred]: no Amazon page read says so in those words.
- **Finances v0** (financesV0.json, model commit db2936aa) [command-verified].
  - `RemovalShipmentEvent` ("A removal shipment event for a removal order"): `MerchantOrderId` ("The merchant removal `orderId`"), `OrderId`, `TransactionType` ("Possible values: `WHOLESALE_LIQUIDATION`"), and per item `RemovalShipmentItemId`, `FulfillmentNetworkSKU`, `Quantity`, `Revenue`, `FeeAmount` ("The fee that Amazon charged to the seller for the removal of the item. The amount is a negative number."), `TaxAmount`, `TaxWithheld`.
  - `RemovalShipmentAdjustmentEvent`: "A financial adjustment event for FBA liquidated inventory. A positive value indicates money owed to Amazon by the buyer (for example, when the charge was incorrectly calculated as less than it should be). A negative value indicates a full or partial refund owed to the buyer (for example, when the buyer receives damaged items or fewer items than ordered)." Per item `AdjustedQuantity`, `RevenueAdjustment`.
  - `FBALiquidationEvent` with `OriginalRemovalOrderId` (finance pack H4).
- **Finances v2024-06-19** `listTransactions` (Finance and Accounting) carries `REMOVAL_SHIPMENT_ITEM_ID` as a related identifier ("An identifier for an item in a removal shipment") [command-verified].
- **Retirement.** Finances v0 is deprecated, with removal on 2027-08-27 (finance pack, Deprecation Schedule).

**(b) What practitioners add.**

- **Value sets Amazon does not publish:**
  - `order-type`: "Return", "Disposal", "Liquidations" (GorillaROI, 2025-02-27, https://help.gorillaroi.com/en/articles/10670129-gorilla_removalsdetails-get-details-from-removal-orders); five types, "Return, Disposal, Donation, Liquidation and Order Disposal" (SellerSpace, 2025-08-01, https://www.sellerspace.com/en/help/doc/removal-reports-use-guide/);
  - `order-status`: "Completed", "Pending", "Cancelled" (GorillaROI); also "Delivered" (SellerSpace); "Canceled" spelt with one l (InventoryLab, 2025-06-05);
  - `disposition`: "Sellable", "Unsellable". [opinion]
- **No store column.**
  - 领星 Lingxing: "移除货件需要确定店铺（针对欧洲和北美的货件数据会有这种情况）" (a removal shipment's store has to be set by hand for European and North American data). Its removal-order help says Amazon offers no cancellation interface, and a liquidation-type order cannot be created through the interface until created in Seller Central (https://www.lingxing.com/help/article/removeInbound, …/removeOrder, undated).
  - SellerSpace: "the data returned by the Amazon API cannot determine which store a removal order belongs to". [opinion] Neither removal report lists a marketplace column [official, FBA Reports page].
- **Reimbursements report `reason` values seen for removals:** `REMOVAL_ORDER_LOST`, `REMOVAL_ORDER_DAMAGED` (Synder; Lingxing OpenAPI doc; finance pack). [opinion]
- **One order, many parcels.** PrepVia: a 600-unit removal "can arrive as a dozen boxes over five weeks, from four different fulfillment centers". The shipment report maps tracking numbers to SKUs and quantities "but not to the contents of each carton". [opinion]

**(c) Into a skill.**

- The two reports, their roles and grain: order × SKU × disposition, and shipment × SKU.
- That the shipment report omits cancelled and disposed units.
- That the shipment id and the delivery date are not in it.
- That no removal report says which store an order belongs to.
- The Finances events for removals and liquidations, with their meanings.

**Read at run time.** The reports above for the seller's own account, through the door. The value sets of `order-type`, `order-status`, `order-source` and `disposition` are read from the seller's own rows; Amazon publishes none.

---

## G. Lost, short, wrong and damaged removal shipments

**(a) Amazon's rule.** The scope (§ A), the windows (§ B) and the evidence (§ D) apply.

- **Lost or damaged by the carrier.** The scope names "a carrier used by Amazon". A unit lost by that carrier is Amazon's under the policy [official]. Amazon's carrier and tracking number for each parcel are in Removal Shipment Detail [official].
- **Processing time.** Amazon staff: removals "typically take 10 to 14 business days to pick, pack, and process. However, the time may increase to 90 days or more during peak removal periods. After the shipment has left the fulfillment center, please allow an additional two weeks for the carrier to deliver." [official, staff] (stock pack E-R2)

**(b) What practitioners add.**

- **Charged, "Completed", never shipped.** A UK seller (thread posted 2025-06-13) reports a removal order shown as "Completed" and charged, with two UPS shipments of 128 units whose tracking numbers UPS called "invalid" (https://sellercentral-europe.amazon.com/seller-forums/discussions/t/d804ff56-c3ad-4c0f-a8d0-5b75c7137448). [opinion]
- **Accepted, then refused on ASIN status.** A seller (DE host, posted 2025-05-24): Amazon accepted FC mishandling for 12 missing units, then declined payment because the ASIN had since been deactivated as "prohibited" (https://sellercentral.amazon.de/seller-forums/discussions/t/dd5bdcce-13d7-437d-8ea9-e56d4272d1a4). This fits the eligibility line "complies with FBA product restrictions" (§ A). [opinion; the link to the policy is inferred]
- **Another seller's goods, or items not in the catalog.** "removal boxes sometimes hold more than the order states, or another seller's product" (PrepVia). [opinion]
- **Six months, 411 of about 1,000 units outstanding** (posted 2024-08-22). Support told the seller "Please wait up to 150 days". Amazon had split the order into about ten removal orders by cancelling parts (https://sellercentral.amazon.com/seller-forums/discussions/t/f14d6bee-4bb6-42be-9040-5201938181ed). [opinion]
- **Losses split by stage** (环至美物流, 2025-06-04): Amazon packing errors ("人工装箱失误：这是最常见的原因"); "已移除" shown with nothing shipped; carrier loss; LTL boxes lost in break-bulk. [opinion]
- **The arrival stretches past the window.** "If you wait for the dribble to finish before reconciling, the claim window on the boxes that never arrive can close" (PrepVia). [opinion]

**(c) Into a skill.**

- Shortfall arithmetic per order × FNSKU: `shipped-quantity` (orders) against the sum of `shipped-quantity` in the shipment report, against what the seller received (the seller's own record; no SP-API field).
- A shipment's tracking number is the key to the carrier's delivery record.
- An order can be "Completed" with parcels that never moved.
- Arrival can stretch past a claim window.

**Read at run time.**

- Both removal reports (Pricing or Amazon Fulfillment).
- The seller's receiving count.
- The carrier's tracking page per `tracking-number`. A public web page, outside the SP-API; whether cx may fetch it is a door question.
- Whether a reimbursement already exists: `GET_FBA_REIMBURSEMENTS_DATA` by FNSKU and date (Pricing or Amazon Fulfillment).

---

## H. Cancelled removal orders, and fees on them

**(a) Amazon's rule.**

- **Why Amazon cancels.** "Please note that Amazon may cancel a removal order if the inventory isn't available for removal, for example, when it's part of a pending customer order." [official, staff] (Jameson_Amazon, thread posted 2024-11-12, https://sellercentral.amazon.com/seller-forums/discussions/t/3ead5335-1d9c-46f2-a41c-197b892e2ba3)
- **When the fee is charged.** Since 2026-03-01 (US, orders created from that date) removal and disposal fees are charged "on a per-unit basis at the time each unit is removed or disposed of. Previously, these fees were charged all at once when the entire removal or disposal order was completed." [official] (News 2f4edad8, US marketplace field, article 2026-01-29, revised; stock pack E-R4)
  - UK from 2026-05-01: "Effective from May 1, 2026" (News 862f270b, posted 2026-04-09, marketplace field UK, read 2026-11-13; stock pack).
  - Under per-unit charging, a cancelled unit is never removed and so is not charged [inferred from the rule's wording].
- **Cancelling a seller-created order.** It can be cancelled only in Planning status; orders Amazon creates cannot be cancelled (stock pack E-R3).

**(b) What practitioners add.**

- **Units cancelled out of an order may be lost.** PrepVia: "A cancellation is the system reporting that it could not find enough of what you asked for where it expected to find it." Units that sold meanwhile are no problem. Units the ledger still shows on hand may be lost inventory, which a fulfilment-centre claim covers. [opinion]
- **Cancellations, overage and storage fees.** A seller (posted 2024-06-05) reports 1,828 and 1,457 units cancelled from two removal orders, units "stuck in 'FC Processing'", and overage fees refused because "the items are still in the FC" (https://sellercentral.amazon.com/seller-forums/discussions/t/e7588253-14dd-449e-9f37-1a1ebac70210). [opinion]
- **Disposal orders cancelled again and again.** Sellers report it (posted 2026-02-02 and 2025-08-18); one was told the unit was "in a warehouse that does not accept removals" (threads 4e166a45, 367e6a81). [opinion]
- **No Amazon text read says whether a fee charged before 2026-03-01 on an order completed with cancelled units was refunded** [inferred from absence].

**(c) Into a skill.**

- `cancelled-quantity` names units that did not leave.
- Under per-unit charging, the fee follows units removed or disposed, so a fee with no matching shipped or disposed unit has no counterpart in Amazon's stated rule [inferred].
- A unit cancelled from a removal and absent from both the shipment report and sellable stock never left the facility, so the removals page does not cover it; the policy page that covers a unit lost inside the facility is the fulfilment-centre operations page, which is the fc-lost-damaged area's [inferred from the scope sentence].

**Read at run time.**

- Removal Order Detail (`cancelled-quantity`, `removal-fee`, `order-source`).
- The ledger detail for the FNSKU (Amazon Fulfillment).
- Fee lines: Finances `listTransactions` (Finance and Accounting), and v0 `RemovalShipmentEvent.FeeAmount` (Finance and Accounting, or Amazon Fulfillment in NA and FE).
- Seller Central Payments → Transaction view, which Amazon names for "shipment level charges and when units are removed".

---

## I. Disposals: charged but still in stock, or disposed without a request

**(a) Amazon's rule.**

- **Not eligible.** "The item is not pending disposal or was not disposed of at your request or because we have exercised a right to do so." [official] (policy, § A)
- **Outside the portal.** The IDR portal "doesn't include defects under … warehouse disposals." [official] (finance pack E3)
- **Required removals.** When Amazon identifies "unsuitable units", the seller has "only 14 days to create a removal order before Amazon automatically disposes of the inventory", and "You cannot cancel a required removal order once Amazon creates it". [official, staff] (stock pack D8)
- **UK/EU notice.** Unfulfillable stock with no automated settings is disposed of or donated "after 23 days' notice" (from 2024-09-16), and "it can't be cancelled". [official] (stock pack D7)
- **US Donations.** "Dispose" means donation, mandatory from 2025-10-30, at the usual disposal fee (finance pack P-ref-48, P-ref-49).
- **Dangerous goods.** Disposal after a dangerous-goods classification is § L; disposal of stranded units under the settings is § M.
- **Amazon may dispose of what it reimbursed.** "We may dispose of any item for which we reimburse you under this policy, including by selling it." [official] (policy)

**(b) What practitioners add.**

- **Seller Labs** (Nhan Dinh, 2026-03-18): the ledger reason "Inventory disposed of" means "Amazon disposed of the unit on their own" and is claimable "Yes — if you didn't request it". Match on "FNSKU and date range — not just FNSKU alone". [opinion] (https://www.sellerlabs.com/blog/fba-reimbursement-audit-amazon-owes-you-2026/) Amazon's own policy line (above) excludes disposals "because we have exercised a right to do so". The two disagree on a disposal Amazon chose. Not resolved.
- **Seller Investigators** (Carbon6) lists "Disposed by Amazon"; GETIDA lists units "disposed of"; Refund Retriever lists "Disposed of inventory" (finance pack, What practitioners add). [opinion]
- **Charged twice for one unit.** My Amazon Guy (Noah Wickham, 2025-10-31): found units, once reimbursed, were reversed and then charged disposal (finance pack). [opinion]
- **Units back after liquidation.** A seller (posted 2024-06-12) liquidated all units, saw zero stock and a "liquidation was completed" notice, then found a 200-unit removal order "I did not create" charged $469 (https://sellercentral.amazon.com/seller-forums/discussions/t/71219d12-c888-4de7-8d6a-693de43e40cf). [opinion]

**(c) Into a skill.**

- A disposal the seller asked for, and a unit pending disposal, are outside the policy.
- A disposal by Amazon's right is outside the policy in Amazon's words; practitioners claim it anyway.
- "Charged but still showing" is a mismatch between `disposed-quantity` (Removal Order Detail) or the disposal fee line, and the ledger's ending balance or FBA inventory for the FNSKU.
- Before 2026-03-01 (US) the fee posted at order completion, so a mismatch on an older order may be timing. Since then the fee posts per unit.

**Read at run time.**

- Removal Order Detail (`order-type`, `disposed-quantity`, `order-source`).
- Ledger detail with `eventType` `Adjustments` and `VendorReturns`, and summary `Disposed` (Amazon Fulfillment).
- FBA inventory: `getInventorySummaries` (stock pack's).
- The disposal fee lines in Finances.
- Whether the seller asked for the disposal: `order-source`, whose values Amazon does not publish, and the automated settings, which are Seller Central only (stock pack S1).

---

## J. Liquidation as it bears on a removal claim

Liquidation as money is the finance pack's (fulfilment-charges.md § H4; P-ref-49). This section covers only what touches a claim.

**(a) Amazon's rule** [official, command-verified in financesV0.json].

- A liquidation sale posts as `RemovalShipmentEvent` with `TransactionType` `WHOLESALE_LIQUIDATION` and per-item `Revenue` and `FeeAmount`.
- A later buyer dispute posts as `RemovalShipmentAdjustmentEvent`. Its description: "A negative value indicates a full or partial refund owed to the buyer (for example, when the buyer receives damaged items or fewer items than ordered)."
- `FBALiquidationEvent` ("This event is used only in the US marketplace") carries `OriginalRemovalOrderId`.
- A liquidation order "cannot be canceled" once confirmed (stock pack E-L4).

**(b) What practitioners add.**

- **Missing from the report.** A seller reports liquidations, "including the immediate liquidation quantity after customer returns", missing from Removal Order Detail (stock pack O5). [opinion]
- **Not created through the API.** Lingxing: a liquidation-type removal order cannot be created through the interface until made in Seller Central. [opinion]
- **No Amazon or practitioner text read describes a reimbursement claim for units sent to liquidation that never reached the liquidator** [inferred from absence]. Topher_Amazon's staff guide (thread 6fee30d4, posted 2025-06-23, re-read 2026-11-13) covers fees, timing and cancelling, and says nothing of units missing from a liquidation order or of a claim for them. The search budget for this pass ran out before Chinese and practitioner sources on liquidation shortfalls could be searched; this absence is weaker than the others in this file.

**Shortfalls: what the rules and the data allow** (added 2026-11-13).

- **Units sent to liquidation that never reached it.** The removals page's scope covers units lost or damaged "while removing your inventory from a fulfillment center to your returns shipping address" (§ A). A liquidation order's units go to a contracted liquidator, not to the seller's returns address, so the scope sentence does not cover them by its wording [inferred]. A unit that never left the facility falls under the fulfilment-centre operations page, which is fc-lost-damaged's [inferred from the scope sentence, as in § H].
- **What the data shows per unit.** `FBALiquidationEvent` carries `PostedDate`, `OriginalRemovalOrderId`, `LiquidationProceedsAmount` and `LiquidationFeeAmount` and nothing else: no quantity, no SKU, no FNSKU [command-verified, financesV0.json at db2936aa]. Units appear per item only in `RemovalShipmentEvent` with `TransactionType` `WHOLESALE_LIQUIDATION` (`FulfillmentNetworkSKU`, `Quantity`, `Revenue`, `FeeAmount`), keyed by `MerchantOrderId`. Removal Order Detail gives the order's `requested-quantity`, `cancelled-quantity`, `shipped-quantity` and `disposed-quantity`. A unit requested for liquidation and neither shipped, cancelled nor back in stock, or shipped and absent from every `WHOLESALE_LIQUIDATION` item line, has no counterpart in Amazon's stated events [inferred].
- **Proceeds below the stated rate.** Amazon's staff text says liquidators pay a gross recovery value "typically 5-10% of the product's original value" (stock pack S19, E-L1). "Typically" is not a promise, and no Amazon text read gives a seller a claim when proceeds fall below it [inferred]. The amounts, the fees and the 90-day payment are money: finance pack P-ful-11, stock pack S19.
- **Who can be liquidated.** Dangerous goods, recalled stock and some other classes are not eligible (stock pack S20); a liquidation order cannot be cancelled once confirmed (stock pack E-L4).

**(c) Into a skill.**

- A liquidation buyer's damage or shortfall claim comes back to the seller as a negative revenue adjustment tied to the removal order. It is not a reimbursement.
- A liquidation shortfall is visible only by joining the removal order's quantities to the item lines of the liquidation sale, because the US liquidation payment event carries no quantity.
- Units sent to liquidation are outside the removals page's scope sentence by its wording; no Amazon text read names a claim for them or for proceeds below the typical rate.

**Read at run time.** Finances v0 `listFinancialEvents` (`RemovalShipmentEventList`, `RemovalShipmentAdjustmentEventList`, `FBALiquidationEventList`; roles: sp-api-claims-surface SU5), or `listTransactions` (Finance and Accounting); then Removal Order Detail by `order-id`. `FBALiquidationEvent` is "used only in the US marketplace"; how a liquidation posts elsewhere is the finance pack's (P-ful-11).

---

## K. What the SP-API cannot do here, and the roles for what it can

**(a) Amazon's rule** [official, Role Mappings; FBA Reports page].

| Read | Role Amazon names |
|---|---|
| Removal Order Detail, Removal Shipment Detail | Pricing or Amazon Fulfillment |
| Reimbursements report | Pricing or Amazon Fulfillment |
| FBA customer returns report | Pricing or Amazon Fulfillment |
| Ledger detail and summary | Amazon Fulfillment |
| Finances v0 `listFinancialEvents` | Finance and Accounting; Amazon Fulfillment (NA, FE); AISP (EU) |
| Finances `listTransactions` | Finance and Accounting |
| Support API (reading a filed case) | see sp-api-claims-surface SU8, SU10 |
| `POST_FLAT_FILE_FBA_CREATE_REMOVAL` (creates removal orders; a write, not a claim) | Amazon Fulfillment (stock pack S18) |
| `getItemEligibilityPreview` (whether an ASIN is under dangerous-goods review or classed unfulfillable; § L) | Amazon Fulfillment (stock pack I20) |

**Not possible through the SP-API, for removals specifically:** opening a removal claim ("Resolve a removal order issue"), attaching photos, cancelling a removal order (stock pack S17), reading the automated unfulfillable and stranded settings (stock pack S15), and contesting a dangerous-goods classification (no operation in the models at db2936aa names a dangerous-goods review, a safety data sheet or an exemption sheet [command-verified: grep of operation ids and descriptions]; whether a listing's own hazmat attributes, set through the Listings Items API under product-type schemas that are not in the models, reach the review was not read [open]). That no operation files, evidences or disputes any claim is sp-api-claims-surface's (SU12); Shipping API v2 `createClaim` is a carrier claim, not a removal claim (SU13).

---

## L. Dangerous goods: reclassification, disposal, and whether a wrong one is claimable

Added 2026-11-13. Dangerous goods as a stock state (review blocks sale and inbound; review times in the eligibility reason codes) are the stock pack's (G18; programs-and-regions.md H1, J9). This section covers only what bears on a claim.

**(a) Amazon's rule.**

- **The eligibility reason code** (FBA Inbound Eligibility v1, `fbaInbound.json` at db2936aa, read 2026-11-13) [official, command-verified]:
  - `FBA_INB_0015`: "Dangerous goods (Hazmat). The product is regulated as unfulfillable and not eligible for sale with Amazon. We ask that you refrain from sending additional units in new shipments. We will need to dispose of your dangerous goods inventory in accordance with the terms of the Amazon Business Services Agreement. If you have questions or concerns, please contact Seller Support within five business days of this notice."
  - `FBA_INB_0014`: under review the product "is unfulfillable and cannot be received at Amazon fulfilment centers or ordered by customers".
- **The agreement.** The Australian Business Solutions Agreement (Amazon.com.au, PDF `AmazonServicesBusinessSolutionsAgreement_2024edits1.pdf` on m.media-amazon.com, created 2024-06-12, read 2026-11-13) [official; AU text; other stores' agreements not read in this pass]:
  - F-7.2: "We may dispose of any Unsuitable Unit (and you will be deemed to have consented to our action): (a) immediately if we reasonably determine that the Unit creates a safety, health, or liability risk to Amazon, our personnel, or any third party; or (b) if you fail to direct us to return or dispose of the Unit within thirty (30) days … after we notify you that (i) its removal is required …".
  - F-7.3: "Title to each disposed Unit will transfer to us (or a third party we select such as a charity) at no cost to us … You agree that we may retain any proceeds we may receive from the disposal."
  - "Unsuitable Unit" includes a Unit that "is an FBA Excluded Product", "does not comply with Law or the Agreement" or "is unsellable or unsuitable for storage and fulfilment".
  - On loss in storage: "If there is a loss of or damage to any Units while they are being stored, we will reimburse you in accordance with the FBA Guidelines".
- **The reimbursement policy** excludes an item that does not comply "with FBA product restrictions and with FBA inventory requirements", and an item disposed of "because we have exercised a right to do so" (§ A, US PDF 2024-12-18). [official]
- **Seller Support's wording, as a seller quoted it** (thread ebd40f57, posted 2024-08-02, US field, read 2026-11-13): "It is your responsibility to know whether the products you are shipping are regulated as hazardous materials. Hazardous materials that are shipped to Amazon fulfillment centers may be subject to disposal without reimbursement, even if they have not been previously identified by Amazon as hazardous materials." "Existing inventory needs to be destroyed. If you feel it's non hazmat we request you to submit SDS and wait 2 business days for the review to be completed." [official text relayed by a seller]
  - Search summaries of 2026-11-13 attribute the first two sentences to Amazon's help page *FBA prohibited products* (G201730840), and "Products identified as unfulfillable dangerous goods upon receipt at a fulfillment center may be disposed of at your expense" to *Dangerous goods identification guide (hazmat)* (201003400). Neither page was read; both are help pages that serve a script shell. [search summary; page unread]
- **Staff on documents and timing.** Michelle_Amazon (reply of 2025-06-06 in thread 5c1c2d65, US field, read 2026-11-13): "Products with complete and correct dangerous goods information will be reviewed and classified within two business days"; "You'll have 14 business days to provide the requested documentation. If the documentation is not provided during this period, the inventory will be disposed of, at your expense." [official, staff]
- **Staff on an immediate disposal after approval.** A seller (thread 978f97fe, posted 2026-08-06, UK field) reports an ASIN approved for the FBA Dangerous Goods Programme, 117 units sold, then 267 units moved from sellable to defective and disposed of the same day after a physical review found an "Extremely Flammable" pictogram; the seller relays Amazon's citing Section F.7.3 of the European agreement and "no reimbursement will be provided". Glenn_Amazon replied (2026-08-10): "Based on your general description the correct actions were taken. While uncommon, if units pose significant dangers to the Fulfillment Center this may result in immediate disposal of inventory." [official, staff; the seller's account opinion]

**(b) What practitioners and sellers add.**

- **Sellers asking for reimbursement after a wrong flag.** A seller (thread 29f8a8cd, posted 2025-09-11, US field) passed a compliance review, yet units kept being treated as defective and some were disposed of, about USD 25,000; the seller asks Amazon to "handle reimbursement under the FBA lost/damaged policy". No outcome is in the thread as read. [opinion]
- **Repeated flags and blocked removals.** A seller (thread cb7207be, posted 2025-12-04, US field) reports a product flagged as hazardous "multiple times" after two SDS submissions, and a removal order that could not be created while the SKU was "stuck under the hazmat classification". The 2024-08-02 seller (ebd40f57) also reports a removal order that "did not work" for an ASIN classed prohibited. [opinion]
- **An older UK case.** A seller (thread 0128a8b3, posted 2021-10-08) reports a removal order cancelled and the units destroyed instead; another seller replying guesses a hazmat flag. [opinion]
- **No practitioner or Chinese source read describes a successful reimbursement for units disposed of after a dangerous-goods classification later found wrong.** The search budget ran out before gs.amazon.cn and Chinese practitioner pages on 危险品 disposal could be searched [absence; search incomplete].

**(c) Into a skill.**

- Amazon classes a unit unfulfillable dangerous goods, may dispose of it, and states the agreement as the basis; under the Australian agreement's wording, disposal for a safety risk can be immediate and the seller is deemed to consent.
- The policy excludes units that fail FBA product restrictions and units disposed of by Amazon's right; no Amazon text read says a disposal after a classification later found wrong is reimbursable, and Amazon's staff and Seller Support describe disposal "without reimbursement" [inferred from absence for the wrong-classification case].
- The route Amazon names against a classification is the review itself (a safety data sheet or exemption sheet, within the time Amazon states) and a Seller Support contact within the time the notice states; these run before disposal.
- Dangerous goods are not eligible for liquidation (stock pack S20), and sellers report removal orders blocked while a classification stands.

**Read at run time.**

- Whether an ASIN is under review or classed unfulfillable: `getItemEligibilityPreview` reason codes (Amazon Fulfillment; stock pack I20, J9).
- Whether units were disposed of, and when: the ledger detail (Amazon Fulfillment) and Removal Order Detail (`order-type`, `disposed-quantity`, `order-source`); whether a DG disposal shows as a removal order at all was asked by the 2026-08-06 seller and is unread.
- The time limits Amazon states (documents, contact): the notice the seller received and the store's dangerous-goods pages in Seller Central, which the seller opens. See *Values that move*.

---

## M. Removal of stranded units

Added 2026-11-13. Stranding itself (definition, the stranded report, auto-removal, relisting, the listing side) is the stock pack's: research/README.md S1 to S8 and skills/stuck-stock/references/stranded.md. Storage charged on units stranded by Amazon's error is fee-overcharges'.

**(a) Amazon's rule.**

- Stranded units leave by a removal order the seller creates, or by Amazon's auto-removal or disposal under the stranded settings; with no setting the units are disposed of (stock pack S3). The settings cannot be read through the SP-API (S15).
- Once they leave, stranded units are removal units like any other: the removals page's scope (§ A), windows (§ B) and evidence (§ D) apply; no Amazon text read gives stranded removals a rule of their own [inferred from absence].
- A disposal under the stranded settings, or with no setting, is a disposal at the seller's request or by Amazon's exercise of a right, both outside the policy (§ I) [inferred from the policy's wording].

**(b) What practitioners add.** Seller Labs (updated 2026-09-03, via stock pack P9): units stranded by a dangerous-goods review sit in a fulfilment centre with "zero sellable quantity". No practitioner text read describes a claim specific to stranded removals [absence].

**(c) Into a skill.** A removal of stranded units is claimed like any removal; its disposal under the settings is outside the policy; stranding and its storage are other homes'.

**Read at run time.** `GET_STRANDED_INVENTORY_UI_DATA` (`stranded-reason`, `date-stranded`, `Date-to-take-auto-removal`; stock pack S2) joined to Removal Order Detail by SKU and date; then the removal reports as in § F.

---

## Positions

Tags: [read in official docs], [command-verified], [opinion], [inferred]. "Seat's own" enters no skill.

- **RM1.** A removal claim covers eligible units lost or damaged by Amazon, or by a carrier Amazon used, after they left an Amazon facility on the way to the seller's return address. It does not cover units returned because the seller broke a policy. Source: removals-claims page text (EU redline 2024-08-20; Hopted copy of the US page); the same sentences on Amazon Supply Chain's SCP page, another programme's (read 2026-11-13). The live Seller Central page was not read by a permitted route. [read in official docs]
- **RM2.** All removal claims are filed manually: every Amazon automation post of 2024 says so, and nothing read through 2026-11-13 announces removal automation. The posts and their stores are fc-lost-damaged's (post-to-store table); the IDR portal's exclusion of removals and warehouse disposals is filing-and-conduct's (FL5). Sources: News 81c3235d, 6605eede, d0fc997e (read 2026-11-13). [read in official docs; absence inferred]
- **RM3.** Amazon's removal claim kinds are lost in transit; damaged in transit; damaged, different or incomplete units received; and grading disputes on customer returns. Sources: EU redline 2024-08-20; News 96a05f4a (UAE, 2024-08-06). [read in official docs]
- **RM4.** The Seller Central route for a removal claim is the "Resolve a removal order issue" tool (G9ZB3H4DP4H72U6R), keyed by removal order ID (see filing-and-conduct FL4). Sources: Indy_Amazon 0e07abc1 (2026-08-13); Hopted copy. [read in official docs]
- **RM5.** A News post's windows are read as the store its post object names; the store of each post, and the tag of that reading, are fc-lost-damaged's (post-to-store table). This file adds that no removal-related post read names its store in its body text, so none could test the field against a store stated in the text. Sources: 862f270b, d8f9a56c (read 2026-11-13). [command-verified for the absence of a store in the text; the field reading as fc-lost-damaged tags it]
- **RM6.** A lost-in-transit removal claim has both an earliest and a latest filing day, and other removal claims a latest day counted from delivery back; the lengths are per store and per date, read on the store's removals-claims page and the latest News post with the store's marketplace field. Evidence, US: posted 2024-07-24, effective 2024-10-23, lost in transit "15-75 days from the shipment-creation date", "All other removal claims must be filed within 60 days of the shipment being delivered back to you" (81c3235d, read 2026-11-13). Before that, the US help page text: lost no sooner than "14 days from the last confirmed movement", all claims within "18 months of the date the item was removed" (Hopted copy, Wayback 2026-07-13; the same text struck in the EU redline of 2024-08-20). [read in official docs]
- **RM7.** Amazon's store-level posts can change all removal windows at once, can move the anchor of the grading window from delivery to the date of removal, and can add a re-evaluation window; the Australia post of 2025-08-14 (effective 2025-10-15) did all three, and no post with a US marketplace field carrying these windows was found. The values are in *Values that move*. Source: d8f9a56c (Australia field, read 2026-11-13). [read in official docs; US absence inferred]
- **RM8.** The anchor of a lost-removal window differs by store: the UAE post counts it from the shipment's ship date where the US, Canada, UK and Sweden posts count from shipment creation, and the UAE post gives received-units problems (damaged, different, incomplete) a window of their own from delivery. The values are in *Values that move*. Source: 96a05f4a (UAE field, posted 2024-08-06, effective 2024-09-05, read 2026-11-13). [read in official docs]
- **RM9.** Amazon's own texts give three anchors for the earliest filing day of a lost-removal claim: shipment creation, ship date, and the last confirmed carrier movement. A claim filed before it is refused as too early. Sources: RM6–RM8; ReclaimHQ for the refusal. [read in official docs; refusal opinion]
- **RM10.** Amazon's US staff post of 2026-08-13 gives removals 18 months "of the shipment being delivered or lost". That length matches the pre-2024 help page (which counted from removal, not from delivery or loss), not any News post. Amazon's own pages disagree, and no Amazon text read says which governs. Sources: 0e07abc1; RM6. [read in official docs]
- **RM11.** A grading dispute concerns customer returns Amazon graded customer-damaged or defective. It needs the unit physically returned through a removal order, and adds an explanation of the disagreement to the claim. Source: EU redline 2024-08-20. [read in official docs]
- **RM12.** The grading-dispute window's length and its anchor (delivery of the removal back to the seller, or the date of removal from the network) are per store and per date, read on the store's removals-claims page or tool. For the US, permitted sources give two readings and leave the current one unread: the older page text counts 30 days from delivery (Hopted copy, Wayback 2026-07-13), and the US post effective 2024-10-23 gives "all other removal claims" 60 days from delivery back, which takes in grading only by inference (81c3235d). A newer reading of the live US page recorded elsewhere in this pack came through a route closed on 2026-11-10 and could not be confirmed by a permitted route on 2026-11-13. Values and other stores: *Values that move*. Sources: Hopted copy; 81c3235d; EU redline 2024-08-20; d8f9a56c; all read 2026-11-13. [read in official docs; grading under "all other" inferred; strike command-verified]
- **RM13.** A disposed unit cannot be the subject of a grading dispute, which needs the unit returned. Automated or required disposals can remove that path before the seller acts. Sources: RM11; stock pack D7, D8; seller thread 8299f3f0. [inferred from official text]
- **RM14.** Amazon's list for a removal claim: removal order ID; shipment ID with active tracking or proof of delivery; ASINs/FNSKUs and quantities; LPN; images of the units, their packaging, the shipping box and the shipping label; and for grading, an explanation. Source: EU redline 2024-08-20 (the US copy lacks the label image). [read in official docs]
- **RM15.** Removal Shipment Detail has no shipment-id column and no delivery date. The shipment ID that Amazon's claim asks for is not in any SP-API report read. Source: FBA Reports page (2026-10-13). [read in official docs; absence command-verified by reading the column list]
- **RM16.** Photos of the box, label and units can only be taken when the parcel is opened. Seller Support has asked for per-unit unboxed photos with LPN stickers. Sources: Mr Prime (2026-10-01); seller thread da0a8dbe (2026-06-25). [opinion]
- **RM17.** Chinese practitioners treat a continuous unboxing video as the core evidence. No Amazon text read names video. Sources: 环至美物流 (2025-06-04); 搜狐 (2025). [opinion; absence inferred]
- **RM18.** Removal claims before a customer order are valued at sourcing cost, and units unsellable when removed at "a reduced estimated cost". The redlines strike the earlier "estimated proceeds" sentence for removal claims in the US, UK, Japan and Canada (Chinese) texts. The US 2024-12-18 and UK 2024-12-11 texts name the base "manufacturing cost"; the US 2025-02-24 and JP texts name it "sourcing cost". The JP text (as of 2025-02-19) also names the *Manage Your Sourcing cost* page on the IDR portal and a periodic refresh of Amazon's estimates "After April 1, 2025". Sources: Amazon policy PDFs of 2024-12-11 to 2025-02-24 (JP re-read 2026-11-13); finance pack P-ref-14 for the US effective date. [read in official docs; strikeouts command-verified]
- **RM19.** (withdrawn: the per-unit cap and the valuation-dispute window are homed in value-and-reversals, VR29 and VR20; this file's JP reads are handed there under *Notes for other files of this pack*.)
- **RM20.** Removal Order Detail is order × SKU × disposition, with requested, cancelled, disposed, shipped and in-process quantities and the fee. Removal Shipment Detail is shipment × SKU, with carrier and tracking, and omits cancelled and disposed units. Both need Pricing or Amazon Fulfillment and can only be requested. Source: FBA Reports page. [read in official docs]
- **RM21.** Amazon publishes no value sets for `order-type`, `order-status`, `order-source` or `disposition`. Practitioners report Return / Disposal / Liquidations (also Donation), Pending / Completed / Cancelled (spelling varies), and Sellable / Unsellable. Sources: FBA Reports page; GorillaROI; SellerSpace; InventoryLab. [read in official docs for the absence; values opinion]
- **RM22.** Neither removal report has a store or marketplace column. ERPs report that in NA and EU unified accounts they cannot tell which store a removal belongs to. Sources: FBA Reports page; Lingxing; SellerSpace. [read in official docs; opinion]
- **RM23.** A removal order can ship as many parcels, from several fulfilment centres, over weeks; Amazon gives no fixed processing time, and the actual span of one order is read from its own `request-date`, `shipment-date` and `last-updated-date`. Evidence: Amazon staff (US, stock pack E-R2): "typically take 10 to 14 business days … may increase to 90 days or more during peak removal periods … allow an additional two weeks for the carrier"; PrepVia (2026-08-25): a 600-unit removal "can arrive as a dozen boxes over five weeks, from four different fulfillment centers". [read in official docs; opinion]
- **RM24.** A removal order can show "Completed" and charged while some of its tracking numbers never moved. Source: seller thread d804ff56 (2025-06-13). [opinion]
- **RM25.** Amazon cancels removal-order units that are not available for removal, for example units tied to a pending customer order. Cancelled units stay in Amazon's network or were sold. Sources: Jameson_Amazon 3ead5335 (2024-11-12); PrepVia. [read in official docs; opinion]
- **RM26.** Removal and disposal fees now post per unit as each unit is removed or disposed; before the change they posted when the whole order completed. The change date is per store, read on each store's News post. Evidence: US "Effective March 1 … new orders created on or after March 1" (News 2f4edad8, marketplace field US, article 2026-01-29, revised from 2026-02-15); UK "Effective from May 1, 2026" (News 862f270b, https://sellercentral.amazon.co.uk/seller-forums/discussions/t/862f270b-81cd-4d78-8a02-7b95156040e6, posted 2026-04-09, marketplace field UK). Both read 2026-11-13. Sources: those posts; stock pack P-holding-costs-30. [read in official docs]
- **RM27.** Under per-unit charging, a removal or disposal fee with no matching shipped or disposed unit for that order and FNSKU has no basis in Amazon's stated rule. Source: RM26. [inferred]
- **RM28.** The policy excludes units disposed of at the seller's request, by Amazon's exercise of a right, or pending disposal. Practitioners claim units disposed by Amazon without a request as reimbursable. The two disagree. Sources: policy PDF 2024-12-18; Seller Labs (2026-03-18); Seller Investigators. [read in official docs; opinion]
- **RM29.** A liquidation buyer's damage or shortfall comes back as `RemovalShipmentAdjustmentEvent` (negative `RevenueAdjustment` against the removal order), not as a reimbursement. A liquidation sale posts as `RemovalShipmentEvent` with `TransactionType` `WHOLESALE_LIQUIDATION`. Source: financesV0.json (commit db2936aa). [command-verified]
- **RM30.** `listTransactions` links removal lines by the related identifier `REMOVAL_SHIPMENT_ITEM_ID`. Finances v0 links them by `MerchantOrderId` (the removal order id) and `RemovalShipmentItemId`. Source: finances_2024-06-19.json, financesV0.json. [command-verified]
- **RM31.** Practitioners report removal reimbursements under the reasons `REMOVAL_ORDER_LOST` and `REMOVAL_ORDER_DAMAGED`. Amazon publishes no reason list. Sources: Synder; Lingxing OpenAPI doc; finance pack P-ref-19. [opinion]
- **RM32.** The ledger detail's `VendorReturns` event type is where removals post. Source: FBA Reports page lists `VendorReturns` and says the ledger shows "removals". [inferred]
- **RM33.** A removal claim needs the ASIN to comply with FBA restrictions at claim time. A seller reports an accepted removal claim later refused because the ASIN was deactivated as prohibited. Sources: policy eligibility list; seller thread dd5bdcce (2025-05-24). [read in official docs; opinion]
- **RM34.** A seller reported a suspension after several removal-loss reimbursement requests (2019). Amazon's conduct rule on insufficiently researched, premature or high-volume requests is filing-and-conduct's (FL11). Source: seller thread e93106ad (2019-01-09). [opinion]
- **RM35.** No SP-API operation opens a removal claim, attaches its evidence, cancels a removal order or contests a dangerous-goods classification; reading a filed case is the restricted Support API's (see sp-api-claims-surface SU8, SU10, SU12). Sources: models at db2936aa; stock pack S17. [command-verified]
- **RM36.** Some Chinese guides misrender the help page's "no sooner than 14 days" as "within 14 days" (14天内提交). Source: 百运网 2025-04-05 against the English page text. [command-verified by comparison; opinion source]
- **RM37.** Many 2026 practitioner pages still state 15–75 / 60 days, and others state 15–135 / 120. Neither group cites a store. Sources: PrepVia, Mr Prime, ReclaimHQ; SellerSprite, Olifant, Marketplace Officer. [opinion]
- **RM38.** Amazon may dispose of units of a product it classes unfulfillable dangerous goods, and states the Business Solutions Agreement as the basis; the eligibility reason code asks the seller to contact Seller Support within a stated number of business days of the notice. The number is in *Values that move*. Sources: `FBA_INB_0015`, `fbaInbound.json` at db2936aa; Seller Support text relayed in thread ebd40f57 (2024-08-02). [read in official docs; command-verified]
- **RM39.** Under the Australian Business Solutions Agreement Amazon may dispose of an Unsuitable Unit immediately if it reasonably determines a safety, health or liability risk, the seller being "deemed to have consented"; otherwise after a notice period; title passes to Amazon and Amazon may keep any proceeds. Other stores' agreements were not read in this pass. Source: AU BSA PDF created 2024-06-12, F-7.2, F-7.3, definitions (read 2026-11-13). [read in official docs]
- **RM40.** No Amazon text read makes a unit disposed of after a dangerous-goods classification reimbursable, including a classification the seller holds to be wrong: the policy excludes units that fail FBA product restrictions and units disposed of by Amazon's exercise of a right; Seller Support's relayed text says such units "may be subject to disposal without reimbursement, even if they have not been previously identified by Amazon as hazardous materials"; and staff called an immediate disposal after DG-programme approval "the correct actions" (2026-08-10). Sellers ask for reimbursement under the lost-and-damaged policy, and no outcome was read. Sources: US policy PDF 2024-12-18; threads ebd40f57, 978f97fe, 29f8a8cd (read 2026-11-13). [read in official docs; wrong-classification case inferred from absence; sellers' requests opinion]
- **RM41.** The challenge Amazon names against a dangerous-goods classification is the review: a safety data sheet or exemption sheet within the time Amazon states, failing which the units are disposed of at the seller's expense. It runs before disposal; no route after disposal was read. Sources: Michelle_Amazon (2025-06-06, thread 5c1c2d65); Seller Support text in ebd40f57; sell.amazon.com blog (2025-01-04) for the upload tool. [read in official docs; absence of a post-disposal route inferred]
- **RM42.** Sellers report that a removal order cannot be created, or fails, while an ASIN stands classified as dangerous goods, so units can be disposed of without having left. Sources: threads ebd40f57 (2024-08-02), cb7207be (2025-12-04). [opinion]
- **RM43.** A removal of stranded units is a removal like any other once the units leave, under the removals page's scope, windows and evidence; a disposal under the stranded settings, or with no setting, falls in the policy's excluded classes. Stranding itself is the stock pack's (S1 to S8, stranded.md). Sources: § A, § I; stock pack S3, S15. [inferred from the policy's wording]
- **RM44.** The removals page's scope sentence covers units on their way to the seller's returns address; units on a liquidation order go to a liquidator, so the sentence does not cover them by its wording, and no Amazon text read names a claim for liquidation units lost before the liquidator or for proceeds below the typical recovery rate. Sources: scope sentence (§ A); Topher_Amazon 6fee30d4 (2025-06-23); stock pack S19. [inferred from the wording and from absence]
- **RM45.** The US liquidation payment event carries no quantity and no SKU (`FBALiquidationEvent`: `PostedDate`, `OriginalRemovalOrderId`, `LiquidationProceedsAmount`, `LiquidationFeeAmount`); units liquidated per FNSKU are read from `RemovalShipmentEvent` lines with `TransactionType` `WHOLESALE_LIQUIDATION` and joined to Removal Order Detail by order id. Source: financesV0.json at db2936aa; FBA Reports page. [command-verified]
- **RM46.** A Japanese-store English redline names sourcing cost for removal claims, *Manage Your Sourcing cost* on the IDR portal, and a periodic refresh of estimates after 2025-04-01, which bears on value-and-reversals' VR16 (no source for JP). Source: JP redline, PDF created 2025-02-19, "as of 02/19" (re-read 2026-11-13); the store is read from the JPY cap, "consumption tax" and the G/09 path. [read in official docs; store inferred]

---

## Values that move

| Value | As read | Store | Where cx reads it at run time |
|---|---|---|---|
| Lost-in-transit window | 15–75 days from creation (US/CA eff. 2024-10-23; UK eff. 2025-01-09; SE 2025-01-15); 15–75 calendar days from ship date (UAE eff. 2024-09-05); 15–135 days from creation (AU eff. 2025-10-15); 18 months (US staff 2026-08-13; pre-2024 page) | as listed | Seller Central *FBA inventory reimbursement policy: Removals claims* (US hub G200213130 links it) and the "Resolve a removal order issue" tool (G9ZB3H4DP4H72U6R); latest News post with the store's marketplace field |
| Damaged / different / incomplete window | 60 days of delivery back (US/CA/UK/SE); 30 calendar days of delivery (UAE); 120 days of delivery (AU); 18 months (old page; US staff 2026) | as listed | same |
| Grading-dispute window | US: 30 days of delivery (older page text, Hopted copy, Wayback 2026-07-13); 60 days of delivery back if grading sits under "all other removal claims" (81c3235d, eff. 2024-10-23; inference); a newer live-page reading not confirmable by a permitted route on 2026-11-13. EU: 30 struck, 60 days of delivery added (redline 2024-08-20; a 30 left on the returns page). AU: 120 days from removal (eff. 2025-10-15). UK: 60 days of delivery (Mr Prime, 2026-10-01, opinion) | as listed | same; the seller opens the US tool, which is not readable by cx |
| Per-unit cap; valuation-dispute window | see value-and-reversals VR29, VR20 (JP values handed there: *Notes for other files of this pack*) | — | — |
| Removal processing time | 10–14 business days, 90 days or more at peak (US staff, stock pack E-R2); 30 days or more at peak (JP, stock pack S16, not re-read here) | US, JP | cannot be read; the actual time is read per order from `request-date`, `shipment-date`, `last-updated-date` |
| Removal / disposal fee rates and charge timing | finance pack § H; per-unit from 2026-03-01 (US), 2026-05-01 (UK) | US, UK | rate pages (finance pack); charges: `removal-fee`, Finances |
| Dangerous goods: contact window on an unfulfillable classification | "within five business days of this notice" (`FBA_INB_0015`, models db2936aa, read 2026-11-13) | not stated (model text) | the notice the seller received; `getItemEligibilityPreview` reason text |
| Dangerous goods: time to provide documents before disposal | 14 business days (Michelle_Amazon, 2025-06-06, US field) | US | the review notice; Seller Central dangerous-goods pages (seller opens) |
| Dangerous goods: review time | two business days with complete information (Michelle_Amazon, 2025-06-06); 2 business days (Seller Support text, 2024-08-02); 4 and 4–7 business days (reason codes; stock pack J9) | US; model | reason text from `getItemEligibilityPreview` |
| Notice before Amazon disposes of an Unsuitable Unit (not for an immediate safety disposal) | thirty (30) days, "or as otherwise specified in the applicable Program Policies" (AU BSA, PDF 2024-06-12) | AU | the store's Business Solutions Agreement |
| Liquidation recovery | "typically 5%–10% of the product's value" (US staff, Kris_Amazon 2026-10-06, via stock pack holding-costs.md G2; not re-read here) | US | cannot be read before sale; actual from `FBALiquidationEvent` / `RemovalShipmentEvent.Revenue` |

---

## Corrections and additions to the other packs

1. **Finance pack research/areas/refunds-reimbursements-adjustments.md § E2, § F, P-ref-13, P-ref-16.**
   - The pack says "no page names the store" for the 2024 automation posts. Each post object carries a `marketplaceId` [command-verified; the mapping's home in this pack is fc-lost-damaged's post-to-store table]:
     - 6605eede is Canada, not a general 2024-07-24 post;
     - 81c3235d (US, same day, American spelling, not cited by the finance pack) says customer returns 60–120 days, not 45–105;
     - d0fc997e is UK;
     - 1101821c is Sweden;
     - d8f9a56c (the 2025-10-15 windows) is Australia.
   - The finance pack's table presents d8f9a56c's windows with no store. The stock pack's inbound.md already labels d8f9a56c Australia and 96a05f4a UAE.
   - The US customer-return window posted for 2024-10-23 was 60–120 days (81c3235d). The 45–105 days is the CA, UK and SE posts' figure.
2. **Finance pack § F "The conflict".** The surmise that the 2026-08-13 staff post restates an older page has evidence now. Its 18-month removal window and its 60-day/18-month customer-return window match the pre-2024 help-page text (Hopted copy; the struck text in Amazon's EU redline of 2024-08-20).
3. **Finance pack § E4 / P-ref-14.** No error. Added: the redlines show the "estimated proceeds" valuation struck for removal claims specifically in the US (2024-12-18, 2025-02-24), UK (2024-12-11), JP (2025-02-19) and CA-Chinese (2025-02-24) texts.
4. **Finance pack § F windows table.** It lacks the UAE 2024-09-05 post (removal damaged, different or incomplete 30 days; lost 15–75 days from ship date) and the help page's own lower bound ("no sooner than 14 days from the last confirmed movement"), which differs from the News posts' "15 days from shipment creation".
5. **Stock pack research/areas/stuck-stock.md R4.** It lists Removal Shipment Detail as `order-id`, `shipment-date`, `shipped-quantity`, `carrier`, `tracking-number`, `removal-order-type`. The full list (E-R6 there, correct) also has `request-date`, `sku`, `fnsku`, `disposition`, `shipment-status` (IN only). Neither says that the report has no shipment id, which Amazon's removal claim requires (RM15).
6. **The brief's premise that "reading a case's answer" has no door.** The Support API reads a case's status and its contacts, behind the restricted Selling Partner Support role. sp-api-claims-surface now holds it (SU8 to SU10); this entry stands only as the correction of the premise.
7. **Stock pack research/README.md S22 (`P-stuck-stock-36`) and stuck-stock.md E-L5.** S22 says `listFinancialEvents` "needs Finance and Accounting". Amazon's role mappings name Finance and Accounting, Amazon Fulfillment (NA and FE only) and AISP (EU only) for it (sp-api-claims-surface SU5; § K here). S22 also does not say that `FBALiquidationEvent` carries no quantity and no SKU (financesV0.json at db2936aa, command-verified), which is what makes a per-unit liquidation reconciliation depend on `RemovalShipmentEvent` lines (RM45).
8. **Stock pack G18 (`P-programs-and-regions-35`).** No error. Added: the reason code `FBA_INB_0015` asks for a Seller Support contact within five business days of the notice, and the AU agreement (F-7.2) allows immediate disposal for a safety risk with deemed consent (§ L); a staff reply of 2026-08-10 confirms an immediate disposal after DG-programme approval (thread 978f97fe).

---

## Notes for other files of this pack

These are facts this file read that another file of this pack is home to; that file's seat decides.

1. **value-and-reversals VR16, VR29, VR20 and its open question 3 (Japan).** The JP redline (English, `https://m.media-amazon.com/images/G/09/rainier/help/redline_FBA_reimbursement_policy__EN_version.pdf`, PDF created 2025-02-19, "※This Help page is as of 02/19", re-read 2026-11-13) evidences, for Japan:
   - sourcing-cost valuation of pre-order claims, removals included: "For shipment to Amazon claims, removal claims, and fulfillment center operations claims, we will reimburse you the sourcing cost of the item";
   - the MYSC page: "You can provide your sourcing cost for an item on the “Manage Your Sourcing cost” page on the Inventory Defect & Reimbursement (IDR) portal";
   - a refresh date different from the US: "After April 1, 2025, we will periodically refresh our cost estimates";
   - the cap: "The maximum reimbursement amount for a single unit of any FBA eligible item is 675,000 JPY";
   - the dispute window: "you can file a claim using the Contact Us page in Seller Central within 60 days after we issued the reimbursement", beside "You can dispute a reimbursement claim using the Get support page in Seller Central";
   - the 30-day repeat rule: "a reimbursement amount dispute decision was already provided for the item within the last 30 days".
   VR16's "No Amazon or Japanese-language source evidences it for JP" is contradicted by this English JP page; whether the live JP page still says so, and whether Japanese-language layers match, is unread. The store is read from the JPY amount, "consumption tax" and the G/09 path [inferred].
2. **fc-lost-damaged (post-to-store table).** No removal-related post read here names its store in its text (862f270b, d8f9a56c), so none tests the `marketplaceId` reading; the table's tag stays that file's.
3. **fee-overcharges.** Storage charged on units stranded by Amazon's error, or held under a dangerous-goods review Amazon later lifts, is that file's (critic's gap list); § L and § M here hold only the removal and disposal side.

---

## Seat's own

None among the positions. The order of sections and the choice of what counts as an "edge" in the summary (dangerous goods, stranded, liquidation) are this seat's arrangement and enter no skill.

---

## Open questions for a first run on a real account

1. Which removal windows does the "Resolve a removal order issue" tool enforce for this seller's store: 15–75 / 60, 15–135 / 120 / 120, or 18 months? And from which event does it count the lower bound (creation, ship date, last movement)?
2. Is there a US News post, unread here, that issued the 2025-10-15 windows for the US?
3. Where does the claim form's "Shipment ID" come from, and does any report the seller can read (Seller Central or SP-API) carry it?
4. What values do `order-type`, `order-status`, `order-source` and `disposition` take in this seller's Removal Order Detail? Do Donation, Liquidation and Grade and Resell orders appear, and under which values?
5. Does the ledger detail post removals and disposals under `VendorReturns`, with `Reference ID` = the removal `order-id`?
6. What `carrier` strings and tracking formats does Removal Shipment Detail carry (UPS, USPS, Amazon Logistics, LTL)? Does an LTL removal have one tracking number for many cartons?
7. In a NA or EU unified account, does a removal report request scoped to one marketplace return only that store's orders, or all of them?
8. What `reason` values do removal reimbursements carry in the Reimbursements report, and does `case-id` fill for them?
9. For orders created before 2026-03-01 with `cancelled-quantity` > 0, does `removal-fee` match the units actually shipped or disposed?
10. Do liquidation adjustments (`RemovalShipmentAdjustmentEvent`) appear for this seller, and how are they labelled in `listTransactions`?
11. Can the seller's application hold the Selling Partner Support (Restricted) role, so that a filed removal case can be read back?
12. What grading-dispute window does the US "Resolve a removal order issue" tool show today? No permitted route read the live page (§ B).
13. What windows do the removals-claims pages give in DE, FR, IT, ES, JP, MX and IN? No News post with those marketplace fields was found, and the pages are not readable by a permitted route.
14. When Amazon disposes of units after a dangerous-goods classification, does a removal order (and `order-id`) appear in Removal Order Detail, or only ledger rows? Which ledger reason does it carry?
15. Has any seller been reimbursed for units disposed of after a dangerous-goods classification that was later reversed? (No source read; Chinese and gs.amazon.cn sources not searched in this pass.)
16. For a US liquidation order, does the sum of `RemovalShipmentEvent` `WHOLESALE_LIQUIDATION` quantities match Removal Order Detail `shipped-quantity` for the same order id, and are units that never reached the liquidator ever reimbursed, and under which `reason`?
17. Which Business Solutions Agreement clause governs a dangerous-goods disposal in the US, UK and EU stores (the 2026-08-06 seller relays "Section F.7.3" of the European agreement; only the Australian text was read)?

---

## Pages read

| Title | Address | Publisher | Page date | Read on | Used for |
|---|---|---|---|---|---|
| Update on Reimbursement Automation and Eligibility Window to file reimbursement claims (US) | https://sellercentral.amazon.com/seller-forums/discussions/t/81c3235d-4c44-47ba-96c5-883cecab3244 | Amazon (News_Amazon) | 2024-07-24 | 2026-11-13 | § A, § B, RM2, RM5, RM6 |
| Same title (CA field, British spelling) | https://sellercentral.amazon.com/seller-forums/discussions/t/6605eede-df8e-4498-803f-cb612d95d7ce | Amazon | 2024-07-24 | 2026-11-13 | § B, RM5, corrections |
| Same title (UK field) | https://sellercentral.amazon.com/seller-forums/discussions/t/d0fc997e-de50-4100-9803-76b7993b66df | Amazon | 2024-10-10 | 2026-11-13 | § B, RM5 |
| Update on eligibility window to file reimbursement claims (SE field) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/1101821c-7ff1-495a-b8a5-71ff01e3afc3 | Amazon | 2025-01-15 | 2026-11-13 | § B, RM5 |
| Update on reimbursement claim window eligibility on FBA (UAE field) | https://sellercentral.amazon.com/seller-forums/discussions/t/96a05f4a-537a-49d2-a918-703c47716bc0 | Amazon | 2024-08-06 | 2026-11-13 | § A, § B, RM3, RM8 |
| Update to FBA inventory reimbursement claim windows (AU field; also on .co.uk, -europe, .ca hosts) | https://sellercentral.amazon.com/seller-forums/discussions/t/d8f9a56c-882f-437c-ad34-cccd11cfa465 | Amazon | 2025-08-14 | 2026-11-13 | § B, § C, RM7, RM12 |
| FBA Lost Your Inventory? Steps to File a Reimbursement Claim | https://sellercentral.amazon.com/seller-forums/discussions/t/0e07abc1-9026-4540-a005-153d9e78bf04 | Amazon (Indy_Amazon) | 2026-08-13 | 2026-11-13 | § A, § B, § D, RM4, RM10 |
| [April FBA Series] Reimbursement Deep Dive | https://sellercentral.amazon.com/seller-forums/discussions/t/969ce6b1-2baf-445a-830a-9ebcbdecf14e | Amazon (KJ_Amazon) | 2026-04-09 | 2026-11-13 | § A (help page name) |
| FBA removal and disposal fees to be charged as units are processed | https://sellercentral.amazon.com/seller-forums/discussions/t/2f4edad8-31d4-443b-8b22-12776c4f685a | Amazon | 2026-01-29 (revised) | 2026-11-13 | § H, RM26 |
| Ongoing Charges and Unfulfilled Removal Orders (Jameson_Amazon reply) | https://sellercentral.amazon.com/seller-forums/discussions/t/3ead5335-1d9c-46f2-a41c-197b892e2ba3 | Amazon staff / seller | 2024-11-12 | 2026-11-13 | § H, RM25 |
| Removal Order Reimbursement (Bryce_Amazon reply) | https://sellercentral.amazon.com/seller-forums/discussions/t/b3bb247e-1d58-45c7-bd84-a9196edd6fbf | Amazon staff / seller | 2024-09-28 | 2026-11-13 | § A |
| Amazon removal order: wrong item returned to me | https://sellercentral.amazon.com/seller-forums/discussions/t/aa7d890f-a9ac-457b-a160-4dc8e2346342 | seller; Jameson_Amazon | 2024-08-21 | 2026-11-13 | § D |
| FBA removal and disposal fees to be charged as units are processed (UK field) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/862f270b-81cd-4d78-8a02-7b95156040e6 | Amazon | 2026-04-09 | 2026-11-13 | § H, RM26 |
| Inventory Defect and Reimbursement portal now available (US field, EU host) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/b175b700-09c4-4350-8a22-24f60a724042 | Amazon | 2025-01-21 | 2026-11-13 | § A, RM2 |
| Selling Partner Support API; Retrieve the Contact History for a Support Case | https://developer-docs.amazon.com/sp-api/docs/support-api | Amazon (SP-API docs) | updatedAt 2026-09-30 | 2026-11-13 | § K, RM35 |
| Removal Order Reimbursement – Moving Goalposts… | https://sellercentral.amazon.com/seller-forums/discussions/t/da0a8dbe-487f-47f2-9207-5ad59d77d531 | seller; Angie_Amazon, Manny_Amazon | 2026-06-25 | 2026-11-13 | § D, RM16 |
| Units Missing in Removal Order by UPS | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/d804ff56-c3ad-4c0f-a8d0-5b75c7137448 | seller | 2025-06-13 | 2026-11-13 | § G, RM24 |
| Units Missing in Removal Order (DE host) | https://sellercentral.amazon.de/seller-forums/discussions/t/dd5bdcce-13d7-437d-8ea9-e56d4272d1a4 | seller | 2025-05-24 | 2026-11-13 | § G, RM33 |
| Legal Actions? Stuck in 6+ Month Removal Order Limbo | https://sellercentral.amazon.com/seller-forums/discussions/t/f14d6bee-4bb6-42be-9040-5201938181ed | seller; Dominic_Amazon | 2024-08-22 | 2026-11-13 | § G |
| Thousands in Overage Fees after Canceling Removal Orders | https://sellercentral.amazon.com/seller-forums/discussions/t/e7588253-14dd-449e-9f37-1a1ebac70210 | seller; Dominic_Amazon | 2024-06-05 | 2026-11-13 | § H |
| Disposal orders continuously canceled by Amazon | https://sellercentral.amazon.com/seller-forums/discussions/t/4e166a45-3cfb-443c-a183-a7dbc4b36450 | seller | 2026-02-02 | 2026-11-13 | § H |
| MOD HELP REQUESTED! FBA Removal / Disposal Order being Canceled Repeatedly | https://sellercentral.amazon.com/seller-forums/discussions/t/367e6a81-a968-498f-aafe-8a58f56ff964 | seller; Bryce_Amazon | 2025-08-18 | 2026-11-13 | § H |
| Removal order I did not create, units appearing from nowhere | https://sellercentral.amazon.com/seller-forums/discussions/t/71219d12-c888-4de7-8d6a-693de43e40cf | seller | 2024-06-12 | 2026-11-13 | § I |
| FBA Destroys Inventory Immediately After Marking It Unsellable | https://sellercentral.amazon.com/seller-forums/discussions/t/8299f3f0-45c5-43a7-add2-e189180eb29f | seller; Glenn_Amazon | 2025-09-09 | 2026-11-13 | § C, RM13 |
| Unable to get more than 20% reimbursement for damaged removal order | https://sellercentral.amazon.com/seller-forums/discussions/t/45e6c264964867c1d0629bca469a97cb | seller (quoting Seller Support) | 2019-07-30 | 2026-11-13 | § E |
| Suspended for reimbursement requests - removal order boxes lost | https://sellercentral.amazon.com/seller-forums/discussions/t/e93106ad3be04c70cbec6272e8729687 | seller | 2019-01-09 | 2026-11-13 | RM34 |
| Account Deactivated due to Removal Damaged Units Issues | https://sellercentral.amazon.com/seller-forums/discussions/t/6b02058a-c5e7-495c-8808-504f9e5de72d | seller; CR_Amazon | 2024-11-08 | 2026-11-13 | background (no fact used) |
| EU Policy Redline (customer return claims; FC operations claim; Removals claims) | https://m.media-amazon.com/images/G/02/rainier/help/EU_Policy_Redline.pdf | Amazon | PDF created 2024-08-20 | 2026-11-13 | § A, § B, § C, § D, RM1, RM3, RM11, RM12, RM14 |
| FBA inventory reimbursement policy (US redline) | https://m.media-amazon.com/images/G/01/rainier/help./PC__Kiwi_Comms_redlined_policy_US_clean.pdf | Amazon | PDF created 2024-12-18 | 2026-11-13 | § A, § E, RM18, RM34 |
| FBA inventory reimbursement policy (US redline, later) | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_US.pdf | Amazon | PDF created 2025-02-24 | 2026-11-13 | § E, RM18 |
| FBA lost and damaged inventory reimbursement policy (UK redline) | https://m.media-amazon.com/images/G/01/rainier/help./_PC__Kiwi_Comms_redlined_policy_UK_clean_version.pdf | Amazon | PDF created 2024-12-11 | 2026-11-13 | § E, RM18 |
| FBA lost and damaged inventory reimbursement policy (JP, English) | https://m.media-amazon.com/images/G/09/rainier/help/redline_FBA_reimbursement_policy__EN_version.pdf | Amazon | "as of 02/19" (2025); PDF 2025-02-19 | 2026-11-13 | § E, RM18, RM19 |
| 亚马逊物流库存赔偿政策 (CA, Chinese redline) | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_CA-zh_cn.pdf | Amazon | PDF created 2025-02-24 | 2026-11-13 | § E, RM18 |
| 亚马逊物流库存赔偿政策 (US, Chinese) | https://m.media-amazon.com/images/G/01/rainier/help./PC__Kiwi_Comms_redlined_policy_US_clean-zh_cn.pdf | Amazon | PDF created 2024-12-20 | 2026-11-13 | § E (agrees with English) |
| FBA lost and damaged inventory reimbursement policy (EU, April 2021 redline) | https://m.media-amazon.com/images/G/02/rainier/help/legal/FBA_inventory_reimbursement_policy_April_2021_English_Redlined.pdf | Amazon | PDF created 2021-04-12 | 2026-11-13 | § E, RM19 |
| Fulfillment by Amazon (FBA) Reports | https://developer-docs.amazon.com/sp-api/docs/report-type-values-fba.md | Amazon (SP-API docs) | updatedAt 2026-10-13 | 2026-11-13 | § F, RM15, RM20, RM32 |
| selling-partner-api-models: financesV0.json, finances_2024-06-19.json, support_2025-02-01.json | https://github.com/amzn/selling-partner-api-models (commit db2936aa, 2026-10-29; local clone) | Amazon | 2026-10-29 | 2026-11-13 | § F, § J, § K, RM29, RM30, RM35 |
| FBA inventory reimbursement policy (US hub) | https://sellercentral.amazon.com/help/hub/reference/external/G200213130 | Amazon | — | 2026-11-13: **unread** (JavaScript shell, HTTP 200, no text; the .co.uk twin the same) | text read through the PDFs and the Hopted copy |
| Resolve a removal order issue (tool) | https://sellercentral.amazon.com/help/hub/reference/external/G9ZB3H4DP4H72U6R | Amazon | — | 2026-11-13: **unread** (JavaScript shell; no permitted route reads it, and the route closed on 2026-11-10 is not used) | named in § A from the Hopted copy and staff post |
| Required removals | https://sellercentral.amazon.com/gp/help/external/202000820 | Amazon | — | 2026-11-13: **unread** (JavaScript shell) | content held by the stock pack (D8, staff post) |
| Amazon FBA Inventory Reimbursement Policy (copy of the US help pages) | https://www.hopted.com/integrations/amazon-sp-api/amazon-help-articles/fba-inventory-reimbursement-policy | Hopted (third-party copy of Amazon text) | undated; Wayback 2026-07-13 | 2026-11-13 | § A, § B, § D, RM1, RM6, RM12 |
| Amazon FBA reimbursements UK: claim windows and routine | https://mrprime.com/insights/fba-reimbursements/ | Mr Prime (Robert Prime) | 2026-10-01 | 2026-11-13 | § A, § B, § C, § D |
| Amazon Removal Order Reimbursements Explained | https://www.refunzo.com/insights/amazon-removal-order-reimbursements-explained | Refunzo (Jimi Patel) | 2025-06-23 | 2026-11-13 | § A |
| Weekly Removal Order Reconciliation SOP (UK) | https://reclaimhq.uk/weekly-removal-order-reconciliation-sop | ReclaimHQ Ltd | undated (© 2026) | 2026-11-13 | § B, RM9 |
| Amazon Removal Orders in 2026: Delays, Claims, Where to Send | https://www.prepvia.com/blogs/amazon-removal-orders-2026-guide | PrepVia (Bernardo Campelo) | 2026-08-25 (mod. 2026-11-01) | 2026-11-13 | § B, § C, § F, § G, § H |
| Amazon Reimbursement Services: What Can You Really Recover? | https://www.sellersprite.com/en/blog/amazon-reimbursement-services | SellerSprite Content Team | 2026-10-23 | 2026-11-13 | § B |
| Amazon FBA Reimbursement Audit 2026 | https://www.sellerlabs.com/blog/fba-reimbursement-audit-amazon-owes-you-2026/ | Seller Labs (Nhan Dinh) | 2026-03-18 | 2026-11-13 | § E, § I, RM28 |
| GORILLA_REMOVALSDETAILS() | https://help.gorillaroi.com/en/articles/10670129-gorilla_removalsdetails-get-details-from-removal-orders | GorillaROI | 2025-02-27 | 2026-11-13 | § F, RM21 |
| Removal Report | https://www.sellerspace.com/en/help/doc/removal-reports-use-guide/ | SellerSpace | 2025-08-01 | 2026-11-13 | § F, RM21, RM22 |
| Removals & Disposals Report | https://inventorylab.threecolts.support/en/articles/10415885-removals-disposals-report | InventoryLab (Threecolts) | 2025-06-05 | 2026-11-13 | § F |
| Amazon FBA Removals: Fees, Challenges… | https://sellercloud.com/blog/amazon-fba-removals/ | Sellercloud | 2026-01-19 | 2026-11-13 | § G (split delivery) |
| REMOVAL_ORDER_DAMAGED | https://synder.com/fees-amazon/removal-order-damaged/ | Synder | undated | 2026-11-13 | RM31 |
| How to Make Sense of the FBA Reimbursement Report | https://getida.com/resources/blog/fba-reimbursements/fba-reimbursement-report/ | GETIDA | undated (images 2024-07) | 2026-11-13 | § F (no removal reason named) |
| How to request reimbursement for damaged Amazon FBA removal orders | https://www.fulltimefba.com/how-to-request-reimbursement-for-damaged-amazon-fba-removal-orders | Full-Time FBA (Stephen Smotherman) | 2019-09-09 | 2026-11-13 | background (no fact used) |
| 领星ERP移除库存退回海外仓业务流程 | https://www.lingxing.com/help/article/removeInbound | 领星 Lingxing | undated | 2026-11-13 | § F, RM22 |
| 亚马逊移除订单在哪里看 | https://www.lingxing.com/help/article/removeOrder | 领星 Lingxing | undated | 2026-11-13 | § F, § J |
| 亚马逊移仓换标少件真相 | https://www.huanzhimei.net/news/1550.html | 环至美（广州）供应链 | 2025-06-04 | 2026-11-13 | § A, § D, § G, RM17 |
| 疑问详解亚马逊FBA货物赔偿与索赔 | https://m.by56.com/news/46973.html | 百运网 | 2025-04-05 | 2026-11-13 | § B, RM36 |
| 开箱视频成维权核心证据 | https://www.sohu.com/a/909477311_122014422 | 搜狐号 | 2025 | 2026-11-13 (search summary) | § D, RM17 |
| Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS) | https://supplychain.amazon.com/support/reimbursements | Amazon (ASCS programme, not FBA) | undated (© 2026) | 2026-11-13 | § A, § B (scope and window wording corroborated) |
| LITHIUM ION BATTERIES - Hazmat Classification | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/ebd40f57-88d7-442b-9d69-3eed7d4db42d | seller (quoting Seller Support); Dominic_Amazon | 2024-08-02 (US field) | 2026-11-13 | § L, RM38, RM40, RM41, RM42 |
| Request to Expedite Hazmat Review – Product Does Not Contain Batteries | https://sellercentral.amazon.com/seller-forums/discussions/t/5c1c2d65-0518-4fc8-b154-38265aa7c34f | seller; Michelle_Amazon (reply 2025-06-06) | 2025-06-05 (US field) | 2026-11-13 | § L, RM41, values |
| 267 FBA DG units disposed without removal option after DG Programme approval | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/978f97fe-b2ac-49b4-b079-699d25067a52 | seller; Glenn_Amazon (reply 2026-08-10, from the page's `createdAt`) | 2026-08-06 (UK field) | 2026-11-13 | § L, RM40 |
| Need help: compliance cleared, but FBA keeps disposing my inventory | https://sellercentral.amazon.com/seller-forums/discussions/t/29f8a8cd-c13e-4e2f-93e7-c4edae6d2894 | seller | 2025-09-11 (US field) | 2026-11-13 | § L, RM40 |
| Looking for Insight — Ongoing Issues With FBA (Hazmat Flags, Defective Units, FC Transfers, and Blocked Removals) | https://sellercentral.amazon.com/seller-forums/discussions/t/cb7207be-faee-42ca-853a-26688ead4a5f | seller | 2025-12-04 (US field) | 2026-11-13 | § L, RM42 |
| Amazon has destroyed my product without my Permission | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/0128a8b35592ae90532903823996a1cc | seller | 2021-10-08 | 2026-11-13 | § L |
| FBA Liquidations: Everything you need to know | https://sellercentral.amazon.com/seller-forums/discussions/t/6fee30d4-e56b-4f50-b78c-69c8237a6c79 | Amazon (Topher_Amazon) | 2025-06-23 | 2026-11-13 (re-read; held by the stock pack, E-L1, E-L2, E-L4) | § J, RM44 |
| What Amazon FBA sellers should know about dangerous goods | https://sell.amazon.com/blog/amazon-hazmat-dangerous-goods | Amazon (Mickey Toogood) | 2025-01-04 | 2026-11-13 | § L, RM41 (upload tool only; no disposal or reimbursement text) |
| Amazon Services Business Solutions Agreement (Amazon.com.au) | https://m.media-amazon.com/images/G/31/rainer/AmazonServicesBusinessSolutionsAgreement_2024edits1.pdf | Amazon | PDF created 2024-06-12 | 2026-11-13 | § L, RM39 |
| FBA Inbound Eligibility model (`fbaInbound.json`) | https://github.com/amzn/selling-partner-api-models (commit db2936aa; local clone) | Amazon | 2026-10-29 | 2026-11-13 | § L, RM38, values |
| FBA prohibited products (G201730840); Dangerous goods identification guide (201003400); Dangerous goods review process (G201749580) | https://sellercentral.amazon.com/gp/help/external/G201730840 and siblings | Amazon | — | 2026-11-13: **unread** (help pages; facts carried from search summaries only, tagged) | § L |
| FBA lost and damaged inventory reimbursement policy (JP, English; re-read) | see the JP row above | Amazon | PDF 2025-02-19 | 2026-11-13 (re-read for § E and *Notes for other files*) | § E, RM18, RM46 |
| 2023年亚马逊移除订单相关知识点 | https://zhuanlan.zhihu.com/p/602279060 | 知乎 | 2023 | 2026-11-13: **unread** (HTTP 403) | — |
| Amazon Removal Orders: The Overlooked Reimbursement Opportunity | https://www.spscommerce.com/community/articles/amazon-removal-order-reimbursement | SPS Commerce (SoStocked) | — | 2026-11-13: **unread** (HTTP 404) | — |

---

## Verification (2026-11-13)

An adversarial check of this file against its cited sources, public pages only, no SP-API call and no login.

**Checked and confirmed** (source re-opened on 2026-11-13):

- The post-object `marketplaceId` of every News post: 81c3235d ATVPDKIKX0DER, 6605eede A2EUQ1WTGCTBG2, d0fc997e A1F83G8C2ARO7P, 1101821c A2NODRKZP88ZB9, 96a05f4a A2VIGQ35RCS4UG, d8f9a56c A39IBJ37TRP1C6, 0e07abc1 and 2f4edad8 ATVPDKIKX0DER; each `datePublished` as listed. The page's first `marketplaceId` hits are the host's store list, not the post's; only the field after `contentMetadata` is the post's.
- Quoted window text in 81c3235d (with "starting October 23" and US customer returns "60-120 days"), 6605eede (45-day lower bound), d0fc997e ("Starting January 9, 2025"), 1101821c, 96a05f4a ("Starting September 5, 2024"), d8f9a56c ("Effective October 15, 2025") and 0e07abc1 (18 months; the "Resolve a removal order issue" route; "Photos of damaged items received in removal orders").
- "all removal claims will still need to be filed manually" in 81c3235d, 6605eede and d0fc997e; the IDR exclusion sentence in b175b700.
- The EU redline (PDF created 2024-08-20): scope text, grading-dispute text, the evidence list with "Images of shipping label", "18 months" struck, red-added 75-day and 60-day text, "no sooner than 14 days from the last confirmed movement" unmarked, grading "30" struck and "60" added (strike rectangle through the glyphs, PyMuPDF), and the customer-returns page's unmarked 30 days.
- The Hopted copy: old 14-day / 18-month / 30-day text, the evidence list without the label image, the tool link G9ZB3H4DP4H72U6R.
- The US (2024-12-18, 2025-02-24), UK (2024-12-11), JP (2025-02-19) and CA-Chinese (2025-02-24) redlines: PDF creation dates, the eligibility list, the pre-fulfilment valuation sentence, the "reduced estimated cost" sentence, caps, dispute windows and the struck "estimated proceeds" sentence for removal claims (PyMuPDF strike detection).
- The FBA Reports page (updatedAt 2026-10-13): both removal reports' roles, "can only be requested", descriptions and column lists; the ledger's `VendorReturns` event type and `Vendor Returns` / `Disposed` summary columns.
- financesV0.json and finances_2024-06-19.json at db2936aa: every event, field and description quoted in § F and § J; `REMOVAL_SHIPMENT_ITEM_ID`. The Finances API page's role table for `listFinancialEvents` and `listTransactions`; the deprecation page's 2027-08-27 removal date for Finances v0.
- support_2025-02-01.json: `listCases`, `getCase`, `listContacts` only; the Support API page names the role "Selling Partner Support (Restricted)"; the contact-history page gives EMAIL / PHONE / CHAT and a `downloadUrl` that "expires after 15 minutes".
- No operation in the models that opens, evidences or disputes a removal claim or cancels a removal order; GitHub main has one commit after db2936aa (b13d1d10, 2026-11-11, a Data Kiosk schema only).
- Forum threads: Jameson_Amazon 3ead5335, Bryce_Amazon b3bb247e, aa7d890f, 8299f3f0, f14d6bee, e7588253, 71219d12, 4e166a45, 367e6a81, 969ce6b1: dates and quotes as stated.
- Practitioners: Mr Prime (74 in the page text, 75 in its table and the announcement), Seller Labs, SellerSprite (applies 15–135 / 120 to US sellers), PrepVia.

**Changed:**

- da0a8dbe was posted 2026-06-25, not 2025-06-25 (§ D, RM16).
- ReclaimHQ's words are "will result in an automatic rejection with a “too early” response", not "triggers an automatic 'too early' rejection" (§ B).
- The US 2024-12-18 and UK 2024-12-11 redlines say "manufacturing cost", not "sourcing cost"; noted in § E and RM18.
- The UK 2024-12-11 redline gives £2,000 and a 90-day valuation dispute; added to § E and *Values that move*.
- The UK per-unit fee date now cites its own News post (862f270b, 2026-04-09, UK field) instead of only the stock pack.
- The IDR post b175b700 now carries its date (2025-01-21) and its field (US, read on the EU host).
- RM10 and § B: the 18-month staff window matches the old page in length only; the anchors differ (removal vs delivery or loss).
- The Support API "launched 2026-09-30" is downgraded to inferred (doc updatedAt and model commit date); Shipping v2 `createClaim` is named and set aside as not a removal claim.
- Moving values taken out of the positions' substance: RM6, RM7, RM8, RM12, RM23 and RM26 now state the rule and where the value is read, with the values as dated evidence by store.
- Forbidden phrasing rewritten: RM10's "a skill states each with its date and picks none" (a behaviour for the skill) is now a fact; § H's "a fee to explain" and "a candidate for a lost-in-warehouse claim" are now statements of which policy page covers what.
- The summary's "the window has changed at least four times" now says the changes were per store.
- *Values that move*: the JP processing figure and the liquidation-recovery figure now name their stock-pack source; they were not re-read here.

**Remaining doubts:**

- The Seller Central policy pages and the "Resolve a removal order issue" tool are JavaScript shells; which window the tool enforces for a store is unread.
- That a post's `marketplaceId` field is the store it governs is still a reading; Amazon does not document the field.
- The d8f9a56c rendering on the .co.uk, -europe and .ca hosts, the Sweden reading of 1101821c beyond its field, Lingxing, SellerSpace, GorillaROI, InventoryLab, Refunzo, 环至美物流, 百运网 and 搜狐 were not re-opened.
- The "about two weeks" carrier allowance and the processing times rest on a staff post read through the stock pack.
- 81c3235d's "October 23" carries no year in the sentence read; 2024 is read from the post date.

---

## Revision (2026-11-13)

After the completeness critic's first round. Public pages by plain GET only; no POST to an Amazon host, no help-hub content call, no SP-API host, no sign-in.

**Changed:**

- **US grading window (critic A5).** § B now states what permitted sources say, each with its date: the older page text (30 days, Hopted copy), the US post effective 2024-10-23 ("all other removal claims", 60 days from delivery back; grading under it inferred), the EU redline, Amazon Supply Chain's page, the Australia post and Mr Prime. A newer live-page reading recorded elsewhere in the pack came through a route closed on 2026-11-10; it is not used, and no permitted route confirmed it. RM12 and the grading row of *Values that move* are rewritten to match; the stale single-value US row is gone.
- **One fact, one home (critic A1, D).** The post-to-store mapping now points to fc-lost-damaged (RM5, § B); the IDR exclusion and the filing route point to filing-and-conduct FL5 and FL4 (RM2, RM4, § A); conduct points to FL11 (RM34); the Support API and "no operation files a claim" point to sp-api-claims-surface SU8, SU10, SU12, SU13 (RM35, § K); the cap and the valuation-dispute window point to value-and-reversals VR29 and VR20 (§ E, *Values that move*).
- **RM19 withdrawn** (cap and dispute window homed in value-and-reversals).
- **Moving values out of positions (critic F).** RM7 and RM8 now state the rule (what a store post can change; which anchor each store uses) and leave the values to *Values that move*.
- **Weak sources (critic G).** RM1 now says the live page was not read by a permitted route and adds Amazon Supply Chain's identical wording, marked as another programme's page.
- **Japan (critic A7).** The JP redline was re-read: sourcing cost for removal claims, the MYSC page on the IDR portal, a refresh "After April 1, 2025", JPY 675,000 cap, 60-day dispute window, 30-day repeat rule. RM18 carries the removal-claim valuation; the cap, dispute window and MYSC facts are handed to value-and-reversals under the new *Notes for other files of this pack* (VR16 and its open question 3 are contradicted).
- **Corrections to other packs.** Entry 6 now notes that sp-api-claims-surface holds the Support API; entries 7 (stock S22 roles and the liquidation event's missing quantity) and 8 (stock G18, addition) are new.

**Added:**

- § L, dangerous goods: the `FBA_INB_0015` reason code, the Australian agreement's F-7.2 and F-7.3, Seller Support's relayed "disposal without reimbursement" text, staff on the 14-business-day document window and on an immediate disposal after DG-programme approval, sellers' reports; whether a wrong classification is claimable (no Amazon text read says so). Positions RM38 to RM42.
- § M, removal of stranded units, pointing to the stock pack for stranding. Position RM43.
- § J, liquidation shortfalls: the scope sentence against units sent to a liquidator, the per-unit join (`FBALiquidationEvent` has no quantity or SKU), proceeds below the typical rate, pointing to the finance pack (P-ful-11) and the stock pack (S19, S20, S22) for money and rules. Positions RM44, RM45.
- RM46, Japan's sourcing-cost text as it bears on value-and-reversals.
- *Values that move*: dangerous-goods contact window, document window, review time, the agreement's notice period.
- *Seat's own* (none among the positions); open questions 12 to 17; thirteen new rows in *Pages read*.

**Not done, and why:**

- The Seller Central help pages (removals claims, dangerous goods, FBA Liquidations) stay unread: they serve a script shell, and a plain GET of the removals-claims page was refused by this session's permission system on 2026-11-13. Their facts are carried by the route they came through and tagged.
- The shared web-search budget ran out partway through; Chinese and gs.amazon.cn sources on dangerous-goods disposal and on liquidation shortfalls, and the DE, FR, IT, ES, JP, MX and IN removal windows (critic C, H), were not searched. These are recorded as open questions 13, 15 and 17.
- Only the Australian Business Solutions Agreement was read; the clause a US, UK or EU dangerous-goods disposal rests on is open (question 17).
