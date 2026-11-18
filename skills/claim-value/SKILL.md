---
name: claim-value
description: "How much an Amazon FBA reimbursement is worth, not whether one is owed, and when Amazon takes a paid one back: the basis a reimbursed unit is valued on (sourcing cost since Amazon's 2025-03-31 change, Amazon's estimate where the seller entered none, the reduced estimate for unsellable units, sale price minus fees after an order and on customer-return claims, where Amazon's texts differ), Manage Your Sourcing Cost and its limits and invoices, Chinese invoices (发票) and Japan's 原価の管理, the per-unit cap by store, the valuation dispute and what its window counts from, amount-per-unit in GET_FBA_REIMBURSEMENTS_DATA, units put back instead of cash, cross-border currency, and Reimbursement_Reversal rows and found units. For any question about why a reimbursement looks low, what a lost unit should have paid, a sourcing cost entry, re-evaluating a value, or a reimbursement Amazon reversed."
---

## What a loss is worth

A unit lost before a customer order is valued at sourcing cost from each store's own date, after 2025-03-31 in the US, CA, UK, DE, FR, IT and ES texts (VR2, VR4).
Sourcing cost is the seller's approved Manage Your Sourcing Cost (MYSC) figure, else Amazon's estimate (VR5, VR8).
A unit lost after an order is valued on the order; which basis a store applies today is read in Amazon's documents, not yet seen on a live account (VR27).
Unsellable units take a reduced estimated cost before an order; after one, the US, CA, UK and DE texts give the discounted sale price minus fees (VR25, VR26).
A per-unit cap differs by store; it is on *FBA inventory reimbursement policy*, which the seller sees signed in, and in Amazon's dated redlines, read by plain GET (VR29).

## Sourcing cost

MYSC holds one cost per FNSKU per marketplace, entered by the seller in Seller Central; no SP-API operation reads or writes it (VR7, VR18).
An approved cost applies only to reimbursements issued after its approval, per US-store staff (VR8).
Amazon limits cost updates per FNSKU, counts differing by store and date, and invoice age, two US-store posts differing (VR11, VR14).

## Disputing a value

A valuation dispute is the seller's step in Seller Central, within a window each store's text sets, counted from the reimbursement or, in Australia's News post, the claim (VR20, VR21).

## Reading a line

`GET_FBA_REIMBURSEMENTS_DATA` names no basis, cost in force, cap or store (VR30).
A line with units put back moves stock, not money (VR34).

## Taken back

Amazon's policy reverses for error or a found unit, with no stated time limit or amount rule (VR36).

How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
How a reimbursement posts to money: @comchatx/cx-amazon-finance-playbook, its refunds-and-reimbursements skill.

## References

[rule.md](references/rule.md): the dated rule, the estimate, Japan.
[sourcing-cost.md](references/sourcing-cost.md): MYSC, limits, proofs, Chinese invoices.
[disputes.md](references/disputes.md): the window and its routes.
[basis.md](references/basis.md): unsellable, post-order, customer return, cap.
[lines.md](references/lines.md): a line's amount, units, currency.
[reversals.md](references/reversals.md): reversals and found units.
[warehouse-claims](../warehouse-claims/SKILL.md), [shipment-claims](../shipment-claims/SKILL.md), [return-claims](../return-claims/SKILL.md), [fee-claims](../fee-claims/SKILL.md): what is owed, by kind.
[claim-filing](../claim-filing/SKILL.md): where a claim is filed.
