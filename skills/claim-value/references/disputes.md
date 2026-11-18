# Disputing a value

## The window

- Amazon sets a window for disputing a reimbursement's valuation (VR20).
- Every policy text read (US, CA, UK, DE, FR, IT, ES, JP, and the US and CA Chinese texts) counts it from the reimbursement's issue (VR20).
- The one News post that states a re-evaluation window, d8f9a56c (posted 2025-08-14), was issued for the Australia store and counts it from the initial claim (VR20).
- The UK's text changed its length between the UK PDF of 2024-12-11 and the redline of 2025-02-24, and the redline does not mark the change (VR20).
- The length for a store is on *FBA inventory reimbursement policy*, which the seller sees signed in, and in that store's latest Seller Forums News post on claim windows, read by plain GET (VR20).
- Which window the self-service workflow enforces for a store, and whether any store besides Australia counts from the claim, is read in Amazon's documents, not yet seen on a live account (VR20).
- Which store a News post was issued for: ../warehouse-claims/SKILL.md.

## The routes

- Every route is the seller's step in Seller Central; no SP-API operation files a dispute (VR18, SU12).
- US-store staff name a self-service Get Help workflow, "Dispute a reimbursement claim": it applies an already approved MYSC cost to pre-order events reimbursed as "sellable", missing-from-inbound included (VR21).
- Staff also name a "reimbursement re-evaluation tool" at its own help-hub address; that it is the same workflow is inferred, not confirmed (VR21).
- US-store staff name "Submit a reimbursement claim dispute" under Get Help, where documents are uploaded for human review (VR21).
- A case reopening is a third path, which staff say is a different process (VR21).
- What each changes: the self-service route applies an approved cost to pre-order events reimbursed as "sellable"; the dispute under Get Help takes uploaded documents for human review; a case reopening is its own process; which route, and whether, is the seller's choice (VR21).
- The policy's repeat rule covers "reimbursement amount dispute[s]" as well as cost updates, with its period on the policy page (VR22).
- In one US-store thread (2026-05-25, 2026-06-05), a cost approved after a reimbursement was paid at the estimate was refused as a case adjustment "Since the reimbursement was processed before your sourcing cost was approved", and staff pointed to the self-service dispute within its window (VR23).
- One seller reports a dated US case where the cost-update lock outlasted the dispute window; this is the seller's account (VR24).

## Reading a dispute's outcome

- The Support API (`listCases`, `getCase`) needs Selling Partner Support (Restricted), outside the five; it would open the status, dates and contacts of the seller's cases, and nothing is built on it (SU8, SU10).
- Whether it shows valuation-dispute cases and their outcome is read in Amazon's documents, not yet seen on a live account (SU8).
- Where a case is filed and its evidence: ../claim-filing/SKILL.md.
