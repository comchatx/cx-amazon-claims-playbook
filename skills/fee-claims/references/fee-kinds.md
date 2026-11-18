# Fee kinds beyond measurement

## Low-price FBA

- Amazon's Spain low-price FBA page (2026) says low-price FBA rates apply automatically to eligible units, with no enrolment; that a unit eligible on Amazon's stated criteria but charged the standard rate is a fulfilment-fee overcharge is the research's inference (FE31).
- The price thresholds and size limits by store are read on the store's low-price FBA page on sell.amazon.<tld>, read by plain GET (FE31).
- The US low-price FBA rule: @comchatx/cx-amazon-finance-playbook, its fees-and-charges skill.
- No Amazon page read states which price, at which moment, decides eligibility: read in Amazon's documents, not yet seen on a live account (FE31).
- Small and Light closed in 2023; the research reads a former Small and Light unit's fee under low-price FBA or the standard rate, with no separate claim of its own (FE49).
- No Amazon page read names a fee claim of Subscribe & Save's own; its fees are the order's fee lines, under the kinds here (FE48).

## Inbound placement

- The placement fee shown in the shipping workflow is an estimate; the fee is charged a stated span after receipt, on the inbound location and the quantities received (US-store staff posts, 2024) (FE25).
- The no-fee optimized option needs compliance, including a stated minimum of identical cartons or pallets per item; the timing and the minimum are on Seller Central's *FBA inbound placement service fee*, which the seller sees signed in (FE25).
- The quote is `listPlacementOptions` (Amazon Fulfillment); plan compliance by plan, shipment and SKU is in Seller Central's placement fee report only (FE25).
- Amazon staff direct a seller to a Seller Support case when a placement fee is charged on a shipment never received; no page read says whether a lost-unit reimbursement includes the placement fee paid on that unit (FE26).

## Partnered-carrier charges

- From 2025-06-12, on domestic US partnered-carrier shipments, a difference between the seller-entered and the carrier-measured weight, dimensions or freight class brings a credit or a charge, shown in the Inbound Performance dashboard; sellers report their disputes of such charges rejected (FE27).
- Confirming a partnered-carrier option agrees to its charge; voiding within the option's window refunds it in full, outside it charges "may apply", and a non-partnered shipment can be voided at any time (FE43).
- The window is `Quote.voidableUntil` from `listTransportationOptions` (Amazon Fulfillment), and `cancelInboundPlan` cancels the whole plan (FE43).
- No Amazon text read refunds a partnered charge once the void window has passed when the carrier never collected; UK sellers report Seller Support declining, and GETIDA and Threecolts list the kind as their own claim type (FE44).
- Amazon's staff guide names partnered-carrier charges in neither fee class, so no page read states their filing limit; which limit the "Fees Charged in Error" route applies is read in Amazon's documents, not yet seen on a live account (FE44).

## Low-inventory-level fee

- Amazon credits low-inventory-level fees caused by Amazon or Amazon-managed inbound and processing delays, monthly, by a stated day of the following month (US-store News post, 2024-05-02) (FE28).
- The credit's timing and conditions are on Seller Central's *Low-inventory-level fee*, which the seller sees signed in; how much of a delay the credit covers is stated on no page read (FE28).
- The weekly fee flag and exemption per SKU are in `GET_FBA_INVENTORY_PLANNING_DATA` (Amazon Fulfillment) (FE28).

## Storage on units Amazon no longer stores

- A US-store staff reply of 2025-04-30 says storage stops promptly once a unit is identified as lost or damaged; a storage line on units already adjusted out has no basis in that statement (FE38).
- No Amazon text read says whether storage charged between a loss and its identification is refunded, or whether a lost-unit reimbursement covers fees paid on the unit (FE38).
- A US-store staff reply of 2025-06-27 says no storage is charged on units in a created removal order during its processing (FE40).
- No Amazon text read says whether researching units bear storage (FE39).
- Whether the storage report's `average_quantity_on_hand` counts researching, lost or removal-pending units is read in Amazon's documents, not yet seen on a live account (FE39, FE40).
- Amazon names system errors among the causes of stranding, but no Amazon text read refunds storage on stranded units, and a seller's direct question drew no staff answer (FE42).
- Whether storage on stranding Amazon caused is ever credited, and by which route, is read in Amazon's documents, not yet seen on a live account (FE42).
- The units lost or damaged and their dates: ../warehouse-claims/SKILL.md.

## Removal and disposal fees

- A removal or disposal fee error is a non-itemised FBA fee error under the staff guide's longer limit (FE41).
- Removal and disposal fees post per unit from a change date per store, read on each store's News post by plain GET; under per-unit charging, a fee with no matching shipped or disposed unit has no basis in Amazon's stated rule, by the research's reading (RM26, RM27).
- No Amazon text read says whether the reimbursement for a removal lost in transit includes the removal fee paid on it; vendors list "Lost Removal Order" as a claim for the units (FE41).
- The removal itself as a claim: ../shipment-claims/SKILL.md.

## Returns processing fee

- Whether the per-return fee or the high-return-rate rule applies follows the product's category assignment, which Amazon decides; a support reply, as a seller relays it, held a shoe-care product to be in the shoes class and the fee accurate (FE29).
- Charged returns-fee units cannot be matched to individual returns from any report found: sellers report Seller Central's returns-fee report has no order numbers, and no SP-API report breaks the fee down (FE30).
- The returns fee's classes and thresholds: @comchatx/cx-amazon-finance-playbook, its fees-and-charges skill.

## Unplanned prep and labelling

- Amazon applies prep or labels a shipment lacked, charges a fee per unit and flags the defect in the Inbound Performance dashboard; units with missing or defective labels are not eligible for reimbursement (FE45).
- Staff name the problems tab under the shipment summary as the route for disputing the fee, a seller's step in Seller Central (FE45).
- The dispute limit is stated two ways and both stand: from when the problem is reported, on the unread *Unplanned services* help page by search summary only; and under the staff guide's non-itemised limit (FE45).
- Which of the two a dispute meets in practice is read in Amazon's documents, not yet seen on a live account (FE45).
- Each fee per shipment, carton and FNSKU is in `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA` (`problem-type`, `fee-type`, `fee-total`; Pricing or Amazon Fulfillment) (FE45).

## Inbound defect fee

- By a US-store News post of 2026-10-30, Amazon waived the deleted or abandoned defect fee for international plans whose remaining shipments arrived within a stated span of the first receive, and reimbursed fees already charged without a claim, shown in the Reimbursements report (FE46).
- The waiver's scope is read on that News post by plain GET; no dispute window for the defect fee was found (FE46).
- Under which `reason` the credit appears in `GET_FBA_REIMBURSEMENTS_DATA`, and whether it carries the shipment ID, is read in Amazon's documents, not yet seen on a live account (FE46).

## AWD box-dimension fees

- For AWD storage and transportation fees only, Amazon reimburses the difference between the fees charged and the fees on corrected box measurements; Amazon's measurement governs, and a box remeasure is limited per box and period (FE47).
- The request is filed within a window counted from the charge date, one claim per fee charge, to Amazon Support or the account manager as a research request, the seller's step (FE47, IN33).
- The window and limits are read on the dated *Amazon Warehousing & Distribution Service Terms* on supplychain.amazon.com, read by plain GET (FE47).
- AWD is not readable on the five roles (FE47).
