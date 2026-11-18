# Windows, one claim per charge, and the route

## The two FBA fee windows

- Itemised FBA fee errors are fees tied to an ASIN or FNSKU, typically from weight or dimension errors: fulfilment, customer returns, monthly storage and long-term storage; their window is counted from each charge's date (FE9, FE16).
- Non-itemised FBA fee errors, such as removal or destroy order fees and prep and labelling fees, fall under a separate, longer limit (FE9, FE41).
- Amazon staff stated both in a US-store guide of 2026-04-17 and in a UK-store copy of 2026-05-13; no length was read for JP, CA, AU, IN, MX or any other store (FE9).
- Today's lengths for the seller's store are on Seller Central's *FBA fees reimbursement policy: Weight and dimensions*, which cx cannot read and the seller sees signed in, and on the store's latest Amazon staff guide on disputing charges, read by plain GET (FE9).
- Whether the windows differ in JP, CA, AU, IN or MX, and whether the itemised window counts from the fee's `postedDate`, the ship date or the settlement date, is read in Amazon's documents, not yet seen on a live account (FE9).
- A charge's date is `postedDate` in Finances `listTransactions` (Finance and Accounting), or `posted-date` in settlement V2 (FE9).
- Finances data reaches further back than the itemised window, so by the research's reading an older overcharge is visible in the data but past the limit Amazon staff state (FE32).
- Monthly and long-term storage are disputable as itemised fees by the staff guide, and the policy text names the storage reports as the source of the dimensions used; a support agent's 2025 line that storage fees "can never be reimbursed" is kept as a seller's report (FE16).

## History

- A Chinese trade article dates the weight-and-dimension fee limit to about 2019-05, replacing a less strict one it does not state; that is 52by's report (FE10).
- The Australia News post that revised FBA inventory claim windows from 2025-10-15 does not cover fee claims (FE10).

## One claim per charge

- Amazon allows one claim per fee charge under the weight-and-dimension fee policy and under the referral-fee policy (FE11).
- The weight-and-dimension text, as a seller quotes it, adds that one request is enough for an FNSKU (FE11).

## Referral fees

- On 2022-03-16 Amazon removed the referral-fee dispute window and introduced fee category guidelines (FE22).
- A seller on the CA forum reports a phone agent citing an "Internal Policy" limit on referral reimbursement; it stands as a seller's report beside Amazon's News post (FE22).
- From 2023-01-13 a referral reimbursement is at the rate in force on the transaction date, disputes contrary to the guidelines then in force are declined, one claim is allowed per charge, and the policy does not apply to other fees (FE23).
- That policy was read in a UK-store staff post of 2024-05-24; no US-store text of it was read, and the policy as the store shows it is Seller Central's *Referral fees reimbursement policy*, which the seller sees signed in (FE23).
- The fee category Amazon assigned is not a column of the SP-API Fee Preview (FE24).

## The route

- Amazon's staff guide names Help > Contact Us > Shipping & FBA > FBA Issue > "Fees Charged in Error" for FBA fee errors, and Selling Partner Support with the Custom Unified Transaction report for referral fees (FE37).
- Opening the case, attaching evidence and answering it are the seller's steps in Seller Central; no SP-API operation files, answers or reopens a fee dispute (FE37, SU12).
- The Support API needs Selling Partner Support (Restricted), a role outside the five, so nothing here is built on it; it would open the status, dates, subject, contacts and attachments of the seller's cases (SU8).
- Case routes by kind, evidence formats and the conduct Amazon penalises: ../claim-filing/SKILL.md.
