# Reads: every claims read with its role, lag and look-back

## Roles

- A role grants operations, reports, feeds and notifications, and a read is allowed when the application holds at least one role Amazon names for it on *Role Mappings for SP-API Operations* and *Role Mappings for SP-API Types* (SU1).
- *Role Mappings for Types* still lists types the deprecation schedule removed, so a type's presence there does not show that it answers (SU40).
- Restricted roles require the developer to give additional information about data use and security controls (SU46).

## Reports inside the five

- The ledger detail and summary, the replacements report, inventory planning, overage fees and customer shipment sales name Amazon Fulfillment as their only role (SU2).
- `GET_FBA_REIMBURSEMENTS_DATA`, the FBA customer returns report, both removal reports, inbound noncompliance, the fee preview and both storage fee reports answer to Pricing or Amazon Fulfillment; `GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL` also to Inventory and Order Tracking (SU3).
- The Reimbursements report carries `currency-unit` and no store or marketplace column, while the ledger detail carries `Country` and `Store` (SU52).
- A developer reports that `GET_FBA_REIMBURSEMENTS_DATA` returns the same rows whatever `marketplaceIds` names; whether it still does is read in Amazon's documents, not yet seen on a live account (SU24).
- The Seller Fulfilled Prime returns reports name Pricing among their roles, cover Seller Fulfilled Prime returns only and carry the `SafeT-…` columns and `Refunded-Amount` (SU48).
- The stranded and reserved inventory reports name Pricing or Amazon Fulfillment, are request-only and updated in near real time; the stranded report carries `date-stranded`, `stranded-reason` and `Date-to-take-auto-removal` (SU59).
- The removal shipment detail excludes cancelled returns and disposed items, and a developer reports that its "Return" rows carry no destination address (SU26).
- The Deferred Transaction Report (`GET_DATE_RANGE_FINANCIAL_HOLDS_DATA`, Finance and Accounting) must first be requested in Seller Central's Payments Reports Repository before the API can fetch it (SU30).
- No report type carries Seller Central's Payments Date Range Report; dimension-fee refunds that tools read there as `Fee Adjustment` are reached through Finances or the settlement report (SU29).
- Settlement reports are scheduled by Amazon and cannot be requested, and the Reports API keeps a report for a maximum stated in the Reports model (SU53).
- No report type read carries liquidation proceeds per removal order; they post as Finances v0 `FBALiquidationEventList` (SU58).

## Operations inside the five

- Fulfillment Inbound v0 `getShipments`, `getShipmentItems`, `getShipmentItemsByShipmentId` and every v2024-03-20 operation name Amazon Fulfillment only (SU4).
- The other inbound reads the claim files use (`listTransportationOptions`, `listPlacementOptions`, `listShipmentPallets`, `listPrepDetails`, `listInboundPlanItems`, `getInboundPlan`, `getBillOfLading`, `getLabels`) and `getItemEligibilityPreview` name Amazon Fulfillment only (SU50).
- v2024-03-20 shipment items carry no received quantity; received units per SKU per shipment through the API are v0 `QuantityReceived` (SU32).
- MCF reads (`getFulfillmentOrder`, `listAllFulfillmentOrders`, `getPackageTrackingDetails`) name Amazon Fulfillment and carry `UNDELIVERABLE`, "Shipment damaged", "Lost by carrier", `CarrierDamaged` and `FulfillerDamaged`; no operation files an MCF claim (SU51).
- Finances v0 `listFinancialEvents` names Finance and Accounting, Amazon Fulfillment (NA and FE only) and AISP (EU only); `…ByOrderId` names Finance and Accounting only (SU5).
- Catalog Items `includedData=dimensions` needs Product Listing and gives catalogue dimensions; Amazon's measured dimensions for fees are in the fee preview and storage fee reports (SU6).
- Product Fees `getMyFeesEstimateForSKU` and `…ForASIN` accept any of twelve roles, `getMyFeesEstimates` Pricing or Product Listing, and each returns an estimate for a price, not a fee charged (SU7).
- Data Kiosk Sales and Traffic counts A-to-z Guarantee and chargeback claims; none of its metrics counts an FBA reimbursement claim (SU57).
- Data Kiosk Seller Analytics counts returned units by ship date with a return-data delay stated in its schema, on Brand Analytics by the operations page; whether a query is accepted on Brand Analytics alone is read in Amazon's documents, not yet seen on a live account (SU54).

## Notifications

- No notification type announces a reimbursement, a ledger adjustment, an inbound receipt or discrepancy, or a support-case change (SU31).
- `TRANSACTION_UPDATE` fires on any new transaction and is not on *Role Mappings for Types*; whether it subscribes on the app's roles is read in Amazon's documents, not yet seen on a live account (SU31).

## Lag

