---
name: return-claims
description: "What Amazon owes an FBA seller on a customer order, keyed by the order id, when the refund, the return and the unit do not line up: a refund or replacement whose unit never came back, a return graded unsellable and the disposition that decides fault, FBA Damaged Inventory Ownership, a wrong item, empty box or switched return, a replacement whose original was not returned, a refund above the sale, a returns reimbursement taken back when the unit arrives, where each store states the customer-return window, the FBA Returns report and the replacements report, Lost_Outbound and Damaged_Outbound, returns under another FNSKU, MCF and seller-fulfilled returns outside the FBA claim, and Remote Fulfillment and EFN returns. For any question about a buyer refunded who kept the item, a return that came back damaged, empty or wrong, whether Amazon owes for it, or what the returns report shows for an order."
---

## What Amazon owes on a return

On an FBA order Amazon refunds or replaces for the seller and debits the seller; it reimburses, in most cases, a unit not returned within the store's set number of days of the refund, reimburses a unit returned unsellable through Amazon's fault, and restocks a sellable return with no money (RT1).
The reimbursement decision follows the unit's physical condition as evaluated at the fulfilment centre, not the buyer's chosen reason (RT2).
Where an FBA unit is lost, damaged or missing, or the wrong item is delivered to the buyer, Amazon, unless the seller caused it, replaces or refunds at its option and reimburses the seller under the FBA Guidelines (RT46).
Outcomes, fault, wrong items, replacements, refunds above the sale and take-backs: references/outcomes.md.

## The window

The customer-return window counts from the refund or replacement date, and its day counts differ by store and Amazon's posts disagree; which statement the claim tool enforces for a store is open: read in Amazon's documents, not yet seen on a live account (RT4, EC5).
Each store's statements and where each is read: references/windows.md.

## The unit side

The FBA Returns report lists only units received at a fulfilment centre, so a refund without a return has no row (RT32).
Its `return-date` is the processing date at the centre, not the start of the claim clock (RT33).
Columns, dispositions, statuses and the replacement link: references/reads.md.

## Edges

Outbound loss before delivery, wrong-FNSKU and commingled returns, MCF and seller-fulfilled returns, Remote Fulfillment and EFN returns: references/edges.md.

## What cx cannot do

No SP-API operation files a claim, replies to or reopens a case, or attaches evidence; each is the seller's step in Seller Central, where the IDR portal, announced for the US store on 2025-01-21, covers customer returns (SU12, FL5).
Routes, evidence and conduct: ../claim-filing/SKILL.md.
What a return reimbursement is worth, reversals and value disputes: ../claim-value/SKILL.md.
Units lost or damaged inside the warehouse: ../warehouse-claims/SKILL.md.
Units short on the way in: ../shipment-claims/SKILL.md.
A return fee charged in error: ../fee-claims/SKILL.md.
SAFE-T, A-to-z and refund money lines: @comchatx/cx-amazon-finance-playbook, skill refunds-and-reimbursements.
How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
