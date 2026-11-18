# The valuation rule, dated

## Before the move to sourcing cost

- Before the 2025 change, pre-order losses (shipment to Amazon, FC operations, removals) were valued at "estimated proceeds": an estimated sale price from median and list prices, "minus referral fees and fulfillment fees" (VR1).
- Amazon's redlines strike that whole block, so it was the pre-2025 pre-order method, not a post-order rule (VR1).
- Amazon's redlined policy PDFs keep struck text in their text layer: a text extraction mixes old and new wording, and only a rendering shows which is live (VR28).

## Sourcing cost

- Pre-order losses are valued at sourcing cost from the date each store's text gives; the redlines regenerated on 2025-02-24 for the US, CA, UK, DE, FR, IT and ES, and the US and CA Chinese texts, carry a start after 2025-03-31 and the page name "Manage Your Sourcing Cost" (Chinese: 管理您的采购成本) (VR2).
- The FR, IT and ES redlines were read from their text layers only, not rendered (VR2).
- Amazon's US definition is the "cost to source a product from a manufacturer, wholesaler, or reseller, or to produce the item"; the first UK draft (2024-12-11) read "the cost to acquire, purchase, or produce the item", and the UK's 2025-02-24 text uses the US wording (VR3).
- Shipping, handling and customs duties are excluded in every version, Japan's included (VR3).
- Sourcing-cost valuation also covers losses "during inventory replenishment handled by Amazon or on behalf of Amazon to fulfillment centers or non-Amazon buildings in marketplaces where we provide the service" (VR4).
- The current text of *FBA inventory reimbursement policy* (G200213130) is a help page the seller sees signed in; cx reads the dated redline PDFs on m.media-amazon.com by plain GET (VR2, VR29).

## Amazon's estimate

- Amazon's estimate is built from "comparable products sold by Amazon, by other sellers, and through other wholesale channels"; a declined seller cost leaves the previously approved amount or the estimate in force (VR5, VR9).
- From a date each store's text gives, Amazon refreshes its estimates periodically, alerts a seller whose provided cost is affected, and marks impacted items in MYSC's status column (VR5).
- Amazon states that a seller's cost data "is not shared with any other seller in Amazon's store, including Amazon Retail" (VR6).
- No SP-API operation reads or writes MYSC, and no model in Amazon's SP-API models holds a sourcing-cost field (VR18).

## Japan

- Amazon's JP policy, in English and Japanese texts created 2025-02-19, values shipment-to-Amazon, removal and FC-operations claims at the item's sourcing cost ("原価"), entered on the IDR portal's "Manage Your Sourcing cost" page ("原価の管理"), with Amazon's estimate otherwise (VR41).
- The JP texts carry the same decline reasons and repeat rule, a per-unit cap in yen, and a valuation-dispute window counted from the reimbursement (VR41).
- The JP texts date the estimate refresh from 2025-04-01 and give no start date for the valuation itself (VR41).
- Whether the JP portal shows the 原価の管理 page today, and whether the JP live policy keeps the 2025-02-19 text, is read in Amazon's documents, not yet seen on a live account (VR16, VR41).
- The JP English and Japanese texts differ on the customer-return basis: references/basis.md.
