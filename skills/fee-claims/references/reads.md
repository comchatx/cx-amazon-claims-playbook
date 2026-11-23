# Reads, their pitfalls, and detection methods

## The measurement Amazon used

- `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` carries Amazon's dimensions and weight per SKU, `product-size-tier` in the US only and `product-size-weight-band` in the EU; it is a current snapshot (FE17).
- Its entry on *FBA Reports* states that it is refreshed at least once every 72 hours, is asked with `dataStartTime` at least 72 hours before now and `dataEndTime` now, and can be requested once per day per seller (read 2026-11-23) (SU20).
- `GET_FBA_STORAGE_FEE_CHARGES_DATA` carries dimensions, weight, `item_volume` and `product_size_tier` per FNSKU, FC and `month_of_charge`; both reports answer to Pricing or Amazon Fulfillment (FE17).
- Amazon keeps no history in the Fee Preview, and Velocity Sellers holds that Amazon sends no notice of a remeasure; so on the five roles a tier change is dated only by comparing dated copies of the report the reader kept (FE19).
- `getMyFeesEstimateForSKU` uses Amazon's measured dimensions once units are received and `getMyFeesEstimateForASIN` the catalogue size; the research reads a different fulfilment fee between them at one price as a sign the two differ (FE21).
- The SP-API Fee Preview has `product-group` and `estimated-referral-fee-per-unit` but no fee-category column, though Amazon's 2022 post says Seller Central's Fee Preview shows upcoming category changes (FE24).
- Whether the assigned fee category can be read through any SP-API surface is read in Amazon's documents, not yet seen on a live account (FE24).

## Pitfalls in the money

- A fulfilment fee rises without any measurement change across the holiday peak, the fuel and logistics surcharge, a price-band crossing and an annual fee change (FE20).
- The dates of Amazon's fee changes and peak periods: @comchatx/cx-amazon-finance-playbook, its fees-and-charges skill.
- Fee corrections reach the seller's records under names Amazon does not list (`Fee Adjustment`, `INCORRECT_FEES_ITEMS`, `INCORRECT_FEES_NON_ITEMIZED`, `NonSubscriptionFeeAdj`, `RE_EVALUATION`), as vendors report them (FE33).
- Whether the two `INCORRECT_FEES_*` names match Amazon's itemised and non-itemised classes, and where they appear, is read in Amazon's documents, not yet seen on a live account (FE33).
- Finances reaches further back than the itemised window (FE32).

## Outside the five roles

- Data Kiosk `economics` returns charged fees per product per date range with the properties that set them, Product Size Tier among them, split at Amazon fee-change dates; it would date a tier change (FE18).
- It needs Selling Partner Insights, a role outside the five, so nothing here is built on it; its start-date limit and retention are in the dataset's schema (FE50, SU33, SU34).
- On the five roles the same questions are read from dated Fee Preview copies, the Storage Fees report, Finances and the Inbound Performance and Reimbursements reports (FE50).

## Practitioners' detection methods, side by side

| Choice | Expected fee from | Charged fee from | Flagged when | Whose (FE34) |
|---|---|---|---|---|
| Order-level difference, seller-kept expected fee | Amazon's estimate or the seller's own carton figures under the store's rates | the order's fee | any difference, valued as (charged − expected) × quantity | 领星 Lingxing (FE34, SU44) |
| Order-level difference against Amazon's estimate | the fee report's estimate | the order's fee | a difference above the vendor's own default, on recently shipped orders | 赛狐 Sellfox (FE34) |
| Baseline and diff | a dated earlier Fee Preview copy | the current copy | the fee moved with no price change | Velocity Sellers; My Amazon Guy; Notifcentral (FE34) |
| SKU estimate against ASIN estimate | `getMyFeesEstimateForASIN` | `getMyFeesEstimateForSKU` | the two differ at one price | the research's reading of Amazon's documentation (FE34, FE21) |

- Each method is its vendor's or practitioner's; none is Amazon's (FE34).
- Reported effects are single cases only, with no study of how often or how large overcharges are (FE35).
