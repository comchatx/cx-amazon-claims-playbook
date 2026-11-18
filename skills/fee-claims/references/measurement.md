# Measurement and remeasurement

## Whose measurement sets the fee

- In this skill's grouping, a wrong measurement or size tier is one kind of overcharge; fulfilment, storage, aged-inventory, returns, removal and placement fees ride on it (FE1).
- Outside the EU certification regime, the weight and dimensions Amazon verifies set every size-tier-based fee (FE2).
- A US-store staff reply of 2023-11-14 says personal measurements are not accepted to contest a measurement, and that inconsistent FC measurements resolve to the largest (FE2).
- Amazon staff state that the measurement includes the packaging and loose bag flaps and handles, measured edge to edge, and name the packing material as the most common cause of seller-versus-FC differences (US-store staff posts, 2024-08-22 and 2025-04-30) (FE36).
- A packaging change after first receipt is a cause practitioners name for remeasures; that is Velocity Sellers' reading, not Amazon's (FE36).
- Each variation is its own product: one variation's fee is no evidence for another, and sellers report remeasures that changed one colour or size and not its siblings (FE3).
- In EU stores under certification the seller's certified dimensions set the fee instead: references/certification.md.
- The dimensional-weight divisor and size-tier rates by store: @comchatx/cx-amazon-finance-playbook, its fees-and-charges skill.

## Remeasurement

- A remeasure needs a sellable unit in an FC; Amazon refuses one for an FNSKU remeasured a stated number of times in a stated period, or once the account's monthly limit is used (US-store staff posts, 2024-09-20 and 2025-04-30) (FE4).
- Amazon asks that only requests expected to change fees be filed, and a staff post says staff can add a request beyond the monthly limit when given a case ID (FE4).
- The per-FNSKU limit is on Seller Central's *Understanding item package weight and dimensions*, which cx cannot read and the seller sees signed in; the account's remaining count shows only in the Seller Central widget (FE4).
- No Amazon text read names a number for the monthly account limit; the practitioners' figures differ from one another and are theirs (FE4).
- Amazon states review times only for a few kinds, remeasurement among them, each on its own page (FL30).
- Requesting a remeasure is the seller's step in Seller Central; no SP-API operation requests or reads one (FE4, SU12).
- A US staff member called remeasurement a step before a successful fee reimbursement, in a case where Seller Support had set a wait before the remeasure; that is one statement, with no rule page behind it (FE12).

## What follows a remeasure

- Amazon staff described a dimension correction paid as one "Fee Adjustment - Weight and Dimension Change" entry per affected order, under Transaction Type "Other" in Seller Central's Transaction View, with no reimbursement ID (US forum, thread of 2025-02-05) (FE13).
- So such a credit does not appear in `GET_FBA_REIMBURSEMENTS_DATA` under a reimbursement ID (FE13).
- The per-order entry is read in Amazon's documents, not yet seen on a live account; how it is typed in `listTransactions` and in settlement V2 is stated on no page read (FE13).
- US sellers report refusals, or no reimbursement, after Amazon confirmed a wrong measurement; in one thread staff advised a new case asking for an order-level audit and refund (FE14).
- Velocity Sellers, Leviathan Sellers, My Amazon Guy and Notifcentral each hold that a remeasure fixes future fees only; that is their reading (FE14).
- Whether any US fee adjustment posts by itself after a remeasure that lowers a tier, or only on request, is read in Amazon's documents, not yet seen on a live account (FE13, FE14).
- In one 2025 case, as a seller relays it, Selling Partner Support asked for a file listing, per FNSKU, the incorrect fee, the correct fee, the difference and the total; Amazon's staff guide asks for shipment IDs, FNSKUs and evidence such as measurements and photos (FE15).
- Case mechanics and the conduct Amazon penalises: ../claim-filing/SKILL.md.