- Amazon generates a near-real-time FBA report no more than once every 30 minutes and a daily one no more than once every four hours, as the opening of *FBA Reports* states (read 2026-11-23); practitioners report it counts per seller and report type across applications (SU19).
- After a report is generated, Amazon generates no updated version of it until that waiting period passes, so within it a report already made holds the newest content Amazon has; `getReports` with `reportTypes` lists the reports already made, and the page does not say what a new request returns within the period (SU61).
- On *FBA Reports* the reimbursements, FBA returns and replacements entries read "Content updated daily", the two removal entries "Content updated in near real-time", and the ledger detail's entry states neither (read 2026-11-23) (SU61).
- The fee preview's refresh interval, `dataStartTime` offset and per-seller request limit are on its *FBA Reports* entry (SU20).
- The Amazon-fulfilled shipments report's span per request, request cap (Seller Central requests count) and delay after shipping are on its *FBA Reports* entry (SU21).
- The long-term storage fee report's required span is on its *FBA Reports* entry (SU22).
- The removal shipment detail has returned different row counts for the same dates asked at different times, and Amazon Developer Services gave no guaranteed time for updates (SU25).
- An Amazon staff reply on a developer issue (2026-07-31) says Seller Central shows a ledger request's range in the store's local time, daylight saving included (SU28).
- A developer reports (2025-04-21) that the API refuses the ledger detail example `"eventType":""` Amazon's page still shows; that leaving `eventType` out returns all events is inferred from the page's stated default (SU27).

## Look-back

- The ledger detail's look-back is stated in its description on *FBA Reports*, the only claims report whose look-back Amazon's SP-API pages state (SU15).
- No look-back is stated for the reimbursements, FBA returns, replacements and removal reports; an Amazon developer-support engineer said the Seller Central reports team keeps them; how far each answers is read in Amazon's documents, not yet seen on a live account (SU16).
- Amazon's help pages for the Reimbursements report, customer returns and the reimbursement policy serve a script shell to a plain GET, so their look-back text is unread (SU45).
- A data vendor's connector sets its own look-back and latency per report, read on the vendor's page (SU17).
- A report's look-back and a claim's window are different facts: a report reaching further back does not make an older event claimable (SU18).
- Some FBA reports are offered in some stores only, stated in each report's store-availability line on *FBA Reports* (SU23).
- Data Kiosk's earliest `startDate` and result retention are in each dataset's schema (SU34).

## Reads outside the five, and what each would open

- Nothing is built on any of these; each names its role and what it would open (SU8, SU33, SU49).
- The Support API (`listCases`, `getCase`, `listContacts`), on Selling Partner Support (Restricted), would open the seller's cases, their status, dates, subject, contacts and attachments (SU8).
- A developer asked Amazon in 2026-10 how to add Selling Partner Support (Restricted) to an approved application apart from its other roles; no Amazon answer was posted (SU60).
- Data Kiosk Economics needs Selling Partner Insights, by Amazon's correction page and developer support, while the Data Kiosk and operations pages still list Brand Analytics; it would open charged fees per MSKU and period (SU33).
- Economics gained removal, disposal, deal, coupon and fuel fees on 2026-09-30 and lost FNSKU granularity on 2025-12-22, and its schema points to unread help pages for its fee types (SU35, SU55).
- `GET_V2_SELLER_PERFORMANCE_REPORT`, on Selling Partner Insights only and request-only, would open `accountStatuses` per marketplace and Account Health metrics (SU49).
- `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE`, on Inventory and Order Tracking or Direct to Consumer Shipping (Restricted), would open seller-fulfilled returns with the SAFE-T columns, `Order Amount` and `Refunded Amount`; its span per request is on *Returns Reports* (SU47).
- Whether the app can be given Selling Partner Insights or Selling Partner Support (Restricted) is read in Amazon's documents, not yet seen on a live account (SU46, SU60).

## Deprecations

- Finances v0 `listFinancialEvents`, `…ByGroupId` and `…ByOrderId` were deprecated on 2025-07-21; their removal date is the one on the *SP-API Deprecation Schedule* (SU36).
- Orders v0 was deprecated on 2026-01-28, with Orders v2026-01-01 (`searchOrders`, `getOrder`) as successor on the same roles; its removal date is on the schedule (SU37).
- The old settlement flat-file and XML reports were removed on 2026-11-11 (SU38).
- The schedule and a release note give different removal dates for `analytics_salesAndTraffic_2023_11_15` (SU39).
- The six inventory adjustment, receipt and reconciliation report types older claims guides name were removed on 2023-01-31 (SU42).
- No release note or deprecation from 2025-01 to 2026-11-04 adds, changes or removes an FBA claims report type, the ledger or the reimbursements report (SU41).
- How a call is made and a report is asked for and landed: the amazon-sp-api skill's references/door.md.
