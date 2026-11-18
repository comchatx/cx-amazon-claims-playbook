---
name: warehouse-claims
description: "Inventory Amazon lost or damaged after receiving it: warehouse lost and damaged units (Lost_Warehouse, Damaged_Warehouse), units lost in transfers between centres, Pan-European FBA, EFN and Remote Fulfillment, at AWD, in an MCF order, and Vine units; whether Amazon pays warehouse losses without a claim in the seller's store, as each store's News post announced it, and the UK staff post that contradicts the UK posts; how each store sets the lost-or-damaged window and where it is read; what the IDR portal covers; the Inventory Ledger's misplaced, damaged, found and correction codes, the Transaction Item ID, researchingQuantity and found units netted against lost ones; and the exclusions. For any question about units Amazon misplaced, lost or damaged in its warehouses, whether Amazon already paid for them, why a ledger row shows lost, found or researching, or whether a warehouse loss can still be claimed."
---

## What counts

Eligible units lost or damaged by an Amazon centre, or a facility run for Amazon, after receipt, reported in the Inventory Ledger, in Amazon's older policy text, via a third-party mirror (FC1).

## Paid without a claim

Amazon announced proactive reimbursement of FC-lost units store by store: the US and Canada from 2024-11-01, the UK from 2025-01-15; no such post was found for other stores (FC3, FC4).
A post's store is the `marketplaceId` in its own post object, not the forum host; checked on four posts, the field is not documented by Amazon (FC45).
A UK staff post of 2026-04-06 says UK warehouse-lost units currently need a manual claim, automatic reimbursement disabled since 2022-08, against Amazon's UK News posts; neither is picked (FC5).

## The window

Set per store, changed by announcement, counted from Amazon's report of the event, as read on 2026-11-13 (FC9, FC10).
cx reads it from the latest News post on claim windows whose `marketplaceId` is the store, by plain GET; the seller sees *FBA inventory reimbursement policy* signed in; no SP-API operation returns it (FC9).

## The IDR portal

Announced for the US store on 2025-01-21; covers warehouse lost, warehouse damage and customer returns, not missing-from-inbound, removals or warehouse disposals; no SP-API operation returns its lists, and using it is the seller's step in Seller Central (FL5, FC13, FC14, SU12).

## The ledger

In third-party reproductions of Amazon's ledger help, loss is M or 5; centre damage is 6, 7, E, H, K or U, each followed by P; N and O also move units because of a reimbursement (FC22).
The ledger's grammar: @comchatx/cx-amazon-stock-playbook, its stock-position skill.

## Beside this skill

Opening, evidencing and answering a case are the seller's steps in Seller Central (SU12).
Routes and evidence: ../claim-filing/SKILL.md.
Value, cap, sourcing cost, reversals: ../claim-value/SKILL.md.
Inbound, AWD-to-FBA shortfalls and removals: ../shipment-claims/SKILL.md.
Returns and outbound losses: ../return-claims/SKILL.md.
Fees: ../fee-claims/SKILL.md.
How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.

## References

[paid-without-claim.md](references/paid-without-claim.md): automation by store, posts, UK contradiction, choices.
[windows-and-idr.md](references/windows-and-idr.md): the window, where it is read, the IDR portal.
[ledger.md](references/ledger.md): codes, Transaction Item ID, researching, netting, pitfalls.
[scope.md](references/scope.md): transfers, AWD, cross-border, MCF, Vine, exclusions.
