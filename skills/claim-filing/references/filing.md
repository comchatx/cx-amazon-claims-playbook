# Filing: entry points, evidence, limits and answers

## Conditions on every claim

- Amazon's policy makes following the process for the claim kind, and giving all requested information, a condition: "We may decline your claim if you do not"; the Supply Chain Portal policy says the same for its programme (FL2).
- A claim is open only for an item Amazon has not already reimbursed, and Amazon's US moderator in 2026 tells sellers to check the Reimbursements report before filing by hand (FL3).
- The account-status condition widened: the 2021-04 UK-path text asked for normal status when filing; the 2025-02-24 US text asks for it when a claim is filed, under review and during any appeals; the US moderator in 2026 excludes blocked, terminated or fraud-status accounts (FL13).
- Claims are ineligible while the account is not in normal status, and a deactivated account is reinstated through Account Health (FL34).
- No Amazon page read charges a fee to file a claim; the costs Amazon names are declined claims, conduct consequences and reversals (FL37).

## Entry points by kind

- Warehouse lost and warehouse damaged, and the IDR portal's rows: ../warehouse-claims/SKILL.md.
- Customer returns: ../return-claims/SKILL.md.
- Amazon locates the Transaction Item ID in the Inventory Ledger, and practitioners paste the ledger's `Reference ID` into the damaged-status tool (FC17).
- Amazon's 2026 staff instructions name an "Inventory Adjustments" report whose API type was removed on 2023-01-31, and Amazon does not state that the ledger's `Reference ID` is the Transaction Item ID; that the tool accepts it is read in Amazon's documents, not yet seen on a live account (FL6).
- The IDR portal, announced 2025-01-21 for the US store, covers warehouse lost, warehouse damage and customer returns, not missing from inbound, removals or warehouse disposals, and is reached from the FBA dashboard's Inventory menu or the Reimbursements report (FL5, FC13).
- Practitioners describe the IDR pages as Overview, Eligible for Claim, In Progress, Resolved and Defect Status Trend (FC15).
- No operation returns the IDR portal's lists or statuses; whether its rows match candidates rebuilt from the reports, and whether it exists outside the US, is read in Amazon's documents, not yet seen on a live account (FC14, FL5).
- Missing from inbound: Seller Central shows per shipment whether it is eligible for investigation and an estimated date it will be (IN11).
- Submitting an inbound research request through the Contents tab's Action required menu creates a Selling Partner Support case whose number shows on that tab (IN13, IN19).
- Amazon's Global Selling China article of 2025-08 advises submitting inbound research on the shipment's item page rather than to Seller Support (IN18).
- Removals: the "Resolve a removal order issue" tool, keyed by removal order ID (RM4).
- FBA fee errors, as Amazon's US and UK staff guides name them: Help > Contact Us > Shipping & FBA > FBA Issue > "Fees Charged in Error"; referral fees: Selling Partner Support with the Custom Unified Transaction report (FE37).
- A value dispute has two routes Amazon's staff name in US-store threads, the self-service "Dispute a reimbursement claim" and "Submit a reimbursement claim dispute" under Get Help, beside a case reopening (VR21).
- AWD: a seller quoted Amazon's AWD help on 2024-09-17 promising fair-value reimbursement on a case to Selling Partner Support when AWD finds fewer boxes than received (FC38).
- The Supply Chain Portal page is both the SCP policy for an active MCF account and the page the AWD terms link as the MCF inventory reimbursement policy; its claims and disputes go through the Supply Chain Portal's Contact Us (FL27).
- One ERP tells sellers to file each claim in the store where the event happened; no Amazon page read says so (FL40).
- Practitioners' menu paths and windows go stale: older Chinese and English guides cite paths and windows the 2024–2025 changes superseded (FL39).

## One claim, one issue

- Amazon's denial text in the Canada store (2022) and the SCP page allow one claim per inbound shipment and decline further claims for it; the US moderator in 2026 put it as one claim per shipment or event (FL7, IN17).
- Amazon allows one claim per fee charge under the weight-and-dimension and referral-fee policies (FE11).
- Amazon's support rule, as US staff gave it in 2025, is one issue per case, and no new case while one is open for the same issue (FL8).
- No Amazon page read states a maximum of items per case or of cases per day; volume enters only as conduct (FL9).
- Practitioners' per-case and per-day figures conflict across AMZ123, Jungle Scout China, SellerSpace and 看点资讯, and cite no Amazon page (FL10).

## Evidence

- Shipment-to-Amazon evidence is proof of ownership (itemised invoice, another seller's receipt or a packing slip, signed for a manufacturer) and proof of delivery: an Amazon-stamped delivery document for LTL or FTL, an active tracking ID per package for small parcel (FL24).
- Amazon accepts ownership documents only in a non-editable format (PDF, JPG, JPEG, PNG, TIFF), refuses pro forma invoices and contracts, and lets the seller hide the price paid (IN16).
- A removal claim asks for the removal order ID, shipment ID, ASINs or FNSKUs, quantities and images; the SCP page adds tracking or proof of delivery, the LPN and proof of cost (FL25).
- A fulfilment-centre claim names the date or location of the loss, the Transaction Item ID or FNSKU, and proof of ownership (FC18).
- A sourcing-cost document goes into Manage Your Sourcing Cost, not into a case (FL26).
- Amazon's US policy of 2025-02-24 lets Amazon decline a sourcing cost for documents "forged, tampered with, or illegible", or when the account is suspected of fraud or significant policy violations (FL14).
- What a value document must carry: ../claim-value/SKILL.md.

## Answers

- Sellers see a case as "Pending Amazon Action" or "Pending Merchant Action", and a reply from the seller hands it back to Amazon (FL28).
- Whether a case in "Pending Merchant Action" closes by itself after a set time is read in Amazon's documents, not yet seen on a live account (FL28, FL31).
- A seller can extend a case by replying that more time is needed (FL33).
- Sellers report cases auto-marked "Answered" with no reply (FL31).
- Among the pages read, Amazon states review or reply times only for inbound research, remeasurement and the seller's reply to an inbound information request, each on its own page; the SCP policy states its own timing for MCF order claims (FL30).
- By Amazon's US staff in 2025, Professional sellers can e-mail, request a call or chat with support; Individual-plan sellers can only e-mail (FL38).
- A paid manual claim appears in `GET_FBA_REIMBURSEMENTS_DATA` with its `case-id`, the API's only link from a case to money (FL29).

## Reopening

- Amazon tells sellers to reopen a closed case for questions rather than open a new one (FL32).
- After a "no further action" decision, Selling Partner Support says a seller is not to seek a different outcome by reopening the case or raising it in other cases, and that Amazon may close cases or limit support otherwise (FL12, FL32).
