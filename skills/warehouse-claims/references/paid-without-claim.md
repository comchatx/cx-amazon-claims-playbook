# Paid without a claim, store by store

## Amazon's announcements

- Amazon's US News post of 2024-07-24 says it will "proactively reimburse you for … items that are lost in our fulfillment centers … as soon as an item is reported as lost" (FC3).
- The same post says "almost all" warehouse-lost, warehouse-damaged and customer-return cases "will now be proactively reimbursed", a manual claim remains for any unit not reimbursed, and all removal claims stay manual (FC3).
- The Canada post of the same day is the same text with its own customer-return window; the finance pack cites the Canada post, not the US one (FC41).
- The UK News post of 2024-10-10 announced the UK start of 2025-01-15 (FC4).
- The US, UK and Canada valuation posts of 2024-12-18 each restate "We now offer automatic reimbursements for items lost in our fulfil(l)ment cent(re|er)s" (FC4).
- The Sweden, Saudi Arabia, Egypt, UAE and Australia posts change windows only (FC4, FC11, FC42).
- No automation post was found, by a search of forums and media, for DE, FR, IT, ES, NL, PL, BE, IE, SE, JP, AU, IN, MX, BR, AE, SA, EG, TR or SG; a Chinese practitioner (AMZ123) assigns the 2025 date to Europe, and the post's own store field narrows it to the UK (FC4).
- Whether automatic `Lost_Warehouse` rows arrive in a store with no automation post is read in Amazon's documents, not yet seen on a live account (FC4).

## The UK contradiction

- A UK staff post (Jameson_Amazon, 2026-04-06) says UK warehouse-lost inventory "Currently requires manual claim submission", automatic reimbursement disabled since 2022-08, with a window counted from "the event" (FC5).
- The same post says warehouse damage to sellable units is reimbursed automatically within a period it states, and damage whose source disposition was customer damaged, inbound carrier damaged, expired or distributor damaged is "Eligible for manual claims" (FC19).
- Amazon's UK News posts state automatic lost reimbursement (2024-10-10 with a start date; 2024-12-18, "We now offer") and a shorter manual window (2024-10-10; 2025-01-15) (FC5).
- Both are Amazon's statements for the UK store; neither is picked (FC5, EC27).
- On value, the same staff post describes "estimated proceeds - your item's value minus applicable fees", while the UK News posts of 2024-12-18 and 2025-02-28 and the UK policy PDF of 2025-02-24 move pre-order losses to sourcing cost (FC35, VR2).
- A seller in that thread reports an "Amazon estimated" value below the manufacturer's own selling price, the invoice figure not given (FC35).
- Whether UK `Lost_Warehouse` rows arrive with a blank `case-id` after 2025-01-15 or only on a case is read in Amazon's documents, not yet seen on a live account (FC5, EC27).

## Where cx reads it for the seller's store

- What Amazon paid in a store is read in `GET_FBA_REIMBURSEMENTS_DATA` (Pricing or Amazon Fulfillment): whether `Lost_Warehouse` and `Damaged_Warehouse` rows with a blank `case-id` arrive after the store's automation date, against the ledger's lost and damaged adjustments in `GET_LEDGER_DETAIL_VIEW_DATA` (Amazon Fulfillment) (EC27, SU2, SU3).
- That a blank `case-id` means Amazon paid unasked is a reading, not Amazon's statement; it is read in Amazon's documents, not yet seen on a live account (EC27).
- The store's announcement is its latest Seller Forums News post on reimbursement whose `marketplaceId` is that store, read by plain GET (FC4, FC45).

## How a post's store is read

- A thread opens on every forum host; `selectedMarketplaceId` follows the host, while the `marketplaceId` in the post object stays the same on every host (FC45).
- On four posts whose store is fixed by their own words, the field named that store; Amazon documents neither the field nor its meaning (FC45).
- One News text is issued as a separate thread per store, and the copies differ in their values, so a value read in one thread is that store's only (FC46).
- On a seller's post the field is the store the seller posted under, which can differ from the store the post discusses (FC47).

## The posts, by store

- 81c3235d, 2024-07-24, US: the automation start and the windows from 2024-10-23 (FC3, FC41).
- 6605eede, 2024-07-24, Canada: the same text with its own customer-return window (FC41, FC46).
- c6da88ce, e62a8ace, 96a05f4a, 2024-08-06, Saudi Arabia, Egypt, UAE: the window set effective 2024-09-05 (FC11).
- d0fc997e, 2024-10-10, UK: automation from 2025-01-15; windows from 2025-01-09 (FC4, FC9).
- 2de1ef2f, 2024-10-16, US: a seller relaying Amazon's text on the window change of 2024-10-23 (FC7).
- 68864b6f, a941ac02, da761b17, 2024-12-18, US, UK, Canada: "We now offer automatic reimbursements" (FC4).
- 1101821c and 9a92846d, 2025-01-15, Sweden and UK: windows only (FC5, FC9).
- b175b700, 2025-01-21, US: the IDR portal launch (FC13).
- 0252e05d, 2025-02-28, UK: the postponed move of pre-order losses to sourcing cost for the UK (FC35).
- d8f9a56c, Australia: the claim-windows post effective 2025-10-15 (FC42).
- 2f44617d, 2026-04-06, UK staff: lost units manual, sellable damage automatic (FC5, FC19).
- 0e07abc1, 2026-08-13, US staff: scope, the window's start, replenishment at sourcing cost (FC2, FC10).
- 5b46fd45, 2021-04-07, UK, a seller quoting Amazon: the researching text (FC6).
- c0d6d3da, a seller's post with the UK field, about Pan-EU sales in Italy, Spain and France (FC47).

## History

- Amazon's 2021 text, as a seller quoted it, says that for adjustments after 2021-03-19 Amazon handles the researching duration, so sellers need not wait it out to file (FC6).
- A Chinese practitioner (雨果网, 2019-06-12) reports rows showing "Damaged at Amazon" with "Transfer to holding" as already reimbursed (FC43).
- Amazon's Chinese FBA FAQ says warehouse-damaged units cannot be removed and are reimbursed automatically and written off (FC44).

## The seller's choices (stated, none picked)

- Waiting for an automatic payment relies on Amazon's stated automation (FC3).
- Filing as soon as an event appears: Amazon's conduct paragraph names "insufficiently researched or premature requests" among activity that may bring delayed support, monitoring or account action, and the US moderator put claims at one per shipment or event in 2026 (FL7, FL11).
- The window runs from Amazon's report of the event in either case (FC10).
- For a UK store, the staff post's lost window and the News posts' window are each Amazon's statement; the store's policy page, which cx cannot read and the seller sees signed in, shows the store's window (FC5, FC9).
- The value of pre-order losses and the sourcing cost: ../claim-value/SKILL.md.
