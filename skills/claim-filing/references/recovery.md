# Recovery: the seller's choices and the amount owed

## The choices, side by side

- Whether to file oneself, pay a share to a service, use a subscription or ERP tool, enter a sourcing cost, or leave a kind alone is the seller's choice; none is picked here (EC25).
- Filing in Seller Central oneself: no commission, the seller's own time, and every kind has its window (EC25).
- A commission service: it files for the seller, takes a share of what is paid, possibly including money Amazon would have paid anyway depending on the contract, and its look-back does not reopen closed windows (EC25, EC4).
- A subscription or ERP tool: it finds candidates and the seller files, for a fixed fee or none (EC25, EC23).
- Entering a sourcing cost on Manage Your Sourcing Cost: once Amazon approves it, eligible pre-order reimbursements issued after the approval date are valued at the seller's own cost instead of Amazon's estimate (EC25, VR8).
- Earlier payments, a declined entry and unsellable units: ../claim-value/SKILL.md.
- Leaving a kind alone: the money in that kind lapses when its window closes, and Amazon's automatic payments continue regardless (EC25).
- A vendor's fee, look-back and contract terms are read on the vendor's own page and contract; no Amazon page or SP-API read gives them (EC4, EC25).
- How seller tools book a reimbursement: @comchatx/cx-amazon-finance-playbook, its refunds-and-reimbursements skill.

## The market

- No Amazon page read bars or endorses third-party reimbursement services (FL19).
- SPS Commerce bought Carbon6 (Seller Investigators, ChargeGuard), announced 2025-01-02 and closed 2025-02 by its two filings' dates, and announced on 2026-06-30 the completed sale of its 3P Revenue Recovery business at an estimated loss, citing its 1P focus (EC11).
- On its earnings calls SPS cited Amazon's policy changes and the take-rate model (EC11).
- The "short shipment" and "redispute" changes SPS said hurt recovery in 2026 concern, by the call's own words, suppliers' shipments to Amazon Retail, not FBA seller claims (EC14).
- Services publish success rates (GETIDA, Seller Investigators as AmpliSell relays it, Nova Data) that state no denominator or method (EC22).
- No Chinese tool or service found files claims for a commission at a current public rate; 船长BI offers a zero-commission assistant covering warehouse lost or damaged only, and 领星, 积加, 赛狐 and 易仓 estimate while the seller files (EC23).
- Lingxing ties a claim to its payment by a seller-entered CASE ID found in the Reimbursements report and shows the ledger `Reference ID` beside each candidate, under per-case and per-day limits of its own; other practitioners match by FNSKU and date range instead (SU43).
- Lingxing values a dimension overcharge as (fee charged − expected fee) × quantity, from the fee preview's measured dimensions, one method among those set side by side (SU44).

## What is published, and what is not

- Amazon publishes no fulfilment-centre loss rate, no share of cases paid without a claim and no reimbursement total; every "share of revenue owed" figure found is a vendor's or tool maker's and states no method (EC6).
- Vendor figures from before Amazon's 2024 window changes, its automation dates or its 2025-03-31 move to sourcing cost measure a pool Amazon has since changed (EC7).
- The loss-rate inputs recovery calculators use (ecomcalctools, Captain BI) are not sourced (EC17).
- No peer-reviewed or industry study of FBA loss, damage or reimbursement rates was found; the nearest research measures store record inaccuracy, store shrink and online returns (EC18).
- Single sellers have published their own inbound accuracy and lost-unit counts, which are counts for one account, not rates for FBA (EC16).
- On customer returns vendors contradict each other: GETIDA reports Amazon auto-pays almost all FBA customer-return issues, sellerboard says unreturned returns are almost entirely seller-initiated (EC15).
- No page read gives the share of a seller's former recoveries left claimable after Amazon's 2024–2025 changes (EC28).

## Amazon's words on the value

- For a unit lost or damaged before a customer order, the per-unit fall from Amazon's 2025-03-31 move to sourcing cost works out, as an inference from the two bases, to 1 − sourcing cost ÷ (sale price − fees), with the cost from Manage Your Sourcing Cost, which no operation reads (EC8).
- Amazon's spokesperson gave the change's purpose as "a more consistent approach as more sellers are using our supply chain services", and said specific cost data is not shared with any other seller, Amazon Retail included (EC9).
- Value per unit follows the moment of loss: before an order at sourcing cost, a customer return on a post-order basis after fees whose exact basis is contested; details in ../claim-value/SKILL.md (EC10).

## The amount owed, as a formula

- A model inferred over Amazon's dated rules, not Amazon's, puts what an amount owed is made of, by kind, as units through the stage × incidence × value per unit × the share Amazon does not pay unasked; the window then cuts what can still be claimed (EC19).
- Units through the stage: `GET_LEDGER_SUMMARY_VIEW_DATA` receipts, or Fulfillment Inbound v0 `getShipmentItems` `QuantityReceived` (Amazon Fulfillment) (EC19, SU4).
- Incidence: the ledger detail's adjustment events against receipts, and v0 `QuantityShipped` against `QuantityReceived` (EC17).
- Value per unit: the seller's sourcing cost, or sale price and fees from `listTransactions` and the fee preview (EC8, EC19).
- The share Amazon pays unasked is a fact of the seller's store: whether `Lost_Warehouse` and `Damaged_Warehouse` rows with blank `case-id` arrive in its `GET_FBA_REIMBURSEMENTS_DATA` after its automation date, against the ledger's lost and damaged adjustments; that a blank `case-id` means paid unasked is read in Amazon's documents, not yet seen on a live account (EC27).
- For customer returns, the split is customer-return rows with blank against filled `case-id`, joined to refunds in `listTransactions` and to the FBA customer returns report (EC15).
- For a mismeasured SKU, what is left is the per-unit overcharge times the units charged inside the itemised fee window, while a non-itemised error reaches further back (EC21).
- The seller's own history of what Amazon paid is `GET_FBA_REIMBURSEMENTS_DATA`: `amount-total` by `reason`, cash against inventory quantities, reversals netted through `original-reimbursement-id`, on Pricing or Amazon Fulfillment (EC26).
- A store's remaining share is read from its own reimbursements, by `reason` and by blank against filled `case-id`, before and after its automation date and 2025-03-31; what that share is for a live store is read in Amazon's documents, not yet seen on a live account (EC28).
