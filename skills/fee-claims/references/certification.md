# The EU certification regime

## History

- From 2025-08-01, sellers with a German business address were asked to certify package dimensions for Amazon.de, as Valuezon relays Amazon (FE5).
- Amazon's Global Selling notice of 2026-03-06 called for certified dimensions on existing Amazon.de ASINs, large and heavy bulky items excluded, by a date stated on the notice (FE5).
- From 2026-05-05, certified dimensions calculate FBA fees on amazon.co.uk, amazon.fr, amazon.it and amazon.es, by Amazon's policy PDF created 2026-03-30 (FE5).
- cifnews and 九方 relay a standard-size phase and a large-item phase for the UK, France, Italy and Spain; those are their relays, not an Amazon post read (FE5).

## The rules

- Certified means measured with a device that complies with the EU Measuring Instruments Directive, a tape measure among them (FE6).
- Existing dimensions not verified by the store's deadline are deemed certified, and new listings carry certified dimensions; on Amazon.de the dimensions entered at listing creation are the basis (FE6).
- Amazon validates the dimensions and may replace incorrect ones with its own certified dimensions; the seller's appeal goes through the remeasure widget, within the monthly limit (FE6).
- Certifying and appealing are the seller's steps in Seller Central; no SP-API operation shows or sets an ASIN's certification status (FE6, SU12).
- The stores, tiers and deadlines in scope are read on Amazon's *FBA item package dimensions certification policy* PDF and the Global Selling notice, both read by plain GET (FE5, FE6).

## The look-back true-up

- Amazon's Amazon.de notice states that certified dimensions that lower FBA fees bring an automatic true-up of the difference for a stated look-back, worded for items sold on Amazon.de (FE7).
- Practitioners (cifnews, 九方) relay the same true-up for the UK, France, Italy and Spain; no Amazon page read states one for the US (FE7).
- The look-back length for the seller's store is read on that store's certification notice (FE7).
- How the true-up posts (one adjustment or per order, under which name, and whether it covers storage) is read in Amazon's documents, not yet seen on a live account (FE7).

## The contradiction on storage

- Amazon's *Rate Card Europe Fees*, effective 2026-11-02, says Amazon's measurement governs storage volume (FE8).
- The certification policy says certified seller dimensions calculate "FBA fees" in the UK, France, Italy and Spain from 2026-05-05 (FE8).
- No page read says whether storage falls under certification; both texts stand with their dates (FE8).
