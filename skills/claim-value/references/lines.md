# Reading a reimbursement line

## What the line carries

- `GET_FBA_REIMBURSEMENTS_DATA` answers to Pricing or Amazon Fulfillment (SU3).
- It carries no column for the valuation basis, the cost in force, the cap or the store (VR30).
- From those columns it follows that whether a line is low shows only beside a basis read elsewhere: MYSC in Seller Central, the seller's own cost, or the order's basis; this is inferred, not Amazon's statement (VR30).
- The report's columns and how a line posts to money: @comchatx/cx-amazon-finance-playbook, its refunds-and-reimbursements skill.

## The basis a line should have

- Whether `Lost_Outbound` and `Damaged_Outbound` lines take the pre-order or the post-order basis is unread; read in Amazon's documents, not yet seen on a live account (VR31).
- An approved cost applies to reimbursements issued after its approval, so it follows, by inference, that the cost to compare a pre-order line with is the one in force when it was issued, not today's MYSC value (VR8, VR32).
- Where an order's sale price and fees are read: @comchatx/cx-amazon-finance-playbook, its refunds-and-reimbursements skill.
- A seller-entered cost from SKU Central and the Revenue Calculator sits in Data Kiosk Economics, which Amazon's correction says needs Selling Partner Insights, outside the five, while its Data Kiosk page lists Brand Analytics (VR19, SU33).
- A materially-different return reported paid at sourcing cost: references/basis.md.

## Units against cash

- Amazon may settle a valid claim by replacing the unit "with a new item of the same FNSKU" instead of paying, and such a line moves units, not money (VR34).
- What `amount-per-unit` and `amount-total` carry on a line with units put back is read in Amazon's documents, not yet seen on a live account (VR34).
- A unit put back arrives in the ledger as an N or O row: references/reversals.md.

## Store and currency

- The report carries `currency-unit` per line and no store column; Finances v0 `AdjustmentEvent` carries `StoreName` and an ISO 4217 `CurrencyCode` per amount, with no marketplace id (VR43, SU52).
- No Amazon text read says in which store and currency a reimbursement posts for a unit lost in a Pan-European transfer, in another country's FC under EFN, or in US stock sold through Remote Fulfillment, or in which store its value is disputed; this is read in Amazon's documents, not yet seen on a live account (VR43).
- A developer reports that the report returns the same rows whatever `marketplaceIds` names (SU24).
- A sourcing cost is entered per marketplace, and the proof-of-value list asks for the currency of the transaction (VR7, VR13).

How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
