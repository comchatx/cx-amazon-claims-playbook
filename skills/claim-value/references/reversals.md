# Reversals and found units

## Amazon's rule

- Amazon's policy names two grounds for reversing a reimbursement: it was made in error, or the reimbursed item was found and returned to inventory (VR36).
- The policy states no time limit for a reversal and no rule for the amount reversed, in its English, Chinese and Japanese texts (VR36).
- Whether a reversal's amount ever differs from the original `amount-total`, and whether every reversal has a matching ledger row, is read in Amazon's documents, not yet seen on a live account (VR36).
- US-store staff send a seller who doubts a reversal to the inventory ledger, to see whether the units were added back, and to Seller Support; no staff post names a dispute window for a reversal (VR37).
- Raising a reversal with Seller Support is the seller's step in Seller Central; no SP-API operation does it (SU12).

## What sellers report

- US-store sellers report reversals months after payment, in one thread more than a year after, including a unit "damaged" in the FC later reversed and added back as sellable, and bulk reversals with no unit visible as returned (VR38).

## In the data

- An FBA reversal shows as report reason `Reimbursement_Reversal` and in settlement descriptions (VR39).
- Finances v0 `ReimbursementClawback` is an India-only Easy Ship value and does not mark FBA reversals (VR39).
- Ledger codes N and O move units "because you received an Amazon reimbursement" or "because Amazon has reimbursed you for them", so a row that adds units back is not always a physical find; read from that wording, N or O is an ownership move tied to a reimbursement, F a find (VR40).
- The ledger's codes in full: @comchatx/cx-amazon-stock-playbook, its stock-position skill.
- A reversal's report columns and settlement lines: @comchatx/cx-amazon-finance-playbook, its refunds-and-reimbursements skill.
- Found units netted against lost ones: ../warehouse-claims/SKILL.md.
