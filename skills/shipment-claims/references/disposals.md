# Cancelled removals, fees, disposals, liquidation, dangerous goods, stranded units

## Cancelled units and per-unit fees

- Amazon cancels removal-order units that are not available for removal, for example units tied to a pending customer order; cancelled units stay in Amazon's network or were sold (Jameson_Amazon, 2024-11-12; PrepVia) (RM25).
- Removal and disposal fees now post per unit as each unit is removed or disposed, where they once posted when the whole order completed; the change date is per store, read on each store's News post by plain GET (US post 2f4edad8, article 2026-01-29; UK post 862f270b, posted 2026-04-09) (RM26).
- Under per-unit charging, a removal or disposal fee with no matching shipped or disposed unit for that order and FNSKU has no basis in Amazon's stated rule, by the research's inference from that rule; read in Amazon's documents, not yet seen on a live account (RM26, RM27).
- Fee rates and where the charge posts: @comchatx/cx-amazon-finance-playbook, its fees-and-charges skill.
- A removal fee disputed as wrongly charged: ../fee-claims/SKILL.md.

## Disposals

- The policy (US PDF 2024-12-18) excludes units disposed of at the seller's request, by Amazon's exercise of a right, or pending disposal, while practitioners (Seller Labs, 2026-03-18; Seller Investigators) claim units Amazon disposed of without a request as reimbursable; the two disagree (RM28).
- Because a grading dispute needs the unit returned, a disposed unit cannot be graded in dispute, and an automated or required disposal can remove that path; this is the research's inference from Amazon's text (RM13).

## Liquidation

- The removals page's scope sentence covers units on their way to the seller's returns address; liquidation units go to a liquidator, and no Amazon text read names a claim for liquidation units lost before the liquidator or for proceeds below the typical recovery Amazon staff describe (Topher_Amazon, 2025-06-23) (RM44).
- A liquidation buyer's damage or shortfall comes back as `RemovalShipmentAdjustmentEvent`, a negative `RevenueAdjustment` against the removal order, not as a reimbursement; a liquidation sale posts as `RemovalShipmentEvent` with `TransactionType` `WHOLESALE_LIQUIDATION` (RM29).
- The US liquidation payment event `FBALiquidationEvent` carries no quantity and no SKU (`PostedDate`, `OriginalRemovalOrderId`, `LiquidationProceedsAmount`, `LiquidationFeeAmount`); units liquidated per FNSKU are read from `RemovalShipmentEvent` lines and joined to Removal Order Detail by order id; read in Amazon's documents, not yet seen on a live account (RM45).

## Dangerous goods

- Amazon may dispose of units of a product it classes unfulfillable dangerous goods, stating the Business Solutions Agreement as the basis, and the eligibility reason code `FBA_INB_0015` asks the seller to contact Seller Support within a number of business days of the notice, read in the notice and in `getItemEligibilityPreview` reason text (Amazon Fulfillment) (RM38).
- Under the Australian Business Solutions Agreement (PDF 2024-06-12, F-7.2, F-7.3), Amazon may dispose of an Unsuitable Unit at once for a safety, health or liability risk, the seller "deemed to have consented", otherwise after a notice period; title passes to Amazon, which may keep any proceeds; other stores' agreements were not read (RM39).
- No Amazon text read makes a unit disposed of after a dangerous-goods classification reimbursable, a classification the seller holds wrong included: the US policy PDF of 2024-12-18 excludes units failing FBA product restrictions and units disposed of by Amazon's right, Seller Support's relayed text says such units "may be subject to disposal without reimbursement", and staff called an immediate disposal after DG-programme approval "the correct actions" (2026-08-10); sellers ask under the lost-and-damaged policy, with no outcome read (RM40).
- The challenge Amazon names against a dangerous-goods classification is the review: a safety data sheet or exemption sheet within the time Amazon states, failing which the units are disposed of at the seller's expense; it runs before disposal, and no route after disposal was read (Michelle_Amazon, 2025-06-06) (RM41).
- Sellers report that a removal order cannot be created, or fails, while an ASIN stands classified as dangerous goods, so units can be disposed of without having left (2024-08-02; 2025-12-04) (RM42).

## Stranded units

- By the research's reading of the policy's wording, a removal of stranded units is a removal like any other once the units leave, under the removals page's scope, windows and evidence, and a disposal under the stranded settings, or with no setting, falls in the policy's excluded classes (RM43).
- Stranding itself: @comchatx/cx-amazon-stock-playbook, its stuck-stock skill.
