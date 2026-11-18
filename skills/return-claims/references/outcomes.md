# Outcomes: what Amazon owes on a refunded or replaced FBA order

## The three outcomes

- On an FBA order Amazon refunds or replaces on the seller's behalf and debits the seller (RT1).
- In most cases Amazon charges the buyer and reimburses the seller when the unit is not returned within the store's set number of days of the refund; US and Canada staff posts read 2026-11-13 state that number, and where the seller sees it for any other store is open, not yet seen on a live account (RT1).
- A unit returned sellable goes back to the seller's inventory and no money is owed (RT1).
- A unit returned unsellable is reimbursed only where Amazon is responsible for its condition (RT1).
- The decision follows the unit's physical condition as evaluated at the fulfilment centre, not the reason the buyer chose (RT2).
- Under the FBA Service Terms Amazon decides refunds on FBA units and notifies the seller when it holds the seller responsible; the seller may appeal within a period counted from that notification, and in Australia may also ask for the unsuitable unit back for inspection (RT29).
- The appeal period is the one in F-8.2 of the store's Business Solutions Agreement; Amazon's NA redline (2019) and AU agreement (2023) were read as PDFs (RT29).

## Dispositions and fault

- `DAMAGED` and `CARRIER DAMAGED` read "We take responsibility for the damage" on Amazon's returns report help as the listing pack read it on 2026-10-14; Gorilla ROI's close copy of that table adds that ownership passes to Amazon and the unit is compensated under the reimbursement policy (RT9).
- In Gorilla ROI's copy of the same table, `CUSTOMER DAMAGED` and `DEFECTIVE` leave the unit in the seller's unsellable inventory (RT9).
- In that copy, `CUSTOMER DAMAGED` can mean only that the packaging was opened (RT9).
- A dispute of a customer-damaged or defective grade needs the unit physically returned through a removal order and is a removal claim; in Amazon's EU redline of 2024-08-20 the claim adds an explanation of the disagreement (RT13, RM11).
- The grading-dispute window's length and anchor are per store and per date, read on the store's removals-claims page or tool, which the seller sees signed in; Australia's News post of 2025-08-14, read by plain GET, counts it from the date the unit was removed from the network (RT13, RM12).
- As PPC Land quotes Amazon's text, a seller enrolled in FBA Damaged Inventory Ownership keeps enrolled Amazon-fault damaged inventory in its unfulfillable stock and decides its removal, and that inventory is not eligible for damage reimbursements (RT11).
- The enrolment's scope, all ASINs or a list, is on *FBA Damaged Inventory Ownership* as the seller sees it signed in; no SP-API read shows the enrolment (RT11).

## Wrong item, empty box, switcheroo

- On Amazon's returns report help as the listing pack read it on 2026-10-14, the reason code `SWITCHEROO` is the buyer's claim "Amazon sent me the wrong item", not Amazon's finding that the buyer swapped the unit (RT18).
- The contract covers a wrong item delivered to the buyer, as it covers a unit lost, damaged or missing (RT46).
- Amazon's US policy redlines of 2024-12-18 and 2025-02-24 put the customer-return claim under "Post-Order Lost or Damaged Events", while sellers in two US forum threads of 2025 report wrong-item claims paid at sourcing cost, one dating it from 2025-04-01; which basis a store pays is read in Amazon's documents, not yet seen on a live account (RT17, VR27).
- One US seller reported on 2026-08-05 a materially different return reimbursed through removal handling at sourcing cost rather than the order basis (VR33).

## Replacements

- Amazon may settle a lost, damaged, missing or wrong unit by shipping a replacement to the buyer and reimbursing the seller under the FBA Guidelines, keeping its fees (RT46).
- The customer-return window counts from the refund or replacement date (RT4).
- The replacement-to-original link in the reports and orders reads: references/reads.md.

## Refund above the sale

- No Amazon page read provides for repaying a refund above the order's charge; the contract leaves refunds to Amazon and makes the seller pay where Amazon finds the seller responsible (RT24).
- Sellers on the EU forum in 2025 report FBA refunds of several times the order value, called "goodwill" or a "concession", refused for reimbursement (RT24).
- Recovery services list "refund overcharge" as a claim type (RT24).
- On seller-fulfilled orders, `Refunded Amount` beside `Order Amount` sits in `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE`, whose roles, Inventory and Order Tracking or Direct to Consumer Shipping (Restricted), are outside the five; either would open those columns (RT39).

## Reimbursed, then the unit comes back

- Under the FBA Service Terms, if a refunded or replaced unit comes back sellable and Amazon restocks it, the seller repays its Replacement Value; with the policy's reversal sentence this is the basis for taking back a returns reimbursement (RT30).
- Practitioners name the transaction description `COMPENSATED_CLAWBACK` ("Reversal of previous refunds") as Amazon taking back a reimbursement when a unit is found or a return arrives sellable; Amazon publishes no definition read here (RT31).
- Whether that description and the Reimbursements report's reversal row are one event is read in Amazon's documents, not yet seen on a live account (RT30, RT31).
- Reversal grounds, links and found units: ../claim-value/SKILL.md.
