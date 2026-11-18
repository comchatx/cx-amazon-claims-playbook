# Windows and stores: where each kind's window is stated

## The windows by kind

- The table of windows by kind and store as read, and warehouse losses: ../warehouse-claims/SKILL.md.
- Read together, Amazon's windows and the services' look-backs mean, by inference, that what an audit can still claim is bounded by each kind's window in the seller's store, not by a service's look-back, so whether a look-back exceeds the window depends on the kind and on which statement governs the store (EC4).
- Warehouse lost or damaged: set per store and changed by announcement, stated on *FBA inventory reimbursement policy* (G200213130), which the seller sees signed in, and in the store's latest News post on claim windows, read by plain GET; no operation returns it (FC9).
- Customer returns: counted from the refund or replacement date, stated on *Customer return claims* (G9N934L7Y4SFWPJ4), which the seller sees signed in, and in the store's latest News post (RT4).
- Amazon's 2024 posts under one title give customer-return windows whose bounds differ between the US post and the Canada and UK posts, and a 2026-08-13 US staff post states a different one again; each is that store's statement on its date, and which the claim tool enforces is read in Amazon's documents, not yet seen on a live account (EC5).
- Missing from inbound: a per-store length counted from verified delivery, filed after the shipment is closed, stated on *FBA inventory reimbursement policy: Shipment to Amazon claims* (GEYPWTSQRTXXXMVB), which the seller sees signed in, and in the store's News (IN7).
- Removals: an earliest and a latest day for lost in transit and a latest day for other removal claims, per store and date, on the store's removals-claims page and its latest News post (RM6).
- Removal grading disputes: length and anchor per store and date, on the store's removals-claims page or tool (RM12).
- Valuation disputes: every policy text read counts from the reimbursement's issue, while Australia's News post counts from the initial claim; the length is on G200213130 as the seller's store shows it and in that store's latest News post (VR20).
- FBA fee errors: Amazon staff state a window from each charge's date for itemised fees and a longer limit for non-itemised ones, on *FBA fees reimbursement policy: Weight and dimensions* (GL7U4JFSDXUTQAJ), which the seller sees signed in, and the store's latest staff guide; the charge date is `listTransactions` `postedDate` (FE9, EC21).
- One Chinese claim assistant, 船长BI, states a fixed span a first claim reaches back; by inference, items in it outside the window Amazon applies to their kind are not claimable (EC24).
- Fee claims, valuation and inbound in detail: ../fee-claims/SKILL.md, ../claim-value/SKILL.md and ../shipment-claims/SKILL.md.

## Where Amazon contradicts itself

- For UK warehouse-lost units, a UK staff post of 2026-04-06 says the claim is manual, with automatic reimbursement disabled there since 2022-08, against Amazon's UK News posts stating automatic reimbursement from 2025-01-15; both are stated, neither picked (FC5, EC27).
- Amazon announced automatic reimbursement of warehouse-lost units store by store, each in its own News thread with its own start date (2024-11-01 in the US and Canada; the UK in its own post), and no such announcement was found for any store besides the US, Canada and the UK (FC3, FC4).

## A forum post's store

- A Seller Forums post's store is the `marketplaceId` in its own post object, the same on every forum host, while `selectedMarketplaceId` follows the host; Amazon does not document the field, and the reading was checked on four posts whose store their own words fix (FC45).
- Amazon issues one News text as separate threads per store with values that differ between the copies, so a value read in one thread is that store's value only (FC46).
- On a seller's post the field is the store the seller posted under, which can differ from the store the post discusses (FC47).
- The post-to-store table: ../warehouse-claims/SKILL.md.
