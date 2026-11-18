# The customer-return window

## The rule

- The window counts from the customer refund or replacement date (RT4).
- Amazon refuses a claim filed before the window opens or after it closes (RT4).
- The day counts differ by store and Amazon's posts disagree; the window is read for the seller's store on *Customer return claims* as the seller sees it signed in in Seller Central, and in the latest Seller Forums News post on claim windows for that store, read by plain GET (RT4).
- This pack reads a News post's store from the post object's `marketplaceId`, which stays the same on every forum host; on four posts checked the field named the post's own store, and Amazon does not document it (RT5, FC45).
- The returns report's `return-date` is the processing date at the centre, not the refund date the window counts from (RT33).
- Where a refund's date posts in the seller's money: @comchatx/cx-amazon-finance-playbook, skill refunds-and-reimbursements.

## Amazon's statements, read 2026-11-13, none picked

- US: News 81c3235d, posted 2024-07-24, effective 2024-10-23, states the window after the refund or replacement date and that claims must not be submitted before it opens (RT4, RT5, EC5).
- Canada: News 6605eede, the same announcement posted 0.7 seconds apart from the US issue, states a different window for Canada, effective 2024-10-23 (RT5).
- UK (News d0fc997e, 2024-10-10; 9a92846d, 2025-01-15), Sweden (News 1101821c, 2025-01-15) and Australia (News d8f9a56c, 2025-08-14): each states the window counted from the refund or replacement date for its store (RT4).
- US staff post 0e07abc1 of 2026-08-13 states a window whose end differs from the US News post's (EC5).
- Chinese media of 2025-01 reported a US move to another window; no US post read carries it, and the posts of 2025-01-15 with that window are the Sweden and UK issues (RT7).
- Which of these statements the claim tool enforces for a store is open: read in Amazon's documents, not yet seen on a live account (RT4, EC5).

## The not-returned clock

- In most cases Amazon charges the buyer and reimburses the seller when the unit is not returned within the store's set number of days of the refund (RT1).
- Amazon staff posts state that number for the US and Canada; where the seller sees it for any other store is open, not yet seen on a live account (RT1).
