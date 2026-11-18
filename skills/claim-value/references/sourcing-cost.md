# Manage Your Sourcing Cost

## What it holds

- MYSC holds one sourcing cost per FNSKU per marketplace, chosen on a marketplace dropdown (VR7).
- A US-store staff post of 2026-04-10 says the page lists active FNSKUs "with planned shipments or current inventory", and in the same post that new ASINs appear only once "fully received and processed"; the two sentences disagree, and both are Amazon's (VR7).
- In US-store staff posts and relayed replies (2026-02 to 2026-05), an approved cost applies automatically to eligible pre-order reimbursements issued after its approval date; it does not revalue earlier ones and is not re-submitted periodically (VR8).
- MYSC shows only the current value and its last update, by one seller thread; whether the cost in force at a past date can be read anywhere is read in Amazon's documents, not yet seen on a live account (VR32).
- MYSC is evidenced for the US, CA, UK, DE, FR, IT, ES and JP (VR16).
- Entering or updating a cost is the seller's step in Seller Central; no SP-API operation reads or writes MYSC, and no model holds a sourcing-cost field (VR18, SU12).

## Declines and limits

- Amazon may decline a cost for four policy reasons: an outlier, forged or illegible documents, an account suspected of fraud or violations, and a repeat within a stated period of a decision without new information (VR9).
- A declined submission leaves the previously approved amount or Amazon's estimate in force (VR9).
- The repeat period is on *FBA inventory reimbursement policy*, which the seller sees signed in, and in the dated redlines cx reads by plain GET (VR9, VR22).
- A US-store staff post (2025-11-25) says a value Amazon's system judges an outlier is rejected automatically, with no step to upload an invoice (VR10).
- US- and UK-store staff posts (2025-11-25, 2026-01-15) say Amazon does not tell the seller why an invoice was or was not accepted (VR10).
- The entered cost must equal the figure on the proof-of-value document; a mismatch is itself a decline reason (VR12).
- Amazon limits cost updates per FNSKU within a period: a Canada-store Seller Support reply relayed on 2025-03-19 and US-store staff posts of 2025-11-25 to 2026-02-24 state different counts, and no source read settles whether the count changed over time or differs by store (VR11).
- The count for a store is on the help page *Manage Your Sourcing Cost*, which the seller sees signed in, and a refusal shows in MYSC's Update status column as "Number of attempts exceeded"; which count holds today is read in Amazon's documents, not yet seen on a live account (VR11).
- Amazon states a maximum age for a proof-of-value invoice; two US-store staff posts (2025-06-12, 2025-12-01) state different ages, neither cites the help page, and which holds today is read in Amazon's documents, not yet seen on a live account (VR14).
- One seller reports a dated US case (2025-10-23) where a decline under the attempt lock outlasted the dispute window counted from the reimbursement; this is the seller's account (VR24).

## Proof of value

- The fields Amazon's help page lists, as a seller copied it from the Canada store (2025-03-19): document name, number and date; the buyer entity as registered with Amazon, its address and tax ID; the issuer's name, address and ID; product code, description and quantity; the per-unit or net cost; the currency (VR13).
- Accepted documents, by that copy: manufacturer, wholesaler, purchase or commercial invoices; staff also name retail receipts, and a pro forma with proof of payment; formats in that copy are PDF, JPG, JPEG and PNG (VR13).
- For self-manufactured goods, staff name an internal cost document showing product, unit cost and date, component invoices with a cost breakdown, and a Seller Support case for manual review (VR15).
- A practitioner, Eagle Eye (2026-09-12), reports a multi-product invoice refused because the FNSKU's line could not be isolated, and the same invoice accepted through a support case with the line highlighted (VR17).

## Chinese sellers' cost proofs

- Amazon's list asks for the buyer to be "your business name registered with Amazon" and for the currency of the transaction, and staff say the business name on the invoice "must exactly match your Amazon registration" (VR44).
- No Amazon text read states a required language, or rules on a mainland VAT invoice (发票), a 1688 order receipt or a payment-platform receipt; which of these Amazon accepts is read in Amazon's documents, not yet seen on a live account (VR44).
- An invoice whose buyer is a different entity from the selling account, such as a Hong Kong or mainland purchasing company buying for a US LLC, does not show the registered business as buyer; this is inferred from the field, not an Amazon ruling (VR44).
- Chinese practitioners (贾科斯 of 易销AI, 2025-08-07, Canada and Germany cases; AMZ123, 2024-12-27) report Chinese-language invoices refused and English ones accepted, and name these choices side by side, as theirs: a mainland VAT invoice (专票 or 普票) verifiable on the State Taxation Administration's check site; an English commercial invoice from the supplier in the store's currency with the supplier's tax number; a commercial or pro forma invoice from the supplier or forwarder; a contract with payment record and stamped receipt; customs papers, one of which a Canada-store case saw refused as unclear (VR45).

## Another cost Amazon holds

- Data Kiosk `analytics_economics_2024_03_15` carries a seller-entered `cost.costOfGoodsSold`, which Amazon says comes from SKU Central and the Revenue Calculator, not MYSC (VR19).
- Whether that cost and the MYSC cost are one value is read in Amazon's documents, not yet seen on a live account (VR19).
- Amazon's correction page and its developer support (2025-04-23) say the Economics dataset needs Selling Partner Insights, a role outside the five, while the Data Kiosk and operations pages still list Brand Analytics; that read would open the `cost.costOfGoodsSold` field (VR19, SU33).
