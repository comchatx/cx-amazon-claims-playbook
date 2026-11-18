---
name: shipment-claims
description: "What Amazon owes a seller for FBA units lost, damaged or short on the way into Amazon or back out, keyed by shipment or removal order. Inbound: a shipment received short or damaged, receiving discrepancies, Research missing units on the Contents tab, CLOSED and the eligibility date, overages, proof of ownership and delivery, partnered against own carrier, small parcel against LTL, carrier-damaged arrivals, the US prep change, the end of commingling, AWD and AWD-to-FBA shipments, AGL freight, loss with a forwarder. Outbound: removals lost, short, damaged or different, grading disputes, the removal reports, cancelled removal units, removal and disposal without a unit, liquidation shortfalls, dangerous-goods disposals and stranded removals; where each window is stated per store. For any question about a shipment to Amazon that arrived short or damaged, or a removal, disposal or liquidation Amazon may owe for."
---

## Into Amazon

Amazon's policy covers units lost or damaged at a facility or by a carrier operated by or for Amazon, if, among other conditions, the seller sent the plan's items and quantities (IN1, IN39).
Arrivals classed distributor damaged or damaged by inbound carrier were damaged before receipt; Amazon names the seller's carrier as the route (IN2).
The window is a per-store length from verified delivery, filed after the shipment is closed; Amazon states it for the US and for the UAE, Saudi Arabia and Egypt, and no page read states it for the UK, the EU or JP (IN7, IN8, IN9, IN35, IN36).
No operation returns the verified delivery date, the eligibility date or the reconciliation result; Seller Central shows them (IN10, IN29).
Amazon allows one claim per shipment and declines further ones (IN17, FL7).
Window, research, evidence, carriers, overages: references/inbound.md.
Prep and labels, commingling, AWD, AGL, first mile: references/inbound-programs.md.

## Out of Amazon

A removal claim covers units lost or damaged by Amazon or a carrier Amazon used on the way to the seller's return address; each 2024 automation post says these are filed by hand (RM1, RM2).
Kinds: lost in transit; damaged in transit; damaged, different or incomplete units received; grading disputes on customer returns (RM3).
The route is "Resolve a removal order issue", keyed by removal order ID (RM4).
Windows and their anchors differ by store and date, and Amazon's US texts disagree with each other (RM6, RM7, RM8, RM10).
The claim asks for a shipment ID that no SP-API report read carries; read in Amazon's documents, not yet seen on a live account (RM14, RM15).
Windows, grading, evidence, value: references/removals.md.
Cancelled units, fees, disposals, liquidation, dangerous goods, stranded units: references/disposals.md.

## Reads and the seller's steps

No operation opens an inbound or removal claim or attaches its evidence; each is the seller's step in Seller Central (IN29, RM35, SU12).
Reports, operations, roles and their pitfalls: references/reads.md.
Calls and reports: the amazon-sp-api skill's references/door.md.
Shipment state: @comchatx/cx-amazon-stock-playbook, its stock-inbound skill.
What a claim pays: ../claim-value/SKILL.md.
Filing routes, limits and conduct: ../claim-filing/SKILL.md.
Units lost inside the network after receipt: ../warehouse-claims/SKILL.md.
Customer returns and their grading: ../return-claims/SKILL.md.
Inbound and removal fees charged wrongly: ../fee-claims/SKILL.md.
