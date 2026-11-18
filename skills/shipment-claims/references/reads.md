# Reads: what the SP-API shows for a shipment or removal claim, and what it cannot do

## Inbound

- Shipped against received per SKU is `QuantityShipped` beside `QuantityReceived` in the v0 items list (Amazon Fulfillment) (IN20).
- No Fulfillment Inbound operation (v0 or 2024-03-20) returns a delivery, check-in, receiving or closed date, so the window's start cannot be read from the API (IN10).
- Its proxies are the first `Receipts` event in `GET_LEDGER_DETAIL_VIEW_DATA`, the selected delivery window or carrier appointment (`getShipment`, `listTransportationOptions`) and the carrier's tracking; the ledger proxy is read in Amazon's documents, not yet seen on a live account (IN10).
- Distributor-damaged and carrier-damaged arrivals are read as dispositions in `GET_LEDGER_DETAIL_VIEW_DATA` (Amazon Fulfillment); their spelling there is read in Amazon's documents, not yet seen on a live account (IN2).
- A small-parcel tracking ID is read at `getShipment` `trackingDetails.spdTrackingDetail` and written with `updateShipmentTrackingDetails` (IN5).
- In the 2024-03-20 model each SPD tracking ID carries `trackingNumberValidationStatus` (`VALIDATED`, `NOT_VALIDATED`, `NOT_SUPPORTED`, the last meaning Amazon cannot find tracking for it), and the model asks that a number not validated after a stated time be verified and updated (IN6).
- No operation exposes a shipment's research eligibility or eligibility date, the "Investigation completed" line, the reconciliation result, the claim window or Amazon's verified delivery date; these are Seller Central views under Shipping Queue, Contents or Reconcile (IN29).
- The payment for an inbound claim is read in `GET_FBA_REIMBURSEMENTS_DATA`, which answers to Pricing or Amazon Fulfillment (IN21, SU3).

## Removals and disposals

- Removal Order Detail is order by SKU by disposition, with requested, cancelled, disposed, shipped and in-process quantities and the fee; Removal Shipment Detail is shipment by SKU, with carrier and tracking; both need Pricing or Amazon Fulfillment and can only be requested (RM20, SU3).
- Amazon's FBA Reports page gives no value sets for `order-type`, `order-status`, `order-source` or `disposition`; practitioners (GorillaROI; SellerSpace; InventoryLab) report Return, Disposal and Liquidations (also Donation), Pending, Completed and Cancelled (spelling varies), and Sellable and Unsellable (RM21).
- Neither removal report has a store or marketplace column, and ERPs report that in NA and EU unified accounts they cannot tell which store a removal belongs to (Lingxing; SellerSpace) (RM22).
- Removal Shipment Detail carries no shipment-id column and no delivery date; read in Amazon's documents, not yet seen on a live account (RM15).
- The ledger detail's `VendorReturns` event type is where removals post, by the research's reading of the FBA Reports page; read in Amazon's documents, not yet seen on a live account (RM32).
- `listTransactions` links removal lines by the related identifier `REMOVAL_SHIPMENT_ITEM_ID`; Finances v0 links them by `MerchantOrderId` (the removal order id) and `RemovalShipmentItemId` (RM30).
- Finances v0 `listFinancialEvents` names Finance and Accounting, Amazon Fulfillment in NA and FE, and AISP in the EU (SU5).
- Practitioners report removal reimbursements under the reasons `REMOVAL_ORDER_LOST` and `REMOVAL_ORDER_DAMAGED`; Amazon publishes no reason list (Synder; Lingxing) (RM31).
- Liquidation events and their join: references/disposals.md.

## What no operation does

- No operation opens an inbound or removal claim, requests inbound research, attaches evidence, cancels a removal order or contests a dangerous-goods classification; each is the seller's step in Seller Central (IN29, RM35, SU12).
- Reading a filed case is the Support API's (`listCases`, `getCase`, `listContacts`), on Selling Partner Support (Restricted), a role outside the five; it would open the status, dates, subject, contacts and attachments of the seller's cases, and nothing here is built on it (SU8, IN13).
- AWD inbound counts need Amazon Warehousing and Distribution, a role outside the five (IN27).
- AWD inbound and its claim rule: references/inbound-programs.md.
