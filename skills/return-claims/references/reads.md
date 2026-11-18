# Reads: the FBA Returns report and the replacement link

## The FBA Returns report

- `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` lists only units received at a fulfilment centre; it is updated daily, can only be requested, is tab-delimited and answers to Pricing or Amazon Fulfillment (RT32, SU3).
- A refund given without a return is never in it (RT32).
- `return-date` is the date the returned unit was processed at the centre (the help page as the listing pack read it), not the refund date; the claim clock counts from the refund or replacement (RT33).
- Column names differ by source: the SP-API page has `order-id` and `license-plate-number`, the help page as the listing pack read it has `lpn`, and Openbridge, a data vendor, gives `amazon-order-id` and `lpn`; which of these a seller's file carries is read in Amazon's documents, not yet seen on a live account (RT34).
- Dispositions are written with a space on Amazon's help page as the listing pack read it (`CUSTOMER DAMAGED`) and with an underscore in a practitioner's copy (`CUSTOMER_DAMAGED`); read in Amazon's documents, not yet seen on a live account (RT35).
- Status values appear in sentence case, capitalised differently, in two copies of Amazon's page, and partly in UPPER_SNAKE in one ERP's filters (`IMMEDIATE_DISPOSAL`); read in Amazon's documents, not yet seen on a live account (RT35).
- `reason` is chosen by the buyer from a list; Amazon's codes and their descriptions are held by the listing pack (RT38).
- Amazon's SP-API pages state no look-back for the returns, replacements and reimbursements reports (SU16).
- No SP-API notification announces an FBA customer return's receipt or grading; `SHIPMENT_TRACKING_MILESTONE_CHANGED` carries `RETURN_RECEIVED`, a carrier-tracking milestone its schema does not tie to FBA customer returns (RT40).

## The replacement link

- `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA` covers only NA and IN stores and needs Amazon Fulfillment (RT20).
- Elsewhere the link from a replacement to its original is Orders v0 `IsReplacementOrder` / `ReplacedOrderId`, deprecated, or Orders v2026-01-01 `associatedOrders` with `REPLACEMENT_ORIGINAL_ID` (RT20, SU37).
- Whether the orders read shows every replacement outside NA and IN, customer-service replacements included, is read in Amazon's documents, not yet seen on a live account (RT20).

## The money side

- The Reimbursements report's columns and `reason` values: @comchatx/cx-amazon-finance-playbook, skill refunds-and-reimbursements.
- What a paid row says about its claim and its value: ../claim-value/SKILL.md.
- How a report is asked for and landed: the amazon-sp-api skill's references/door.md.
