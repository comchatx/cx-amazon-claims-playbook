# Inbound programmes: prep and labels, commingling, AWD, AGL, first mile

## Prep and labels

- For US shipments created from 2026-01-01, units arriving without proper prep and item labelling are not reimbursed if damaged or "untraceable"; shipments created before keep Amazon's prep service even if they arrive later; this covers inventory reaching US FBA through AWD, AGL, Amazon SEND and Supply Chain Portal (Jameson_Amazon, US, 2025-12-01; the boundary day is the research's reading of "created before" and "created after") (IN23).
- A plan's creation date is `createdAt` from `getInboundPlan` or `listInboundPlans`, and the prep and label owner per item is `prepOwner` and `labelOwner` (Amazon Fulfillment) (IN23).

## The end of commingling

- Amazon's UK and Canada News posts of 2025-12-08 announced that commingling ends for inventory shipped from a date the posts state, read by plain GET; brand representatives with a manufacturer barcode need no Amazon sticker, while resellers and products without one use Amazon stickers; the posts say nothing about reimbursement (IN24).
- PPC Land (2026-03-24) reports that after the change units arriving without the required barcode are flagged defective and not reimbursed; a practitioner's report (IN25).

## AWD inbound and AWD to FBA

- AWD shipment claims take the window of the MCF inventory reimbursement policy, counted from verified delivery to the AWD site, with one claim per shipment and one AWD facility claim per box, filed by support case; units lost in AWD transit to an FBA centre are reimbursed under the MCF policy and valued by its methodology (AWD service terms, 2026-01-14) (IN26, IN17).
- The "MCF inventory reimbursement policy" the AWD terms name is the page *Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS)* on supplychain.amazon.com, linked at each of its five mentions; its window, cap and valuation are its own, read there by plain GET, and its eligibility requires an MCF account "in Active state" (IN34, FL27).
- The AWD terms set a filing window for fee claims on box dimensions, counted from the charge date (section 4.2), read on the terms by plain GET (IN33).
- The AWD model returns expected and received quantity per SKU for an AWD inbound shipment (`getInboundShipment` with `skuQuantities=SHOW`) in product units, cases or pallets, and Amazon's tutorial says no AWD report is in the API; the role is Amazon Warehousing and Distribution, outside the five, and would open that count (IN27).
- AWD to FBA replenishment shipments carry FBA shipment IDs; for missing units on them staff opened cases and asked for proof of ownership, not proof of delivery (KJ_Amazon, US, 2025-02-13) (IN28).

## Amazon Global Logistics

- Under the *Amazon Global Logistics Freight Service Terms* (dated 2026-01-14), Amazon bears risk of loss only from receipt at Origin until delivery at Destination, which means an Amazon facility; for China-origin ocean carriage the contracting party is Beijing Century Joyo Courier Co., Limited, and claims go only against that party, not the carrier (IN37).
- For a sealed container Amazon could not count, delivered with the seal intact, Amazon is not liable for shortages or damage unless proximately caused by its own independent action, nor for loss caused by inadequate packaging (IN37).
- An AGL Freight loss or damage claim is a written notice within a period counted from delivery, or from the scheduled delivery date for lost cargo; legal action has its own period from Amazon's written disallowance; a credited amount not contested in writing within a stated period is a complete settlement (IN38).
- Recovery is limited per shipment for an ocean bill of lading to the US unless higher liability was agreed in writing at booking, otherwise by the convention or the customs-declared value, whichever is less, with a cumulative cap per period; the seller must prove negligence of Amazon, its contractor or the performing carrier, and must insure the cargo itself (IN38).
- Each AGL period and limit is read on the terms as dated on supplychain.amazon.com by plain GET; Amazon's Seller Central AGL claims page is one cx cannot read, and the seller sees it signed in (IN38).
- AGL's billing clauses: @comchatx/cx-amazon-finance-playbook, its fees-and-charges skill.

## The first mile

- By the research's reading of the policy's scope sentence, loss before Amazon signs, with a carrier or forwarder the seller engaged, falls outside it; Amazon's Chinese article names forwarder, warehouse and customs counting errors and cartons broken in transit as causes of in-box shortfalls (gs.amazon.cn, 2025-08) (IN39).
- Practitioners describe first-mile recovery as a claim against the forwarder or airline under its contract, each theirs: an exception noted on the delivery document at receipt, a short written notice for hidden damage, weight-based convention limits unless the cargo was insured, and a set of AWB or bill of lading, commercial invoice, packing list and photos (百运网, 2026-11-09); 深圳美辰物流 (AMZ123, 2023-10-27) tells a carrier problem from a warehouse problem by the tracking (IN40).
