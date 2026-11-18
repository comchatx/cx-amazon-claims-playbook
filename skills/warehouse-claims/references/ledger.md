# The ledger, found against lost, and what the API carries

The ledger's grammar (event types, reason codes, reconciled and unreconciled quantity): @comchatx/cx-amazon-stock-playbook, its stock-position skill.
How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.

## The codes this skill reads

- Lost is M or 5, misplaced (FC22).
- Damage at a centre is 6, 7, E, H, K or U, each followed by a P row (FC22).
- Found is F and N; O is a correction; D is disposed (FC22).
- N and O also move units because of a reimbursement, so a net that counts N as a find can count a reimbursement as a recovered unit (FC25, VR40).
- The code table is Openbridge's and Reason Automation's reproduction of Amazon's ledger help (FC22).
- Whether a store's file carries codes outside that table is read in Amazon's documents, not yet seen on a live account (FC22).
- For a reimbursed unit, whether an N or O row appears, and on what date against the report's `approval-date`, is read in Amazon's documents, not yet seen on a live account (FC25).

## Transaction Item ID

- Amazon locates the Transaction Item ID in the Inventory Ledger, and a practitioner pastes the ledger's `Reference ID` into "Check warehouse damaged reimbursement status", so an adjustment row's `Reference ID` serves as the Transaction Item ID by practitioner use (FC17).
- Whether that tool accepts the ledger's `Reference ID` is read in Amazon's documents, not yet seen on a live account (FC17).

## Researching

- `getInventorySummaries` returns `researchingQuantity`, "the misplaced or warehouse damaged units that are actively being confirmed at our fulfillment centers"; it is the only SP-API field that names misplaced units (FC30).
- How its age buckets line up with the M rows, and when a unit leaves researching, is read in Amazon's documents, not yet seen on a live account (FC30).

## Amazon's own checks

- Amazon's older policy text, as a third-party mirror shows it, names three pre-claim checks: Manage FBA Inventory shows the unit was not found or restored; the Inventory Ledger gives the date and adjustment code; the Reimbursements report, "by FNSKU and date", shows it was not already reimbursed (FC20).
- A practitioner (My Amazon Guy, 2025-10-31) relays seller reports of found units coming back months after a reimbursement, the reimbursement reversed and the units sometimes expired and charged for removal or disposal (FC28).
- One practitioner reports reversals of part of one account's 2023 reimbursements (FC29).
- How a reversal is read: ../claim-value/SKILL.md.

## Practitioners' ways, side by side (theirs, none picked)

- Selecting open losses: Spaghetti filters the ledger detail's Adjustments on M and 5 with an unreconciled quantity of at least one; 知无不言 drops blank and zero unreconciled rows of the older reconciliation report and reads the M rows; Seller Labs flags negative rows with the misplaced, damaged and disposed reasons (FC23).
- Netting: per pair of rows, M then F nets to zero (ZonGuru); per FNSKU, E and M against F and N, a negative difference read as missing stock (连连) (FC24).
- Matching a loss to a payment: Seller Labs matches by FNSKU and date range, not FNSKU alone, because no identifier links a ledger adjustment to a Reimbursements report row (FC27).

## Pitfalls of the data

- N and O can stand for a reimbursement, not a find (FC25).
- A found unit can appear at another centre, on another date, or under another FNSKU through codes 3 and 4; a net on the summary view by country hides this, while the detail view carries each row's `Fulfillment Center` (FC26).

## What the SP-API carries

- Finances v0 describes `FBAInventoryReimbursement` as occurring "if a seller's inventory is damaged"; `LostOrDamagedReimbursement` is an Easy Ship type, not FBA (FC31).
- The AWD API model, the Data Kiosk schemas and the notification schemas carry no field for lost, damaged or reimbursed units (FC32).
- No notification type announces a reimbursement or a ledger adjustment (SU31).
- The ledger names Amazon Fulfillment as its only role; the Reimbursements report answers to Pricing or Amazon Fulfillment (SU2, SU3).
