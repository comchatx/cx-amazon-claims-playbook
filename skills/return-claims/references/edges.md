# Edges: outbound loss, wrong FNSKU, MCF and seller-fulfilled, cross-border

## Lost or damaged after the order, before delivery

- Where an FBA unit is lost, damaged, missing or the wrong item is delivered, Amazon, unless the seller caused it, replaces or refunds at its option and reimburses the seller under the FBA Guidelines, keeping its fees (RT46).
- Amazon's US policy redlines of 2024-12-18 and 2025-02-24 value a loss by whether it happened before or after the end customer's order, name only the customer-return claim under their post-order heading, and list no separate outbound claim kind (RT47).
- That a unit lost or damaged after the order and before delivery is handled as a customer-return case is the research's inference from that text (RT47).
- `Lost_Outbound` and `Damaged_Outbound` are Reimbursements report `reason` values seen in public files; no Amazon page read defines them and no SP-API model names them (RT48).
- Whether those rows arrive with no filed case and at which basis they are valued is read in Amazon's documents, not yet seen on a live account (RT48, VR31).
- Sellers of non-returnable FBA items in one US thread opened 2026-03-13 report refunds for buyer-reported transit damage denied at first contact for being non-returnable and approved on escalation; no Amazon reply in the thread states a rule (RT49).
- Seller 365, a recovery vendor, defines "Lost Outbound" as a shipment that leaves a centre and is never delivered, counting customer orders and lost removal orders in it (RT50).
- Shipping API v2 `createClaim` files a carrier claim on a parcel, not an FBA reimbursement (SU13).

## Wrong-FNSKU and commingled returns

- Amazon defined commingling as fulfilling orders from the closest exact-match inventory "even if that inventory belonged to a different seller"; its UK and Canada News posts of 2025-12-08 end it for inventory shipped on or after a date they state, read by plain GET (RT51, IN24).
- No Amazon page read says to whose inventory a returned commingled unit is credited (RT51).
- Recovery vendors list returns received under a different FNSKU than ordered as a claim type; Amazon names no such kind in pages read (RT52).
- The returns report row carries `sku` and `fnsku` beside the order; that such a return would show there is the research's inference, and whether a seller's file holds one is read in Amazon's documents, not yet seen on a live account (RT52).

## MCF and seller-fulfilled returns

- MCF units are the seller's to refund and return; an MCF return Amazon receives is returned or disposed at the seller's direction and cost, outside the FBA customer-return claim (RT44).
- An Amazon moderator's reply of 2026-04-23 pointed an FBA seller to SAFE-T and the Guided Refund Workflow, both seller-fulfilled programmes, so that reply is no rule source for FBA (RT43).
- `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE` carries `Order Amount`, `Refunded Amount`, `Return delivery date`, `A-to-Z Claim` and five `SafeT` columns, with a per-request date span stated on Amazon's *Returns Reports* page (RT39).
- Its roles, Inventory and Order Tracking or Direct to Consumer Shipping (Restricted), are outside the five; were the app to hold either, it would open seller-fulfilled refunds against order amounts and SAFE-T claim states (RT39, SU47).
- The Seller Fulfilled Prime returns reports name Pricing and carry the same SAFE-T columns, for Prime orders only (SU48).
- SAFE-T and A-to-z claims as money: @comchatx/cx-amazon-finance-playbook, skill refunds-and-reimbursements.

## Cross-border returns

- A Remote Fulfillment with FBA return is sent back to the US and is subject to the FBA customer-returns policy (RT53).
- From 2025-03-25 Amazon credits return fees on Remote Fulfillment returns in the Mexico and Brazil stores, automatically and within a period its US News post of 2025-03-10 states, read by plain GET, as a "Refund" transaction with details "Remote Fulfillment credit" (RT54).
- A return fee charged with no credit: ../fee-claims/SKILL.md.
- Amazon's EFN handbook (updated 2022-01) says that under EFN between the UK and the EU returned items are sent to the source store; sellers report returns landing in other EU centres and storage charged there (RT55).
- No page read states the store or currency of a cross-border return's reimbursement, and it is not yet seen on a live account (RT55).
- The Reimbursements report carries `currency-unit` and no store column, while the ledger detail carries `Country` and `Store` (SU52).
