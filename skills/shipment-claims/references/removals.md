# Removal claims: scope, windows, grading, evidence, value, shipments

## Scope and route

- A removal claim covers eligible units lost or damaged by Amazon, or by a carrier Amazon used, after they left an Amazon facility on the way to the seller's return address; it does not cover units returned because the seller broke a policy (EU redline 2024-08-20; Hopted copy of the US page) (RM1).
- Every removal claim is filed by hand: each Amazon automation post of 2024 says so, and nothing read to 2026-11-13 announces removal automation; the IDR portal (announced 2025-01-21 for the US store) excludes removals and warehouse disposals (RM2, FL5).
- Amazon's removal claim kinds are lost in transit; damaged in transit; damaged, different or incomplete units received; and grading disputes on customer returns (RM3).
- The Seller Central route is the "Resolve a removal order issue" tool (G9ZB3H4DP4H72U6R), keyed by removal order ID (Indy_Amazon, US, 2026-08-13) (RM4).
- A removal claim needs the ASIN to comply with FBA restrictions at claim time; a seller reports an accepted removal claim later refused because the ASIN was deactivated as prohibited (2025-05-24) (RM33).
- A seller reported a suspension after several removal-loss requests (2019); Amazon's conduct rule on premature or high-volume requests is in ../claim-filing/SKILL.md (RM34, FL11).

## Windows, store by store

- A lost-in-transit removal claim has both an earliest and a latest filing day, and the other kinds a latest day counted from delivery back; the lengths are per store and per date (RM6).
- US: the post of 2024-07-24 (81c3235d), in force from 2024-10-23, counts lost in transit from shipment creation and "all other removal claims" from delivery back; before it, the US help page counted the earliest day from the last confirmed movement and every claim from the removal date (Hopted copy; the same text struck in the EU redline of 2024-08-20) (RM6).
- US, again: Amazon's staff post of 2026-08-13 gives removals a length counted "of the shipment being delivered or lost" that matches the pre-2024 page, not any News post; Amazon's own texts disagree, and none read says which governs (RM10).
- Australia: the post of 2025-08-14, in force from 2025-10-15, changed every removal window, moved the grading anchor from delivery to the date of removal and added a re-evaluation window; no post with a US marketplace field carrying these was found (RM7).
- UAE: the post of 2024-08-06, in force from 2024-09-05, counts lost removals from the ship date where the US, Canada, UK and Sweden posts count from creation, and gives damaged, different or incomplete units a window of their own from delivery (RM8).
- Amazon's texts give three anchors for the earliest day of a lost-removal claim (creation, ship date, last confirmed carrier movement); that a claim filed before it is refused as too early is a practitioner's report (ReclaimHQ) (RM9).
- A News post's windows are read as the store its post object names; no removal-related post read names its store in its own text (RM5).
- Where today's value is read for the seller's store: *FBA inventory reimbursement policy: Removals claims* and the "Resolve a removal order issue" tool, which cx cannot read and the seller sees signed in, and the store's latest Seller Forums News post on claim windows, read by plain GET; which window and anchor the tool enforces is read in Amazon's documents, not yet seen on a live account (RM6, RM9).
- Practitioner pages of 2026 state two different window sets, neither citing a store: PrepVia, Mr Prime and ReclaimHQ against SellerSprite, Olifant and Marketplace Officer (RM37).
- Some Chinese guides render the help page's "no sooner than" earliest day as a latest day (百运网, 2025-04-05) (RM36).

## Grading disputes

- A grading dispute concerns customer returns Amazon graded customer-damaged or defective; it needs the unit physically returned through a removal order and adds an explanation of the disagreement to the claim (EU redline 2024-08-20) (RM11).
- Its length and anchor (delivery of the removal back, or the date of removal from the network) are per store and per date; for the US the older page text counts from delivery and the post in force from 2024-10-23 takes grading in under "all other removal claims" only by inference, and the live US page is unread by a permitted route (RM12).
- Because a grading dispute needs the unit returned, a disposed unit cannot be its subject, and an automated or required disposal can remove that path before the seller acts; this is the research's inference from Amazon's text (RM13).
- Grading on customer returns themselves: ../return-claims/SKILL.md.

## Evidence

- Amazon's list for a removal claim: removal order ID; shipment ID with active tracking or proof of delivery; ASINs or FNSKUs and quantities; LPN; images of the units, their packaging, the shipping box and the shipping label; and, for grading, an explanation (EU redline 2024-08-20; the US copy lacks the label image) (RM14).
- Removal Shipment Detail has no shipment-id column and no delivery date, so the shipment ID the claim asks for is in no SP-API report read; read in Amazon's documents, not yet seen on a live account (RM15).
- Mr Prime (2026-10-01) notes that photos of the box, label and units can be taken only when the parcel is opened, and a seller thread (2026-06-25) reports Seller Support asking for per-unit unboxed photos with LPN stickers; both are practitioners' reports (RM16).
- Chinese practitioners treat a continuous unboxing video as the core evidence; no Amazon text read names video (RM17).

## Value

- Removal claims before a customer order are valued at sourcing cost, and units unsellable when removed at "a reduced estimated cost"; the redlines strike the earlier "estimated proceeds" sentence for removal claims in the US, UK, Japan and Canada (Chinese) texts; the US 2024-12-18 and UK 2024-12-11 texts name "manufacturing cost", the US 2025-02-24 and JP texts "sourcing cost" (RM18).
- The JP English redline (2025-02-19) names sourcing cost for removal claims, *Manage Your Sourcing cost* on the IDR portal and a periodic refresh of estimates after 2025-04-01; the store is read from its currency, "consumption tax" and its path (RM46).
- The valuation rule, the cap and the dispute: ../claim-value/SKILL.md.

## Lost, short, wrong and damaged removal shipments

- A removal order can ship as many parcels from several fulfilment centres over weeks (US staff; PrepVia, 2026-08-25); Amazon gives no fixed processing time, and one order's actual span is read from its own `request-date`, `shipment-date` and `last-updated-date` in Removal Order Detail (RM23).
- A removal order can show "Completed" and charged while some of its tracking numbers never moved (a seller thread, 2025-06-13) (RM24).
- Removal Shipment Detail omits cancelled and disposed units, which Removal Order Detail carries per order, SKU and disposition (RM20).
