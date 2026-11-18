# No door: what no SP-API operation can do in a claim

## What the models hold

- No operation among the 394 in Amazon's models files a claim, opens a case, attaches evidence or enters a sourcing cost (SU12).
- None updates, replies to or reopens an FBA reimbursement or support case, requests a remeasurement, disputes a fee or a reimbursement's value, or acts in the IDR pages (SU12).
- Each of these is done in Seller Central by the seller or a user the seller authorises (FL1).
- The models' one claim-creating operation, Shipping API v2 `createClaim`, files a carrier claim on one parcel by tracking ID, is not an FBA inventory reimbursement and is absent from the Role Mappings page (SU13).
- Amazon's agentic toolkit has no reimbursement or claims tool, and its `support-case-helper` sends the seller to the Seller Central Help Center when no such tool exists (SU14).

## The Support API

- The Support API v2025-02-01 (`listCases`, `getCase`, `listContacts`) needs Selling Partner Support (Restricted), outside the app's five roles; nothing is built on it (SU8).
- It launched on 2026-09-30 (SU9).
- Its three operations are reads: `listCases` takes a sort order, a page size and a token, no date, case type, reimbursement, ID or marketplace; a case carries no type, amount or reimbursement ID; attachments come by an expiring `downloadUrl` (SU10).
- Amazon's pages contradict each other on it: the roles page says the role can "retrieve, search, and manage support cases", the model has no search filter and no write, and a tutorial describes a contact `status` the model lacks (SU11).
- Its model takes no marketplace parameter and states no history reach for `listCases`; how far back a seller's cases are listed is read in Amazon's documents, not yet seen on a live account (SU56).

## The seller's steps in Seller Central

- Open a case or claim: by kind, references/filing.md.
- Request inbound research: the shipment's Contents tab Action required menu, which creates a Selling Partner Support case (IN13, IN19).
- Attach evidence: uploaded in the case or tool, in a non-editable format (IN16, FL24).
- Read an answer, reply or reopen: in the case in Seller Central, where a seller's reply hands it back to Amazon and a closed case is reopened for questions (FL28, FL32).
- Enter or update a sourcing cost: Manage Your Sourcing Cost, one cost per FNSKU per marketplace (VR7, FL26).
- Dispute a reimbursement's value: the Get Help "Dispute a reimbursement claim" workflow or "Submit a reimbursement claim dispute" (VR21).
- Request a remeasure: Seller Central's remeasure request, with conditions Amazon states (FE4).
- Dispute an FBA fee: Help > Contact Us, "Fees Charged in Error" (FE37).
- File a removal claim: "Resolve a removal order issue", by removal order ID (RM4).
- Use the IDR portal: the seller's step, from the FBA dashboard's Inventory menu or the Reimbursements report in Seller Central (FL5).
- No operation returns the IDR portal's lists, statuses or resolution reasons (FC14).
- Request the Deferred Transaction Report the first time: the Payments Reports Repository (SU30).
- Download the Payments Date Range Report: Seller Central only, no report type (SU29).
- File an MCF order claim on a Supply Chain Portal account: the Supply Chain Portal's Contact Us (FL27).
