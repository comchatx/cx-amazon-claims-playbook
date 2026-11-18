"""A synthetic seller's tree for the skill-creator runs of the claims playbook: no real seller, no Amazon call, no network.

    python3 -I evals/fixture.py <dir>            replaces <dir>/tenant and <dir>/stub-replies, leaves the rest of <dir>
    python3 -I evals/fixture.py <dir> --summary  the same, then prints the figures the cases are graded on, as JSON

Seller A1FIXTURESELLER, brand "Kettlewick" (kettles and tea and coffee tools). Today is 2026-11-17, a Tuesday. Two stores:
  US  ATVPDKIKX0DER   origin https://sellingpartnerapi-na.amazon.com  USD, fulfilment centres QQA1 and QQB2
  UK  A1F83G8C2ARO7P  origin https://sellingpartnerapi-eu.amazon.com  GBP, fulfilment centres QQL1 and QQL2
The seller's application holds the door's five roles (Product Listing, Pricing, Brand Analytics, Finance and Accounting,
Amazon Fulfillment). A call that needs another role is answered 403 Unauthorized: the Support API (/support/2025-02-01/...),
the Data Kiosk Economics dataset, GET_V2_SELLER_PERFORMANCE_REPORT, AWD (research README § 6; SU8, SU33, SU49).

<dir>/tenant is what the box holds after earlier sessions: the seller's notes (costs and what was entered in Manage Your
Sourcing Cost, packaging measured by the seller, claims the seller remembers, invoices) and three earlier landed replies
under raw/amazon-sp-api/ (a getShipments of 2026-10-01, a Fee Preview of 2026-08-15, a Reimbursements report read
2026-06-30). <dir>/stub-replies is what Amazon answers "now", for evals/cx, out of the run's sight: inventory summaries,
inbound shipments (v0), finance transactions (2024-06-19), orders (2026-01-01), catalog items (2022-04-01), and
report-sources/, the rows a requested report is cut from.

Every figure is invented. The shapes follow Amazon's models at db2936aa (fulfillmentInbound v0, finances 2024-06-19,
orders 2026-01-01, catalogItems 2022-04-01, fbaInventory, reports 2021-06-30) and the report column lists on Amazon's
*FBA Reports* page as the research prints them (research/method/sp-api-claims-surface.md § 2; the stock pack's
sp-api-stock-surface.md for full lists). Where the research gives no value set or format (a reimbursement `condition`, a
returns `status` spelling, a date format, a removal `order-source`, a fee name), the value here is a guess, named in README.md.

Catalog (tenant/notes/costs.md):
  US  KW-KETTLE-BLK   X00KCBLK01 B0CLAIM001  49.99  cost 14.20, entered in MYSC, approved 2025-04-10
      KW-SCALE-DGT    X00KCSCL06 B0CLAIM006  34.99  cost  7.90, entered in MYSC 2026-05-28, approved 2026-06-02
      KW-INFUSER-2PK  X00KCINF04 B0CLAIM004  12.99  cost  1.85, not entered
      KW-FROTHER      X00KCFRO09 B0CLAIM009  17.99  cost  3.30, not entered
      KW-MUG-SET4     X00KCMUG08 B0CLAIM008  27.99  cost  7.10, not entered
  UK  KW-KETTLE-BLK-UK X00KCBLKU1 B0CLAIM001 44.99 GBP  cost 11.60, entered in MYSC (UK), approved 2025-05-02
      KW-MUG-SET4-UK   X00KCMUGU8 B0CLAIM008 24.99 GBP  cost  5.70, not entered
      KW-INFUSER-UK    X00KCINFU4 B0CLAIM004 10.99 GBP  cost  1.50, not entered

SCENARIOS, two per skill. Each names its right answer and the research positions (research/README.md, the files under
research/areas, method and beyond) it rests on; --summary prints the figures. "Window" below always means: the rule and
the place it is read; a length is the dated Amazon text's (research README § 4, § 5), never this fixture's.

warehouse-claims
  W1 us-lost-unpaid (US). "Which of my black kettles lost in the warehouse did Amazon pay, which came back, which are
     still open? File the rest for me." Ledger detail, KW-KETTLE-BLK, Adjustments: 07-14 M -3 (QQA1, reconciled 3),
     07-29 N +1, 08-22 M -2 (QQA1, reconciled 2), 09-05 F +2 (at QQB2, not QQA1), 10-03 M -4 (QQB2, unreconciled 4),
     10-20 E -1 then P +1, 11-12 M -2 (QQA1, unreconciled 2). Reimbursements: 07-29 Lost_Warehouse 3 units (2 cash at
     14.20 = 28.40, 1 inventory), blank case-id; 10-24 Damaged_Warehouse 1 at 14.20, blank case-id. So: paid without a
     case 3 lost + 1 damaged; found 2 at another FC (FC26); the N +1 is the inventory unit of the July reimbursement, not
     a find (FC25, VR40); open 4 units of 10-03 (45 days ago today), Reference ID KC1003A1, QQB2; 2 units of 11-12 still
     researching (getInventorySummaries researchingQuantity 2; FC30; FC6). A naive net M - F - N = 11 - 3 = 8 is wrong.
     US proactive reimbursement from 2024-11-01 (FC3, FC4); the US window counts from the loss report (FC10) and its
     length is read on the US News post and the policy page (FC9; README § 4). Match by FNSKU and date range (FC27).
     No operation files a claim or opens a case (SU12, FL1); the lost route is a Get Support case by FNSKU or
     Transaction Item ID, damaged by the status tool (FL4); IDR covers warehouse lost (FL5); evidence FC17, FC18.
  W2 uk-lost-two-texts (UK). "Amazon UK lost 5 mug sets last month. Does UK pay lost stock automatically or must I
     claim? What has been paid?" Ledger UK, KW-MUG-SET4-UK: 04-02 M -1 (reconciled 1), 06-11 M -2 (reconciled 2),
     10-09 M -5 (QQL1, unreconciled 5, 39 days ago). Reimbursements (EU origin): 04-08 Lost_Warehouse 1 at 4.85 GBP,
     blank case-id; 07-02 Lost_Warehouse 2 at 4.85 GBP, case-id 1987654321 (notes/claims.md: the seller filed it).
     Amazon states two things for the UK: automatic from 2025-01-15 (News d0fc997e, 2024-10-10) and manual, "automatic
     reimbursement disabled since August 2022" (staff 2f44617d, 2026-04-06): both stated, neither picked (FC4, FC5,
     EC27). The seller's own rows show one paid without a case and one with: they do not settle the rule. The UK window
     is also stated two ways (News: 60 days, eff. 2025-01-09; staff 2026: lost 18 months of the event; FC9, FC5). The
     report has no store column (SU52); the ledger's Country is GB. 4.85 is below the seller's 5.70, cost not entered
     in MYSC (claim-value's ground, VR7, VR8).

shipment-claims
  S1 inbound-short-closed-vs-receiving (US). "FBA18KWINF1 and FBA19KWSCL2 came up short. Which can I claim now, how
     many, by when?" v0: FBA18KWINF1 CLOSED, 480 shipped, 462 received (18 short; ledger Receipts 08-26 300, 08-28 162 at
     QQB2; Inbound Performance carton FBA18KWINF1U000004 expected 40, received 22); FBA19KWSCL2 RECEIVING, 600 shipped,
     570 received (ledger 11-09 400, 11-11 170). No Lost_Inbound reimbursement for either. The request is filed after
     CLOSED (IN7); CLOSED is all received or a timeout, not proof (IN14); no operation returns the delivery date or the
     eligibility date (IN10, IN29), so the window's start is not readable by cx; the US length is the staff post's and
     gs.amazon.cn's (IN7; README § 4). Route: the shipment's Reconcile tab, "Research missing units" (FL4, IN13); one
     claim per shipment (FL7, IN17); evidence IN15, IN16, FL24; value at sourcing cost, pre-order (IN21). The earlier
     landed getShipments (2026-10-01) shows FBA18KWINF1 RECEIVING then: status is read today.
  S2 uk-removal-lost (UK). "Removal KWUKRMV0921: 60 infusers sent back, 40 arrived. Claim it for me; what does Amazon
     need?" Removal Order Detail: requested 60, shipped 60, Completed, created 2026-09-21 (57 days ago), removal-fee
     31.80 GBP. Removal Shipment Detail: shipped 2026-09-25, DPD 15501234567890 40 units, Evri H01KWF0000012345 20 units;
     no shipment id column (RM15). Ledger UK VendorReturns -60 on 09-25. notes/claims.md: 40 arrived by DPD 09-30.
     Removal claims are all manual (RM2); route "Resolve a removal order issue" by removal order ID (RM4, FL4); evidence
     RM14, the shipment ID read by the seller in Seller Central (RM15); the UK lost-in-transit window has an earliest
     and a latest day counted from creation, read on the UK News post (RM6, RM9; README § 4); row counts can differ
     when re-asked (SU25); no operation opens a removal claim (RM35).

return-claims
  R1 refunded-not-returned (US). "Find orders refunded where the item never came back. Am I owed anything yet?"
     listTransactions Refund lines and the FBA Returns report:
       113-4000001-0000001 kettle   refunded 07-02, returned 07-15 SELLABLE, Unit returned to inventory: nothing owed
       113-4000002-0000002 scale    refunded 07-20, not returned, CustomerReturn reimbursed 09-22 at 24.78, blank case-id
       113-4000003-0000003 frother  refunded 08-10, not returned, no reimbursement: 99 days today
       113-4000004-0000004 kettle   refunded 10-01, not returned, no reimbursement: 47 days today
       113-4000005-0000005 mug set  refunded 08-20, returned 09-03 CUSTOMER_DAMAGED: not reimbursed (RT3), a grade
                                    dispute is a removal claim (RT13)
       113-4000006-0000006 infuser  replaced (113-4000006-0000106 shipped 08-01, replacements report), original not
                                    returned, no reimbursement: 108 days since the replacement
     The clock counts from the refund or replacement (RT4); the US window is stated two ways (News 81c3235d; staff
     2026-08-13; RT5, RT6) and its length is read there; the "not returned" days before Amazon reimburses (RT1, RT8);
     a refund without a return never shows in the returns report (RT32); return-date is processing at the FC (RT33);
     route by order ID (FL4), IDR (FL5); value on the order basis (VR27, VR31).
  R2 uk-wrong-item-disposition (UK). "英国站 203-5000011-0000011 的买家退回来的不是我的水壶。退货报告怎么写的？亚马逊会赔吗？"
     Returns report UK: 203-5000011-0000011 KW-KETTLE-BLK-UK, return-date 10-14, SELLABLE, reason SWITCHEROO, status
     Unit returned to inventory, LPN LPNRK0011UK1 (refund 10-06). SWITCHEROO is the buyer's claim that Amazon sent the
     wrong item, not Amazon's finding of a swap (RT18); grading follows the unit's condition at the FC (RT2); the unit
     is the evidence and the claim follows its removal (RT16); the LPN ties a removed unit to the row (RT37); removal
     evidence RM14, removal claim kind "different" (RM3). Also 203-5000012-0000012 mug set, 10-29, CUSTOMER_DAMAGED,
     DEFECTIVE, LPN LPNRK0012UK8: customer damaged is not reimbursed (RT3) and a grade dispute needs the unit back
     (RT13, RM11). Disposition spellings differ by source (RT35). UK windows read on the UK News post (RT4; RM12).

fee-claims
  F1 mis-tier (US). "Amazon charges my infuser 2-pack as a bigger size. My box is 6.0 x 4.5 x 0.7 in, 0.30 lb. What do
     they have, how much extra, can you get it remeasured?" Fee Preview today: 6.2 x 4.6 x 1.4 in, 0.38 lb,
     Large Standard-Size; the earlier landed Fee Preview (2026-08-15) and the storage report for 2026-06..08 show
     6.0 x 4.5 x 0.7, 0.30 lb, Small Standard-Size; from 2026-09 the storage rows carry the new measurement (FE17, FE19).
     listTransactions: FBAPerUnitFulfillmentFee 3.22 on infuser charges posted through 2026-09-01, 3.71 from the first
     charge posted 2026-09-03 (the fee table changes on 2026-09-02, a day with no infuser charge; --summary: the count
     and the difference). Catalog dimensions are the catalogue's, not an FC measurement (SU6).
     Amazon's measurement governs, a seller's own is not accepted alone (FE2); a remeasure is the seller's step in
     Seller Central with its conditions (FE4, FE12; SU12); a corrected measurement does not prove past fees come back
     (FE14); rate changes can look like overcharges (FE20); itemised window counted from each charge, read on the help
     page and the store's staff guide (FE9); the route (FE37); a correction can post as "Fee Adjustment - Weight and
     Dimension Change" with no reimbursement ID (FE13; two such lines on scale orders, 2026-06-12).
  F2 uk-fee-window-classes (UK). "Two UK charges: the removal fee on cancelled removal KWUKRMV0315 (March), and FBA fees
     on my mug sets since July. Which window applies to each and where do I read it?" Removal Order Detail: KWUKRMV0315
     requested 30, cancelled 30, shipped 0, disposed 0, removal-fee 15.30 GBP, Cancelled; listTransactions: a removal fee
     -15.30 GBP posted 2026-03-28 (234 days ago). Mug orders since 2026-07-01: 36 FBAPerUnitFulfillmentFee lines of 4.12 GBP;
     Fee Preview UK 31.2 x 22.0 x 14.6 cm, 1.32 kg; the seller measured 30.0 x 21.5 x 14.0 cm, 1.18 kg. Removal fees
     are non-itemised, fulfilment fees itemised, two limits by Amazon's UK staff (FE9; ff7c3c15, 2026-05-13); read on the
     help page GL7U4JFSDXUTQAJ (cannot be read by cx) and the store's latest staff guide, the charge date from
     `postedDate`; a fee with no removed unit is removals-disposals' (FE41, RM26, RM27), and the UK's per-unit charging
     starts 2026-05-01 (News 862f270b, RM26), after this order's creation, so per-unit charging does not settle a March
     fee; the UK certification regime lets certified seller dimensions set fees (FE5, FE6), set in Seller Central.

claim-value
  V1 under-valued-after-mysc (US). "Amazon paid $6.10 each for lost scales; my cost is $7.90. Under-valued?"
     Reimbursements, KW-SCALE-DGT: 2025-02-11 Lost_Warehouse 2 at 19.84 (before the 2025-03-31 change; VR1);
     2025-05-06 Lost_Warehouse 3 at 6.10 and 2026-02-17 Damaged_Warehouse 1 at 6.10 (after the change, before the cost
     was approved 2026-06-02: Amazon's estimate; VR2, VR5); 2026-09-08 Lost_Warehouse 2 at 7.90 (after approval, equals
     the entered cost; VR8); 2026-09-22 CustomerReturn 1 at 24.78 (order basis, not cost; VR27, VR31). An approved cost
     applies to reimbursements issued after approval and does not revalue earlier ones (VR8, VR23); compare with the cost
     in force at approval-date (VR32); the report names no basis (VR30); the dispute window counts from the
     reimbursement and is read on the policy page or redlines (VR20); routes (VR21); 4 units x (7.90 - 6.10) = 7.20 below
     the seller's cost on the two estimate lines.
  V2 uk-reversal (UK). "UK: £23.20 was taken back as a reimbursement reversal. What for, did my units come back?"
     Reimbursements UK: 2026-05-19 2590000052 Lost_Warehouse KW-KETTLE-BLK-UK 2 at 11.60 = 23.20 GBP, blank case-id;
     2026-10-27 2590000140 Reimbursement_Reversal, original-reimbursement-id 2590000052, original-reimbursement-type
     Lost_Warehouse, -23.20, cash -2. Ledger UK: 05-12 M -2 (QQL1), 10-22 F +1 (QQL2). Two units reversed against one
     found: a mismatch of one unit (VR36, VR37, VR38, VR40, FC26). Amazon publishes no reversal deadline or amount rule
     (VR36); the seller's route is Seller Support (VR37). listTransactions UK carries the reversal posted 10-27.

claim-filing
  C1 file-it-for-me (US). "File all my open claims and attach my invoices from my notes, then give me the case numbers."
     No operation files a claim, opens a case or attaches evidence (SU12, FL1); the Support API reads cases only and
     needs Selling Partner Support (Restricted), outside the five: answered 403 (SU8, SU10); a paid manual claim's case
     shows only as `case-id` in the Reimbursements report (FL29). The open items a run can find: W1's 4 kettles
     (KC1003A1), S1's 18 infusers on FBA18KWINF1, R1's 113-4000003-0000003 and the replacement of 113-4000006-0000006.
     Route by kind (FL4), IDR scope (FL5), evidence formats (IN16, FL24), one claim per shipment (FL7), the conduct rule
     on premature or insufficiently researched requests (FL11) stated as Amazon's rule; an automated agent must identify
     itself (FL22). notes/invoices.md names the invoices; their files are not on the box.
  C2 uk-window-where (UK). "UK: customer refunded on 2026-09-02 for 203-5000021-0000021, mug set never came back. What
     is the exact deadline? Don't guess." listTransactions UK: Refund posted 2026-09-02 for the order; no returns row; no
     reimbursement row. The clock counts from the refund (RT4); the UK window as read 2026-11-13 is the UK News post
     d0fc997e's (README § 4; RT4) and the *Customer return claims* page, which cx cannot read (a script shell; § 5); the
     News post is read by a plain GET, not reachable in this run; the "not returned" days are read for the US and Canada only
     (RT8); 76 days since the refund today.
"""
import datetime as dt
import json
import os
import shutil
import sys

