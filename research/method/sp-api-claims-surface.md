# The SP-API surface of a claims audit: reads, roles, lag, look-back, and the steps with no door

Seat: sp-api-claims-surface, brief 548. Date read for every page: 2026-11-13. Tags: [read in official docs], [command-verified], [opinion], [inferred], seat's own. Routes used: plain GET of developer-docs.amazon.com pages and their `.md` twins, GitHub (web and `gh api`), and third-party sites; the SP-API models by grep of a local clone at commit db2936aa (2026-10-29), with main b13d1d10 (2026-11-11) read on GitHub. No POST to an Amazon host, no help-hub content call, no SP-API host, no sign-in, no seller data.

This file is the pack's home for: the roles of every read the claims files lean on (with retention, look-back and lag), the Support API's shape, and the statement that no SP-API operation files a claim, opens a case, attaches evidence or enters a sourcing cost (SU12). The other files point here for these and do not restate them.

**Summary.** Every read a claims audit needs (ledger, reimbursements, FBA returns, replacements, removal order and shipment detail, fee preview, storage fees, stranded and reserved stock, inbound performance, inbound shipment items and their transport, placement and prep reads, MCF order reads, Finances, Orders, catalogue dimensions, fee estimates) is reachable through the five roles in the seller's app. Eight of the claims report types in §2.1 answer to Pricing or Amazon Fulfillment (a ninth, Amazon-fulfilled shipments, also to Inventory and Order Tracking), and the ledger, replacements, planning, overage and customer-shipment-sales reports answer to Amazon Fulfillment alone. Four reads the other files lean on are **outside** the five: the seller-fulfilled returns report by return date (Inventory and Order Tracking or Direct to Consumer Shipping (Restricted)), the Seller Performance Report (Selling Partner Insights only), Data Kiosk's Economics dataset (Selling Partner Insights per Amazon's correction, confirmed by Amazon developer support in 2025), and the Support API (Selling Partner Support (Restricted)). The Seller Fulfilled Prime returns reports, which carry the same SAFE-T columns for Prime orders, answer to Pricing. No SP-API operation opens, files, answers or attaches evidence to an FBA reimbursement case. None enters a sourcing cost, requests a remeasurement or acts in the lost-and-damaged (IDR) pages. The one case read, the Support API (live since 2026-09-30), is read-only. Amazon's own agentic toolkit and its Claude connector have no claims or case tool. Amazon states almost no look-back for the claim reports; the 18-month figures come from the ledger page and from practitioners. Values that differ by store or date sit in *Values that move*.

What this file adds past the other packs: the role of every claims read in one place, including the ones the finance and stock packs do not name (inbound performance, Amazon-fulfilled shipments, fee preview, storage, overage, catalogue dimensions, fee estimates). It adds the reads' lag and look-back with who says each, the deprecations that touch a claims audit, the list of claim steps with no door and the hand route for each, the Support API's exact shape, the Shipping API's `createClaim` (which is not FBA), the state of Amazon's toolkit and connector, and Amazon developer-support statements on report constraints. Facts already held elsewhere are cited by their position IDs and not restated.

---

## 1. The roles: how Amazon maps a read to a role

**(a) Amazon's rule.**

- *Role Mappings for SP-API Operations*, https://developer-docs.amazon.com/sp-api/docs/role-mappings (the `.md` form at developer-docs.amazon), `updatedAt` 2026-10-28, read 2026-11-13: "Roles control access to all API operations, reports, feeds, and notifications in the Selling Partner API (SP-API)." Each operation lists "Required roles (need at least one)".
- *Role Mappings for SP-API Types*, …/docs/role-mappings-for-types, `updatedAt` 2026-09-09, read 2026-11-13: the same, for report, feed and notification types.
- *Roles in the Selling Partner API*, …/docs/roles-in-the-selling-partner-api, `updatedAt` 2026-11-12, read 2026-11-13. It describes the roles as follows:
  - Amazon Fulfillment: "access to Amazon fulfillment operations and shipping services such as Fulfillment by Amazon (FBA)… You generally use this role for FBA sales reports, order tracking reports, and operations related to order fulfillment."
  - Finance and Accounting: "access to operations that create accounting and financial statements."
  - Pricing: "pricing-related reports, feeds, and operations."
  - Selling Partner Support (Restricted): "grants approved applications access to a selling partner's Amazon support case data. Use this role to retrieve, search, and manage support cases outside of Seller Central."
  - On restricted roles generally: "*Restricted* means that the role requires sensitive information, which might include personally identifiable information (PII). For these roles, you must provide additional information about your data use and security controls."
- That a role added to the application reaches a store only after the store authorises again is the door's fact (the door, "The seller's application"); it is not repeated here.

**Verification.** The two role-mapping pages fetched today are byte-identical to the survey's copies of 2026-11-09. Re-parsing the operations page today gives the same 350 rows as the survey's roles table [command-verified].

**(b) Practitioners.** Amazon Developer Support (CrionaAm, selling-partner-api-models issue #2974, 2022-07-15) wrote: "Most of the report variables and constraints are managed by in house Engineers who cover the Seller Central reports system, rather than SP-API… more comprehensive information about report constraints tends to be available within the report descriptions in seller central." [opinion; an Amazon support engineer on GitHub, not a policy page]

**(c) Into a skill:** the role of each read, from the table in §2, with the page date. **Read at run time:** whether a read answers on the seller's connection. A `403` on a path is Amazon's refusal for a role the application lacks (the door). The pages' dates are re-read when a role question arises.

---

## 2. The reads of a claims audit, with their roles

Abbreviations follow Amazon's role names: AF Amazon Fulfillment, FA Finance and Accounting, PR Pricing, PL Product Listing, BA Brand Analytics, SPI Selling Partner Insights, IOT Inventory and Order Tracking, D2C(R) Direct-to-Consumer Shipping (Restricted), SPS(R) Selling Partner Support (Restricted), TI(R) Tax Invoicing (Restricted), AISP Account Information Service Provider. "In app" means at least one named role is among the five (PL, PR, BA, FA, AF).

Sources: the two Role Mappings pages (2026-10-28 operations, 2026-09-09 types); *FBA Reports* (…/docs/report-type-values-fba, `updatedAt` 2026-10-13); *Payment Reports* (…/report-type-values-payment, 2026-09-09); *Settlement Reports* (2026-10-14); *Support API* (2026-09-30); *Data Kiosk API* (2026-10-20); and the models at commit db2936aa (2026-10-29). All were read 2026-11-13 [read in official docs; roles command-verified by grep of the fetched pages].

### 2.1 Report types (Reports API v2021-06-30)

| Report type (page heading) | What it gives a claim | Roles Amazon names | In app | Requested / scheduled; freshness Amazon states | Owner of the detail |
|---|---|---|---|---|---|
| `GET_LEDGER_DETAIL_VIEW_DATA` (Inventory Ledger – Detailed View) | Each lost, damaged, found, disposed, received, returned, removed movement, with `Reference ID`, `Reason`, `Reconciled Quantity`, `Unreconciled Quantity` | AF | yes | Requested only. "You can view all historical movements of your inventory for 18 months in this report." | Stock pack W26–W32, P-stock-states-30 |
| `GET_LEDGER_SUMMARY_VIEW_DATA` (Summary View) | Lost / Found / Damaged / Disposed / Unknown per FNSKU, disposition, country or FC, per month, week or day | AF | yes | Requested only | Stock pack W26, W29 |
| `GET_FBA_REIMBURSEMENTS_DATA` (FBA Reimbursements Report) | What Amazon paid: `approval-date`, `reimbursement-id`, `case-id`, `amazon-order-id`, `reason`, `amount-per-unit`, `amount-total`, cash/inventory quantities, `original-reimbursement-id`/`-type` | PR, AF | yes | Requested only. "Content updated daily." | Finance pack P-ref-17–20, P-ref-35 |
| `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` (FBA Returns Report) | Returns received at an FC: `return-date`, `order-id`, `fnsku`, `quantity`, `detailed-disposition`, `reason`, `status`, `license-plate-number` | PR, AF | yes | Requested only. "Content updated daily." | Finance pack table § API; customer-returns area |
| `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA` (FBA Replacements Report) | Replacement orders with `original-amazon-order-id`, `replacement-reason-code` (the replaced unit's return is a claim line) | AF | yes | Requested only; daily; "NA and Amazon IN stores" | Finance pack table § API |
| `GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA` | Requested / cancelled / disposed / shipped / in-process quantity per removal order, `removal-fee` | PR, AF | yes | Requested only. "Content updated in near real-time." | removals-disposals area |
| `GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA` | Shipped removal units with `carrier`, `tracking-number`, `shipment-date`; "will not include canceled returns or disposed items" | PR, AF | yes | Requested only; near real-time | removals-disposals area |
| `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA` (FBA Inbound Performance Report) | `fba-shipment-id`, `fba-carton-id`, `problem-type`, `expected-quantity`, `received-quantity`, `fee-type`, `fee-total` | PR, AF | yes | Requested only; daily | Stock pack I14 |
| `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` (FBA Fee Preview Report) | Amazon's dimensions and weight on file (`longest-side`, `median-side`, `shortest-side`, `item-package-weight`), size tier (US), estimated fees per unit | PR, AF | yes | Requested only. "updated at least once every 72 hours… specify the `dataStartTime` parameter for a minimum 72 hours prior to NOW and `dataEndTime` to NOW." "This report can only be requested once per day per seller." | fee-overcharges area; finance pack fulfilment-charges |
| `GET_FBA_STORAGE_FEE_CHARGES_DATA` (FBA Storage Fees Report) | Per ASIN/FNSKU/FC: dimensions, `product_size_tier`, `average_quantity_on_hand`, `storage_rate`, `estimated_monthly_storage_fee`, `month_of_charge` | PR, AF | yes | "can be requested or scheduled" | Stock pack holding-costs |
| `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` | `qty-charged`, `amount-charged`, `surcharge-age-tier` | PR, AF | yes | Requested only; the span between `dataStartTime` and `dataEndTime` "should be equal to one month" | Stock pack holding-costs |
| `GET_FBA_OVERAGE_FEE_CHARGES_DATA` | Overage volume and `charged_fee_amount` | AF | yes | Requested only | Stock pack holding-costs |
| `GET_FBA_INVENTORY_PLANNING_DATA` | Inbound working, shipped and received quantities; aged stock | AF | yes | Requested only; no frequency stated | Stock pack W23, W24 |
| `GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL` | Order, shipment, FC, carrier and tracking per shipped item (the sale behind a return or a post-order loss) | PR, AF, IOT | yes | "You can request up to one month of data in a single report." "Amazon accepts a maximum of 12 requests for this report every 8 hours, per selling partner account", counting Seller Central requests too. Delay "approximately one to three hours… In some rare cases… up to 24 hours." | this file |
| `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA` | FBA units shipped per order | AF | yes | Requested only | this file |
| `GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL` / `…_BY_LAST_UPDATE_GENERAL` | Orders with item price (sale price for post-order valuation) | AF, D2C(R), IOT, PR (+PL on last-update) | yes | — | this file |
| `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` | Reimbursement, reversal and fee-adjustment lines as posted | FA | yes | Amazon schedules it; found by `getReports` only (the door) | Finance pack P-ref-33 |
| `GET_DATE_RANGE_FINANCIAL_HOLDS_DATA` (Deferred Transaction Report) | Deferred transactions | FA | yes | "You must request the Deferred Transaction Report through the Payments Reports Repository on Seller Central before you can use the Reports… API to retrieve" it. | Finance pack |
| `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE` (Flat File Returns Report by Return Date; *Returns Reports*, 2026-10-28) | Seller-fulfilled returns only (the page: not FBA returns, not returnless refunds): `Order Amount`, `Refunded Amount`, `Return delivery date`, `A-to-Z Claim`, five `SafeT …` columns, `Order Item ID` | IOT, D2C(R) | **no** | "can be requested or scheduled"; a per-request span stated on the page (*Values that move*) | customer-returns RT39; finance P-ref-11, P-rec-55 |
| `GET_CSV_MFN_PRIME_RETURNS_REPORT` / `GET_XML_MFN_PRIME_RETURNS_REPORT` (Prime Returns Report by Return Date) | Seller Fulfilled Prime returns only; the CSV carries the same `SafeT-…` columns and `Refunded-Amount` | IOT, PR, D2C(R) | yes (PR) | "can be requested or scheduled"; per-request span as above | finance refunds table § API |
| `GET_V2_SELLER_PERFORMANCE_REPORT` (*Performance Reports*, 2026-10-28) | `accountStatuses` per marketplace and the Account Health metrics (filing-and-conduct reads the status) | SPI | **no** | "can only be requested" | filing-and-conduct § conduct |
| `GET_STRANDED_INVENTORY_UI_DATA` (FBA Stranded Inventory Report) | `date-stranded`, `stranded-reason`, `Date-to-take-auto-removal`, fulfillable and unfulfillable quantities (storage charged on stranded units; stranded removals) | PR, AF | yes | Requested only; "Content updated in near real-time" | stock pack `stuck-stock/references/stranded.md` |
| `GET_RESERVED_INVENTORY_DATA` (FBA Reserved Inventory Report) | `reserved_qty`, `reserved_customerorders`, `reserved_fc-processing` (the page lists no FC-transfer column) | PR, AF | yes | Requested only; near real-time | stock pack |
| `GET_AMAZON_FULFILLED_SHIPMENTS_DATA_INVOICING` | EU tax invoicing variant | TI(R) | **no** | restricted (RDT) | not needed for claims |

**No SP-API report type exists for** the Seller Central Payments "Date Range Report" (transaction view). `GET_DATE_RANGE_FINANCIAL_TRANSACTION_DATA` is not on the Role Mappings for Types page or on the Payment Reports page [command-verified: grep of both pages, 0 hits]. The same Date Range Report is where Lingxing tells sellers to find `Fee Adjustment` rows for dimension refunds (§7). Through the API, those rows are reached by Finances or by the settlement report.

**Reports that no longer exist.** The six inventory adjustment, receipt and reconciliation reports that older claims guides name (`GET_FBA_FULFILLMENT_INVENTORY_ADJUSTMENTS_DATA` and the rest) were removed on 2023-01-31. The stock pack holds this (W25, P-stock-states-27), and a guide that still names them is out of date.

### 2.2 Operations

| Operation | What it gives a claim | Roles Amazon names | In app | Notes |
|---|---|---|---|---|
| Fulfillment Inbound v0 `getShipments`, `getShipmentItems`, `getShipmentItemsByShipmentId` | `QuantityShipped` beside `QuantityReceived` per SKU per shipment; `ShipmentStatus` incl. `CLOSED`, `CHECKED_IN`, `DELIVERED` | AF | yes | Not deprecated (stock pack A3, P-inbound-2) |
| Fulfillment Inbound v2024-03-20 `listInboundPlans`, `getShipment`, `listShipmentItems`, `listShipmentBoxes` | Plan, shipment and box contents; shipment status (`CLOSED`, `RECEIVING`, `DELIVERED`, …) | AF | yes | Its `Item` has `quantity` only, with no received quantity [command-verified: no `receiv…` quantity field in `fulfillmentInbound_2024-03-20.json`] |
| Fulfillment Inbound v2024-03-20 `listTransportationOptions`, `listPlacementOptions`, `listShipmentPallets`, `listPrepDetails`, `listInboundPlanItems`, `getInboundPlan` | Partnered or own carrier (`shippingSolution`, `shippingMode`); the placement fee quoted; pallets; prep and label owner | AF | yes | inbound-shortfalls § transport and labels; fee-overcharges § placement |
| Fulfillment Inbound v0 `getBillOfLading`, `getLabels` | Partnered LTL bill of lading; box labels | AF | yes | inbound-shortfalls |
| FBA Inbound Eligibility v1 `getItemEligibilityPreview` | Whether an ASIN may ship under a program (e.g. `COMMINGLING`) | AF | yes | inbound-shortfalls § labels |
| Fulfillment Outbound v2020-07-01 `getFulfillmentOrder`, `listAllFulfillmentOrders`, `getPackageTrackingDetails` | MCF order and package state: package `CurrentStatus` `UNDELIVERABLE` ("Undeliverable because package was lost or destroyed"), tracking events incl. `EVENT_405` "Shipment damaged" and `EVENT_409` "Lost by carrier", returned-item disposition `CarrierDamaged` / `FulfillerDamaged` | AF | yes | No operation files an MCF claim. A v2026-07-04 version (`getOrder`, `listOrders`, …) is in the models; the 2020-07-01 version is not on the deprecation schedule [command-verified] |
| Reports API v2021-06-30 `createReport`, `getReports`, `getReportDocument` | The report lifecycle | any of twelve roles incl. all five | yes | The report type's own role decides (§2.1) |
| Sales v1 `getOrderMetrics` | Ordered sales and units per interval | IOT and PL in every region; ten more roles in FE only | yes (PL) | finance P-api-21 |
| FBA Inventory v1 `getInventorySummaries` | Current researching / unfulfillable quantities | AF, PL | yes | Stock pack W2, B10 |
| Finances v2024-06-19 `listTransactions`, `listSummary`, `listBalances` | Reimbursement, reversal and fee-adjustment transactions; filter by `ORDER_ID` or `FINANCIAL_EVENT_GROUP_ID` | FA | yes | Finance pack P-ref-23, P-ref-34 |
| Finances v0 `listFinancialEvents` | `AdjustmentEventList` (`FBAInventoryReimbursement`), `SAFETReimbursementEvent`, `FBALiquidationEventList` (liquidation proceeds), fee events | AISP (EU only), **AF (NA, FE only)**, FA | yes | Deprecated 2025-07-21, removed 2027-08-27 (finance P-ref-24) |
| Finances v0 `listFinancialEventsByOrderId` / `…ByGroupId` / `listFinancialEventGroups` | Same by order or group | FA (ByGroupId and Groups also AISP) | yes | — |
| Orders v0 `getOrder`, `getOrderItems`, … | Sale price, `ConditionId`, items of an order | AF, BC, BS, D2C(R), FA, IOT, PR, PL, PS(R), SPI, TI(R), TR(R) | yes | Deprecated 2026-01-28, removed 2027-03-27 |
| Orders v2026-01-01 `searchOrders`, `getOrder` | The same in two operations; `breakdowns` (proceeds) added 2026-05-27; `cancellationExecution` added 2026-07-29 | same role list | yes | The successor |
| Catalog Items v2022-04-01 `getCatalogItem` / `searchCatalogItems` with `includedData=dimensions` | `item` and `package` dimensions "associated with the item in the Amazon catalog" | PL | yes | Catalogue dimensions, not a fulfilment-centre measurement [read in official docs: the model's description] |
| Product Fees v0 `getMyFeesEstimateForSKU` / `…ForASIN` | Amazon's current fee estimate for a price | AF, BC, BS, FA, IOT, PR, PL, PS(R), SPI, D2C(R), TI(R), TR(R) | yes | An estimate, not the fee charged |
| Product Fees v0 `getMyFeesEstimates` (batch) | Same, batched | PR, PL | yes | — |
| Data Kiosk `createQuery`, `getQuery`, `getDocument` | The operations; a field's role is checked at `createQuery` | BA (operations page and the Data Kiosk page) | yes | The dataset's role decides (next rows, §4) |
| Data Kiosk `analytics_economics_2024_03_15` | Charged fees per MSKU and period, incl. FBA fulfilment, storage, removal and disposal; `economicsPreview` ahead | **SPI** (Amazon's correction; Amazon developer support 2025-04-23) | **no** | §4, SU33 |
| Data Kiosk `analytics_salesAndTraffic_2024_04_24` | Sales and traffic; A-to-z and chargeback claim counts and rates | BA (correction) | yes | §4, SU57 |
| Data Kiosk `analytics_sellerAnalytics_2025_03_31` | Returned units and return rate, return-defect topics, account health | BA by the operations page; the correction page predates the dataset and does not name it | yes, unconfirmed | §4, SU54 |
| Support API v2025-02-01 `listCases`, `getCase`, `listContacts` | Case status, subject, dates, contacts and attachments | SPS(R) | **no** | §5 |
| Shipping API v2 `createClaim` | A claim on an Amazon Shipping parcel (`LOST_IN_TRANSIT`, `DAMAGED_IN_TRANSIT`, …) | not listed on Role Mappings; its sibling operations need Amazon Logistics or D2C(R) (one of them Amazon Logistics or Product Listing) | **no** | Not an FBA reimbursement (§5) |
| Seller Wallet v2024-03-01 (all) | Wallet balances and transfers | AISP (+PISP to move money) | **no** | Nothing in it touches a claim [inferred from its model] |
| AWD v2024-05-09 | AWD inventory and inbound | AWD | **no** | AWD losses are outside FBA reports (stock pack I1–I4) |

### 2.3 Notifications

| Notification | Use to a claims audit | Role | In app |
|---|---|---|---|
| `REPORT_PROCESSING_FINISHED` | A requested report is ready | (role of the report) | yes |
| `DATA_KIOSK_QUERY_PROCESSING_FINISHED` | A Data Kiosk query is ready | AWD, BA | yes (BA) |
| `TRANSACTION_UPDATE` | "sent whenever there is a new transaction posted to the seller's account"; that a reimbursement is such a transaction is [inferred], the page does not name reimbursements | **not listed** on Role Mappings for Types | unknown |
| `FBA_INVENTORY_AVAILABILITY_CHANGES` | Availability changes per SKU | AF | yes |
| `FBA_OUTBOUND_SHIPMENT_STATUS`, `FULFILLMENT_ORDER_STATUS` | MCF orders | AF | yes |

No notification type announces a reimbursement as such, a ledger adjustment, an inbound receipt or discrepancy, or a support-case change. That is per the *Notification Type Values* page (`updatedAt` 2026-10-28), whose 26 type headings were listed today [command-verified; corrected from 25 on 2026-11-13]. `DATA_KIOSK_QUERY_PROCESSING_FINISHED` is not among those headings; its row above comes from *Role Mappings for Types*. Every notification needs an SQS or EventBridge destination, which the door does not carry [inferred from the door].

**(b) Practitioners on the reads.**

- moltar (developer, issue #1847, 2021-09-13): `GET_FBA_REIMBURSEMENTS_DATA` "returns the same data for all marketplaces, disregarding the `marketplaceIds` parameter", and a repeat request in one region is `CANCELLED` "once per *all* marketplaces". He relayed Amazon Developer Support's answer that the FATAL "was due to throttling error because the throttling rate for the report type is **238 minutes**." [opinion; an old relayed support answer]
- Amazon Developer Services (Marc, issue #4333, 2024-11-20), on `GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA` returning different row counts for the same dates: "there is no guaranteed time until all updates have been properly reflected throughout Amazons backend." The same report's counts differed again for one developer in 2026 (#5323, 2026-07-20/21). Amazon replied: "There shouldn't be restrictions to retrieve the reports." [opinion; Amazon developer-services staff on GitHub]
- Issue #5344 (2026-08-03, open): a removal shipment row of type "Return" carries no destination address. [opinion]
- Issue #4747 (2025-04-21): the ledger detail example `"reportOptions":{"eventType":""}` on Amazon's page is refused with "Member must have length greater than or equal to 1". Amazon's page still prints that example today. [opinion; page text read in official docs]
- Issue #5339 (2026-07-31): Amazon staff (Jawher) explained a one-hour shift between a ledger request's times and Seller Central's displayed range as the store's own time zone, CEST for Germany in May. [opinion; Amazon staff]
- Airbyte's SP-API connector docs (read 2026-11-13): the generation cooldown "applies per seller, per report type, across all applications. Even requests from different apps count toward the same cooldown window." [opinion]

**(c) Into a skill:** every row's role and whether it is in the app; that the claim-report types are request-only, except storage fees and the seller-fulfilled and Prime returns reports (also schedulable) and settlement (Amazon-scheduled); Amazon's stated freshness per type; and the absence of an SP-API Date Range transaction report. **Read at run time:** whether each read answers, which columns the seller's own file carries (its header row; stock pack W13, A3), and the per-store availability of a report, read on its entry on *FBA Reports* (*Values that move*).

### 2.4 The keys each read carries

Which identifier a read carries decides what it can be joined to. From the attribute lists on *FBA Reports* (2026-10-13), *Returns Reports* (2026-10-28) and the models at db2936aa [command-verified]:

| Key | Reads that carry it |
|---|---|
| FNSKU (with MSKU, ASIN) | ledger detail and summary, reimbursements, FBA returns, removal order detail, stranded, reserved, storage, fee preview |
| Inbound shipment ID | ledger detail `Reference ID` ("Transaction ID, such as a shipment ID or adjustment ID", stock pack stock-states F5), inbound performance `fba-shipment-id`, Fulfillment Inbound v0 and v2024-03-20 |
| Removal order ID | removal order detail and removal shipment detail `order-id`; ledger detail `Reference ID` on removal events [inferred from the same definition] |
| Customer order ID | reimbursements `amazon-order-id`, FBA returns `order-id`, replacements `original-amazon-order-id`, Amazon-fulfilled shipments, all-orders, Finances `ORDER_ID`, Orders, seller-fulfilled and Prime returns |
| Case ID | reimbursements `case-id`; Support API `caseId` (outside the app) |
| Fee line and date | Finances `listTransactions` and v0 fee events, settlement V2, storage and long-term storage reports, inbound performance `fee-type`, Economics (outside the app) |
| Store / country | ledger detail `Country` and `Store`; removal order detail none; the reimbursements report carries `currency-unit` but **no store or marketplace column** |

That a reimbursement row names no store matters for Pan-EU, EFN and NA Remote Fulfillment sellers: the store a reimbursement belongs to is not on the row (SU52). That a reimbursements request ignores `marketplaceIds` within a region is a practitioner's report (SU24).

---

## 3. Lag, retention and look-back

**(a) Amazon's words.**

- Ledger detail: "You can view all historical movements of your inventory for 18 months in this report." (*FBA Reports*, 2026-10-13). This is the only claims report whose look-back Amazon's SP-API page states.
- FBA report generation: "A near real-time FBA report is generated no more than once every 30 minutes… A daily FBA report is generated no more than once every four hours… These frequencies describe how often Amazon generates updated report content. They do not set how many report requests you can submit." (*FBA Reports*). The stock pack holds this as W20.
- Reports API: "Reports are retained for a maximum of 90 days", and the report document URL "expires after 5 minutes" (the door; both read in `reports_2021-06-30.json` at db2936aa, not on the *Reports API* overview page of 2026-09-09) [command-verified].
- Data Kiosk economics: `startDate` "must be no more than two years ago". Its leaf fields (36 of them) carry `@resultRetention(duration : "P30D")`, so a query's result is kept 30 days [command-verified: `analytics_economics_2024_03_15.graphql` at db2936aa, lines 97, 19–60; the schema on `main` at b13d1d10 (2026-11-11) adds seven lines above them]. The seller-analytics and sales-and-traffic datasets state the same two-year start limit [command-verified].
- `getInventorySummaries` with `startDateTime` reaches back 18 months (stock pack B10).
- Finances v2024-06-19 answers empty for a range wider than 180 days (finance P-ref-23). v0 `…ByGroupId` "only retrieves a group's data for the past two years" (finance pack API table).
- Amazon-fulfilled shipments: one month per request, 12 requests per 8 hours, a 1–3 hour (rarely 24-hour) delay (§2.1).
- The Deferred Transaction Report: "A single report can provide up to 10 years of data."
- Seller-fulfilled and Prime returns reports: "You can request up to 60 days of data in a single report" (*Returns Reports*, 2026-10-28); no look-back stated.
- Settlement reports "cannot be requested or scheduled. They are automatically scheduled by Amazon. You can search for these reports using the `getReports` operation" (*Settlement Reports*, 2026-10-14). `getReports`' `createdSince`: "The default is 90 days ago. Reports are retained for a maximum of 90 days" (`reports_2021-06-30.json`) [command-verified]. That a settlement report generated more than 90 days ago can no longer be fetched through the API, and cannot be re-created by `createReport`, follows from the two statements [inferred]. Data vendors say the same (Daasity and Saras Analytics help pages, search-result summaries only, read 2026-11-13) [opinion]. A developer's question on it (discussion #338, 2023-10-23) has no Amazon answer.
- Data Kiosk Economics: "The data sets are refreshed daily" (schema description, db2936aa and main) [command-verified]. Its preview reaches forward, not back (`economicsPreview` end date "no more than 120 days after today").
- Data Kiosk Seller Analytics returns: "Return data is computed with a delay of about 45 days, so the most recent ~45 days may be empty or incomplete". Returns are "mapped to the day each unit was shipped", and return-defect counts cover a "trailing six months" (`analytics_sellerAnalytics_2025_03_31.graphql`) [command-verified].
- The Support API: `listCases` takes no date, and the model states no history reach. The page says the API is "available in all Amazon stores", and the model takes no marketplace parameter [command-verified]. How far back a seller's cases are listed is unread.
- **Amazon states no look-back on its SP-API pages** for the reimbursements, FBA returns, replacements, removal order and removal shipment reports. Amazon Developer Support pointed developers to Seller Central's report descriptions for such constraints (#2974, §1).

**Unread (JS shells), and they stay unread.** The Seller Central help pages for these reports were tried by plain GET at the `sellercentral.amazon.com/help/hub/reference/external/<ID>`, `sellercentral.amazon.co.uk/…` and `/gp/help/external/<ID>` routes. Each returned about 1,800 characters of shell and no text: G200732720 (Reimbursements report), G200453320 (customer returns), G200213130 (reimbursement policy), GJQTPXHTS6K5PQFD. No quote of their look-back text was found. The customer-returns file read versions of G200213130, G200453320 and G200732720 through the help hub's content call. The office closed that route on 2026-11-10, and this file takes nothing from those readings.

**(b) Practitioners.**

- Fivetran (Amazon Selling Partner connector, "Reports" docs, read 2026-11-13) gives a "Max Look Back Window" and latency per report [opinion; a data vendor's connector limits, not Amazon's]:

| Report | Aggregation | Max look-back | Latency |
|---|---|---|---|
| `GET_FBA_REIMBURSEMENTS_DATA` | DAY | 18 months | 5 days |
| `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` | DAY | 18 months | 2 days |
| `GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA` | MONTH | 2 years | 1 month |
| `GET_FBA_STORAGE_FEE_CHARGES_DATA` | MONTH | 2 years | 1 month |
| `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` | MONTH | 2 years | 1 month |
| `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` | NA | 3 days | NA |
| `GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL` | DAY | 18 months | 1 day |
| `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA` | DAY | 18 months | 1 day |
| `GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL` | DAY | 18 months | 1 day |

- Airbyte (source-amazon-seller-partner docs, read 2026-11-13) caps a single request at 30 days for the all-orders and Amazon-fulfilled-shipments reports and at 60 days for `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE`. It caps other report streams at 365 days, and its start date defaults to no earlier than two years back [opinion].
- Lingxing (领星 help, "费用诊断", undated, read 2026-11-13) lists an inbound-shipment discrepancy only when the shipment closed within 90 days ("货件已经CLOSE90天之内") — the tool's display rule. It restates Amazon's inbound window as "最迟九个月内" after delivery, with no marketplace named [opinion; a tool's reading of Amazon's window]. The window itself is a moving value: its rule and where it is read belong to the inbound area and finance P-ref-16, not to this file.
- Several English vendor pages conflate a report's look-back with a claim window. One example is sellerlabs.com's 2026 audit guide and others ("18 months" vs "60 days") [opinion]. The two are different facts: a report reaching 18 months back does not make an 18-month-old event claimable. The claim windows themselves sit in finance P-ref-16 and the other areas.

**(c) Into a skill:** the ledger's stated reach (Amazon's), the Reports API's keep and what it means for Amazon-scheduled settlement reports, Seller Analytics' return delay, and the generation intervals (the values in *Values that move*). Also that Amazon's SP-API pages state no look-back for the reimbursement, returns and removal reports, and that the practitioners' figures are a vendor's. **Read at run time:** how far back each of the seller's own reports actually reaches. This is read by asking for a range and reading the first row's date; it cannot be read in advance. The rate applied to the seller comes from `x-amzn-RateLimit-Limit` (the door).

---

## 4. Data Kiosk for claims: roles and what it carries

**(a) Amazon's words.**

- *Data Kiosk API* (`updatedAt` 2026-10-20): "Each field available with Data Kiosk requires a certain role. Data Kiosk determines whether the requester has the required roles for each field in the query upon query creation." Its five operations each list Brand Analytics.
- *Correction: Data Kiosk role requirements* (…/changelog/correction-data-kiosk-role-requirements, page undated; announcement referenced 2024-06-19; read 2026-11-13): "The Vendor Analytics and Sales and Traffic datasets require the Brand Analytics role. The Economics dataset requires the Selling Partner Insights role."
- Release notes: 2026-09-30, "Updated the Analytics Economics dataset with deal, coupon, removal, disposal, and fuel fees", and the Seller Analytics dataset added (returns, account health). 2025-12-22, `FNSKU` removed from Economics' `ProductIdentifierGranularity`. 2026-01-28 and 2026-02-23, "claim-related metrics" added to Sales and Traffic 2024-04-24.
- Seller Analytics' account-health claim fields carry `@paamRights(require: ["analytics_sales_and_traffic_view_pa", …])` [command-verified]. These are Seller Central permission names, not SP-API roles.
- The claim fields in Sales and Traffic 2024-04-24 are buyer claims: `accountHealthAtozClaimOrderCount` ("orders with an A-to-z Guarantee claim that was not denied, applies to seller-fulfilled orders only"), `accountHealthChargebackClaimOrderCount`, and the matching rates [command-verified]. None counts an FBA reimbursement claim.
- Economics' `feeTypeName` is an open string. The `economics` query's description sends "supported fee types and advertisement charge types" to Seller Central page GZ8Y22NL2FSRY8M5, and the `economicsPreview` query's to GQNVDV46U9JQ25HY. Both are help pages, not fetched, and unread. The schema's own `PreviewFeeType` enum on main (b13d1d10, 2026-11-11) lists 24 values, among them `FBA_FULFILLMENT_FEES`, `MONTHLY_INVENTORY_STORAGE_FEES`, `AGED_INVENTORY_SURCHARGE`, `LOW_INVENTORY_LEVEL_FEE`, `FBA_INBOUND_PLACEMENT_SERVICE_FEE`, `FBA_REMOVAL_FEE`, `FBA_DISPOSAL_FEE`, `RETURN_PROCESSING_FEE`, `HIGH_RETURN_RATE_FEE` and `FUEL_AND_LOGISTICS_RELATED_SURCHARGE`. Its `FeeType` (the fee types whose components can be broken out) has two: `FBA_FULFILLMENT_FEE`, `FBA_STORAGE_FEE` [command-verified].

**(b) Practitioners and Amazon support on the Economics role.** Issue #567 ("Data Kiosk SKU Economics dataset query authorization issues (403)", opened 2024-05-03). In 2024 Amazon's Solutions Architect (leonardonakagawa) said the dataset was still in beta. On 2025-04-23 a developer posted an Economics query refused with `"code": "Unauthorized", "message": "Unauthorized to access requested fields."`. The same architect answered the same day: "Economics dataset are under Selling Partner Insights role, so can you please ensure if you have it attached to your developer profile and app?", linking the correction page. An earlier commenter (2024-06-24) had the refusal on Economics while Sales and Traffic answered. [opinion; Amazon developer-support staff on GitHub, with developers' reports]

**(c) Into a skill:** Economics sums fees per MSKU and period. It is a cross-check for fee overcharges, not a claim record. Its role is Selling Partner Insights per Amazon's correction and Amazon developer support, which puts it outside the five. The operations page still names Brand Analytics for the operations, and both pages are stated with their dates. Data Kiosk gives no per-unit reimbursement or ledger event. **Read at run time:** whether an Economics query is accepted on the seller's connection. A `createQuery` refused with "Unauthorized to access requested fields" names the fields refused.

---

## 5. Cases, claims and the API: what exists

### 5.1 The Support API (Selling Partner Support)

**(a) Amazon's words.**

- Release notes, 2026-09-30: "Launched the Support API. You can use this API to programmatically retrieve information about a selling partner's Amazon support cases."
- *Support API* (`updatedAt` 2026-09-30): "You can list a selling partner's support cases, retrieve the details and status of a specific case, and review the full history of contacts (email, phone, and chat communications) exchanged with Amazon support, including any scheduled callback appointments and attachments. The Selling Partner Support API is available in all Amazon stores." Availability: "Sellers only". Sandbox: "Static". Each of `getCase`, `listCases` and `listContacts` requires "Selling Partner Support (Restricted)" in NA, EU and FE.
- The model `support_2025-02-01.json` [command-verified]:
  - It has three operations, all reads: `POST /support/2025-02-01/cases` (`listCases`), `GET …/cases/{caseId}` (`getCase`) and `GET …/cases/{caseId}/contacts` (`listContacts`). Each carries a usage plan in the model (value in *Values that move*); the rate applied is returned in `x-amzn-RateLimit-Limit`.
  - `listCases` takes only `sortOrder`, `maxResults` (a page size, bounds in *Values that move*) and `nextToken`. It has no filter by date, by case type, by reimbursement or by ID, and no marketplace parameter.
  - A `Case` carries `caseId`, `status` (`RESOLVED`, `TRANSFERRED`, `PENDING_MERCHANT_ACTION`, `PENDING_AMAZON_ACTION`), `subject`, `primaryEmail`, `ccEmails`, `appointments`, `createdDate`, `lastUpdatedDate` and `resolvedDate`. It has no case type, no amount and no linked reimbursement ID.
  - A `Contact` carries `channel` (`EMAIL`, `PHONE`, `CHAT`) with `emailContent` (sender role `AMAZON` or `SELLING_PARTNER`, `message`, `attachments[]`), `phoneContent.callNotes` or `chatContent` (events, transcript).
  - "The `downloadUrl` expires after 15 minutes."
- No operation in the 394 operations of the models creates, updates, replies to or attaches to a support case [command-verified: scan of every `operationId` and description for case, claim, reimburs, dispute, remeasur, sourcing cost].

**Contradictions on Amazon's pages (stated, not resolved).**

1. The roles page (2026-11-12) says the role lets an application "retrieve, search, and manage support cases". The model (2026-10-29) has no search filter and no write.
2. The tutorials *Retrieve and Review Selling Partner Support Cases* and *Retrieve the Contact History for a Support Case* (both 2026-09-30) name the prerequisite "The Support role". The Role Mappings and the Support API page name "Selling Partner Support (Restricted)".
3. The contact-history tutorial says "Each contact includes… a status (`VALID` or `EXPIRED`)… A contact with a `status` of `EXPIRED` has no content". The model's `Contact` has no `status` property (properties: `contactId`, `channel`, `emailContent`, `phoneContent`, `chatContent`, `createdDate`) [command-verified].
4. The retrieve tutorial says a case "includes the case ID" as `id`; the model's field is `caseId`.

**What it would open, were the role added.** The status and the Amazon replies of the seller's cases, including reimbursement cases. These could be joined by hand-read subject text, or by `caseId` against the Reimbursements report's `case-id` [inferred: both are case identifiers; no Amazon page says they are the same number space]. It is outside the five roles and restricted. Nothing is built on it. The model's example `caseId` is a ten-digit number ("1234567890"); that it is the Case Log's case number is [inferred].

**(b) Practitioners.** A developer (issue #5422, opened 2026-10-26, open, no Amazon reply as of 2026-11-13) asked Amazon how to add Selling Partner Support (Restricted) to an approved private application "without removing existing permissions", and asked for it on a public application separately from its pending review. They describe the use as "the documented read-only operations". [opinion] It shows the role being requested apart from an application's other roles. It does not show how long approval takes.

### 5.2 Shipping API v2 `createClaim` (not FBA)

The Shipping API v2 model has `POST /shipping/v2/claims` (`createClaim`): "This API will be used to create claim for single eligible shipment." Its body is `trackingId`, `claimReason` (`LOST_IN_TRANSIT`, `DAMAGED_IN_TRANSIT`, `DELIVERED_NOT_RECEIVED`, `ITEM_MISSING_SWITCHEROO`, `COD_ABUSE`), `declaredValue` ("required for off-Amazon shipments"), `isReplacementPackageSent`, `proofs` (URLs) and `settlementType` [command-verified]. It is a carrier claim on a parcel shipped with Amazon Shipping or Buy Shipping. It is not an FBA inventory reimbursement. The operation is not on the Role Mappings page, whose Shipping v2 section lists its other operations under Amazon Logistics or D2C(R) [command-verified: no `createClaim` in the page]. It is the only "create a claim" write in the SP-API, and it is outside the five roles.

### 5.3 Amazon's agentic toolkit and connector

- `amzn/selling-partner-agentic-toolkit` (GitHub, last push 2026-11-11, 39 stars, read 2026-11-13) holds twelve skills [command-verified: `gh api` tree]: fba-inbound-management, finance-month-end-closer, invite-secondary-users, five listing skills, seller-analytics, sp-api-knowledge, stockout-prevention and support-case-helper. None names reimbursements or claims. A code search for "reimbursement" in the repository finds one line, a compliance warning about "destruction of fulfillment-center inventory without reimbursement" [command-verified].
- `support-case-helper` (1.0.0, unchanged in substance since the survey's zip): "By default this skill calls no SP-API tools. It is **forward-compatible**…". Its rule: "If no such tool exists (current state): show the seller this exact message… To contact Seller Support, open https://sellercentral.amazon.com/help/center?ref=sp_ai_<agent>" [command-verified].
- `finance-month-end-closer` (added 2026-10-08) uses only `finances_monthEndClosing`, a connector tool absent from every public model [command-verified: survey grep]. Its only mentions of refunds are as items that move a payout.
- The Claude directory's "Amazon Selling Partner connector" lists eight tools, none a case or reimbursement tool (the survey; vendor guides read today agree: sellersonar.com, sellerforge.ai) [opinion for the vendors]. Third-party hosted MCPs advertise reimbursement reads (SellerForge, Sellerise, Novadata). Over the SP-API, these can only be the same reports [inferred]. None files a case through an API, because none exists.

**(c) Into a skill:** no SP-API operation opens or files an FBA case. The Support API is read-only and restricted; Shipping `createClaim` is a carrier claim, not FBA. Amazon's own plugin has no claims tool and sends the seller to the Help Center. **Read at run time:** nothing. Whether a connector or API has since gained a case tool is re-read from the deprecation schedule, the release notes and the toolkit repository when the pack is revised.

---

## 6. The steps of a claim that the SP-API cannot do, and the hand route

Each line names what is missing in the API [command-verified over the 394 operations unless said]; that column is this file's. The Seller Central route, its limits and its windows belong to the file that owns the claim kind or the case route, and are pointed to, not restated (IDR and case routes, limits, conduct: filing-and-conduct; values and the dispute window: value-and-reversals; fee routes and windows: fee-overcharges).

| Step | API | Where the route is held |
|---|---|---|
| Open an FBA reimbursement case (lost/damaged, inbound shortfall, returns, removals) | none | see filing-and-conduct FL4 (entry points by kind), FL1. Amazon's own plugin sends the seller to `…/help/center` (§5.3) |
| Claim lost or damaged units through the lost-and-damaged (IDR) pages | none; no read returns the IDR lists or statuses | see filing-and-conduct FL5; fc-lost-damaged FC13, FC14 |
| Request research on an inbound shipment discrepancy | none (v0 shows `QuantityReceived`; nothing submits) | see inbound-shortfalls IN13, IN29; stock pack I8, I21 |
| Attach evidence (invoices, POD, BOL, photos) | none | see filing-and-conduct § evidence (e.g. FL25 for removals) and each area file's evidence positions |
| Read Amazon's answer on a case | Support API read only, SPS(R), outside the app (§5.1) | the Case Log otherwise (filing-and-conduct) |
| Reply to or reopen a case | none | see filing-and-conduct |
| Enter or update a sourcing (manufacturing) cost | none | see value-and-reversals VR7, VR11, VR18 |
| Dispute a reimbursement's value | none | see value-and-reversals VR20, VR21 |
| Request a remeasurement / dispute a dimension-based fee | none | see fee-overcharges FE4, FE9, FE37 |
| File a removal-order claim | none | see removals-disposals RM35 and its windows (RM6) |
| Request the Deferred Transaction Report the first time | none | Payments Reports Repository (*Payment Reports* page [read in official docs]; SU30) |
| Download the Payments Date Range Report | no report type | Seller Central Payments → Reports Repository (§2.1 [command-verified]; SU29) |

What the SP-API can do around these steps: find the candidates (ledger, reports, Finances), state the evidence numbers a form asks for (shipment ID, FNSKU, `Reference ID`, order ID, tracking number), and see the outcome once paid (the Reimbursements report's `case-id`, and Finances and settlement lines).

**(c) Into a skill:** the table's "API" column, as Amazon's absence. **Read at run time:** none. The Seller Central route is the seller's own screen, which cx does not see.

---

## 7. What practitioners and tools add on the surface (Chinese and English)

- **Lingxing (领星), "费用诊断"** (help page, undated, read 2026-11-13) [opinion]:
  - It sorts discrepancies into 库存差异 (FC lost or damaged, misplaced, carrier transit), 货件签收差异 (received ≠ shipped) and FBA费差异 (wrong size or wrong fee).
  - It shows the ledger's 交易编号 (`Reference ID`) beside each diagnosis.
  - The seller types the CASE ID, and Lingxing watches for it in the 索赔报告: "当CASE ID能够在索赔报告查询到，即表示此产品索赔成功". This is the Reimbursements report's `case-id` used as the join.
  - Its own rules: "每个case只能申请一个SKU，每天最多申请10个SKU", and "一个货件终生只能诊断一次". These are the tool's rules, not Amazon's.
- **Lingxing, "FBA费差异"** (undated) [opinion]:
  - For FBA it prefers the fee preview report's warehouse-measured dimensions, falling back to listing dimensions.
  - Its estimated fee comes "from the API, refreshed every 7 days, or from the report, refreshed daily".
  - 预计赔偿金额 = (实收FBA费 − 应收费用) × quantity.
  - To verify a refund, it tells sellers to download Payments → Date Range Report and filter `Transaction Type = Fee Adjustment`, positive values being refunds.
- **Lingxing on its access** (its FAQ, quoted by sellerhow.com, 2026-09-18): it is an SPN provider and reads "通过SP-API的方式授权" [opinion]. No Chinese ERP read files a claim (finance P-ref-39).
- **Fivetran and Airbyte**: the look-back, latency, per-request windows and cross-app cooldown in §3 [opinion].
- **English vendors** (GETIDA, Seller Investigators, SELLERLOGIC, Refund Retriever; finance P-ref-31, P-tool-17) file through Seller Central by hand or by browser. No vendor page read claims an API that files.

**Choices practitioners make on the surface, side by side** (none is Amazon's, and none is a method of this pack):

- *Tying a paid claim to its case.* (a) Lingxing: the seller types the CASE ID, and a claim counts as paid when that ID appears in the Reimbursements report's `case-id` (SU43). (b) Matching by FNSKU and date range with no shared identifier, as fc-lost-damaged records (see fc-lost-damaged FC27). (c) The Support API's `caseId` against `case-id`, which needs a restricted role and rests on an [inferred] identity of the two numbers (§5.1).
- *Valuing a dimension overcharge.* (a) Lingxing: (fee charged − expected fee) × quantity, with Amazon's measured dimensions from the fee preview report (SU44). (b) The formulas and reads fee-overcharges records from other tools (see fee-overcharges FE34). (c) Data Kiosk Economics' charged fee with its size-tier `properties` per date range, which is outside the five roles (SU33; fee-overcharges FE18).
- *Confirming a fee refund.* (a) Lingxing: the Seller Central Date Range Report filtered on `Fee Adjustment`, which has no SP-API report type (SU29). (b) Finances `listTransactions` or the settlement V2 report (finance P-ref-23, P-ref-33).

---

## 8. Deprecations and changes since 2025 that touch a claims audit

From *SP-API Deprecation Schedule* (`updatedAt` 2026-09-09) and *SP-API Release Notes* (`updatedAt` 2026-11-04), both read 2026-11-13 [read in official docs]:

| Resource | Deprecated | Removed | Claims use |
|---|---|---|---|
| Finances v0 `listFinancialEvents`, `…ByGroupId`, `…ByOrderId` | 2025-07-21 | scheduled (*Values that move*) | Reimbursement and fee events; successor `listTransactions` (finance P-ref-24) |
| Orders v0 `getOrders`, `getOrder`, `getOrderItems`, … | 2026-01-28 | scheduled (*Values that move*) | Sale price for post-order valuation; successor Orders v2026-01-01 |
| `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE`, `…_XML` | 2025-03-17 | 2026-11-11 | Removed two days before this read; `…_FLAT_FILE_V2` stays (the door) |
| `GET_FBA_SNS_FORECAST_DATA`, `GET_FBA_SNS_PERFORMANCE_DATA` | 2025-06-25 | 2025-12-11 | none |
| `ORDER_STATUS_CHANGE` notification | 2023-06-21 | 2026-07-29 | none (ORDER_CHANGE remains) |
| Fulfillment Inbound v0 ten plan/transport operations | 2024-04-01 | 2025-01-21 | The six v0 reads that remain carry `QuantityReceived` (stock pack A2, A3) |
| `analytics_salesAndTraffic_2023_11_15` dataset | 2025-08-27 | **2026-03-27** on the schedule; **2026-02-26** in the release note of 2025-08-27 | Contradiction between Amazon's two pages, stated |

Additions since 2025 that a claims audit can use: Finances `listTransactions` filters by `FINANCIAL_EVENT_GROUP_ID` (2025-12-03) and `ORDER_ID` (2026-01-28), and by `transactionStatus` (2025-06-25). `listSummary` and `listBalances` came on 2026-07-29 (the `SETTLEMENT_ID` filter was rolled back; finance P-ref-23). The Support API came on 2026-09-30. Economics gained removal and disposal fees on 2026-09-30. Orders v2026-01-01 launched 2026-01-28. No release note or deprecation since 2025 adds or removes an FBA claims report type, the ledger or the reimbursements report. No announced item names reimbursement claims, the IDR pages or the Case Log [command-verified: grep of release notes 2025-01 to 2026-11 for reimburs, claim, case, ledger]. (The "claim-related metrics" added to Sales and Traffic on 2026-01-28 and 2026-02-23 count A-to-z Guarantee and chargeback claims, not FBA reimbursement claims: the schema's field descriptions say so (§4, SU57) [command-verified].)

**A further contradiction (found 2026-11-13).** The release note of 2026-07-29 still announces `SETTLEMENT_ID` as a `listTransactions` filter, and the release notes (`updatedAt` 2026-11-04) carry no rollback. The model commit db2936aa (2026-10-29, "SPAPI October Release Finance API Rollback") removed `SETTLEMENT_ID` from `listTransactions`' `relatedIdentifierName`; it stays only on `listSummary` [command-verified: `gh api` diff of db2936aa; `finances_2024-06-19.json`].

**Stale entries on Amazon's Role Mappings for Types page** (2026-09-09), checked against the schedule: it still lists `GET_FBA_SNS_FORECAST_DATA` and `GET_FBA_SNS_PERFORMANCE_DATA` (removed 2025-12-11), `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE` and `…_XML` (removed 2026-11-11), and `ORDER_STATUS_CHANGE` (removed 2026-07-29) [command-verified]. A type's presence on the roles page is therefore not proof that it still answers.

---

## 9. Into a skill, and read at run time (the area in one place)

**Into a skill:**

- The role of each read (§2) and the reads outside the five (Support API, seller-fulfilled returns by return date, the Seller Performance Report, Data Kiosk Economics, Shipping `createClaim`, AWD, Seller Wallet, restricted invoicing types); the Prime returns reports inside them through Pricing.
- The keys each read carries (§2.4), and that a reimbursement row names no store.
- Request-only versus scheduled per type, and Amazon's stated freshness and request limits per type, each with where it is read (values in *Values that move*).
- The ledger's stated reach, the absence of an Amazon-stated look-back for the other claim reports, the Reports API's keep and its effect on settlement reports, and Seller Analytics' return delay.
- The list of steps with no door (§6).
- The Support API's shape and contradictions (§5.1), and Shipping `createClaim` as not FBA.
- The deprecations table (§8), with removal dates read on the schedule.
- The data pitfalls: the region-wide reimbursements report, the moving removal-shipment counts, the empty `eventType` example, and local-time ledger ranges.

**Read at run time:**

- Whether each read answers on the connection (a `403` names a missing role).
- The seller's own files' headers.
- How far back each report actually reaches, by its first row.
- The rate applied to the seller, from `x-amzn-RateLimit-Limit`.
- The deprecation schedule and release notes for anything removed after 2026-11-13.
- The case's own status, which the seller reads in the Case Log.
- Whether a Data Kiosk query is accepted (an Economics query refused with "Unauthorized to access requested fields" names the fields).

---

## Positions

- **SU1.** A role grants access to operations, reports, feeds and notifications; a read is allowed when the application holds at least one role Amazon names for it. Source: *Role Mappings for SP-API Operations* (2026-10-28), *Role Mappings for SP-API Types* (2026-09-09). [read in official docs]
- **SU2.** The ledger detail and summary, `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA`, `GET_FBA_INVENTORY_PLANNING_DATA`, `GET_FBA_OVERAGE_FEE_CHARGES_DATA` and `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA` name Amazon Fulfillment as their only role. Source: *Role Mappings for Types*; *FBA Reports* (2026-10-13). [read in official docs; command-verified by grep] (Adds to finance P-ref-28 and the door, which name some of these.)
- **SU3.** `GET_FBA_REIMBURSEMENTS_DATA`, `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`, both removal reports, `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA`, `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA`, `GET_FBA_STORAGE_FEE_CHARGES_DATA` and `GET_FBA_FULFILLMENT_LONGTERM_STORAGE_FEE_CHARGES_DATA` each answer to Pricing or Amazon Fulfillment. `GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL` also answers to Inventory and Order Tracking. Source: *FBA Reports*; *Role Mappings for Types*. [read in official docs]
- **SU4.** Fulfillment Inbound v0 `getShipments`, `getShipmentItems`, `getShipmentItemsByShipmentId` and every v2024-03-20 operation name Amazon Fulfillment only. Source: *Role Mappings for Operations*. [read in official docs] (Stock pack P-inbound-2 holds the v0 reads' meaning.)
- **SU5.** Finances v0 `listFinancialEvents` names AISP (EU only), Amazon Fulfillment (NA, FE only) and Finance and Accounting. `…ByOrderId` names Finance and Accounting only. Source: *Role Mappings for Operations*. [read in official docs] (Finance pack table holds it.)
- **SU6.** Catalog Items v2022-04-01 (`includedData=dimensions`) needs Product Listing. Its dimensions are those "associated with the item in the Amazon catalog". Amazon's measured dimensions on file for fees are carried by the fee preview and storage fee reports. Source: `catalogItems_2022-04-01.json`; *FBA Reports*. [read in official docs] That the two may differ is [inferred].
- **SU7.** Product Fees v0 `getMyFeesEstimateForSKU` and `…ForASIN` accept any of twelve roles, including PL, PR, AF and FA. `getMyFeesEstimates` needs Pricing or Product Listing. They return an estimate for a price, not a fee charged. Source: *Role Mappings for Operations*; `productFeesV0.json`. [read in official docs]
- **SU8.** The Support API v2025-02-01 (`listCases`, `getCase`, `listContacts`) needs Selling Partner Support (Restricted), a role outside the seller's app. It would open the status, dates, subject and the Amazon email, phone and chat contacts and attachments of the seller's cases, reimbursement cases included. Nothing is built on it. Source: *Support API* (2026-09-30); *Role Mappings for Operations*. [read in official docs]
- **SU9.** The Support API launched on 2026-09-30. Source: *SP-API Release Notes*. [read in official docs]
- **SU10.** The Support API's three operations are reads. `listCases` filters by nothing: it takes a sort order, a page size and a token, and no date, case type, reimbursement, ID or marketplace. A case carries no type, amount or reimbursement ID. Contact attachments come by a `downloadUrl` that expires. The operations carry a usage plan in the model, and the rate applied is returned in `x-amzn-RateLimit-Limit`. The page-size bounds, URL life and default rate are in *Values that move*. Source: `support_2025-02-01.json`. [command-verified]
- **SU11.** Amazon's pages contradict each other on the Support API. The roles page (2026-11-12) says the role can "retrieve, search, and manage support cases", while the model has no search filter and no write. The tutorials (2026-09-30) call the role "the Support role". The contact-history tutorial describes a contact `status` (`VALID`/`EXPIRED`) that the model's `Contact` does not have. Source: those pages; `support_2025-02-01.json`. [read in official docs; command-verified]
- **SU12.** No operation among the 394 in Amazon's models files a claim, opens a case, attaches evidence or enters a sourcing cost. None updates, replies to or reopens an FBA reimbursement or support case, requests a remeasurement, disputes a fee or a reimbursement's value, or acts in the lost-and-damaged (IDR) pages. The models' one claim-creating write is Shipping v2 `createClaim`, a carrier claim (SU13). Source: the models at db2936aa; main at b13d1d10 (2026-11-11) adds no operation. [command-verified] (This position is the pack's home for the statement; filing-and-conduct FL1, inbound-shortfalls IN29, removals-disposals RM35 and value-and-reversals VR18 point here. It extends finance P-ref-29 to remeasurement, value disputes and the IDR pages.)
- **SU13.** The SP-API's one claim-creating operation, Shipping API v2 `createClaim`, files a carrier claim (`LOST_IN_TRANSIT`, `DAMAGED_IN_TRANSIT`, `DELIVERED_NOT_RECEIVED`, `ITEM_MISSING_SWITCHEROO`, `COD_ABUSE`) on one shipment by tracking ID. It is not an FBA inventory reimbursement, and it is absent from the Role Mappings page. Source: `shippingV2.json`; *Role Mappings for Operations*. [command-verified]
- **SU14.** Amazon's agentic toolkit (`amzn/selling-partner-agentic-toolkit`, 12 skills, last push 2026-11-11) has no reimbursement or claims skill or tool. Its `support-case-helper` "by default" calls no SP-API tool and, "If no such tool exists (current state)", sends the seller to the Seller Central Help Center. Source: the repository. [command-verified]
- **SU15.** The ledger detail's look-back is stated on Amazon's *FBA Reports* page, in the ledger detail's description. It is the only claims report whose look-back Amazon's SP-API pages state. The value is in *Values that move*. Source: *FBA Reports*. [read in official docs] (Stock pack P-stock-states-30 holds the ledger.)
- **SU16.** Amazon's SP-API pages state no look-back for the reimbursements, FBA returns, replacements and removal reports. An Amazon developer-support engineer said such constraints are kept by the Seller Central reports team and described in Seller Central's report pages. Source: *FBA Reports*; issue #2974 (2022-07-15). [read in official docs; opinion for the engineer's statement]
- **SU17.** A data vendor's connector sets its own look-back and latency per report type. These are the vendor's settings, not Amazon's, and are read on the vendor's page. The values read are in §3's Fivetran table and *Values that move*. Source: Fivetran "Amazon Selling Partner – Reports" (undated, no marketplace named). [opinion]
- **SU18.** A report's look-back and a claim's window are different facts: a report reaching back 18 months does not make an older event claimable, and several vendor pages conflate them. Source: finance P-ref-16 (windows); vendor pages in §3. [inferred from Amazon's separate statements]
- **SU19.** Amazon sets a minimum interval between generations of an FBA report: one for near-real-time and one for daily reports, stated in the opening of *FBA Reports*. Practitioners report the cooldown counts per seller and report type across all applications. Values in *Values that move*. Source: *FBA Reports* [read in official docs] (stock pack W20); Airbyte docs [opinion].
- **SU20.** The fee preview report's refresh interval, its required `dataStartTime` offset and its per-seller request limit are stated in the report's own entry on *FBA Reports*. Its size-tier and future-fee columns are marked for one store only on the same entry. Values in *Values that move*. Source: *FBA Reports*. [read in official docs]
- **SU21.** The Amazon-fulfilled shipments report's span per request, its request cap per window (Seller Central requests count toward it) and its delay after shipping are stated in the report's own entry on *FBA Reports*. Values in *Values that move*. Source: *FBA Reports*. [read in official docs]
- **SU22.** The long-term storage fee report's required request span is stated in its entry on *FBA Reports*. Value in *Values that move*. Source: *FBA Reports*. [read in official docs]
- **SU23.** Some FBA reports are offered in some stores only. The store list is stated in each report's "Amazon store availability" line or its description on *FBA Reports* (replacements; inventory planning; Fee Preview columns). Values in *Values that move*. Where read: *FBA Reports*. [read in official docs]
- **SU24.** A developer reports that `GET_FBA_REIMBURSEMENTS_DATA` returns the same rows whatever `marketplaceIds` names, and that a second request within the cooldown in another store of the region is cancelled. Amazon support then gave its interval as 238 minutes (2021). Source: issue #1847. [opinion]
- **SU25.** The removal shipment detail report has returned different row counts for the same dates when asked at different times (2024, 2026). Amazon Developer Services said "there is no guaranteed time until all updates have been properly reflected throughout Amazons backend." Source: issues #4333, #5323. [opinion; Amazon staff]
- **SU26.** The removal shipment detail "will not include canceled returns or disposed items", and its "Return"-type rows carry no destination address. Source: *FBA Reports* [read in official docs]; issue #5344 [opinion].
- **SU27.** The ledger detail example `"reportOptions":{"eventType":""}` on Amazon's page is refused by the API ("length greater than or equal to 1"). Leaving `eventType` out returns all events. Source: issue #4747 (2025-04-21) [opinion]; the page still shows the example [read in official docs]. That omission returns all events is [inferred] from "Default is the empty string".
- **SU28.** Seller Central displays a ledger request's range in the store's local time, daylight saving included. Source: issue #5339, Amazon staff reply (2026-07-31). [opinion]
- **SU29.** No SP-API report type carries Seller Central's Payments Date Range (transaction) Report. Dimension-fee refunds that tools read there as `Fee Adjustment` are reached through Finances or the settlement report. Source: *Role Mappings for Types*; *Payment Reports* (2026-09-09) [command-verified: no `GET_DATE_RANGE_FINANCIAL_TRANSACTION_DATA`]; Lingxing FBA费差异 [opinion for the `Fee Adjustment` row].
- **SU30.** The Deferred Transaction Report (`GET_DATE_RANGE_FINANCIAL_HOLDS_DATA`, Finance and Accounting) must first be requested in Seller Central's Payments Reports Repository before the API can fetch it. Source: *Payment Reports*. [read in official docs]
- **SU31.** No notification type announces a reimbursement, a ledger adjustment, an inbound receipt or discrepancy, or a support-case change. `TRANSACTION_UPDATE` is sent "whenever there is a new transaction posted to the seller's account" and is not on the Role Mappings for Types page; that a reimbursement posting triggers it is [inferred]. Source: *Notification Type Values* (2026-10-28, 26 type headings); *Role Mappings for Types*. [command-verified]
- **SU32.** Fulfillment Inbound v2024-03-20's shipment items carry `quantity` and no received quantity. Received units per SKU per shipment through the API are v0 `QuantityReceived`. Source: `fulfillmentInbound_2024-03-20.json`, `fulfillmentInboundV0.json`. [command-verified] (Stock pack I3, P-inbound-2 own it.)
- **SU33.** The Data Kiosk Economics dataset needs Selling Partner Insights, a role outside the five. Amazon's correction page says so. Amazon developer support repeated it on 2025-04-23 to a developer whose Economics query was refused with "Unauthorized to access requested fields". The Data Kiosk page and the operations page still list Brand Analytics for the Data Kiosk operations, and a field's role is checked when the query is created. Source: *Data Kiosk API* (2026-10-20); *Correction: Data Kiosk role requirements* [read in official docs]; issue #567 [opinion; Amazon staff]. (Corrects finance P-ref-28 and P-api-23, which leave it open; fee-overcharges FE18 leans on this dataset.)
- **SU34.** Data Kiosk's earliest `startDate` and its result retention are stated in each dataset's schema: the `startDate` description, and `@resultRetention` on leaf fields. Values in *Values that move*. Source: the Economics, Seller Analytics and Sales and Traffic schemas at db2936aa. [command-verified]
- **SU35.** Economics gained removal, disposal, deal, coupon and fuel fees on 2026-09-30, and lost FNSKU granularity on 2025-12-22. Source: *SP-API Release Notes*. [read in official docs]
- **SU36.** Finances v0 `listFinancialEvents`, `…ByGroupId` and `…ByOrderId` were deprecated on 2025-07-21. Their removal date is the one on the *SP-API Deprecation Schedule*, which Amazon has moved for other resources (value in *Values that move*). Source: *SP-API Deprecation Schedule*. [read in official docs] (Finance P-ref-24 owns it; re-read unchanged.)
- **SU37.** Orders v0 (`getOrders`, `getOrder`, `getOrderItems`, `getOrderAddress`, `getOrderBuyerInfo`, `getOrderItemsBuyerInfo`) was deprecated on 2026-01-28. Its removal date is read on the schedule (value in *Values that move*). Its successor is Orders v2026-01-01 (`searchOrders`, `getOrder`), with the same role list. Source: *SP-API Deprecation Schedule*; *Release Notes* 2026-01-28; *Role Mappings for Operations*. [read in official docs]
- **SU38.** `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE` and `…_XML` were removed on 2026-11-11 (deprecated 2025-03-17). Source: *SP-API Deprecation Schedule*. [read in official docs] (The door holds it.)
- **SU39.** The deprecation schedule gives 2026-03-27 for the removal of the `analytics_salesAndTraffic_2023_11_15` dataset; the release note of 2025-08-27 gives 2026-02-26. Source: both pages. [read in official docs]
- **SU40.** Role Mappings for Types (2026-09-09) still lists types the schedule has removed: SnS reports, the old settlement flat and XML, and `ORDER_STATUS_CHANGE`. A type's presence there does not show that it answers. Source: both pages. [command-verified]
- **SU41.** No release note or deprecation from 2025-01 to 2026-11-04 adds, changes or removes an FBA claims report type, the ledger or the reimbursements report. None names reimbursement claims, the IDR pages or the Case Log. Source: *SP-API Release Notes*; *Deprecation Schedule*. [command-verified: grep]
- **SU42.** The six inventory adjustment, receipt and reconciliation report types that older claims guides name were removed on 2023-01-31 (deprecated 2022-06-13; the schedule's row names six types, including current-inventory, inventory-summary and monthly-inventory, beside adjustments, receipts and reconciliation). Source: *SP-API Deprecation Schedule*. [read in official docs] That the Inventory Ledger replaced them is not on the schedule; it is the stock pack's (W25) [inferred here]. (Stock pack W25 / P-stock-states-27 own it.)
- **SU43.** Lingxing (领星) ties a claim to its payment by a seller-entered CASE ID found in the Reimbursements report's `case-id`, and shows the ledger `Reference ID` beside each candidate. It limits its own diagnosis to one SKU per case and ten SKUs a day, which are its own rules, not Amazon's. Other practitioners match by FNSKU and date range instead (§7 lists the choices side by side). Source: Lingxing help "费用诊断" (undated, read 2026-11-13). [opinion]
- **SU44.** One tool, Lingxing, values a dimension overcharge as (fee charged − expected fee) × quantity, taking Amazon's measured dimensions from the fee preview report. It is one of the choices set side by side in §7 and in fee-overcharges FE34. Source: Lingxing help "FBA费差异". [opinion]
- **SU45.** Amazon's Seller Central help pages for the Reimbursements report (G200732720), customer returns (G200453320) and the reimbursement policy (G200213130) render as JavaScript shells by plain GET on the US, UK and `/gp/help/external` routes as of 2026-11-13. Their look-back text was not read. They stay unread here: the help hub's content call is a route the office closed on 2026-11-10. Source: this seat's fetches. [command-verified]
- **SU46.** Restricted roles require the developer to give "additional information about your data use and security controls". Source: *Roles in the Selling Partner API* (2026-11-12). [read in official docs]
- **SU47.** `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE` (seller-fulfilled returns by return date, with the five SAFE-T columns, `Order Amount` and `Refunded Amount`) needs Inventory and Order Tracking or Direct to Consumer Shipping (Restricted), both outside the five. It covers seller-fulfilled returns only, not FBA returns and not returnless refunds. It can be requested or scheduled, and its per-request span is stated on *Returns Reports* (value in *Values that move*). Source: *Returns Reports* (2026-10-28); *Role Mappings for Types*. [read in official docs; command-verified]
- **SU48.** The Seller Fulfilled Prime returns reports (`GET_CSV_MFN_PRIME_RETURNS_REPORT`, `GET_XML_MFN_PRIME_RETURNS_REPORT`) name Pricing among their roles, so they are in the app. They cover Seller Fulfilled Prime returns only. The CSV form carries the same `SafeT-…` columns and `Refunded-Amount`. Source: *Returns Reports*; *Role Mappings for Types*. [read in official docs; command-verified] (Finance pack refunds table holds the roles; customer-returns RT39 points to the non-Prime report only.)
- **SU49.** `GET_V2_SELLER_PERFORMANCE_REPORT` (`accountStatuses` per marketplace and Account Health metrics) names Selling Partner Insights as its only role, outside the five. It can only be requested. Source: *Performance Reports* (2026-10-28); *Role Mappings for Types*. [read in official docs; command-verified]
- **SU50.** The Fulfillment Inbound reads the inbound and fee files lean on beyond SU4 all name Amazon Fulfillment only: v2024-03-20 `listTransportationOptions`, `listPlacementOptions`, `listShipmentPallets`, `listPrepDetails`, `listInboundPlanItems` and `getInboundPlan`, and v0 `getBillOfLading` and `getLabels`. FBA Inbound Eligibility v1 `getItemEligibilityPreview` does too. Source: *Role Mappings for Operations* (2026-10-28). [read in official docs; command-verified]
- **SU51.** MCF order reads (Fulfillment Outbound v2020-07-01 `getFulfillmentOrder`, `listAllFulfillmentOrders`, `getPackageTrackingDetails`) name Amazon Fulfillment. The model carries a package status `UNDELIVERABLE` ("lost or destroyed"), tracking events "Shipment damaged" and "Lost by carrier", and returned-item dispositions `CarrierDamaged` and `FulfillerDamaged`. No operation files an MCF claim. Source: `fulfillmentOutbound_2020-07-01.json`; *Role Mappings for Operations*. [command-verified]
- **SU52.** The Reimbursements report carries `currency-unit` and no store or marketplace column. The ledger detail carries `Country` and `Store`. Which store a reimbursement belongs to is therefore not on the reimbursement row. Source: *FBA Reports* attribute lists (2026-10-13). [read in official docs] That a Pan-EU, EFN or Remote Fulfillment seller's row can be tied to a store only through the order or the ledger is [inferred].
- **SU53.** Settlement reports are scheduled by Amazon and cannot be requested, and the Reports API keeps a report for a stated maximum (value in *Values that move*). So a settlement report older than that keep cannot be fetched or re-created through the API [inferred]. Source: *Settlement Reports* (2026-10-14); `reports_2021-06-30.json` [read in official docs; command-verified]; vendors' help pages (search summaries) [opinion].
- **SU54.** Data Kiosk Seller Analytics counts returned units by ship date, and its schema states a return-data delay (value in *Values that move*). Its role is Brand Analytics by the operations page. Amazon's correction page predates the dataset and does not name it. Source: `analytics_sellerAnalytics_2025_03_31.graphql`; *Role Mappings for Operations*. [command-verified; read in official docs]
- **SU55.** The Economics schema points to Seller Central help pages for its supported fee types (GZ8Y22NL2FSRY8M5 for `economics`, GQNVDV46U9JQ25HY for `economicsPreview`), both unread. The schema's own `PreviewFeeType` enum lists the preview fee types, removal and disposal fees among them since main b13d1d10. Source: `analytics_economics_2024_03_15.graphql` at db2936aa and main. [command-verified]
- **SU56.** The Support API's model takes no marketplace parameter and states no history reach for `listCases`; its page says it is "available in all Amazon stores". How far back a seller's cases are listed is not stated. Source: `support_2025-02-01.json`; *Support API* (2026-09-30). [command-verified; read in official docs]
- **SU57.** The claim metrics in Data Kiosk Sales and Traffic are A-to-z Guarantee claims ("applies to seller-fulfilled orders only") and chargeback claims, counts and rates. None counts an FBA reimbursement claim. Source: `analytics_salesAndTraffic_2024_04_24.graphql`. [command-verified]
- **SU58.** Liquidation proceeds post as Finances v0 `FBALiquidationEventList` under `listFinancialEvents`; no report type read carries liquidation proceeds per removal order. Source: `financesV0.json`; *FBA Reports*. [command-verified] (Removals-disposals owns what is owed on liquidation.)
- **SU59.** The stranded and reserved inventory reports name Pricing or Amazon Fulfillment, are request-only and are "updated in near real-time". The stranded report carries `date-stranded`, `stranded-reason` and `Date-to-take-auto-removal`. Source: *FBA Reports*. [read in official docs] (Stock pack `stuck-stock/references/stranded.md` owns stranding.)
- **SU60.** Selling Partner Support (Restricted) is requested for an application apart from its other roles: a developer asked Amazon in 2026-10 how to add it to an approved application without disturbing its other roles. No Amazon answer was posted. Source: issue #5422. [opinion] (SU46 holds Amazon's requirement for restricted roles.)
- **SU61.** After an FBA report is generated, Amazon generates no updated version of it until its waiting period passes (SU19), so within that period a report already made holds the newest content Amazon has; `getReports` (`GET /reports/2021-06-30/reports`, `reportTypes`) lists reports already made. *FBA Reports* does not say what a new request returns within the period. Its entries read "Content updated daily" for the reimbursements, FBA returns and replacements reports and "Content updated in near real-time" for the removal order and removal shipment detail reports; the ledger detail's entry states neither. Source: *FBA Reports*, opening and entries (2026-10-13, read 2026-11-23); `reports_2021-06-30.json`. [read in official docs] That the report already made holds the newest content is [inferred] from the opening's sentence.

No position here is a sequence, a threshold, a rule of when to ask the seller, or a ceiling on what cx reads.

---

## Corrections to the other packs and to the survey

1. **The survey's first roles table (roles01).** It carries empty role cells for Finances v0 `listFinancialEvents`, all Orders v0 and v2026-01-01 reads, every Reports API operation, Product Fees `getMyFeesEstimateForSKU`/`…ForASIN` and Sales `getOrderMetrics`, from a parser defect. The survey's second table (roles01b) holds the values Amazon's page gives (e.g. `listFinancialEvents`: AISP (EU only), AF (NA, FE only), FA) [command-verified: both tables against today's page]. Any later seat must read roles01b.
2. **Finance pack P-ref-29 and lines-and-reads "What no operation does"** ("The Support API reads cases and creates none"). This holds by the model. Amazon's roles page of 2026-11-12, a day before this read, describes the role as able to "retrieve, search, and manage support cases", and the tutorials call it "the Support role" (SU11). The skill line stays true and could cite the contradiction.
3. **Finance pack table, Support API row** ("`listCases` (POST as read)"). Confirmed POST. Add: no filters, no case type or amount, attachments' 15-minute URLs, launched 2026-09-30 (SU9, SU10).
4. **Finance pack P-ref-28, P-api-23 and P-ful-18, and the skill lines that carry them** (`fees-and-charges/references/where-fees-land.md`, `money-reads/references/roles-and-tools.md`, `tax-lines/references/reads.md`, `tax-lines/references/eu-uk.md`). They hold the Economics role open between Brand Analytics and Selling Partner Insights, with "the live `createQuery` result decides it". Evidence beyond the two pages now exists. Issue #567: on 2025-04-23 an Economics query was refused with "Unauthorized to access requested fields", and Amazon's Solutions Architect answered the same day: "Economics dataset are under Selling Partner Insights role". Earlier commenters had the refusal while Sales and Traffic answered. The pages still disagree, as they say. The finding: Economics is outside the five roles unless the app adds Selling Partner Insights (SU33). P-ref-28's "Data Kiosk Sales and Traffic and seller analytics (Brand Analytics)" holds for Sales and Traffic by the correction page. For Seller Analytics it rests on the operations page alone, since the correction predates the dataset (SU54).
5. **Finance pack P-ref-29's scope.** It lists refunds, claims, chargebacks and sourcing cost. It does not name remeasurement, value disputes, the IDR pages or attaching evidence; SU12 adds them by the same command-verified scan.
6. **Amazon's Role Mappings for Types is stale** against its own deprecation schedule (SU40). The door's statement of `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE` / `_XML` as removed 2026-11-11 is right; the roles page still lists them.
7. **Finance pack refunds-and-reimbursements references/claims.md, and every claims source naming "Inventory Adjustments reports"** (e.g. vendor guides read today). Those report types were removed in 2023 (SU42). The stock pack already holds the removal; nothing in the packs is wrong. A vendor source that names them describes reports that no longer answer.
8. **filing-and-conduct, "Read at run time" for account status** (`GET_V2_SELLER_PERFORMANCE_REPORT` `accountStatuses`, "role per sp-api-claims-surface"). The report names Selling Partner Insights only, which is outside the five (SU49). Through the seller's app the account status is not readable; the seller reads Account Health.
9. **fee-overcharges FE18 and FE19, and B's critic note.** They build detection on Data Kiosk Economics, which needs Selling Partner Insights, outside the five (SU33). The positions should say the read is outside the app.
10. **customer-returns RT39 and §10** point to `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE` under IOT or D2C(R), which is right and outside the five (SU47). The Seller Fulfilled Prime returns reports carry the same SAFE-T columns under Pricing, inside the five, for Prime orders only (SU48).
11. **removals-disposals, its revision note** ("The Support API 'launched 2026-09-30' is downgraded to inferred (doc updatedAt and model commit date)"). The *SP-API Release Notes* (`updatedAt` 2026-11-04) say under 2026-09-30 "Launched the Support API" [read in official docs, re-read 2026-11-13]. The date is Amazon's statement, not an inference (SU9).
12. **This file's own earlier text** ("Economics: open" in §2.2; GQNVDV46U9JQ25HY as the Economics fee-type page in §4). Economics is now SPI, outside the app (SU33). GQNVDV46U9JQ25HY is the preview query's fee-type page, and the `economics` query's is GZ8Y22NL2FSRY8M5 (SU55).
13. **Within this pack, the Support API's shape and "no operation files a claim"** are restated in filing-and-conduct FL1 and § B, inbound-shortfalls IN29 and its API table, removals-disposals RM35 and its API table, value-and-reversals VR18, and fc-lost-damaged FC14. Their facts agree with SU8–SU12, with one exception: the removals launch date (item 11). Each can point to SU8–SU12 and SU56 instead of restating them.

---

## Values that move

Each value is Amazon's as read, or a vendor's where marked, with its store and date. The positions state the rule and where it is read; the value is here. "All / none named" means the page names no store.

| Value | As read | Marketplace | Date read | Source | Position |
|---|---|---|---|---|---|
| Ledger detail look-back | "for 18 months" | none named | 2026-11-13 | *FBA Reports* (2026-10-13), ledger detail | SU15 |
| FBA report generation interval | near real-time: 30 minutes; daily: four hours | none named | 2026-11-13; 2026-11-23 | *FBA Reports*, opening | SU19 |
| Fee preview refresh, start offset, request limit | "at least once every 72 hours"; `dataStartTime` "a minimum 72 hours prior to NOW"; "once per day per seller" | none named | 2026-11-13; 2026-11-23 | *FBA Reports*, fee preview | SU20 |
| Fee preview size-tier and future-fee columns | `product-size-tier`, `estimated-future-order-handling-fee-per-order`, `expected-future-fulfillment-fee-per-unit`: "US store only" | US | 2026-11-13 | *FBA Reports*, fee preview | SU20 |
| Amazon-fulfilled shipments: span, cap, delay | one month per request; 12 requests every 8 hours per selling partner account; 1–3 hours, rarely 24 | the delay sentence names JP, EU, NA | 2026-11-13 | *FBA Reports* | SU21 |
| Long-term storage request span | "should be equal to one month" | none named | 2026-11-13 | *FBA Reports* | SU22 |
| Replacements report availability | "NA and Amazon IN stores" | NA, IN | 2026-11-13 | *FBA Reports* | SU23 |
| Inventory planning availability | "Not available in the NL, PL, SE, or BE stores"; BR returns a reduced set | NL, PL, SE, BE, BR | 2026-11-13 | *FBA Reports* | SU23 |
| Removal order detail `service-speed` | "available in EU stores" | EU | 2026-11-13 | *FBA Reports* | §2.1 |
| Seller-fulfilled and Prime returns: span per request | "up to 60 days of data in a single report" | none named | 2026-11-13 | *Returns Reports* (2026-10-28) | SU47, SU48 |
| Reports API keep; document URL life | "retained for a maximum of 90 days"; URL "expires after 5 minutes" | all | 2026-11-13 | `reports_2021-06-30.json` (db2936aa) | §3, SU53 |
| `getReports` default usage plan | 0.0222 requests/s, burst 10 | all | 2026-11-13 | `reports_2021-06-30.json` | §3 |
| Deferred Transaction Report span | "up to 10 years of data" | none named | 2026-11-13 | *Payment Reports* (2026-09-09) | SU30 |
| Data Kiosk earliest start | "no more than two years ago" (Economics, Seller Analytics, Sales and Traffic) | all | 2026-11-13 | the three schemas (db2936aa) | SU34 |
| Data Kiosk result retention | `P30D` on leaf fields (36 in Economics) | all | 2026-11-13 | the schemas | SU34 |
| Economics refresh; preview reach | "refreshed daily"; preview end "no more than 120 days after today" | all | 2026-11-13 | Economics schema (db2936aa, main b13d1d10) | §3, SU55 |
| Seller Analytics return delay | "a delay of about 45 days"; return defects "trailing six months" | all | 2026-11-13 | Seller Analytics schema (db2936aa) | SU54 |
| Support API usage plan | 0.1 requests/s, burst 10, each operation (added to the model 2026-10-28) | all | 2026-11-13 | `support_2025-02-01.json` | SU10 |
| Support API `listCases` page size | `maxResults` 1–50, default 10 | all | 2026-11-13 | `support_2025-02-01.json` | SU10 |
| Support API attachment URL life | "expires after 15 minutes" | all | 2026-11-13 | `support_2025-02-01.json` | SU10 |
| Finances v2024-06-19 range | empty for a range over 180 days | all | (finance pack) | see finance P-ref-23 | §3 |
| Finances v0 `…ByGroupId` reach | "the past two years" | all | (finance pack) | see finance pack API table | §3 |
| Finances v0 removal date | 2027-08-27 (deprecated 2025-07-21) | all | 2026-11-13 | *SP-API Deprecation Schedule* (2026-09-09) | SU36 |
| Orders v0 removal date | 2027-03-27 (deprecated 2026-01-28) | all | 2026-11-13 | *SP-API Deprecation Schedule* | SU37 |
| `analytics_salesAndTraffic_2023_11_15` removal | 2026-03-27 (schedule) vs 2026-02-26 (release note 2025-08-27) | all | 2026-11-13 | both pages | SU39 |
| Reimbursements report interval (relayed) | 238 minutes | none named | 2021 (relay) | issue #1847 [opinion] | SU24 |
| Vendor look-back and latency | reimbursements 18 months / 5 days; FBA returns 18 months / 2 days; removal order detail and storage 2 years / 1 month | none named | 2026-11-13 | Fivetran [opinion] | SU17 |
| Vendor per-request caps | 30 days (all-orders, Amazon-fulfilled shipments), 60 days (seller-fulfilled returns), 365 days (others), start ≤ 2 years | none named | 2026-11-13 | Airbyte [opinion] | §3 |

## Seat's own

- The grouping of the reads by the key they carry (§2.4) is this seat's arrangement of Amazon's attribute lists. The lists are Amazon's; the grouping is not a finding.
- "What it would open, were the role added" (§5.1): the join of `caseId` to `case-id` is the seat's inference, and nothing is built on it.
- The reading that a settlement report older than the Reports API's keep is out of the API's reach (SU53) is the seat's inference from two Amazon statements.
- Which reads the claims files lean on was found by this seat's grep of the pack on 2026-11-13. A read a later revision adds needs its row here.

---

## Open questions for a first run on a real account

1. How far back each of `GET_FBA_REIMBURSEMENTS_DATA`, `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`, both removal reports, the replacements and inbound performance reports actually answers on the store: the first row's date for a request whose start the seller's run sets.
2. Whether the reimbursements report still ignores `marketplaceIds` within a region (SU24), and for a Pan-European or NA multi-store seller, which `currency-unit` values appear.
3. Whether a blank `case-id` means an automatic reimbursement (finance P-ref-20 leaves it open), and whether `case-id` values match the Case Log's case numbers.
4. Whether `TRANSACTION_UPDATE` subscribes on the app's roles. It is not on the types page.
5. Whether a Data Kiosk Economics query is refused on the seller's connection without SPI, as issue #567 reports (SU33).
6. Whether the removal shipment detail's counts for one past month change between two requests a week apart on this store (SU25).
7. Whether `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA`'s `expected-quantity` / `received-quantity` match v0 `QuantityShipped` / `QuantityReceived` for the same shipment and SKU.
8. Whether the fee preview's dimensions differ from Catalog Items' `package` dimensions for the same ASIN (SU6), and which one the storage fee report uses.
9. The rate the seller is actually given for `createReport` and the claim reports (`x-amzn-RateLimit-Limit`), and whether a second same-type request inside four hours returns the same document or `CANCELLED`.
10. Whether the store's Reimbursements report carries any column past the 18 the SP-API page lists (the header row).
11. Whether the app can be given Selling Partner Insights (Economics, the Seller Performance Report) and Selling Partner Support (Restricted) (the Support API), and what Amazon asks for each (SU33, SU49, SU60). This is the office's and the door's question, not a run's.
12. Whether a Seller Analytics query is accepted on Brand Analytics alone (SU54).
13. How far back `listCases` lists a seller's cases, and whether `caseId` equals the Case Log number and the Reimbursements report's `case-id` (SU56, §5.1). Needs the restricted role.
14. Whether a settlement report generated more than the Reports API's keep ago is still returned by `getReports` (SU53).
15. Whether the Prime returns reports answer, empty, for a seller with no Seller Fulfilled Prime orders (SU48).

---

## Pages read

| Title | Address | Publisher | Page date | Read on | Used for |
|---|---|---|---|---|---|
| Role Mappings for SP-API Operations | https://developer-docs.amazon.com/sp-api/docs/role-mappings | Amazon | 2026-10-28 | 2026-11-13 | §1, §2, SU1–SU8, SU13 |
| Role Mappings for SP-API Types | https://developer-docs.amazon.com/sp-api/docs/role-mappings-for-types | Amazon | 2026-09-09 | 2026-11-13 | §2, SU2, SU3, SU31, SU40 |
| Roles in the Selling Partner API | https://developer-docs.amazon.com/sp-api/docs/roles-in-the-selling-partner-api | Amazon | 2026-11-12 | 2026-11-13 | §1, SU11, SU46 |
| Fulfillment by Amazon (FBA) Reports | https://developer-docs.amazon.com/sp-api/docs/report-type-values-fba | Amazon | 2026-10-13 | 2026-11-13 | §2.1, §3, SU2–SU3, SU15, SU19–SU23, SU26–SU27 |
| Payment Reports | https://developer-docs.amazon.com/sp-api/docs/report-type-values-payment | Amazon | 2026-09-09 | 2026-11-13 | SU29, SU30 |
| Settlement Reports | https://developer-docs.amazon.com/sp-api/docs/report-type-values-settlement | Amazon | 2026-10-14 | 2026-11-13 | §2.1, §3, SU53 |
| Returns Reports | https://developer-docs.amazon.com/sp-api/docs/report-type-values-returns | Amazon | 2026-10-28 | 2026-11-13 | §2.1, §3, SU47, SU48 |
| Inventory Reports | https://developer-docs.amazon.com/sp-api/docs/report-type-values-inventory | Amazon | 2026-10-28 | 2026-11-13 | §3 (freshness wording) |
| Reports API | https://developer-docs.amazon.com/sp-api/docs/reports-api | Amazon | 2026-09-09 | 2026-11-13 | §3 |
| SP-API Deprecation Schedule | https://developer-docs.amazon.com/sp-api/docs/sp-api-deprecations | Amazon | 2026-09-09 | 2026-11-13 | §8, SU36–SU40, SU42 |
| SP-API Release Notes | https://developer-docs.amazon.com/sp-api/docs/sp-api-release-notes | Amazon | 2026-11-04 | 2026-11-13 | §4, §8, SU9, SU35, SU37, SU39, SU41 |
| Support API | https://developer-docs.amazon.com/sp-api/docs/support-api | Amazon | 2026-09-30 | 2026-11-13 | §5.1, SU8 |
| Retrieve and Review Selling Partner Support Cases | https://developer-docs.amazon.com/sp-api/docs/retrieve-review-support-cases | Amazon | 2026-09-30 | 2026-11-13 | SU11 |
| Retrieve the Contact History for a Support Case | https://developer-docs.amazon.com/sp-api/docs/retrieve-contact-history-support-case | Amazon | 2026-09-30 | 2026-11-13 | SU11 |
| Data Kiosk API | https://developer-docs.amazon.com/sp-api/docs/data-kiosk-api | Amazon | 2026-10-20 | 2026-11-13 | §4, SU33 |
| Correction: Data Kiosk role requirements | https://developer-docs.amazon.com/sp-api/changelog/correction-data-kiosk-role-requirements | Amazon | undated (refers to 2024-06-19) | 2026-11-13 | SU33 |
| Notification Type Values | https://developer-docs.amazon.com/sp-api/docs/notification-type-values | Amazon | 2026-10-28 | 2026-11-13 | §2.3, SU31 |
| Fulfillment Inbound API | https://developer-docs.amazon.com/sp-api/docs/fulfillment-inbound-api | Amazon | 2026-09-09 | 2026-11-13 | §2.2 |
| Migrating Fulfillment Inbound workflows | https://developer-docs.amazon.com/sp-api/docs/migrating-fulfillment-inbound-workflows | Amazon | 2026-09-09 | 2026-11-13 | §2.2 |
| Product Fees API | https://developer-docs.amazon.com/sp-api/docs/product-fees-api | Amazon | 2026-09-09 | 2026-11-13 | §2.2 |
| Finances API | https://developer-docs.amazon.com/sp-api/docs/finances-api | Amazon | 2026-09-09 | 2026-11-13 | §2.2 |
| selling-partner-api-models (models and Data Kiosk schemas) | https://github.com/amzn/selling-partner-api-models (commit db2936aa) | Amazon | 2026-10-29 | 2026-11-13 | SU6, SU10, SU12, SU13, SU32, SU34 |
| Issue #2974 (report look-back unclear) | https://github.com/amzn/selling-partner-api-models/issues/2974 | GitHub / Amazon Developer Support | 2022-07-10/15 | 2026-11-13 | §1, SU16 |
| Issue #1847 (reimbursements report and marketplaces) | https://github.com/amzn/selling-partner-api-models/issues/1847 | GitHub | 2021-09-13/21 | 2026-11-13 | SU24 |
| Issue #4333 (removal shipment detail inconsistent) | https://github.com/amzn/selling-partner-api-models/issues/4333 | GitHub / Amazon Developer Services | 2024-11-17/20 | 2026-11-13 | SU25 |
| Issue #5323 (removal shipment detail counts) | https://github.com/amzn/selling-partner-api-models/issues/5323 | GitHub / Amazon Developer Services | 2026-07-20/21 | 2026-11-13 | SU25 |
| Issue #5344 (removal "Return" rows lack address) | https://github.com/amzn/selling-partner-api-models/issues/5344 | GitHub | 2026-08-03 | 2026-11-13 | SU26 |
| Issue #4747 (ledger `eventType` empty refused) | https://github.com/amzn/selling-partner-api-models/issues/4747 | GitHub | 2025-04-21 | 2026-11-13 | SU27 |
| Issue #5339 (ledger range time shift) | https://github.com/amzn/selling-partner-api-models/issues/5339 | GitHub / Amazon Developer Services | 2026-07-31 | 2026-11-13 | SU28 |
| selling-partner-agentic-toolkit (tree, commits, support-case-helper, finance-month-end-closer) | https://github.com/amzn/selling-partner-agentic-toolkit | Amazon | last push 2026-11-11 | 2026-11-13 | §5.3, SU14 |
| Amazon Selling Partner – Reports (connector docs) | https://fivetran.com/docs/connectors/applications/amazon-selling-partner/reports | Fivetran | undated | 2026-11-13 | §3, SU17 |
| Amazon Seller Partner source docs | https://docs.airbyte.com/integrations/sources/amazon-seller-partner | Airbyte | undated (connector 6.0.x) | 2026-11-13 | §3, SU19 |
| 费用诊断 (Fee/inventory diagnosis) | https://www.lingxing.com/help/article/FeeDiagnosis | 领星 Lingxing | undated | 2026-11-13 | §7, SU43 |
| 领星FBA费差异功能介绍 | https://www.lingxing.com/help/article/FBAFeeDifference | 领星 Lingxing | undated | 2026-11-13 | §7, SU29, SU44 |
| 领星ERP怎么样？(review quoting Lingxing FAQ) | https://www.sellerhow.com/lingxing-erp-review-zh/ | sellerhow.com | 2026-09-18 | 2026-11-13 (search result) | §7 |
| Amazon Remeasurement Request | https://amzdudes.com/amazon-remeasurement-request-how-to-fix-incorrect-dimensions-get-reimbursements/ | AMZDUDES | 2026-05-22 | 2026-11-13 | §6 |
| Seller Forums search results on remeasurement (News_Amazon 90-day post relayed; CA/UK threads) | https://sellercentral.amazon.ca/seller-forums/discussions/t/ae6a5220-e749-4726-8660-d5a64e35dd6c and related results | Amazon Seller Forums (via search) | various | 2026-11-13 (search snippets only) | §6 |
| Reimbursement filing route guides | https://myamazonguy.com/amazon-reimbursement/amazon-reimbursement-guide-2024/ ; https://m.sellersprite.com/en/blog/how-to-claim-amazon-fba-reimbursements-2025 ; https://spctek.com/how-to-get-your-money-back-for-amazon-damaged-inventory/ | My Amazon Guy; SellerSprite; SPCTEK | 2024–2026 | 2026-11-13 (search snippets) | §6 |
| FBA reimbursement audit guide | https://www.sellerlabs.com/blog/fba-reimbursement-audit-amazon-owes-you-2026/ | Seller Labs | 2026 | 2026-11-13 (search snippet) | §3 (window vs look-back conflation) |
| Amazon Selling Partner Plugin for Claude | https://sellersonar.com/blog/amazon-selling-partner-plugin/ | Seller Sonar | 2026 | 2026-11-13 (search snippet) | §5.3 |
| Amazon Seller MCP guide | https://www.sellerforge.ai/blog/amazon-seller-central-mcp-guide | SellerForge | 2026 | 2026-11-13 (search snippet) | §5.3 |
| Reimbursements report (G200732720) | https://sellercentral.amazon.com/help/hub/reference/external/G200732720 | Amazon | — | **unread** (plain GET; stays unread, help-hub content call closed 2026-11-10; JS shell on US, UK, /gp routes) | SU45 |
| Customer returns (G200453320) | https://sellercentral.amazon.com/help/hub/reference/external/G200453320 | Amazon | — | **unread** (plain GET; stays unread, help-hub content call closed 2026-11-10; JS shell) | SU45 |
| FBA inventory reimbursement policy (G200213130) | https://sellercentral.amazon.com/help/hub/reference/external/G200213130 | Amazon | — | **unread** (plain GET; stays unread, help-hub content call closed 2026-11-10; JS shell) | SU45 |
| Economics preview supported fee types (GQNVDV46U9JQ25HY) | https://sellercentral.amazon.com/help/hub/reference/GQNVDV46U9JQ25HY | Amazon | — | **unread** (named in the schema; not fetched) | §4, SU55 |
| Economics supported fee types (GZ8Y22NL2FSRY8M5) | https://sellercentral.amazon.com/gp/help/GZ8Y22NL2FSRY8M5 | Amazon | — | **unread** (named in the schema; not fetched) | §4, SU55 |
| Performance Reports | https://developer-docs.amazon.com/sp-api/docs/report-type-values-performance | Amazon | 2026-10-28 | 2026-11-13 | §2.1, SU49 |
| Data Kiosk schemas: Economics on main | https://github.com/amzn/selling-partner-api-models/blob/main/schemas/data-kiosk/analytics_economics_2024_03_15.graphql (b13d1d10) | Amazon | 2026-11-11 | 2026-11-13 | §4, SU55 |
| Data Kiosk schemas: Seller Analytics, Sales and Traffic | the models clone, `schemas/data-kiosk/` (db2936aa) | Amazon | 2026-10-29 | 2026-11-13 | §3, §4, SU54, SU57 |
| Fulfillment Outbound models (2020-07-01, 2026-07-04) | the models clone, `models/fulfillment-outbound-api-model/` (db2936aa) | Amazon | 2026-10-29 | 2026-11-13 | §2.2, SU51 |
| Issue #567 (Data Kiosk Economics 403) | https://github.com/amzn/selling-partner-api-models/issues/567 | GitHub / Amazon Developer Support | 2024-05-03 to 2025-04-23 | 2026-11-13 | §4, SU33 |
| Issue #5422 (Support API role request) | https://github.com/amzn/selling-partner-api-models/issues/5422 | GitHub | 2026-10-26 / 2026-11-02 | 2026-11-13 | §5.1, SU60 |
| Discussion #338 (settlement report older than retention) | https://github.com/amzn/selling-partner-api-models/discussions/338 | GitHub | 2023-10-23 (no answer) | 2026-11-13 | §3, SU53 |
| Settlement reports (vendor help) | https://support.daasity.com/knowledge/integration-amazon-seller-central-settlement ; https://help.sarasanalytics.com/en_US/amazon-selling-partner/faq-%E2%80%93-flatfilev2settlementreport- | Daasity; Saras Analytics | undated | 2026-11-13 (search-result summaries only) | §3, SU53 |

---

## Verification (2026-11-13)

An adversarial check of this file, the same day, from public pages only (no SP-API call, no login, no seller data).

**Checked and confirmed.**

- Page dates: *FBA Reports* 2026-10-13, *Role Mappings for Types* 2026-09-09, *Role Mappings for Operations* 2026-10-28 (350 operation rows), *Roles in the Selling Partner API* 2026-11-12, *Deprecation Schedule* 2026-09-09, *Release Notes* 2026-11-04, *Support API* 2026-09-30, both Support tutorials 2026-09-30, *Payment Reports* 2026-09-09, *Settlement Reports* 2026-10-14, *Returns Reports* 2026-10-28, *Inventory Reports* 2026-10-28, *Notification Type Values* 2026-10-28, *Data Kiosk API* 2026-10-20 (each from the page's `.md` `updatedAt`).
- SU2, SU3: every role named, report by report, on *FBA Reports*; MFN returns by return date IOT, D2C(R) on *Returns Reports* and the types page.
- SU4, SU5, SU7, SU37 roles on the operations page: v0 inbound reads and all 45 v2024-03-20 rows AF only; `listFinancialEvents` AISP (EU only), AF (NA, FE only), FA; `…ByOrderId` FA only; `getMyFeesEstimateForSKU` and Orders the same twelve roles; `getMyFeesEstimates` PR, PL.
- Report quotes on *FBA Reports*: ledger "for 18 months"; "Content updated daily" (reimbursements, returns, replacements, inbound performance); 72 hours and once per day (fee preview); "equal to one month" (long-term storage); one month, 12 per 8 hours, Seller Central counted, one to three hours (Amazon-fulfilled shipments); "NA and Amazon IN stores"; "can be requested or scheduled" (storage fees only); "will not include canceled returns or disposed items"; the 30-minute and four-hour generation intervals; the `eventType: ""` example still printed. Request-only status of every other claims report. The reimbursements report lists 18 columns, `approval-date`, `reimbursement-id`, `case-id` and `original-reimbursement-id`/`-type` among them.
- SU8–SU11 against `support_2025-02-01.json` and the pages: three operations, POST `listCases` with `sortOrder`, `maxResults` (1–50, default 10) and `nextToken` only; 0.1/s burst 10 (added to the model 2026-10-28); `Case` and `Contact` properties as stated, no `status` on `Contact`; `downloadUrl` 15 minutes; roles page "retrieve, search, and manage"; tutorials "Support role", contact `VALID`/`EXPIRED`, case `id`; "Sellers only", "Static", "all Amazon stores"; launch note 2026-09-30.
- SU12, SU13: 394 operations in the models; the only operations whose id or description matches claim/reimburs/dispute/remeasur/sourcing cost/case are the three Support reads, Shipping v2 `createClaim`, and incidental matches (vendor DF `getOrders`, Easy Ship, `createRestrictedDataToken`) that touch no claim. `createClaim` body, enums and "off-Amazon" `declaredValue` as stated; `createClaim` absent from the operations page.
- `amzn/selling-partner-api-models` on `main`: one commit after db2936aa, b13d1d10 (2026-11-11), which changes only the Economics schema (new `PreviewFeeType` values for deal, coupon, removal, disposal and fuel fees; a dynamic-sandbox directive). No operation added; SU12 and SU13 hold on `main`.
- SU14: toolkit last push 2026-11-11, 39 stars, the twelve skills named; no skill on reimbursements or claims; `support-case-helper` 1.0.0 Help Center message.
- SU32: v2024-03-20 `Item` has `quantity` and no received quantity; v0 carries `QuantityReceived`; the status values named.
- SU33, SU35: Data Kiosk operations list Brand Analytics; the correction names Selling Partner Insights for Economics; the release-note items of 2026-09-30, 2025-12-22, 2026-01-28 and 2026-02-23.
- SU36–SU40, SU42: every deprecation date in §8 against the schedule; the 2026-02-26 date in the 2025-08-27 release note; the types page still lists the SnS, old settlement and `ORDER_STATUS_CHANGE` entries; `GET_DATE_RANGE_FINANCIAL_TRANSACTION_DATA` on neither the types page nor *Payment Reports*.
- SU30 and the 10-year Deferred Transaction Report line on *Payment Reports*.
- SU24, SU25, SU26, SU27, SU28, SU16: issues #1847, #4333, #5323, #5344, #4747, #5339, #2974 — authors, dates and quotes as stated.
- SU17 and the §3 Fivetran table: every row's aggregation, look-back and latency; the Airbyte per-request caps (30, 30, 30, 60, 365 days), the two-year start default and the cross-application cooldown sentence.
- SU43, SU44 and §7: the Lingxing quotes (one SKU per case, ten a day, one diagnosis per shipment, the CASE ID join, 90-day closed-shipment display, nine-month window restated, API every 7 days, report daily, `Fee Adjustment`).

**Changed.**

- Summary: "Ten of the FBA report types answer to Pricing or Amazon Fulfillment" → eight of the §2.1 claims types, plus Amazon-fulfilled shipments with IOT; customer-shipment-sales added to the AF-only list (it was in SU2 but not the summary).
- §2.3 and SU31: *Notification Type Values* has 26 type headings, not 25; `DATA_KIOSK_QUERY_PROCESSING_FINISHED` is not among them; "reimbursements included" for `TRANSACTION_UPDATE` is not on the page and is now [inferred].
- §2.2: `createClaim`'s sibling operations — one of them names Amazon Logistics or Product Listing, not only AL or D2C(R).
- §3: the Reports API's 90-day keep and 5-minute URL are now sourced to `reports_2021-06-30.json` (the *Reports API* overview page does not state them); "every field carries `@resultRetention`" → its 36 leaf fields; line numbers pinned to db2936aa.
- §3 Lingxing: the 90-day display rule and the nine-month window quoted in Lingxing's words; the window marked as a moving value owned elsewhere, marketplace unstated.
- §5.3 and SU14: the toolkit quote restored to "By default this skill calls no SP-API tools".
- §6 remeasurement row: the 90-day value kept as relayed evidence with stores and date; the window's rule left to the fee-overcharges area.
- §8: added the `SETTLEMENT_ID` contradiction (release note 2026-07-29 vs the model's rollback at db2936aa) and marked the "claim-related metrics" note's meaning [inferred].
- SU15, SU17, SU19–SU22, SU34: rewritten to state the rule and where the value is read, with the value kept as evidence (page date, date read, marketplace).
- SU42: "the Inventory Ledger replaced them" is not on the deprecation schedule → [inferred], from the stock pack; the six types named in full.
- Open question 1: the fixed 24-month request reach (a reading ceiling of ours) → a start the seller's run sets.
- Corrections item 7: a "should not repeat" instruction → a fact about the vendor sources.
- No path on this machine was found in the file.

**Remaining doubts.**

- §1's "byte-identical to the survey's copies of 2026-11-09" was not re-checked (the survey's copies were not opened).
- The Seller Central help pages (G200732720, G200453320, G200213130, GQNVDV46U9JQ25HY) were not re-fetched; SU45 stands on the original seat's fetches.
- The Claude directory connector's eight tools, the SellerForge/Sellerise/Novadata claims, and the myamazonguy/sellersprite/spctek/sellerlabs/sellersonar/amzdudes snippets were not re-read; they stay [opinion].
- The toolkit's code search was run over its `.md`, `.json`, `.ts`, `.py` and `.yaml` files only.
- SU25's second Amazon quote (#5323, "There shouldn't be restrictions to retrieve the reports") answers a report failure, not the changing counts; its weight on SU25 is small.
- §6's route column (menus, "after `CLOSED`") is the stock pack's and practitioners'; it describes Seller Central, which moves, and was not re-read.

---

## Revision (2026-11-13)

After the completeness critic's first round. Routes: plain GET of developer-docs pages and `.md` twins, GitHub (`gh api`), and third-party pages; a grep of the models clone at db2936aa and main b13d1d10 on GitHub. No POST to an Amazon host, no help-hub content call, no SP-API host, no sign-in, no seller data. The session's web-search budget ran out after one search; the remaining evidence came from Amazon's pages, the models and GitHub.

**Added.**

- A statement of what this file is home for: roles, the Support API's shape, and "no operation files a claim" (SU12).
- §2.1 rows: the seller-fulfilled returns report corrected (requested or scheduled, per-request span, columns; outside the five), the Prime returns reports (Pricing, in the app), the Seller Performance Report (SPI, outside), the stranded and reserved inventory reports.
- §2.2 rows: the Fulfillment Inbound transport, placement, pallet, prep and plan-item reads; v0 bill of lading and labels; FBA Inbound Eligibility; the Fulfillment Outbound (MCF) reads with their lost and damaged statuses; the Reports API lifecycle; `getOrderMetrics`; liquidation events in Finances v0. Data Kiosk is split by dataset: Economics SPI (outside), Sales and Traffic BA, Seller Analytics BA by the operations page only.
- §2.4, the keys each read carries, and that a reimbursement row names no store (critic B, cross-border).
- §3: returns-report spans, settlement reports versus the Reports API's keep, Economics' daily refresh, Seller Analytics' return delay, and the Support API's lack of a date or marketplace parameter.
- §4: the claim fields in Sales and Traffic are A-to-z and chargeback claims (this closes an [inferred] in §8); the fee-type help pages corrected (GZ8Y22NL2FSRY8M5 for `economics`, GQNVDV46U9JQ25HY for the preview), both unread; the `PreviewFeeType` list on main; issue #567, where Amazon developer support puts Economics under Selling Partner Insights.
- §5.1: issue #5422 on requesting the restricted Support role; the `caseId` example.
- §7: the practitioners' choices set side by side (tying a payment to a case, valuing a dimension overcharge, confirming a fee refund) (critic E).
- Positions SU47–SU60.
- *Values that move*, *Seat's own*, corrections 8–13, open questions 11–15 and new pages read.

**Changed.**

- The summary names the four reads outside the five and the Prime returns reports inside them.
- §6 now keeps only the "API" column, which is this file's. Its routes, windows and limits are pointers to filing-and-conduct, value-and-reversals, fee-overcharges, inbound-shortfalls and removals-disposals (critic D homes). The relayed 90-day remeasure value moved out to fee-overcharges.
- SU10, SU15, SU17, SU19–SU23, SU34, SU36 and SU37 now state the rule and where it is read, with their values moved to *Values that move* (critic F).
- SU12 is now the pack's home for the statement "no operation files a claim, opens a case, attaches evidence or enters a sourcing cost".
- SU33: the Economics role is Selling Partner Insights by the correction and Amazon developer support, outside the five, and the page contradiction is kept.
- SU43 and SU44 are reframed as one tool's choice among others.
- SU45: the three help pages stay unread, and the closed route is named.
- Correction 4 (finance P-ref-28, P-api-23, P-ful-18) now carries the #567 evidence.
- §8: the planned removal dates moved to *Values that move*.

**Withdrawn.** None.

**Not changed, by the ruling.** G200732720, G200453320, G200213130, GJQTPXHTS6K5PQFD, GQNVDV46U9JQ25HY and GZ8Y22NL2FSRY8M5 stay unread. The customer-returns file's readings of the first three came through the help hub's content call, which the office closed on 2026-11-10, and this file takes nothing from them.

## Revision (2026-11-23)

- *FBA Reports* re-read verbatim at `https://developer-docs.amazon/sp-api/docs/report-type-values-fba`, where the `.com` address now redirects (page updated 2026-10-13): the opening's two generation limits, and the fee preview, reimbursements, FBA returns, replacements, removal and ledger detail entries.
- Added SU61: a report already made within its waiting period, `getReports`, and which entries read "Content updated daily" or "in near real-time".
- The skills now carry the two generation limits (SU19) and the fee preview's refresh, start offset and request limit (SU20) beside their place and the day read; the *Values that move* rows for both gain the re-read date.
