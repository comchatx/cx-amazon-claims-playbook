# What counts, and where the edges are

## What counts

- Amazon's older policy text, as a third-party mirror shows it, covers eligible units "lost or damaged by an Amazon fulfillment center or a facility operated on behalf of Amazon, after Amazon receives them from you", reported "in your Inventory Ledger report" (FC1).
- Amazon's US and UK policy PDFs of 2025-02-24 carry the general clause: an item "lost or damaged at a facility or by a carrier operated by Amazon or on behalf of Amazon" is replaced with a new item of the same FNSKU or reimbursed (FC1).
- US staff (2026-08-13) and the US and UK PDFs put "lost and damage claims during inventory replenishment handled by Amazon or on behalf of Amazon" at sourcing cost (FC2, VR4).
- The evidence Amazon names is the date or location of the loss (for example the FC ID), the Transaction Item ID or FNSKU, and proof of ownership; for a unit unsellable when lost, Amazon "may request additional information or documentation" to set a reduced value (FC18).
- Routes and evidence by kind: ../claim-filing/SKILL.md.

## Transfers between centres

- A unit lost in a transfer between centres has no claim type of its own in Amazon's pages read; by the research's reading, not Amazon's statement, the ledger shows it as an adjustment, with units in transit kept in "In Transit Between Warehouses" (FC36).

## AWD and AWD to FBA

- Amazon's AWD service terms (dated 2026-01-14) replace or reimburse units lost or damaged at an AWD facility or by an Amazon-operated carrier; the facility window starts "on the date that the Unit was identified by Amazon as lost or damaged", and valuation follows the MCF reimbursement methodology (FC37).
- The MCF policy the AWD terms name is the Supply Chain Portal reimbursements page, so an AWD claim's window, cap and valuation are read there by plain GET (IN26, IN34).
- Amazon's AWD help text, as a seller quoted it on 2024-09-17, promises "fair value" reimbursement when AWD finds fewer boxes than received "during facility audit or replenishment of boxes to the FBA network", on a case to Selling Partner Support (FC38).
- Sellers' threads (2025) describe AWD-to-FBA replenishment shipments as carrying FBA shipment ids and replenishment order ids, with their shortfalls pursued as inbound shortfalls, and report Amazon asking for carrier tracking they cannot hold (FC39).
- Whether AWD-to-FBA shortfalls appear as negative receipts or as adjustments, and under which reimbursement `reason`, is read in Amazon's documents, not yet seen on a live account (FC39).
- Inbound shortfalls: ../shipment-claims/SKILL.md.

## Cross-border: Pan-European FBA, UK–EU and EFN

- No Amazon page read names a claim type, window, route or reimbursing store for a unit lost while Amazon moves it across borders, or for EFN stock (FC48).
- By the research's reading, the ledger records such a loss as an adjustment at a centre, with `Country` and `Store` on each row and the move as `WhseTransfers`, and Amazon's AU agreement (2024-06-12) lets it "move Units among facilities" and reimburses loss "while they are being stored" under the FBA Guidelines (FC48).
- A reimbursement's store and currency are read from the Reimbursements report's `currency-unit`, Finances v0 `AdjustmentEvent.StoreName` and `AdjustmentAmount.CurrencyCode`, and Finances v2024-06-19 `marketplaceDetails.marketplaceId`; no Amazon page read states the rule (FC49).
- The Reimbursements report has no store or marketplace column; the ledger detail carries `Country` and `Store` (SU52).
- A developer reports the Reimbursements report returning the same rows whatever `marketplaceIds` names within a region (SU24).
- One ERP tells sellers to file in the Seller Central of the store where the event happened; no Amazon page read states this (FL40).
- In which store, report and currency a cross-border loss posts is read in Amazon's documents, not yet seen on a live account (FC48, FC49).

## NA Remote Fulfillment

- Under Remote Fulfillment the units stay in US centres while offers sell on Amazon.ca, Amazon.com.mx and Amazon.com.br; no page read states the store or currency of a reimbursement for such a unit (FC50).
- Whether such a reimbursement posts in a currency other than the US dollar is read in Amazon's documents, not yet seen on a live account (FC50).

## MCF orders

- An MCF order lost or damaged on the way to the buyer is claimed under Amazon's MCF terms, not as an FC-operations claim (FC51).
- Amazon's MCF pages exclude orders "marked as delivered by the carrier" and MCF fees, and the India page excludes MCF used to fulfil Amazon orders or to remove stock (FC51).
- Their window, value basis and cap are their own, read by plain GET on the Supply Chain Portal reimbursements page and on Amazon India's *Reimbursements for your MCF orders* (FC51).
- Losses on the way to an Amazon buyer: ../return-claims/SKILL.md.

## Vine units

- Vine units are FBA inventory ("FBA inventory must be sent to Amazon fulfillment centers for products to be shipped to Vine Voices"), and no Amazon page read addresses one lost or damaged before it reaches the Vine Voice (FC52).
- How Vine shipments appear in the ledger, and whether a unit lost on its way to a reviewer gets a `Lost_Outbound` row, is read in Amazon's documents, not yet seen on a live account (FC52).

## Exclusions

- Amazon's eligibility list in the US and UK policy PDFs of 2025-02-24 excludes units pending disposal or disposed of, defective or customer-damaged units, units outside FBA product restrictions, and, in the US, units on cancelled or deleted shipments; it names no exclusion for expiry, recall or force majeure (FC54).
- On expired stock damaged at a centre, the UK staff post of 2026-04-06 lists it as "Eligible for manual claims" (FC54, FC19).
- Amazon's AU agreement (2024-06-12) disclaims liability for failure to perform "by reasons, events or other matters beyond our reasonable control" and makes the seller responsible for recall costs; no reimbursement page or post read applies either to a unit lost in a centre; the US agreement's clauses were not re-read (FC55).
- A seller enrolled in FBA Damaged Inventory Ownership keeps its enrolled Amazon-fault damaged units in its unfulfillable stock, and they "will not be eligible for damage reimbursements"; the enrolment is on a page cx cannot read, which the seller sees signed in, and no SP-API read shows it (RT11).
- Whether the store's policy page names expiry, recall or force majeure among its exclusions is read in Amazon's documents, not yet seen on a live account (FC54).
