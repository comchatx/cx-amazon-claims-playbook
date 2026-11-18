# The FC window and the IDR portal

## The window's rule

- Before the 2024 change, Amazon's policy text, as a third-party mirror shows it, counted the FC window from "the date the item was reported lost or damaged in your Inventory Ledger report" (FC7).
- A seller on the US store relays Amazon's text that from 2024-10-23 the eligibility windows, except for shipment-to-Amazon claims, were shortened (FC7).
- Chinese practitioners give a pre-2024 length that no Amazon text read supports (FC8).
- The window is set per store and changed by announcement; posts read carry windows for the US, Canada, the UK, Sweden, Saudi Arabia, Egypt, the UAE and Australia, and none was found for DE, FR, IT, ES, NL, PL, BE, IE, JP, IN, MX, BR, TR or SG; read 2026-11-13 (FC9).
- It counts from Amazon's report of the event, not the seller's discovery: "after the item was reported lost or damaged" (US, Canada and UK News), "the date the loss or damage event appears in your reports" (US staff, 2026-08-13), "the date the unit is marked as … 'Misplaced'" (Saudi Arabia) (FC10).
- The Saudi Arabia, Egypt and UAE window set, effective 2024-09-05, counts calendar days from the "Inventory Adjustment report" and was issued for those three stores, not for the US, the UK or the EU; only the Egypt copy lists carrier-damaged returns and lost customer returns, and the set links a summary page, unread, that cx cannot read (FC11).
- The UK staff post of 2026-04-06 counts the lost window from "the event" and says damaged claims are "Available immediately after the damage event is visible", with no end stated, against the UK News posts (FC5, FC9).

## Where cx reads a store's window

- The store's latest Seller Forums News post on claim windows, the one whose `marketplaceId` is that store, by plain GET (FC9).
- *FBA inventory reimbursement policy* as the store shows it, a page cx cannot read, which the seller sees signed in (FC9).
- No SP-API operation returns a window (FC9).
- Which window the store's policy page shows today, and whether Contact Us refuses a lost-unit claim outside it, is read in Amazon's documents, not yet seen on a live account (FC9).

## Pitfalls of the sources

- The US staff post of 2026-08-13 sends sellers to "Reports > Fulfillment > Inventory Adjustments", and the Middle East posts and the Supply Chain Portal policy count from the "Inventory Adjustment report", which Amazon retired on 2023-01-31 for the Inventory Ledger (FC12).
- The Supply Chain Portal reimbursements policy is a different programme from Seller Central FBA, for an active MCF account; its window, cap and fallback values are its own, read on that page by plain GET (FC40, FL27).

## The ledger's reach

- The ledger detail's look-back is stated on Amazon's *FBA Reports* page; no Amazon page read says what becomes of a loss row still unreconciled past it (FC53, SU15).
- A report's look-back and a claim's window are different facts (SU18).
- Whether an unreconciled M row persists to the edge of the ledger's reach, and is later reimbursed, found or dropped, is read in Amazon's documents, not yet seen on a live account (FC53).

## The IDR portal

- News_Amazon announced the Inventory Defect and Reimbursement portal on 2025-01-21 in a thread whose store is the US; no launch post for another store was found (FC13).
- Its scope is warehouse lost, warehouse damage and customer returns; it "doesn't include defects under missing from inbound, removals or warehouse disposals" (FL5).
- It is reached from the FBA dashboard's Inventory menu or from the Reimbursements report; its help page is one cx cannot read, which the seller sees signed in (FL5).
- Practitioners (eComEngine, My Amazon Guy) describe its pages as Overview, Eligible for Claim, In Progress, Resolved and Defect Status Trend, with resolutions Reimbursed, Reconcile and Ineligible, built from the ledger, the customer returns report and the policy (FC15).
- No operation or schema in Amazon's SP-API models returns its Eligible-for-Claim list, its statuses or its resolution reasons (FC14).
- Using the portal is the seller's step in Seller Central; no SP-API operation acts in it (SU12).
- Whether the portal exists outside the US, and whether its Eligible-for-Claim rows match candidates rebuilt from the ledger and the Reimbursements report, is read in Amazon's documents, not yet seen on a live account (FC13, FC14).
