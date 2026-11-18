# Inbound claims: scope, window, research, evidence, carriers, overages

## Scope at the door

- Amazon's FBA reimbursement policy covers items lost or damaged "at a facility or by a carrier operated by Amazon or on behalf of Amazon", one of its conditions being that the seller sent "the exact items and quantities stated in your shipping plan" (US policy PDF 2024-12-18; DE 2025-02-24) (IN1).
- Arrivals classed "distributor damaged" or "damaged by inbound carrier" were damaged before Amazon received them; they are unfulfillable and removed, and the reimbursement route Amazon names is the seller's carrier (NR_Amazon, US, 2025-04-11) (IN2).
- Loss before delivery, while the goods are with a carrier or forwarder the seller engaged, is outside the policy's scope sentence and is claimed under the seller's contract with that carrier; that scope reading is the research's inference from the sentence (IN39).
- Amazon's policy puts shipment-to-Amazon claims in its pre-order class, valued at sourcing (earlier manufacturing) cost; the "estimated proceeds" sentence is struck in the rendered US 2024-12-18, US 2025-02-24 and JP 2025-02-19 texts, so it is the pre-2025 basis (IN21).
- What that basis pays, and the cap: ../claim-value/SKILL.md.

## The window, store by store

- The window for units missing from an inbound shipment is a per-store length counted from verified delivery to the fulfilment centre, and the request is filed after the shipment is closed; no operation states it (IN7).
- US: stated by Amazon moderator Indy_Amazon (2026-08-13), by gs.amazon.cn articles of 2025-03 and 2025-08 marked for the US store, and by a seller quoting the help page (2024-09-26); read in Amazon's documents, not yet seen on a live account (IN7).
- UAE, Saudi Arabia and Egypt: Amazon's post *Update on reimbursement claim window eligibility on FBA* (posted 2024-08-06, in force from 2024-09-05) sets a minimum and a maximum count of calendar days from the delivery date, issued as three threads, one per store (IN8).
- None of Amazon's News posts on claim windows for the US, Canada, the UK, Sweden or Australia names a window for shipments to Amazon (IN9).
- UK: the redline of 2024-12-11 changes the claim windows from 2025-01-09 "except for shipment to Amazon claims" and does not state the inbound length (IN35).
- EU stores and JP: the EU redline set of 2024-08-20 carries no Shipment to Amazon page and the JP policy of 2025-02-19 names the claims with no length; a UK staff post of 2025-06-06 gives a filing limit for lost or damaged inventory naming no kind and no start, and a UK seller relayed a Seller Central refusal by age since arrival (2025-01-08) (IN36).
- Where today's value is read for the seller's store: Amazon's help page *FBA inventory reimbursement policy: Shipment to Amazon claims* (GEYPWTSQRTXXXMVB), which cx cannot read and the seller sees signed in; the store's Seller Forums News post on claim windows, read by plain GET; and the shipment's eligibility date on its Contents tab, which the seller sees (IN7, IN11).
- Practitioners state inbound windows no Amazon page read supports, each theirs: Refunzo (2026-01-18), 百运网 (2026-05-27), Helium 10 and SELLERLOGIC for the EU, and AMZ123 (2025-05-19) (IN31).

## Closed, eligible, researched

- Amazon's pages define `CLOSED` as all units received or, where counts disagree, a timeout from shipment creation whose length the pages state differently: sell.amazon.com *How to track FBA shipments* (modified 2025-10-03), gs.amazon.cn (2025-08) and a staff post (2023-10-10); the v0 model gives no timeout, and status per shipment is read with `getShipments` (v0) or `getShipment` (2024-03-20) (IN14).
- A shipment can sit Delivered for some days before Checked-in, longer at peak, up to a maximum Amazon's Chinese article states (gs.amazon.cn, 2025-08); with a partnered carrier it shows Shipped at pickup, with the seller's own carrier once valid tracking is entered (IN32).
- Seller Central shows per shipment whether it is eligible for investigation and an estimated date; staff call that date standard procedure and say discrepancies "can auto-correct during the receiving process, but it's not guaranteed" (Angie_Amazon, US, 2026-04-09) (IN11).
- "Investigation completed – shipment contents counted and confirmed" means Amazon matched boxes to the plan and counted the units; the units are then no longer eligible for research, Selling Partner Support adds units it locates, and otherwise Amazon deems them short-shipped and pays nothing (Julia_Amzn, UK, 2024-08-20) (IN12).
- Submitting a research request creates a Selling Partner Support case whose number shows on the Contents tab; staff give the research's duration as a range, not a rule, read on sell.amazon.com's tracking guide and staff posts, and say not all discrepancies are reimbursed (IN13, FL30).
- Amazon's Chinese article says a request sent to Seller Support will likely be sent back to the shipment's item page, and that the research does not change the seller's existing inventory (gs.amazon.cn, 2025-08) (IN18).
- Amazon allows one claim per shipment and declines further claims for it (IN17, FL7).

## Evidence

- For lost units Amazon asks for the shipment ID; proof of ownership (a supplier invoice, another seller's receipt or the manufacturer's signed packing slip, with purchase date, product names, quantity, issuer and buyer); and proof of delivery: for LTL/FTL an Amazon-stamped document with box count and total weight at pickup, for small parcel active tracking IDs (IN15, FL24).
- Lost units are filed on the shipment's Contents tab, damaged units through a support case (IN15).
- Ownership documents are accepted only in a non-editable format (PDF, JPG, JPEG, PNG, TIFF); pro forma invoices and contracts are refused, and the price paid may be hidden (gs.amazon.cn, 2025-03) (IN16).
- Amazon's Chinese pages name 库存所有权证明 and, for LTL/FTL, a carrier's 提货单 that "须经亚马逊盖章"; Chinese practitioners name the forwarder's stamped 签收单 instead and report that warehouses often do not stamp at receipt (百运网, 2026-05-27; AMZ123, 2024-05-12); whether a 签收单 alone meets the LTL/FTL requirement is read in Amazon's documents, not yet seen on a live account (IN41).
- Small parcel with the seller's own carrier: the SCP page and Hopted's copy of the FBA page tie payment to the tracking ID being on the shipment; Amazon's FBA texts read list tracking IDs among what to have ready and require a unique tracking code per box, without tying payment to it in words (IN5).

## Partnered carrier against the seller's own

- For a loss by an Amazon-partnered carrier, staff told a seller to file with Amazon under the Shipment to Amazon policy, with proof of ownership and proof of delivery (TaylorR_Amazon, US, 2024-11-29); that the seller cannot claim from the partnered carrier is a seller's statement and UPS's answer as a seller relayed it, on no Amazon page read (IN3).
- A carrier's proof of delivery shows that boxes arrived, not what was in them: a Seller Support email of 2023-08-07 declined a partnered-carrier loss on that ground, and the seller later relayed a refund in progress (IN4).

## Overages

- Overages are researched through the same Action required menu ("Extra units shipped"; shortages under "Units not shipped" or "Research missing units"), and no Amazon page read states that an overage offsets a shortage (IN19).
- The Contents tab and the v0 items list shipped against received per SKU, so an overage on one SKU and a shortage on another are separate lines (IN20).
- Practitioners count a shortfall two ways, side by side and theirs: per shipment and SKU (PrepVia, 2026-08-25; 优麦云, 2024-06-05), or across shipments, which sellers report fulfilment centres doing; no practitioner read recommends netting for a claim (IN20).
