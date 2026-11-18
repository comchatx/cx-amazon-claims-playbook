---
name: fee-claims
description: "Whether an Amazon fee a seller was charged had a basis in Amazon's own rule, and what Amazon says about getting it back: FBA fulfilment, storage, returns and placement fees on a wrong measurement or size tier, Amazon's measurement against the seller's, remeasurement, the EU dimensions certification regime and its look-back, the itemised and non-itemised fee-error windows by store, one claim per charge, a referral fee on the wrong category, low-price FBA not applied, placement fees against the quote, partnered-carrier charges, the low-inventory-level fee, storage on lost, researching or stranded units, removal and disposal fees with no unit, unplanned prep, the inbound defect fee, AWD box fees, and what the Fee Preview, Storage Fees and Inbound Performance reports show. For any question about a fee that looks too high, a size tier that changed, a remeasure, or whether an overcharge can still be disputed in the seller's store."
---

## What counts

In this skill an overcharge is a fee charged on a basis Amazon's own rule did not support; a rise from an announced rate change, peak, surcharge or price band is not one (FE1, FE20).
Rates, fee lines and where each charge posts: @comchatx/cx-amazon-finance-playbook, its fees-and-charges skill.

## Measurement

Outside EU certification, the measurement Amazon verifies sets every size-tier fee (FE2).
Each variation is its own product (FE3).
The SP-API Fee Preview keeps no history, and Velocity Sellers holds that Amazon sends no notice of a remeasure (FE19).
On Amazon.de and, from 2026-05-05, amazon.co.uk, .fr, .it and .es, certified seller dimensions set the fee; Amazon states an automatic look-back true-up for Amazon.de, and no Amazon page read states one for the US (FE5, FE6, FE7).
After a US remeasure, staff described past fees credited per order (2025-02-05); US sellers report refusals after a confirmed wrong measurement (FE13, FE14).

## Windows

Amazon staff state a window from each charge's date for itemised FBA fee errors and a longer limit for non-itemised ones (US-store guide 2026-04-17, UK-store copy 2026-05-13); lengths: *FBA fees reimbursement policy: Weight and dimensions*, seen signed in, and the store's latest staff guide, read by plain GET (FE9).
Amazon allows one claim per fee charge under the weight-and-dimension and referral-fee policies; Amazon removed the referral-fee dispute window on 2022-03-16 (FE11, FE22).

## The seller's steps

No SP-API operation requests a remeasurement, certifies dimensions or disputes a fee; each is the seller's step in Seller Central, an FBA fee error by the staff guide's "Fees Charged in Error" case (FE4, FE6, FE37, SU12).

## Reads

Amazon's measurement on file is in `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` and `GET_FBA_STORAGE_FEE_CHARGES_DATA` (Pricing or Amazon Fulfillment); a charge's date is `postedDate` in Finances `listTransactions` (Finance and Accounting) (FE17, FE9).
Data Kiosk `economics` would date a tier change but needs Selling Partner Insights, outside the five roles (FE18, FE50).
How calls and reports are made: the amazon-sp-api skill's references/door.md.

## References

[measurement.md](references/measurement.md): measurement, remeasurement.
[certification.md](references/certification.md): EU certification.
[windows.md](references/windows.md): windows, referral fees, the route.
[fee-kinds.md](references/fee-kinds.md): low-price, placement, carrier, low-inventory, storage, removal, returns, prep, defect, AWD fees.
[reads.md](references/reads.md): reports, pitfalls, detection methods.
[claim-filing](../claim-filing/SKILL.md): case routes, evidence, conduct.
[claim-value](../claim-value/SKILL.md): what a reimbursement is worth.
[warehouse-claims](../warehouse-claims/SKILL.md), [shipment-claims](../shipment-claims/SKILL.md), [return-claims](../return-claims/SKILL.md): the units themselves.