if len(sys.argv) < 2:
    sys.exit("usage: python3 -I evals/fixture.py <dir> [--summary]")
root = os.path.abspath(sys.argv[1])
SUMMARY = "--summary" in sys.argv[2:]
T = os.path.join(root, "tenant")
S = os.path.join(root, "stub-replies")
for d in (T, S):
    if os.path.isdir(d):
        shutil.rmtree(d)

SELLER = "A1FIXTURESELLER"
US, UK = "ATVPDKIKX0DER", "A1F83G8C2ARO7P"
TODAY = dt.date(2026, 11, 17)
D = dt.date.fromisoformat
CUR = {US: "USD", UK: "GBP"}
STORE_NAME = {US: "Amazon.com", UK: "Amazon.co.uk"}
COUNTRY = {US: "US", UK: "GB"}


def put(base, rel, data, raw=False):
    p = os.path.join(base, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(data if raw else json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def r2(x):
    return round(x + 1e-9, 2)


def days_ago(s):
    return (TODAY - D(s)).days


# sku: (fnsku, asin, title, price, cost, fc)
CAT = {
    US: {
        "KW-KETTLE-BLK": ("X00KCBLK01", "B0CLAIM001", "Kettlewick Gooseneck Electric Kettle 1L, Matte Black", 49.99, 14.20, "QQA1"),
        "KW-SCALE-DGT": ("X00KCSCL06", "B0CLAIM006", "Kettlewick Digital Coffee Scale with Timer", 34.99, 7.90, "QQA1"),
        "KW-INFUSER-2PK": ("X00KCINF04", "B0CLAIM004", "Kettlewick Stainless Steel Tea Infuser, 2-Pack", 12.99, 1.85, "QQB2"),
        "KW-FROTHER": ("X00KCFRO09", "B0CLAIM009", "Kettlewick Handheld Milk Frother", 17.99, 3.30, "QQA1"),
        "KW-MUG-SET4": ("X00KCMUG08", "B0CLAIM008", "Kettlewick Double-Wall Glass Mugs, Set of 4", 27.99, 7.10, "QQB2"),
    },
    UK: {
        "KW-KETTLE-BLK-UK": ("X00KCBLKU1", "B0CLAIM001", "Kettlewick Gooseneck Electric Kettle 1L, Matte Black", 44.99, 11.60, "QQL1"),
        "KW-MUG-SET4-UK": ("X00KCMUGU8", "B0CLAIM008", "Kettlewick Double-Wall Glass Mugs, Set of 4", 24.99, 5.70, "QQL1"),
        "KW-INFUSER-UK": ("X00KCINFU4", "B0CLAIM004", "Kettlewick Stainless Steel Tea Infuser, 2-Pack", 10.99, 1.50, "QQL1"),
    },
}
# referral and fulfilment fee per unit as charged on orders; the infuser's fulfilment fee changes on 2026-09-02
FEES = {US: {"KW-KETTLE-BLK": (7.50, 6.38), "KW-SCALE-DGT": (5.25, 4.96), "KW-INFUSER-2PK": (1.95, 3.22), "KW-FROTHER": (2.70, 3.71),
             "KW-MUG-SET4": (4.20, 6.04)},
        UK: {"KW-KETTLE-BLK-UK": (6.75, 4.86), "KW-MUG-SET4-UK": (3.75, 4.12), "KW-INFUSER-UK": (1.65, 2.71)}}
INF_NEW_FEE, INF_CHANGE = 3.71, D("2026-09-02")


def fee_of(store, sku, day):
    ref, ful = FEES[store][sku]
    if store == US and sku == "KW-INFUSER-2PK" and day >= INF_CHANGE:
        ful = INF_NEW_FEE
    return ref, ful


# ---------------------------------------------------------------- orders
# (store, orderId, sku, created date, hour) ; specific orders of the return cases first
SPECIFIC = [
    (US, "113-4000001-0000001", "KW-KETTLE-BLK", "2026-06-24"),
    (US, "113-4000002-0000002", "KW-SCALE-DGT", "2026-07-12"),
    (US, "113-4000003-0000003", "KW-FROTHER", "2026-08-01"),
    (US, "113-4000004-0000004", "KW-KETTLE-BLK", "2026-09-22"),
    (US, "113-4000005-0000005", "KW-MUG-SET4", "2026-08-12"),
    (US, "113-4000006-0000006", "KW-INFUSER-2PK", "2026-07-24"),
    (UK, "203-5000011-0000011", "KW-KETTLE-BLK-UK", "2026-09-28"),
    (UK, "203-5000012-0000012", "KW-MUG-SET4-UK", "2026-10-15"),
    (UK, "203-5000021-0000021", "KW-MUG-SET4-UK", "2026-08-25"),
]
REPLACEMENT = {"original": "113-4000006-0000006", "replacement": "113-4000006-0000106", "shipped": "2026-08-01", "sku": "KW-INFUSER-2PK",
               "reason": "5"}
ORDERS = []
for store, oid, sku, day in SPECIFIC:
    ORDERS.append({"store": store, "orderId": oid, "sku": sku, "day": D(day), "hour": 15, "replacement": False})
ORDERS.append({"store": US, "orderId": REPLACEMENT["replacement"], "sku": "KW-INFUSER-2PK", "day": D(REPLACEMENT["shipped"]), "hour": 9,
               "replacement": True})

FIRST = D("2026-05-25")
n = 0
d = FIRST
while d <= D("2026-11-14"):
    k = d.toordinal()
    if k % 3 != 0:  # the infuser sells most days
        n += 1
        ORDERS.append({"store": US, "orderId": "113-7%06d-%07d" % (k % 1000000, n), "sku": "KW-INFUSER-2PK", "day": d, "hour": 11 + n % 8,
                       "replacement": False})
    if k % 5 == 0:
        n += 1
        ORDERS.append({"store": US, "orderId": "113-8%06d-%07d" % (k % 1000000, n), "sku": "KW-KETTLE-BLK", "day": d, "hour": 13, "replacement": False})
    if k % 7 == 2:
        n += 1
        ORDERS.append({"store": US, "orderId": "113-8%06d-%07d" % (k % 1000000, n), "sku": "KW-SCALE-DGT", "day": d, "hour": 16, "replacement": False})
    if d >= D("2026-07-01") and k % 4 == 1:
        n += 1
        ORDERS.append({"store": UK, "orderId": "203-6%06d-%07d" % (k % 1000000, n), "sku": "KW-MUG-SET4-UK", "day": d, "hour": 10, "replacement": False})
    if d >= D("2026-06-01") and k % 9 == 4:
        n += 1
        ORDERS.append({"store": UK, "orderId": "203-6%06d-%07d" % (k % 1000000, n), "sku": "KW-KETTLE-BLK-UK", "day": d, "hour": 12, "replacement": False})
    d += dt.timedelta(1)
ORDERS.sort(key=lambda o: (o["day"], o["hour"], o["orderId"]))
BY_ID = {o["orderId"]: o for o in ORDERS}

REFUNDS = {  # orderId: refund date
    "113-4000001-0000001": "2026-07-02", "113-4000002-0000002": "2026-07-20", "113-4000003-0000003": "2026-08-10",
    "113-4000004-0000004": "2026-10-01", "113-4000005-0000005": "2026-08-20",
    "203-5000011-0000011": "2026-10-06", "203-5000012-0000012": "2026-10-22", "203-5000021-0000021": "2026-09-02",
}

# ---------------------------------------------------------------- returns report rows
RET_HEAD = ["return-date", "order-id", "sku", "asin", "fnsku", "product-name", "quantity", "fulfillment-center-id", "detailed-disposition",
            "reason", "status", "license-plate-number", "customer-comments"]
RETURNS = [
    (US, "2026-07-15T14:02:11+00:00", "113-4000001-0000001", "QQA1", "SELLABLE", "UNWANTED_ITEM", "Unit returned to inventory", "LPNRK0001US4", ""),
    (US, "2026-09-03T10:41:37+00:00", "113-4000005-0000005", "QQB2", "CUSTOMER_DAMAGED", "NOT_AS_DESCRIBED", "Unit returned to inventory",
     "LPNRK0005US9", "glass smaller than pictured"),
    (UK, "2026-10-14T09:17:52+00:00", "203-5000011-0000011", "QQL1", "SELLABLE", "SWITCHEROO", "Unit returned to inventory", "LPNRK0011UK1",
     "Not the kettle I ordered"),
    (UK, "2026-10-29T13:05:20+00:00", "203-5000012-0000012", "QQL1", "CUSTOMER_DAMAGED", "DEFECTIVE", "Unit returned to inventory",
     "LPNRK0012UK8", "one mug cracked"),
]


def ret_row(store, when, oid, fc, disp, reason, status, lpn, comment):
    sku = BY_ID[oid]["sku"]
    fn, asin, title = CAT[store][sku][:3]
    return {"return-date": when, "order-id": oid, "sku": sku, "asin": asin, "fnsku": fn, "product-name": title, "quantity": 1,
            "fulfillment-center-id": fc, "detailed-disposition": disp, "reason": reason, "status": status, "license-plate-number": lpn,
            "customer-comments": comment}


# ---------------------------------------------------------------- reimbursements report rows (18 columns)
RB_HEAD = ["approval-date", "reimbursement-id", "case-id", "amazon-order-id", "reason", "sku", "fnsku", "asin", "product-name", "condition",
           "currency-unit", "amount-per-unit", "amount-total", "quantity-reimbursed-cash", "quantity-reimbursed-inventory",
           "quantity-reimbursed-total", "original-reimbursement-id", "original-reimbursement-type"]
# (store, approval date, id, case, order, reason, sku, per unit, cash, inventory, original id, original type)
RB = [
    (US, "2025-02-11", "2480000412", "", "", "Lost_Warehouse", "KW-SCALE-DGT", 19.84, 2, 0, "", ""),
    (US, "2025-05-06", "2480000655", "", "", "Lost_Warehouse", "KW-SCALE-DGT", 6.10, 3, 0, "", ""),
    (US, "2026-02-17", "2480000893", "", "", "Damaged_Warehouse", "KW-SCALE-DGT", 6.10, 1, 0, "", ""),
    (US, "2026-05-14", "2480000961", "", "", "Lost_Warehouse", "KW-MUG-SET4", 6.85, 1, 0, "", ""),
    (US, "2026-07-29", "2481000101", "", "", "Lost_Warehouse", "KW-KETTLE-BLK", 14.20, 2, 1, "", ""),
    (US, "2026-09-08", "2481000140", "", "", "Lost_Warehouse", "KW-SCALE-DGT", 7.90, 2, 0, "", ""),
    (US, "2026-09-22", "2481000152", "", "113-4000002-0000002", "CustomerReturn", "KW-SCALE-DGT", 24.78, 1, 0, "", ""),
    (US, "2026-10-24", "2481000177", "", "", "Damaged_Warehouse", "KW-KETTLE-BLK", 14.20, 1, 0, "", ""),
    (UK, "2026-04-08", "2590000031", "", "", "Lost_Warehouse", "KW-MUG-SET4-UK", 4.85, 1, 0, "", ""),
    (UK, "2026-05-19", "2590000052", "", "", "Lost_Warehouse", "KW-KETTLE-BLK-UK", 11.60, 2, 0, "", ""),
    (UK, "2026-07-02", "2590000088", "1987654321", "", "Lost_Warehouse", "KW-MUG-SET4-UK", 4.85, 2, 0, "", ""),
    (UK, "2026-10-27", "2590000140", "", "", "Reimbursement_Reversal", "KW-KETTLE-BLK-UK", 11.60, -2, 0, "2590000052", "Lost_Warehouse"),
]


def rb_row(r):
    store, day, rid, case, oid, reason, sku, per, cash, inv, orig, otype = r
    fn, asin, title = CAT[store][sku][:3]
    return {"approval-date": day + "T07:00:00+00:00", "reimbursement-id": rid, "case-id": case, "amazon-order-id": oid, "reason": reason,
            "sku": sku, "fnsku": fn, "asin": asin, "product-name": title, "condition": "New", "currency-unit": CUR[store],
            "amount-per-unit": "%.2f" % per, "amount-total": "%.2f" % (per * cash), "quantity-reimbursed-cash": cash,
            "quantity-reimbursed-inventory": inv, "quantity-reimbursed-total": cash + inv, "original-reimbursement-id": orig,
            "original-reimbursement-type": otype}


# ---------------------------------------------------------------- ledger detail events
LD_HEAD = ["Date", "FNSKU", "ASIN", "MSKU", "Title", "Event Type", "Reference ID", "Quantity", "Fulfillment Center", "Disposition",
           "Reason", "Country", "Reconciled Quantity", "Unreconciled Quantity", "Date and Time", "Store"]
# (store, date, sku, event, ref, qty, fc, disposition, reason, reconciled, unreconciled)
ADJ = [
    (US, "2025-04-28", "KW-SCALE-DGT", "Adjustments", "KC0428A6", -3, "QQA1", "SELLABLE", "M", 3, 0),
    (US, "2026-02-10", "KW-SCALE-DGT", "Adjustments", "KC0210E6", -1, "QQA1", "SELLABLE", "E", 1, 0),
    (US, "2026-02-10", "KW-SCALE-DGT", "Adjustments", "KC0210E6", 1, "QQA1", "WAREHOUSE_DAMAGED", "P", "", ""),
    (US, "2026-05-07", "KW-MUG-SET4", "Adjustments", "KC0507A8", -1, "QQB2", "SELLABLE", "M", 1, 0),
    (US, "2026-07-14", "KW-KETTLE-BLK", "Adjustments", "KC0714A1", -3, "QQA1", "SELLABLE", "M", 3, 0),
    (US, "2026-07-29", "KW-KETTLE-BLK", "Adjustments", "KC0729N1", 1, "QQA1", "SELLABLE", "N", "", ""),
    (US, "2026-08-22", "KW-KETTLE-BLK", "Adjustments", "KC0822A1", -2, "QQA1", "SELLABLE", "M", 2, 0),
    (US, "2026-09-01", "KW-SCALE-DGT", "Adjustments", "KC0901A6", -2, "QQA1", "SELLABLE", "M", 2, 0),
    (US, "2026-09-05", "KW-KETTLE-BLK", "Adjustments", "KC0905F1", 2, "QQB2", "SELLABLE", "F", "", ""),
    (US, "2026-10-03", "KW-KETTLE-BLK", "Adjustments", "KC1003A1", -4, "QQB2", "SELLABLE", "M", 0, -4),
    (US, "2026-10-20", "KW-KETTLE-BLK", "Adjustments", "KC1020E1", -1, "QQA1", "SELLABLE", "E", 1, 0),
    (US, "2026-10-20", "KW-KETTLE-BLK", "Adjustments", "KC1020E1", 1, "QQA1", "WAREHOUSE_DAMAGED", "P", "", ""),
    (US, "2026-11-12", "KW-KETTLE-BLK", "Adjustments", "KC1112A1", -2, "QQA1", "SELLABLE", "M", 0, -2),
    (US, "2026-08-26", "KW-INFUSER-2PK", "Receipts", "FBA18KWINF1", 300, "QQB2", "SELLABLE", "", "", ""),
    (US, "2026-08-28", "KW-INFUSER-2PK", "Receipts", "FBA18KWINF1", 162, "QQB2", "SELLABLE", "", "", ""),
    (US, "2026-11-09", "KW-SCALE-DGT", "Receipts", "FBA19KWSCL2", 400, "QQA1", "SELLABLE", "", "", ""),
    (US, "2026-11-11", "KW-SCALE-DGT", "Receipts", "FBA19KWSCL2", 170, "QQA1", "SELLABLE", "", "", ""),
    (UK, "2026-04-02", "KW-MUG-SET4-UK", "Adjustments", "KL0402A8", -1, "QQL1", "SELLABLE", "M", 1, 0),
    (UK, "2026-05-12", "KW-KETTLE-BLK-UK", "Adjustments", "KL0512A1", -2, "QQL1", "SELLABLE", "M", 2, 0),
    (UK, "2026-06-11", "KW-MUG-SET4-UK", "Adjustments", "KL0611A8", -2, "QQL1", "SELLABLE", "M", 2, 0),
    (UK, "2026-09-25", "KW-INFUSER-UK", "VendorReturns", "KWUKRMV0921", -60, "QQL1", "SELLABLE", "", "", ""),
    (UK, "2026-10-09", "KW-MUG-SET4-UK", "Adjustments", "KL1009A8", -5, "QQL1", "SELLABLE", "M", 0, -5),
    (UK, "2026-10-22", "KW-KETTLE-BLK-UK", "Adjustments", "KL1022F1", 1, "QQL2", "SELLABLE", "F", "", ""),
]
# the US M rows still open keep their unreconciled quantity as a positive count, as the report prints it
ADJ = [a[:10] + (abs(a[10]) if isinstance(a[10], int) else a[10],) for a in ADJ]


def ld_rows(store):
    out = []
    for a in ADJ:
        st, day, sku, ev, ref, q, fc, disp, reason, rec, unrec = a
        if st != store:
            continue
        fn, asin, title = CAT[store][sku][:3]
        out.append({"Date": day, "FNSKU": fn, "ASIN": asin, "MSKU": sku, "Title": title, "Event Type": ev, "Reference ID": ref, "Quantity": q,
                    "Fulfillment Center": fc, "Disposition": disp, "Reason": reason, "Country": COUNTRY[store], "Reconciled Quantity": rec,
                    "Unreconciled Quantity": unrec, "Date and Time": day + ("T09:12:44-07:00" if store == US else "T08:40:10+01:00"),
                    "Store": STORE_NAME[store]})
    for o in ORDERS:
        if o["store"] != store:
            continue
        fn, asin, title, _, _, fc = CAT[store][o["sku"]]
        ship = o["day"] + dt.timedelta(1)
        if ship > TODAY - dt.timedelta(1):
            continue
        out.append({"Date": ship.isoformat(), "FNSKU": fn, "ASIN": asin, "MSKU": o["sku"], "Title": title, "Event Type": "Shipments",
                    "Reference ID": "Q%s%s" % (ship.strftime("%m%d"), o["orderId"][-4:]), "Quantity": -1, "Fulfillment Center": fc,
                    "Disposition": "SELLABLE", "Reason": "", "Country": COUNTRY[store], "Reconciled Quantity": "", "Unreconciled Quantity": "",
                    "Date and Time": ship.isoformat() + "T19:05:00" + ("-07:00" if store == US else "+01:00"), "Store": STORE_NAME[store]})
    for r in RETURNS:
        if r[0] != store:
            continue
        row = ret_row(*r)
        out.append({"Date": row["return-date"][:10], "FNSKU": row["fnsku"], "ASIN": row["asin"], "MSKU": row["sku"], "Title": row["product-name"],
                    "Event Type": "CustomerReturns", "Reference ID": row["order-id"], "Quantity": 1, "Fulfillment Center": row["fulfillment-center-id"],
                    "Disposition": row["detailed-disposition"], "Reason": "", "Country": COUNTRY[store], "Reconciled Quantity": "",
                    "Unreconciled Quantity": "", "Date and Time": row["return-date"], "Store": STORE_NAME[store]})
    out.sort(key=lambda r: (r["Date"], r["MSKU"], r["Event Type"]))
    return out


LS_HEAD = ["Date", "FNSKU", "ASIN", "MSKU", "Title", "Disposition", "Starting Warehouse Balance", "In Transit Between Warehouses",
           "Receipts", "Customer Shipments", "Customer Returns", "Vendor Returns", "Warehouse Transfer In/Out", "Found", "Lost",
           "Damaged", "Disposed", "Other Events", "Ending Warehouse Balance", "Unknown Events", "Location", "Store"]
SUMMARY_COL = {"Receipts": "Receipts", "Shipments": "Customer Shipments", "CustomerReturns": "Customer Returns", "VendorReturns": "Vendor Returns"}
REASON_COL = {"M": "Lost", "5": "Lost", "F": "Found", "N": "Found", "O": "Other Events", "E": "Damaged", "6": "Damaged", "7": "Damaged",
              "H": "Damaged", "K": "Damaged", "U": "Damaged", "D": "Disposed"}
START_BAL = {"KW-KETTLE-BLK": 260, "KW-SCALE-DGT": 140, "KW-INFUSER-2PK": 420, "KW-FROTHER": 90, "KW-MUG-SET4": 120,
             "KW-KETTLE-BLK-UK": 110, "KW-MUG-SET4-UK": 150, "KW-INFUSER-UK": 200}


def ls_rows(store, details):
    out = []
    first, last = D("2025-05-18"), TODAY - dt.timedelta(1)
    for sku in CAT[store]:
        fn, asin, title = CAT[store][sku][:3]
        ev = {}
        for r in details:
            if r["MSKU"] == sku and r["Disposition"] == "SELLABLE":
                col = SUMMARY_COL.get(r["Event Type"]) or REASON_COL.get(r["Reason"]) or "Unknown Events"
                ev.setdefault(r["Date"], {}).setdefault(col, 0)
                ev[r["Date"]][col] += r["Quantity"]
        bal = START_BAL[sku]
        day = first
        while day <= last:
            e = ev.get(day.isoformat(), {})
            row = {"Date": day.isoformat(), "FNSKU": fn, "ASIN": asin, "MSKU": sku, "Title": title, "Disposition": "SELLABLE",
                   "Starting Warehouse Balance": bal, "In Transit Between Warehouses": 0, "Location": COUNTRY[store], "Store": STORE_NAME[store]}
            for c in ("Receipts", "Customer Shipments", "Customer Returns", "Vendor Returns", "Warehouse Transfer In/Out", "Found", "Lost",
                      "Damaged", "Disposed", "Other Events", "Unknown Events"):
                row[c] = e.get(c, 0)
            bal += sum(e.values())
            row["Ending Warehouse Balance"] = bal
            out.append(row)
            day += dt.timedelta(1)
        assert bal >= 0, (sku, bal)
    return out


# ---------------------------------------------------------------- report sources
def source(rtype, mkt, header, rows, kind="snapshot", gz=False, date=None, bom=False):
    rows = [{c: r.get(c, "") for c in header} for r in rows]
    put(S, "report-sources/%s-%s.json" % (rtype, mkt), {"reportType": rtype, "marketplaceId": mkt, "kind": kind, "gzip": gz,
                                                       "bom": bom, "header": header, "date": date, "rows": rows})


for store in (US, UK):
    det = ld_rows(store)
    source("GET_LEDGER_DETAIL_VIEW_DATA", store, LD_HEAD, det, kind="ledger-detail", gz=True, date="Date")
    source("GET_LEDGER_SUMMARY_VIEW_DATA", store, LS_HEAD, ls_rows(store, det), kind="ledger-summary", gz=True, date="Date")
    source("GET_FBA_REIMBURSEMENTS_DATA", store, RB_HEAD, [rb_row(r) for r in RB if r[0] == store], kind="range", date="approval-date")
    source("GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA", store, RET_HEAD, [ret_row(*r) for r in RETURNS if r[0] == store], kind="range",
           date="return-date")

RP_HEAD = ["shipment-date", "sku", "asin", "fulfillment-center-id", "original-fulfillment-center-id", "quantity", "replacement-reason-code",
           "replacement-amazon-order-id", "original-amazon-order-id"]
source("GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_REPLACEMENT_DATA", US, RP_HEAD, [
    {"shipment-date": REPLACEMENT["shipped"] + "T18:22:40+00:00", "sku": "KW-INFUSER-2PK", "asin": "B0CLAIM004", "fulfillment-center-id": "QQB2",
     "original-fulfillment-center-id": "QQB2", "quantity": 1, "replacement-reason-code": REPLACEMENT["reason"],
     "replacement-amazon-order-id": REPLACEMENT["replacement"], "original-amazon-order-id": REPLACEMENT["original"]}],
    kind="range", date="shipment-date")

RM_HEAD = ["request-date", "order-id", "order-source", "order-type", "service-speed", "order-status", "last-updated-date", "sku", "fnsku",
           "disposition", "requested-quantity", "cancelled-quantity", "disposed-quantity", "shipped-quantity", "in-process-quantity",
           "removal-fee", "currency"]
source("GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA", UK, RM_HEAD, [
    {"request-date": "2026-03-15T11:02:40+00:00", "order-id": "KWUKRMV0315", "order-source": "Seller-initiated Manual Removal", "order-type": "Return",
     "service-speed": "Standard", "order-status": "Cancelled", "last-updated-date": "2026-03-27T16:20:05+00:00", "sku": "KW-MUG-SET4-UK",
     "fnsku": "X00KCMUGU8", "disposition": "Sellable", "requested-quantity": 30, "cancelled-quantity": 30, "disposed-quantity": 0,
     "shipped-quantity": 0, "in-process-quantity": 0, "removal-fee": "15.30", "currency": "GBP"},
    {"request-date": "2026-09-21T10:14:00+01:00", "order-id": "KWUKRMV0921", "order-source": "Seller-initiated Manual Removal", "order-type": "Return",
     "service-speed": "Standard", "order-status": "Completed", "last-updated-date": "2026-09-26T08:51:12+01:00", "sku": "KW-INFUSER-UK",
     "fnsku": "X00KCINFU4", "disposition": "Sellable", "requested-quantity": 60, "cancelled-quantity": 0, "disposed-quantity": 0,
     "shipped-quantity": 60, "in-process-quantity": 0, "removal-fee": "31.80", "currency": "GBP"}], kind="range", date="request-date")
source("GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA", US, RM_HEAD, [
    {"request-date": "2026-06-03T10:11:00-07:00", "order-id": "KWDSP0603", "order-source": "Seller-initiated Manual Removal", "order-type": "Disposal",
     "service-speed": "Standard", "order-status": "Completed", "last-updated-date": "2026-06-10T08:45:30-07:00", "sku": "KW-MUG-SET4",
     "fnsku": "X00KCMUG08", "disposition": "Unsellable", "requested-quantity": 9, "cancelled-quantity": 0, "disposed-quantity": 9,
     "shipped-quantity": 0, "in-process-quantity": 0, "removal-fee": "3.15", "currency": "USD"}], kind="range", date="request-date")

RS_HEAD = ["request-date", "order-id", "shipment-date", "sku", "fnsku", "disposition", "shipped-quantity", "carrier", "tracking-number",
           "removal-order-type"]
source("GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA", UK, RS_HEAD, [
    {"request-date": "2026-09-21T10:14:00+01:00", "order-id": "KWUKRMV0921", "shipment-date": "2026-09-25T15:40:00+01:00", "sku": "KW-INFUSER-UK",
     "fnsku": "X00KCINFU4", "disposition": "Sellable", "shipped-quantity": 40, "carrier": "DPD", "tracking-number": "15501234567890",
     "removal-order-type": "Return"},
    {"request-date": "2026-09-21T10:14:00+01:00", "order-id": "KWUKRMV0921", "shipment-date": "2026-09-25T15:42:00+01:00", "sku": "KW-INFUSER-UK",
     "fnsku": "X00KCINFU4", "disposition": "Sellable", "shipped-quantity": 20, "carrier": "Evri", "tracking-number": "H01KWF0000012345",
     "removal-order-type": "Return"}], kind="range", date="shipment-date")

NC_HEAD = ["issue-reported-date", "shipment-creation-date", "fba-shipment-id", "fba-carton-id", "fulfillment-center-id", "sku", "fnsku", "asin",
           "product-name", "problem-type", "problem-quantity", "expected-quantity", "received-quantity", "performance-measurement-unit",
           "coaching-level", "fee-type", "currency", "fee-total", "problem-level", "alert-status"]
source("GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA", US, NC_HEAD, [
    {"issue-reported-date": "2026-08-28", "shipment-creation-date": "2026-08-05", "fba-shipment-id": "FBA18KWINF1", "fba-carton-id": "FBA18KWINF1U000004",
     "fulfillment-center-id": "QQB2", "sku": "KW-INFUSER-2PK", "fnsku": "X00KCINF04", "asin": "B0CLAIM004", "product-name": CAT[US]["KW-INFUSER-2PK"][2],
     "problem-type": "Unit quantity discrepancy", "problem-quantity": 18, "expected-quantity": 40, "received-quantity": 22,
     "performance-measurement-unit": "Units", "coaching-level": "Informational", "fee-type": "", "currency": "USD", "fee-total": "0.00",
     "problem-level": "Carton", "alert-status": "Active"},
    {"issue-reported-date": "2026-11-10", "shipment-creation-date": "2026-10-20", "fba-shipment-id": "FBA19KWSCL2", "fba-carton-id": "FBA19KWSCL2U000012",
     "fulfillment-center-id": "QQA1", "sku": "KW-SCALE-DGT", "fnsku": "X00KCSCL06", "asin": "B0CLAIM006", "product-name": CAT[US]["KW-SCALE-DGT"][2],
     "problem-type": "Unlabeled", "problem-quantity": 12, "expected-quantity": 12, "received-quantity": 12, "performance-measurement-unit": "Units",
     "coaching-level": "Warning", "fee-type": "FBA Label Service Fee", "currency": "USD", "fee-total": "6.60", "problem-level": "Unit",
     "alert-status": "Active"}], kind="range", date="issue-reported-date")

# Fee Preview: column order is the all-store list, then the store's own columns (a guess, README.md)
FP_ALL = ["sku", "fnsku", "asin", "amazon-store", "product-name", "product-group", "brand", "fulfilled-by", "your-price", "sales-price",
          "longest-side", "median-side", "shortest-side", "length-and-girth", "unit-of-dimension", "item-package-weight", "unit-of-weight",
          "currency", "estimated-fee-total", "estimated-referral-fee-per-unit"]
FP_US = FP_ALL + ["product-size-tier", "estimated-future-order-handling-fee-per-order", "expected-future-fulfillment-fee-per-unit",
                  "estimated-order-handling-fee-per-order", "estimated-variable-closing-fee", "expected-fulfillment-fee-per-unit",
                  "estimated-future-fee", "estimated-future-pick-pack-fee-per-unit", "estimated-future-weight-handling-fee-per-unit"]
FP_UK = FP_ALL + ["estimated-order-handling-fee-per-order", "has-local-inventory", "product-size-weight-band",
                  "expected-domestic-fulfilment-fee-per-unit", "expected-efn-fulfilment-fee-per-unit-uk", "expected-efn-fulfilment-fee-per-unit-de",
                  "expected-efn-fulfilment-fee-per-unit-fr", "expected-efn-fulfilment-fee-per-unit-it", "expected-efn-fulfilment-fee-per-unit-es",
                  "expected-efn-fulfilment-fee-per-unit-se"]
DIMS_US = {  # sku: (l, m, s in, lb, tier) as Amazon has them today
    "KW-KETTLE-BLK": (12.6, 9.1, 7.9, 3.10, "Large Standard-Size"), "KW-SCALE-DGT": (9.8, 7.4, 2.4, 1.30, "Large Standard-Size"),
    "KW-INFUSER-2PK": (6.2, 4.6, 1.4, 0.38, "Large Standard-Size"), "KW-FROTHER": (10.0, 2.6, 2.2, 0.40, "Large Standard-Size"),
    "KW-MUG-SET4": (11.8, 8.3, 5.5, 2.60, "Large Standard-Size")}
INF_OLD = (6.0, 4.5, 0.7, 0.30, "Small Standard-Size")
DIMS_UK = {"KW-KETTLE-BLK-UK": (32.0, 23.1, 20.1, 1.41, "Standard Parcel 6"), "KW-MUG-SET4-UK": (31.2, 22.0, 14.6, 1.32, "Standard Parcel 5"),
           "KW-INFUSER-UK": (17.8, 15.2, 2.0, 0.18, "Standard Parcel 1")}


def fp_us(sku, dims, ful):
    fn, asin, title, price = CAT[US][sku][:4]
    l, m, s, w, tier = dims
    ref = FEES[US][sku][0]
    return {"sku": sku, "fnsku": fn, "asin": asin, "amazon-store": "US", "product-name": title, "product-group": "Kitchen", "brand": "Kettlewick",
            "fulfilled-by": "AMAZON_NA", "your-price": "%.2f" % price, "sales-price": "%.2f" % price, "longest-side": l, "median-side": m,
            "shortest-side": s, "length-and-girth": r2(l + 2 * (m + s)), "unit-of-dimension": "inches", "item-package-weight": w,
            "unit-of-weight": "pounds", "currency": "USD", "estimated-fee-total": "%.2f" % (ref + ful), "estimated-referral-fee-per-unit": "%.2f" % ref,
            "product-size-tier": tier, "estimated-future-order-handling-fee-per-order": "", "expected-future-fulfillment-fee-per-unit": "",
            "estimated-order-handling-fee-per-order": "0.00", "estimated-variable-closing-fee": "0.00", "expected-fulfillment-fee-per-unit": "%.2f" % ful,
            "estimated-future-fee": "", "estimated-future-pick-pack-fee-per-unit": "", "estimated-future-weight-handling-fee-per-unit": ""}


fp_rows_us = [fp_us(k, v, fee_of(US, k, TODAY)[1]) for k, v in DIMS_US.items()]
source("GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA", US, FP_US, fp_rows_us)
fp_rows_uk = []
for sku, (l, m, s, w, band) in DIMS_UK.items():
    fn, asin, title, price = CAT[UK][sku][:4]
    ref, ful = FEES[UK][sku]
    fp_rows_uk.append({"sku": sku, "fnsku": fn, "asin": asin, "amazon-store": "UK", "product-name": title, "product-group": "Kitchen",
                       "brand": "Kettlewick", "fulfilled-by": "AMAZON_EU", "your-price": "%.2f" % price, "sales-price": "%.2f" % price,
                       "longest-side": l, "median-side": m, "shortest-side": s, "length-and-girth": r2(l + 2 * (m + s)),
                       "unit-of-dimension": "centimeters", "item-package-weight": w, "unit-of-weight": "kilograms", "currency": "GBP",
                       "estimated-fee-total": "%.2f" % (ref + ful), "estimated-referral-fee-per-unit": "%.2f" % ref,
                       "estimated-order-handling-fee-per-order": "0.00", "has-local-inventory": "Y", "product-size-weight-band": band,
                       "expected-domestic-fulfilment-fee-per-unit": "%.2f" % ful, "expected-efn-fulfilment-fee-per-unit-uk": "",
                       "expected-efn-fulfilment-fee-per-unit-de": "", "expected-efn-fulfilment-fee-per-unit-fr": "",
                       "expected-efn-fulfilment-fee-per-unit-it": "", "expected-efn-fulfilment-fee-per-unit-es": "",
                       "expected-efn-fulfilment-fee-per-unit-se": ""})
source("GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA", UK, FP_UK, fp_rows_uk)

SF_HEAD = ["asin", "fnsku", "product_name", "fulfillment_center", "country_code", "longest_side", "median_side", "shortest_side",
           "measurement_units", "weight", "weight_units", "item_volume", "volume_units", "product_size_tier", "average_quantity_on_hand",
           "average_quantity_pending_removal", "estimated_total_item_volume", "month_of_charge", "storage_rate", "storage_utilization_ratio",
           "storage_utilization_ratio_units", "base_rate", "utilization_surcharge_rate", "avg_qty_for_sus", "est_vol_for_sus", "est_base_msf",
           "est_sus", "currency", "estimated_monthly_storage_fee", "dangerous_goods_storage_type", "eligible_for_inventory_discount",
           "qualifies_for_inventory_discount", "total_incentive_fee_amount", "breakdown_incentive_fee_amount", "average_quantity_customer_orders"]
SF_US_RATE = {"2026-06": (0.78, 0.0), "2026-07": (0.78, 0.0), "2026-08": (0.78, 0.0), "2026-09": (0.78, 0.0), "2026-10": (2.40, 0.69)}
sf_us = []
for month, (base, sus) in SF_US_RATE.items():
    for sku in ("KW-INFUSER-2PK", "KW-KETTLE-BLK"):
        fn, asin, title = CAT[US][sku][:3]
        l, m, s, w, tier = INF_OLD if (sku == "KW-INFUSER-2PK" and month < "2026-09") else DIMS_US[sku]
        vol = round(l * m * s / 1728, 4)
        avg = 380.0 if sku == "KW-INFUSER-2PK" else 210.0
        tv = round(vol * avg, 4)
        sf_us.append({"asin": asin, "fnsku": fn, "product_name": title, "fulfillment_center": CAT[US][sku][5], "country_code": "US",
                      "longest_side": l, "median_side": m, "shortest_side": s, "measurement_units": "inches", "weight": w, "weight_units": "pounds",
                      "item_volume": vol, "volume_units": "cubic feet", "product_size_tier": tier, "average_quantity_on_hand": avg,
                      "average_quantity_pending_removal": 0, "estimated_total_item_volume": tv, "month_of_charge": month,
                      "storage_rate": r2(base + sus), "storage_utilization_ratio": 24.8, "storage_utilization_ratio_units": "weeks",
                      "base_rate": base, "utilization_surcharge_rate": sus, "avg_qty_for_sus": avg, "est_vol_for_sus": tv,
                      "est_base_msf": r2(tv * base), "est_sus": r2(tv * sus), "currency": "USD", "estimated_monthly_storage_fee": r2(r2(tv * base) + r2(tv * sus)),
                      "dangerous_goods_storage_type": "--", "eligible_for_inventory_discount": "N", "qualifies_for_inventory_discount": "N",
                      "total_incentive_fee_amount": 0, "breakdown_incentive_fee_amount": "", "average_quantity_customer_orders": 0})
source("GET_FBA_STORAGE_FEE_CHARGES_DATA", US, SF_HEAD, sf_us, kind="range", date="month_of_charge")
sf_uk = []
for month in ("2026-07", "2026-08", "2026-09", "2026-10"):
    l, m, s, w, band = DIMS_UK["KW-MUG-SET4-UK"]
    vol = round(l * m * s / 1e6, 6)
    avg = 140.0
    tv = round(vol * avg, 4)
    sf_uk.append({"asin": "B0CLAIM008", "fnsku": "X00KCMUGU8", "product_name": CAT[UK]["KW-MUG-SET4-UK"][2], "fulfillment_center": "QQL1",
                  "country_code": "GB", "longest_side": l, "median_side": m, "shortest_side": s, "measurement_units": "centimeters", "weight": w,
                  "weight_units": "kilograms", "item_volume": vol, "volume_units": "cubic meters", "product_size_tier": band,
                  "average_quantity_on_hand": avg, "average_quantity_pending_removal": 0, "estimated_total_item_volume": tv, "month_of_charge": month,
                  "storage_rate": 22.10, "storage_utilization_ratio": 15.2, "storage_utilization_ratio_units": "weeks", "base_rate": 22.10,
                  "utilization_surcharge_rate": 0, "avg_qty_for_sus": avg, "est_vol_for_sus": tv, "est_base_msf": r2(tv * 22.10), "est_sus": 0,
                  "currency": "GBP", "estimated_monthly_storage_fee": r2(tv * 22.10), "dangerous_goods_storage_type": "--",
                  "eligible_for_inventory_discount": "N", "qualifies_for_inventory_discount": "N", "total_incentive_fee_amount": 0,
                  "breakdown_incentive_fee_amount": "", "average_quantity_customer_orders": 0})
source("GET_FBA_STORAGE_FEE_CHARGES_DATA", UK, SF_HEAD, sf_uk, kind="range", date="month_of_charge")

# ---------------------------------------------------------------- inventory summaries (US, UK)
INV = {US: {"KW-KETTLE-BLK": (198, (0, 0, 0), (6, 11, 2), (2, 0, 0)), "KW-SCALE-DGT": (512, (0, 0, 30), (4, 20, 3), (0, 0, 0)),
            "KW-INFUSER-2PK": (344, (0, 0, 0), (3, 0, 0), (0, 0, 0)), "KW-FROTHER": (71, (0, 0, 0), (1, 0, 0), (0, 0, 0)),
            "KW-MUG-SET4": (96, (0, 0, 0), (2, 0, 0), (0, 0, 0))},
       UK: {"KW-KETTLE-BLK-UK": (87, (0, 0, 0), (2, 0, 0), (0, 0, 0)), "KW-MUG-SET4-UK": (118, (0, 0, 0), (3, 0, 0), (0, 0, 0)),
            "KW-INFUSER-UK": (140, (0, 0, 0), (0, 0, 0), (0, 0, 0))}}
UNF = {"KW-KETTLE-BLK": (0, 1, 0, 0, 0, 0), "KW-SCALE-DGT": (0, 0, 0, 0, 0, 0), "KW-MUG-SET4": (1, 0, 0, 0, 0, 0),
       "KW-MUG-SET4-UK": (1, 0, 0, 0, 0, 0)}
for store in (US, UK):
    rows = []
    for sku, (f, (w, sh, rc), (pc, pt, fp), (r1, r2_, r3)) in INV[store].items():
        fn, asin, title = CAT[store][sku][:3]
        u = UNF.get(sku, (0, 0, 0, 0, 0, 0))
        tot = f + w + sh + rc + pc + pt + fp + r1 + r2_ + r3 + sum(u)
        rows.append({"asin": asin, "fnSku": fn, "sellerSku": sku, "condition": "NewItem", "lastUpdatedTime": "2026-11-17T06:12:40Z",
                     "productName": title, "totalQuantity": tot, "stores": [STORE_NAME[store]], "inventoryDetails": {
                         "fulfillableQuantity": f, "inboundWorkingQuantity": w, "inboundShippedQuantity": sh, "inboundReceivingQuantity": rc,
                         "reservedQuantity": {"totalReservedQuantity": pc + pt + fp, "pendingCustomerOrderQuantity": pc,
                                              "pendingTransshipmentQuantity": pt, "fcProcessingQuantity": fp},
                         "researchingQuantity": {"totalResearchingQuantity": r1 + r2_ + r3, "researchingQuantityBreakdown": [
                             {"name": "researchingQuantityInShortTerm", "quantity": r1}, {"name": "researchingQuantityInMidTerm", "quantity": r2_},
                             {"name": "researchingQuantityInLongTerm", "quantity": r3}]},
                         "unfulfillableQuantity": {"totalUnfulfillableQuantity": sum(u), "customerDamagedQuantity": u[0], "warehouseDamagedQuantity": u[1],
                                                   "distributorDamagedQuantity": u[2], "carrierDamagedQuantity": u[3], "defectiveQuantity": u[4],
                                                   "expiredQuantity": u[5]}}})
    put(S, "getInventorySummaries-%s.json" % store, {"pagination": {}, "payload": {"granularity": {"granularityType": "Marketplace",
                                                                                                   "granularityId": store}, "inventorySummaries": rows}})

put(S, "getMarketplaceParticipations-na.json", {"payload": [{"marketplace": {"id": US, "countryCode": "US", "name": "Amazon.com",
    "defaultCurrencyCode": "USD", "defaultLanguageCode": "en_US", "domainName": "www.amazon.com"},
    "participation": {"isParticipating": True, "hasSuspendedListings": False}, "storeName": "Kettlewick"}]})
put(S, "getMarketplaceParticipations-eu.json", {"payload": [{"marketplace": {"id": UK, "countryCode": "GB", "name": "Amazon.co.uk",
    "defaultCurrencyCode": "GBP", "defaultLanguageCode": "en_GB", "domainName": "www.amazon.co.uk"},
    "participation": {"isParticipating": True, "hasSuspendedListings": False}, "storeName": "Kettlewick"}]})

# ---------------------------------------------------------------- inbound v0 (US)
ADDR = {"Name": "Kettlewick Supply", "AddressLine1": "1 Fixture Way", "City": "Newark", "StateOrProvinceCode": "NJ", "CountryCode": "US",
        "PostalCode": "07105"}
V0 = [("FBA18KWINF1", "KW infuser 2026-08", "QQB2", "CLOSED", [("KW-INFUSER-2PK", 480, 462)], 40),
      ("FBA19KWSCL2", "KW scale 2026-10", "QQA1", "RECEIVING", [("KW-SCALE-DGT", 600, 570)], 12),
      ("FBA18KWKTL4", "KW kettle 2026-07", "QQA1", "CLOSED", [("KW-KETTLE-BLK", 240, 240)], 8)]
put(S, "getShipments-%s.json" % US, {"payload": {"ShipmentData": [
    {"ShipmentId": sid, "ShipmentName": name, "ShipFromAddress": ADDR, "DestinationFulfillmentCenterId": fc, "ShipmentStatus": st,
     "LabelPrepType": "SELLER_LABEL", "AreCasesRequired": True, "BoxContentsSource": "INTERACTIVE"} for sid, name, fc, st, _, _ in V0]}})
for sid, name, fc, st, items, case in V0:
    put(S, "getShipmentItemsByShipmentId-%s.json" % sid, {"payload": {"ItemData": [
        {"ShipmentId": sid, "SellerSKU": sku, "FulfillmentNetworkSKU": CAT[US][sku][0], "QuantityShipped": q, "QuantityReceived": rcv,
         "QuantityInCase": case, "PrepDetailsList": []} for sku, q, rcv in items]}})
put(T, "raw/amazon-sp-api/getShipments-ATVPDKIKX0DER-2026-10-01.json", {"payload": {"ShipmentData": [
    {"ShipmentId": "FBA18KWINF1", "ShipmentName": "KW infuser 2026-08", "ShipFromAddress": ADDR, "DestinationFulfillmentCenterId": "QQB2",
     "ShipmentStatus": "RECEIVING", "LabelPrepType": "SELLER_LABEL", "AreCasesRequired": True, "BoxContentsSource": "INTERACTIVE"},
    {"ShipmentId": "FBA18KWKTL4", "ShipmentName": "KW kettle 2026-07", "ShipFromAddress": ADDR, "DestinationFulfillmentCenterId": "QQA1",
     "ShipmentStatus": "CLOSED", "LabelPrepType": "SELLER_LABEL", "AreCasesRequired": True, "BoxContentsSource": "INTERACTIVE"}]}})

# ---------------------------------------------------------------- finance transactions (2024-06-19)
TX = []


def money(store, x):
    return {"currencyCode": CUR[store], "currencyAmount": r2(x)}


def bd(store, t, amt, kids=None):
    return {"breakdownType": t, "breakdownAmount": money(store, amt), "breakdowns": kids or []}


def at(day, hh, mm=0):
    return "%sT%02d:%02d:00Z" % (day.isoformat() if isinstance(day, dt.date) else day, hh, mm)


def tx(store, ttype, desc, posted, total, rel=(), items=(), brk=(), ctx=()):
    TX.append({"sellingPartnerMetadata": {"sellingPartnerId": SELLER, "accountType": "Standard Orders", "marketplaceId": store},
               "relatedIdentifiers": [{"relatedIdentifierName": k, "relatedIdentifierValue": v} for k, v in rel],
               "transactionType": ttype, "transactionId": "TX%s%04d" % ("U" if store == US else "K", len(TX) + 1),
               "transactionStatus": "RELEASED", "description": desc, "postedDate": posted, "totalAmount": money(store, total),
               "marketplaceDetails": {"marketplaceId": store, "marketplaceName": STORE_NAME[store]}, "items": list(items),
               "breakdowns": list(brk), "contexts": list(ctx)})


def pctx(store, sku, qty=1):
    return {"contextType": "ProductContext", "asin": CAT[store][sku][1], "sku": sku, "quantityShipped": qty, "fulfillmentNetwork": "AFN"}


def order_lines(store, sku, day, sign=1):
    price = CAT[store][sku][3]
    ref, ful = fee_of(store, sku, day)
    groups = [bd(store, "ProductCharges", sign * price, [bd(store, "OurPricePrincipal", sign * price)]),
              bd(store, "AmazonFees", -sign * (ref + (ful if sign > 0 else 0)),
                 [bd(store, "Commission", -sign * ref)] + ([bd(store, "FBAPerUnitFulfillmentFee", -ful)] if sign > 0 else []))]
    return groups, sum(g["breakdownAmount"]["currencyAmount"] for g in groups)


for o in ORDERS:
    if o["replacement"]:
        continue
    store, sku, day = o["store"], o["sku"], o["day"] + dt.timedelta(1)
    if day >= TODAY:
        continue
    groups, total = order_lines(store, sku, day)
    tx(store, "Shipment", "Order Payment", at(day, 6, 30), total, [("ORDER_ID", o["orderId"])],
       [{"description": CAT[store][sku][2], "totalAmount": money(store, total), "breakdowns": groups, "contexts": [pctx(store, sku)],
         "relatedIdentifiers": []}], groups)
for oid, rday in REFUNDS.items():
    o = BY_ID[oid]
    store, sku = o["store"], o["sku"]
    groups, total = order_lines(store, sku, D(rday), sign=-1)
    tx(store, "Refund", "Refund Order", at(rday, 17, 5), total, [("ORDER_ID", oid), ("REFUND_ID", "RF" + oid[-7:])],
       [{"description": CAT[store][sku][2], "totalAmount": money(store, total), "breakdowns": groups, "contexts": [pctx(store, sku)],
         "relatedIdentifiers": [{"itemRelatedIdentifierName": "ORDER_ADJUSTMENT_ITEM_ID", "itemRelatedIdentifierValue": "AJ" + oid[-7:]}]}], groups)
for r in RB:
    store, day, rid, case, oid, reason, sku, per, cash, inv, orig, otype = r
    if D(day) < D("2026-05-01") or cash == 0:
        continue
    amt = per * cash
    ttype = "FBAInventoryReimbursement" if reason != "Reimbursement_Reversal" else "Adjustment"
    desc = {"Reimbursement_Reversal": "REVERSAL_REIMBURSEMENT", "CustomerReturn": "CUSTOMER_RETURN"}.get(reason, reason.upper())
    rel = [("ORDER_ID", oid)] if oid else []
    tx(store, ttype, desc, at(day, 9, 15), amt, rel,
       [{"description": CAT[store][sku][2], "totalAmount": money(store, amt), "breakdowns": [bd(store, "FBAInventoryReimbursement", amt)],
         "contexts": [pctx(store, sku, abs(cash))], "relatedIdentifiers": [{"itemRelatedIdentifierName": "TRANSACTION_ID", "itemRelatedIdentifierValue": rid}]}],
       [bd(store, "Sales", amt, [bd(store, "FBAInventoryReimbursement", amt)])])
# a weight-and-dimension correction on two scale orders (Amazon's staff wording; no reimbursement id)
scale_orders = [o for o in ORDERS if o["sku"] == "KW-SCALE-DGT" and D("2026-05-25") <= o["day"] <= D("2026-06-05")][:2]
for o in scale_orders:
    tx(US, "Adjustment", "Fee Adjustment - Weight and Dimension Change", at("2026-06-12", 10, 40), 0.42, [("ORDER_ID", o["orderId"])],
       [{"description": CAT[US]["KW-SCALE-DGT"][2], "totalAmount": money(US, 0.42), "breakdowns": [bd(US, "FBAPerUnitFulfillmentFee", 0.42)],
         "contexts": [pctx(US, "KW-SCALE-DGT")], "relatedIdentifiers": []}], [bd(US, "AmazonFees", 0.42, [bd(US, "FBAPerUnitFulfillmentFee", 0.42)])])
# removal fees as charged (UK)
tx(UK, "ServiceFee", "RemovalComplete", at("2026-03-28", 4, 10), -15.30, [],
   [{"description": CAT[UK]["KW-MUG-SET4-UK"][2], "totalAmount": money(UK, -15.30), "breakdowns": [bd(UK, "FBARemovalFee", -15.30)],
     "contexts": [pctx(UK, "KW-MUG-SET4-UK", 30)], "relatedIdentifiers": [{"itemRelatedIdentifierName": "REMOVAL_SHIPMENT_ITEM_ID",
                                                                      "itemRelatedIdentifierValue": "KWUKRMV0315"}]}],
   [bd(UK, "AmazonFees", -15.30, [bd(UK, "FBARemovalFee", -15.30)])])
tx(UK, "ServiceFee", "RemovalComplete", at("2026-09-26", 4, 10), -31.80, [],
   [{"description": CAT[UK]["KW-INFUSER-UK"][2], "totalAmount": money(UK, -31.80), "breakdowns": [bd(UK, "FBARemovalFee", -31.80)],
     "contexts": [pctx(UK, "KW-INFUSER-UK", 60)], "relatedIdentifiers": [{"itemRelatedIdentifierName": "REMOVAL_SHIPMENT_ITEM_ID",
                                                                      "itemRelatedIdentifierValue": "KWUKRMV0921"}]}],
   [bd(UK, "AmazonFees", -31.80, [bd(UK, "FBARemovalFee", -31.80)])])
# monthly storage (US, UK), as charged
for row in sf_us:
    if row["fnsku"] != "X00KCINF04":
        continue
    y, mth = map(int, row["month_of_charge"].split("-"))
    posted = dt.date(y + (mth == 12), mth % 12 + 1, 7)
    tot = sum(r["estimated_monthly_storage_fee"] for r in sf_us if r["month_of_charge"] == row["month_of_charge"])
    tx(US, "ServiceFee", "FBA storage fee", at(posted, 3, 0), -tot, [], [], [bd(US, "AmazonFees", -tot, [bd(US, "FBAStorageFee", -tot)])],
       [{"contextType": "TimeRangeContext", "startTime": "%s-01T00:00:00Z" % row["month_of_charge"], "endTime": at(posted - dt.timedelta(7), 0)}])
TX.sort(key=lambda x: x["postedDate"])
put(S, "transactions.json", {"note": "Finances 2024-06-19 transactions, both stores; evals/cx filters them", "transactions": TX})

# ---------------------------------------------------------------- orders 2026-01-01 and catalog items
ORD_DOCS = {}
for o in ORDERS:
    store, sku = o["store"], o["sku"]
    fn, asin, title, price = CAT[store][sku][:4]
    created = at(o["day"], o["hour"], 12)
    upd = at(o["day"] + dt.timedelta(1), 6, 30)
    if o["orderId"] in REFUNDS:
        upd = at(REFUNDS[o["orderId"]], 17, 5)
    doc = {"orderId": o["orderId"], "createdTime": created, "lastUpdatedTime": upd,
           "salesChannel": {"channelName": "AMAZON", "marketplaceId": store, "marketplaceName": STORE_NAME[store]},
           "fulfillment": {"fulfillmentStatus": "SHIPPED", "fulfilledBy": "AMAZON"},
           "orderItems": [{"orderItemId": "%014d" % (int(o["orderId"].replace("-", "")[-12:]) * 7 % 10 ** 14), "quantityOrdered": 1,
                           "product": {"asin": asin, "title": title, "sellerSku": sku, "condition": {"conditionType": "New"},
                                       "price": {"unitPrice": {"amount": "%.2f" % (0 if o["replacement"] else price), "currencyCode": CUR[store]}}}}]}
    if o["replacement"]:
        doc["associatedOrders"] = [{"orderId": REPLACEMENT["original"], "associationType": "REPLACEMENT_ORIGINAL_ID"}]
    ORD_DOCS[o["orderId"]] = doc
put(S, "orders.json", {"orders": [ORD_DOCS[o["orderId"]] for o in ORDERS]})

CATALOG_DIMS = {  # the catalogue's package dimensions, not an FC measurement (SU6)
    (US, "B0CLAIM004"): ((6.0, 4.5, 0.7, "inches"), (0.30, "pounds")), (US, "B0CLAIM001"): ((12.5, 9.0, 7.8, "inches"), (3.05, "pounds")),
    (US, "B0CLAIM006"): ((9.8, 7.4, 2.4, "inches"), (1.30, "pounds")), (US, "B0CLAIM009"): ((10.0, 2.6, 2.2, "inches"), (0.40, "pounds")),
    (US, "B0CLAIM008"): ((11.8, 8.3, 5.5, "inches"), (2.60, "pounds")),
    (UK, "B0CLAIM008"): ((30.0, 21.5, 14.0, "centimeters"), (1.18, "kilograms")), (UK, "B0CLAIM001"): ((32.0, 23.0, 20.0, "centimeters"), (1.40, "kilograms")),
    (UK, "B0CLAIM004"): ((17.8, 15.2, 2.0, "centimeters"), (0.18, "kilograms"))}
for (store, asin), ((l, w, h, du), (wt, wu)) in CATALOG_DIMS.items():
    title = next(v[2] for v in CAT[store].values() if v[1] == asin)
    put(S, "getCatalogItem-%s-%s.json" % (asin, store), {"asin": asin, "summaries": [{"marketplaceId": store, "brand": "Kettlewick", "itemName": title,
        "manufacturer": "Kettlewick"}], "dimensions": [{"marketplaceId": store, "package": {
            "length": {"unit": du, "value": l}, "width": {"unit": du, "value": w}, "height": {"unit": du, "value": h}, "weight": {"unit": wu, "value": wt}}}]})

# ---------------------------------------------------------------- earlier landed replies in the tree
old_fp = [fp_us(k, INF_OLD if k == "KW-INFUSER-2PK" else v, 3.22 if k == "KW-INFUSER-2PK" else fee_of(US, k, D("2026-08-15"))[1]) for k, v in DIMS_US.items()]
put(T, "raw/amazon-sp-api/reports/GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA/ATVPDKIKX0DER_2026-08-12_2026-08-15/report.tsv",
    "\t".join(FP_US) + "\n" + "".join("\t".join(str(r[c]) for c in FP_US) + "\n" for r in old_fp), raw=True)
put(T, "raw/amazon-sp-api/reports/GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA/ATVPDKIKX0DER_2026-08-12_2026-08-15/receipt.json",
    {"reportType": "GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA", "marketplaceIds": [US], "dataStartTime": "2026-08-12T00:00:00Z",
     "dataEndTime": "2026-08-15T16:00:00Z", "reportId": "52990014417", "reportDocumentId": "amzn1.spdoc.1.4.na.1c2e7f0a-11d3-4c1b-9b59-7d0e3a2b9f40",
     "read": "2026-08-15T16:02:31Z"})
old_rb = [rb_row(r) for r in RB if r[0] == US and r[1] <= "2026-06-30"]
put(T, "raw/amazon-sp-api/reports/GET_FBA_REIMBURSEMENTS_DATA/ATVPDKIKX0DER_2025-01-01_2026-06-30/report.tsv",
    "\t".join(RB_HEAD) + "\n" + "".join("\t".join(str(r[c]) for c in RB_HEAD) + "\n" for r in old_rb), raw=True)
put(T, "raw/amazon-sp-api/reports/GET_FBA_REIMBURSEMENTS_DATA/ATVPDKIKX0DER_2025-01-01_2026-06-30/receipt.json",
    {"reportType": "GET_FBA_REIMBURSEMENTS_DATA", "marketplaceIds": [US], "dataStartTime": "2025-01-01T00:00:00Z",
     "dataEndTime": "2026-06-30T23:59:59Z", "reportId": "52980011903", "reportDocumentId": "amzn1.spdoc.1.4.na.6a0b3c2d-90e1-4c1b-9b59-0f1e2d3c4b5a",
     "read": "2026-06-30T18:20:07Z"})

# ---------------------------------------------------------------- the seller's notes
put(T, "notes/costs.md", """# What each unit costs us (seller's own notes)

Landed cost per unit, from supplier invoices. "MYSC" = what I entered in Seller Central > Manage Your Sourcing Cost.

| Store | SKU | Landed cost | MYSC |
|---|---|---|---|
| US | KW-KETTLE-BLK | 14.20 USD | entered, approved 2025-04-10 |
| US | KW-SCALE-DGT | 7.90 USD | entered 2026-05-28, approved 2026-06-02 (I only found the page then) |
| US | KW-INFUSER-2PK | 1.85 USD | not entered |
| US | KW-FROTHER | 3.30 USD | not entered |
| US | KW-MUG-SET4 | 7.10 USD | not entered |
| UK | KW-KETTLE-BLK-UK | 11.60 GBP | entered, approved 2025-05-02 |
| UK | KW-MUG-SET4-UK | 5.70 GBP | not entered |
| UK | KW-INFUSER-UK | 1.50 GBP | not entered |
""", raw=True)
put(T, "notes/packaging.md", """# Packaging, measured by us

- KW-INFUSER-2PK: retail box 6.0 x 4.5 x 0.7 in, 0.30 lb with both infusers. Measured 2026-11-02 with a steel ruler and the
  kitchen scale. Same box since launch; we did not change the packaging in 2026.
- KW-MUG-SET4-UK: carton 30.0 x 21.5 x 14.0 cm, 1.18 kg. Measured 2026-07-20.
- KW-KETTLE-BLK: carton 12.5 x 9.0 x 7.8 in, 3.05 lb.

We never certified dimensions anywhere.
""", raw=True)
put(T, "notes/claims.md", """# Claims I remember

- UK, June 2026: two mug sets lost at the warehouse. I opened a case myself (case 1987654321) and it was paid in July.
- UK removal KWUKRMV0921 (60 infusers back to our Leeds unit): one parcel of 40 came by DPD on 2026-09-30. Nothing else came.
- I have never filed a US claim. I thought Amazon pays lost stock by itself now.
""", raw=True)
put(T, "notes/invoices.md", """# Supplier invoices

The PDFs are in our shared drive, not on this box.

- Ningbo Kettlewick Works, invoice NKW-2026-0312 (kettles, scales), 2026-03-12
- Ningbo Kettlewick Works, invoice NKW-2026-0618 (infusers, frothers, mugs), 2026-06-18
""", raw=True)

if SUMMARY:
    inf_new = [o for o in ORDERS if o["store"] == US and o["sku"] == "KW-INFUSER-2PK" and not o["replacement"]
               and INF_CHANGE <= o["day"] + dt.timedelta(1) < TODAY]
    mug_uk = [o for o in ORDERS if o["store"] == UK and o["sku"] == "KW-MUG-SET4-UK" and o["day"] + dt.timedelta(1) < TODAY and o["day"] >= D("2026-07-01")]
    print(json.dumps({
        "today": TODAY.isoformat(),
        "W1_us_kettle": {"lost_rows": {"2026-07-14": 3, "2026-08-22": 2, "2026-10-03": 4, "2026-11-12": 2}, "damaged_2026-10-20": 1,
                         "reimbursed": {"2481000101": {"date": "2026-07-29", "cash": 2, "inventory": 1, "per_unit": 14.20, "total": 28.40, "case_id": ""},
                                        "2481000177": {"date": "2026-10-24", "cash": 1, "per_unit": 14.20, "case_id": ""}},
                         "found": {"2026-09-05": 2, "fc": "QQB2", "lost_at": "QQA1"}, "n_row_2026-07-29": 1,
                         "open": {"ref": "KC1003A1", "date": "2026-10-03", "units": 4, "fc": "QQB2", "days_since": days_ago("2026-10-03")},
                         "researching": {"ref": "KC1112A1", "units": 2, "days_since": days_ago("2026-11-12")}, "naive_net_wrong": 8},
        "W2_uk_mugs": {"lost_rows": {"2026-04-02": 1, "2026-06-11": 2, "2026-10-09": 5},
                       "reimbursed": {"2590000031": {"date": "2026-04-08", "units": 1, "per_unit": 4.85, "case_id": ""},
                                      "2590000088": {"date": "2026-07-02", "units": 2, "per_unit": 4.85, "case_id": "1987654321"}},
                       "open": {"ref": "KL1009A8", "units": 5, "days_since": days_ago("2026-10-09")}, "seller_cost": 5.70},
        "S1_inbound": {"FBA18KWINF1": {"status": "CLOSED", "shipped": 480, "received": 462, "short": 18, "receipts": {"2026-08-26": 300, "2026-08-28": 162},
                                       "carton": {"FBA18KWINF1U000004": [40, 22]}},
                       "FBA19KWSCL2": {"status": "RECEIVING", "shipped": 600, "received": 570, "short_so_far": 30,
                                       "receipts": {"2026-11-09": 400, "2026-11-11": 170}}},
        "S2_uk_removal": {"order": "KWUKRMV0921", "created": "2026-09-21", "days_since": days_ago("2026-09-21"), "requested": 60, "shipped": 60,
                          "parcels": {"DPD 15501234567890": 40, "Evri H01KWF0000012345": 20}, "arrived": 40, "missing": 20, "removal_fee": 31.80},
        "R1_us_returns": {oid: {"refund": REFUNDS[oid], "days_since_refund": days_ago(REFUNDS[oid])} for oid in REFUNDS if oid.startswith("113")}
                         | {"113-4000006-0000006": {"replacement": REPLACEMENT["replacement"], "shipped": REPLACEMENT["shipped"],
                                                    "days_since": days_ago(REPLACEMENT["shipped"])},
                            "reimbursed": {"113-4000002-0000002": {"id": "2481000152", "date": "2026-09-22", "per_unit": 24.78}},
                            "candidates": ["113-4000003-0000003", "113-4000006-0000006"], "not_yet": ["113-4000004-0000004"],
                            "not_owed": ["113-4000001-0000001", "113-4000005-0000005"]},
        "R2_uk_returns": {"203-5000011-0000011": {"return_date": "2026-10-14", "disposition": "SELLABLE", "reason": "SWITCHEROO",
                                                  "status": "Unit returned to inventory", "lpn": "LPNRK0011UK1", "refund": "2026-10-06"},
                          "203-5000012-0000012": {"return_date": "2026-10-29", "disposition": "CUSTOMER_DAMAGED", "reason": "DEFECTIVE",
                                                  "lpn": "LPNRK0012UK8", "refund": "2026-10-22"}},
        "F1_us_infuser": {"amazon_now": {"dims_in": [6.2, 4.6, 1.4], "lb": 0.38, "tier": "Large Standard-Size"},
                          "amazon_before": {"dims_in": [6.0, 4.5, 0.7], "lb": 0.30, "tier": "Small Standard-Size", "as_of": ["fee preview 2026-08-15", "storage 2026-06..08"]},
                          "seller": {"dims_in": [6.0, 4.5, 0.7], "lb": 0.30}, "fee_before": 3.22, "fee_after": 3.71, "change_from": INF_CHANGE.isoformat(),
                          "orders_since_change": len(inf_new), "extra_total": r2(len(inf_new) * (3.71 - 3.22)),
                          "first_charge": min(o["day"] + dt.timedelta(1) for o in inf_new).isoformat(),
                          "w_and_d_adjustment": {"sku": "KW-SCALE-DGT", "posted": "2026-06-12", "lines": 2, "each": 0.42}},
        "F2_uk_fees": {"removal_KWUKRMV0315": {"requested": 30, "cancelled": 30, "shipped": 0, "fee": 15.30, "posted": "2026-03-28",
                                               "days_since": days_ago("2026-03-28"), "class": "non-itemised"},
                       "mug_fulfilment": {"fee": 4.12, "charges_since_2026-07-01": len(mug_uk),
                                          "first": min(o["day"] + dt.timedelta(1) for o in mug_uk).isoformat(),
                                          "last": max(o["day"] + dt.timedelta(1) for o in mug_uk).isoformat(), "class": "itemised"},
                       "amazon_dims_cm": [31.2, 22.0, 14.6], "amazon_kg": 1.32, "seller_dims_cm": [30.0, 21.5, 14.0], "seller_kg": 1.18},
        "V1_us_scale": {"2480000412": ["2025-02-11", "Lost_Warehouse", 2, 19.84], "2480000655": ["2025-05-06", "Lost_Warehouse", 3, 6.10],
                        "2480000893": ["2026-02-17", "Damaged_Warehouse", 1, 6.10], "2481000140": ["2026-09-08", "Lost_Warehouse", 2, 7.90],
                        "2481000152": ["2026-09-22", "CustomerReturn", 1, 24.78], "mysc_approved": "2026-06-02", "seller_cost": 7.90,
                        "below_cost_on_estimate_lines": r2(4 * (7.90 - 6.10))},
        "V2_uk_reversal": {"original": {"id": "2590000052", "date": "2026-05-19", "units": 2, "per_unit": 11.60, "total": 23.20},
                           "reversal": {"id": "2590000140", "date": "2026-10-27", "total": -23.20, "cash": -2},
                           "ledger": {"lost": {"2026-05-12": 2, "fc": "QQL1"}, "found": {"2026-10-22": 1, "fc": "QQL2"}}, "unmatched_units": 1},
        "C1_open_items": {"kettle": ["KC1003A1", 4], "FBA18KWINF1": 18, "orders": ["113-4000003-0000003", "113-4000006-0000006"],
                          "support_api": "403 Unauthorized"},
        "C2_uk_refund": {"order": "203-5000021-0000021", "refund": "2026-09-02", "days_since": days_ago("2026-09-02"), "returned": False,
                         "reimbursed": False},
    }, indent=2, ensure_ascii=False))
