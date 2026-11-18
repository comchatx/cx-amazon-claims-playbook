# Recovery economics: what a seller plausibly recovers, and what the paid services sell

Date read for every page: 2026-11-13 unless a row says otherwise.

**Summary.** Amazon publishes no loss rate, no share of cases it pays by itself and no reimbursement total. Every "share of revenue owed" figure in circulation (1%, 1–3%, 3%, 3.5%) comes from a seller of recovery services and states no method. Several of these figures date from before Amazon's 2024 automation and the 2025-03-31 move to sourcing-cost value. The best public evidence of what the 3P recovery market is now worth is a listed company's own numbers. SPS Commerce paid about $210M for Carbon6 (closed 2025-02-07 per its press release; "effective February 4, 2025" per its 10-Q) and sold its 3P recovery business on 2026-06-30 for $9.5M in cash. The press release gives the 1P focus as the reason; the earnings calls name Amazon's policy changes. That business served about 7,300 3P customers and earned about $10.5M a half-year. What a given seller can still claim is a formula over that seller's own reads (EC19): units through each stage, incidence, value per unit, the share Amazon pays unasked in that seller's store, cut by each kind's window. The share paid unasked is not one figure for every store: for UK warehouse-lost units Amazon's own UK posts disagree (a 2025-01-15 automation post against a 2026-04-06 staff post saying the claim is manual), so for a UK store the warehouse-lost kind may be the largest residual rather than the smallest (EC27). Fee overcharges are bounded by two fee windows, one for itemised and one for non-itemised fees, each counted from the charge (EC21). GL's size is not on record for this seat, so the seat's illustration (§5, held under *Seat's own*) is parameterised per unit volume and is not a measurement of any store.

Scope. This file covers item 6 of brief 548 and item 5's "about 30%". Each kind of claim has its own file in this tree: fc-lost-damaged, inbound-shortfalls, customer-returns, removals-disposals, fee-overcharges and value-and-reversals for the rules; sp-api-claims-surface for roles, reports and what the API cannot do; filing-and-conduct for case mechanics and penalised conduct. This file points to them and does not restate them. Homes used here: the post-to-store table and the automation dates are fc-lost-damaged's; the per-unit cap, the valuation-dispute window and the sourcing-cost limits are value-and-reversals'; the Support API and "no operation files a claim" are sp-api-claims-surface's; IDR and case routes are filing-and-conduct's. Vendor rates, look-backs and contract terms are held by the finance pack (cx-amazon-finance-playbook) as P-tool-17 and P-ref-31; §2 records only what this reading adds to them.

---

## 1. Amazon's own words on the money: automation, value, cap

### (a) Amazon's rule

The rules this file's arithmetic uses are held elsewhere; this file points to them.

- **Automation.** Amazon's statement that "almost all" warehouse-lost, warehouse-damaged and customer-return cases are paid without a claim, and that every removal claim stays manual: finance pack P-ref-13 (research/areas/refunds-reimbursements-adjustments.md); the posts, their dates and which store each post was issued for: see fc-lost-damaged FC3, FC4 and its post-to-store table. For the UK, Amazon's posts disagree on warehouse-lost units: see fc-lost-damaged FC5, and EC27 below for what that does to the money.
- **Which store each automation post addresses.** The post-to-store table is fc-lost-damaged's. This file re-checked the reading it rests on (§1(d)).
- **Windows by kind.** Held by each area file and finance P-ref-16. EC4 and EC5 below state only what a window does to an audit's reach.
- **Value.** Sourcing cost before a customer order since 2025-03-31, sale price (or refund) minus fees after: finance pack P-ref-14 and P-ref-15. The basis of a customer-return claim is contested between two files of this pack: see value-and-reversals VR27 and customer-returns RT42.
- **Cap and valuation-dispute window.** See value-and-reversals (its cap and dispute-window positions); finance pack P-ref-40 holds the US PDF of 2024-12-18.
- **Amazon's stated reason for the value change** (spokesperson Mira Dix, quoted by Modern Retail, 2024-12-20, https://www.modernretail.co/?p=113702):
  - "Our primary focus remains on continuously optimizing our network and processes to eliminate defects altogether";
  - the change is "to help drive a more consistent approach as more sellers are using our supply chain services";
  - "Specific cost data is not shared with any other seller in Amazon's store, including Amazon Retail".

  [read in official docs, relayed by press]
- **What Amazon does not publish.** No Amazon page, News post, SP-API document or statement found gives a fulfilment-centre loss rate, the share of cases paid without a claim, or a total reimbursed. The searches behind this include aboutamazon / sell.amazon.com and press quotes of spokespeople (2026-11-13). The 2024-12-20 spokesperson quote gives no figure.

### (b) What practitioners add on the size of the change [opinion]

- **Nova Data** (news page *amazon-reimbursement-policy-manufacturing-cost*, posted 2025-11-28, updated 2025-12-01; the figures are on this news page, not in the 2025-10-15 guide): "Sellers report 50-75% lower recovery amounts. The average recovery dropped from $18.50 to $6.20 per unit for typical products." No method is given. The finance pack already holds this figure.
- **Interviewees in Modern Retail** (2024-12-20), forecasting the drop before it took effect:
  - one seller's eligible claims of $108,000 could fall "more than 42%";
  - another expects payouts down "as much as 70%";
  - a third expects his reimbursements to be cut in half;
  - Josh Rawe (AmpliSell) expected one account's reimbursements to fall from "half a million dollars" to "as little as $250,000".
- **Seller Labs** (Nhan Dinh, 2025-05-29): a $27.99 item with a $5.40 cost is reimbursed "likely under $6", a loss "over 75%". This is the author's own example.
- **AMZ123 老虎站外推广** (2026-11-02, https://www.amz123.com/t/tg6kPptK): a $50 item that cost $12 "现在赔的是12美元" (is now reimbursed at $12). "有卖家报告，赔偿金额平均下降了50%到75%" (sellers report reimbursements down 50–75% on average).
- **Sellerview** (Himanshu Gaba, 2026-06-06): a SKU that "might now reimburse $9" instead of nearly $40. This is a hypothetical.

### (c) Into a skill / Read at run time

- **Into a skill:**
  - The change of value basis on 2025-03-31: point to P-ref-14 and P-ref-15.
  - The arithmetic of its effect on a pre-order loss: the per-unit fall is 1 − sourcing cost ÷ (sale price − fees). This holds whatever the seller's numbers are [inferred].
  - Amazon publishes no loss or automation rate.
- **Read at run time:**
  - the seller's own entered sourcing cost (Manage Your Sourcing Cost, Seller Central only; no SP-API operation reads or writes it, per P-ref-29);
  - the sale price and fees per SKU: Finances v2024-06-19 `listTransactions` (Finance and Accounting); fee preview `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` (Amazon Fulfillment or Pricing) and Product Fees `getMyFeesEstimates` (Pricing or Product Listing);
  - what Amazon actually paid per unit: `amount-per-unit` in `GET_FBA_REIMBURSEMENTS_DATA` (Pricing or Amazon Fulfillment).

### (d) The store each post was issued for: a control on the reading

The pack reads a Seller Forums post's store from the `"marketplaceId"` inside the post object (the one after `"contentMetadata"`), which differs from the host's own store list on the same page; the table lives in fc-lost-damaged. This file re-read six posts by plain GET on 2026-11-13 and checked the field against two posts whose store is known from their own words [command-verified: curl of each thread on the .com host, grep of the post object]:

| Thread | Post-object `marketplaceId` | Store by Amazon's id table | `datePublished` | What the text says about its store |
|---|---|---|---|---|
| 2f44617d (Jameson_Amazon) | A1F83G8C2ARO7P | UK | 2026-04-06 | Title: "Recover Your Lost FBA Inventory: UK Reimbursement Claims Explained" (control) |
| 0e07abc1 (Indy_Amazon) | ATVPDKIKX0DER | US | 2026-08-13 | US-spelled guide (control in spelling only) |
| 81c3235d (News_Amazon) | ATVPDKIKX0DER | US | 2024-07-24 | none |
| 6605eede (News_Amazon) | A2EUQ1WTGCTBG2 | Canada | 2024-07-24 | none |
| d0fc997e (News_Amazon) | A1F83G8C2ARO7P | UK | 2024-10-10 | none |
| 9a92846d (News_Amazon) | A1F83G8C2ARO7P | UK | 2025-01-15 | none |
| d8f9a56c (News_Amazon) | A39IBJ37TRP1C6 | Australia | 2025-08-14 | none |
| ce0bea71 (Roberto_Amazon, fee disputes) | ATVPDKIKX0DER | US | 2026-04-17 | none |

The one post whose title names its store carries that store's id, so the field-equals-store reading passes the one control available; Amazon does not document the field, so the reading stays [inferred] beyond that control. On this reading the 60–120-day returns post is the US one, the 45–105-day posts are Canada's and the UK's, and the 2025-10-15 window update (d8f9a56c) is Australia's, not the US's (see *Corrections to other packs*).

---

## 2. What the paid services sell: fee, look-back, claim kinds

### (a) Amazon's rule

No Amazon page sets or limits what a recovery service may charge. The fee is a private contract between the seller and the service; the finance pack's tools reference holds the vendors' rates and look-backs (P-tool-17; skills/refunds-and-reimbursements/references/tools.md). Amazon's rules for filing apply to whoever files (see filing-and-conduct). That no SP-API operation files a claim is sp-api-claims-surface's (see sp-api-claims-surface; finance P-ref-29). The services file through Seller Central:
- Helium 10 says it is "an official member of the exclusive Amazon Emerald Program" (MRS page, read 2026-11-13);
- Seller Investigators says it "executes all aspects of the reimbursement process within Amazon's Terms of Service".

### (b) What the services publish [opinion; the vendors' own pages unless marked]

**English-language services, as read 2026-11-13.** The finance pack's P-tool-17 (read 2026-11-09) is the home of vendor rates and look-backs. This table is evidence for the additions to it listed under *Corrections to other packs*; it holds no position of its own (EC1–EC3 withdrawn).

| Service | Fee as published | Look-back | Claim kinds named | Its own figures |
|---|---|---|---|---|
| **GETIDA** (getida.com/pricing; undated, © 2026) | "performance-based pricing starting at 20%"; "Pay nothing for the first $400 we recover". SellerHow (Chinese, checked 2026-08-16) read the same page then as "starting at 25%" and the terms (clause 1.10) as 25% of the total recovered; Titan Network and AmpliSell list 25% | "past 18 months worth of Amazon FBA transactions", then "continues in real time" | Disposed, Lost Warehouse, Damaged Inbound, Inbound, Inbound Retro, FNSKU Reconciliation, Lost Removal Order, Cancelled Shipping Costs, Pick & Pack overcharge (US), Wrong FNSKU Returns, Lost in Transit | "more than 90% of claims we open"; "an average of 63% of previously unsuccessful claims approved"; "approximately 40% of claims requiring Proof of Inventory Ownership or Proof of Delivery". On returns: "98.5%" auto-paid within 64 days (finance pack P-ref-31) |
| **Seller Investigators** (Carbon6; sellerinvestigators.com; no page date) | "a 25% commission only after you've been paid" | Not stated | Inbound (canceled shipments, receiving discrepancy, carrier damage); lost (in transit, in warehouse, unfair reimbursement); damaged (in warehouse, disposed by Amazon); customer returns ("not returned within 60 days", refunded more than paid, wrong item, chargeback not refunded); overages (removal orders, weights and dimensions, overcharged orders) | Calculator example: GMV $2,000,000 gives "Annual potential recovery" $20,000, i.e. 1.0%. "We find more money than competitor services for 99% of our new customers" (no basis). AmpliSell (2026-11-09) relays "over $100 million recovered; 95.9% case success rate". The 3P business was sold on 2026-06-30 (§3) |
| **Helium 10 Managed Refund Service** (helium10.com/tools/operations/managed-refund-service/) | Diamond 15%, Platinum 18% on this page. P-tool-17 records the pricing page as 10%/15%, so Helium 10's two pages still conflict | "your last 18 months of FBA transactions" | Inbound lost or damaged; warehouse wrongly disposed, misplaced, lost in removal, dimension discrepancies; customer-related (lost to customer, incorrect FNSKU returns, return or exchange discrepancies) | None. Its 2024 blog: "over 90% of reimbursement claims are currently made within 60 days" |
| **Threecolts Margin Pro** (FBA reimbursement service page, © 2026) | "Typical fee share ranges 15–25%, depending on your volume and our contract term" | "up to 9 months of data" | Reimbursement revaluation, warehouse transfer, damaged/lost/disposed, lost outbound, lost inbound, unused shipping labels, inbound placement fee errors, wrongful disposal, inbound mislabel fees | "$500M+" recovered; "sellers recover 40% of what they're owed"; "1–3%" of annual FBA revenue. "Amazon auto-credits only the most obvious, system-flagged issues" |
| **Threecolts Seller 365** (two pages) | Reimbursements page: "rates ranging from 5% to 15%, depending on your plan". Pro-sellers page: "0% commission for sellers under $1M in annual FBA sales", "10% above $1M". The two pages differ | Not stated | Under "Full claim coverage": lost inventory, damaged goods, return errors, warehouse transfer discrepancies, fee miscalculations (no count of categories on the reimbursements page as read 2026-11-13) | Estimator: $115,500 on $3.3M FBA revenue, "Based on an estimated 3.5% of annual FBA revenue"; "Actual recovery varies by account" |
| **SELLERLOGIC Lost & Found** (finance pack, read 2026-11-09) | 25% (a review site lists 20%) | — | Inbound, stock, FBA fees, missing returns, lost in warehouse, SAFE-T | "3% of their annually generated turnover" |
| **Refund Retriever** (finance pack) | 30% | — | — | — |
| **Refully, TrueOps, AMZRefund** (relayed by AmpliSell, 2026-11-09; own pages not read); **Eva** (search snippet only: AmpliSell's page as read 2026-11-13 does not name Eva) | Refully 18% (first $1,000 free); TrueOps 10% (first $1,000 commission-free); AMZRefund 25%; Eva 10% [unsupported by a page read] | — | — | Modern Retail (2024-12-20): TrueOps "manages reimbursements for 2,000 Amazon sellers" |
| **Jungle Scout "FBA Refunds"** (powered by Carbon6; Brian Connolly, 2023-11-29) | "a small 20% commission" | — | — | "potentially reclaiming thousands of dollars" |
| **sellerboard** (blog 2026-07-14) | Subscription ($19–$79/month per AmpliSell); no commission; does not file | 60-day tracking (AmpliSell) | Lost inventory, refunds with no return, fee overcharges | "roughly 1–3% of an FBA seller's annual revenue"; on $1M, "$10,000–$30,000 a year" |
| **Nova Data** (guide, 2025-10-15, updated 2026-10-08) | Tool | — | "Nine reimbursement categories" | "Recover $1,500-$3,000 annually"; "$2,500 Average annual reimbursements per seller"; a case study of "$4,200 recovered in 90 days" (25 SKUs, $80K/month); "Sellers with documentation get 90%+ approval rates. Those without? Under 40%." |
| **Titan Network** (Dan Ashburn, 2025-07-01, reviewed 2026-04-25) | Lists GETIDA, Carbon6 and Refunds Manager at 25%, Helium 10 MRS at 15/18%, sellerboard at $19/month | — | — | "$1,000 – $3,000 per $100K in annual FBA sales"; its table gives $1M revenue → $10,000–$30,000, or $7,500–$22,500 after a 25% fee |
| **Payability** | No recovery service found on its pages or in search (2026-11-13). Its advance product is in the finance pack (P-tool-18) | — | — | — |
| **Prestozon, Turbo/Seller Hub, AMZ Reimbursement, SellerLegend** | Searched by name (2026-11-13); no page stating a reimbursement fee was found. Listed as unread | — | — | — |

**Contract terms that change what a seller pays** [opinion; new to the packs, offered to the finance tools reference rather than held as a position here]:
- **SellerHow** (2026-08-16, Chinese), from reading the vendors' terms:
  - Seller Investigators reverses its fee when Amazon reverses a reimbursement; no such GETIDA clause was found.
  - GETIDA may change its rate, and a client who does not terminate within a notice period is treated as accepting it (clause 5.2 as SellerHow read it on 2026-08-16: 45 days).
  - Either party terminates without cause on written notice, and GETIDA may still pursue and charge on claims that arose before termination (clause 6.3 as SellerHow read it on 2026-08-16: 60 days' notice).
- **GETIDA** itself warns that some providers file returns claims on days 60–63 and so charge a fee on money Amazon would pay automatically from "day 64+" (finance pack, P-ref-31).

**Chinese-language tools and services** [opinion]:

| Who | Model | Kinds | Look-back | Its figures |
|---|---|---|---|---|
| **船长BI Captain BI 索赔助手** (m.captainbi.com/amz_claim.html; © 2016–2026) | "0抽佣" (zero commission), "船长分文不取" (Captain takes nothing). Its comparison table puts other services at 25% | Lists eight claimable cases (lost or damaged in delivery, misplaced, in warehouse, at receipt; refunded but not returned; returned but not restocked; over-refunded; wrong weight and dimensions). Its FAQ says "新版目前仅支持库存在亚马逊运营中心丢失或残损" (the current version supports only FC lost or damaged) | "首次索赔可追溯到18个月之前" … "每隔1个月为一个索赔周期" (the first claim reaches back 18 months, then monthly); ledger "前18个月至前45天" (18 months to 45 days back) | "每1000万营业额可帮卖家索赔回30万" (¥/$300k recovered per 10M of revenue, i.e. 3%); "会有1%-3%的出错率" (an error rate of 1–3%); "自上线已为卖家用户索赔回数亿元血汗钱" (hundreds of millions recovered). No method |
| **亿数通** (via 雨果网 / 亿卖大学, 2020-10-28, https://www.cifnews.com/article/81125) | Not stated: the article gives no fee for 亿数通 (an earlier reading of "0 commission" is not on the page as read 2026-11-13) | Order claims (customer refunded, item not returned within 45 days); inventory claims; claimable list generated on the 10th and 25th of each month | — | "1000W的年销售额，可找回至少10W的索赔款" (10M of annual sales recovers at least 100k, i.e. 1%), presented as an example; "索赔成功率高达90%以上" (success rate over 90%). Claims services take "最高比例可达所获索赔金额25%的佣金" (up to 25%). Uses the 2020 rules |
| **AMZ Refund, Seller Locker, Refunds Manager** (马帮ERP news, 2020-06-29, https://www.mabangerp.com/main_newsDetail.htm?id=4114) | AMZ Refund: a report priced at "索赔总金额的8%" (8% of the total claimable), after which the seller files. Seller Locker and Refunds Manager: 25% on success | Six kinds (destroyed without request; over-refund; dimension overcharge; warehouse lost or damaged not paid; replacement original not returned; return said paid but not paid) | — | Refunds Manager: lost claims take about 30 days, others at least 45. 马帮 itself offers no claims service in this piece |
| **领星, 积加, 赛狐, 易仓, 店小秘, 优麦云** | No commission; estimate inside the ERP; none files | — | — | Held in the finance pack as P-ref-39 and its ERP table; not repeated |
| **招单猫** (卖家之家, 2024-08-07, https://m.mjzj.com/article/du2ckgmjnthc) | US-based staff file; "索赔成功后才收费" (charges only on success), no rate given | — | — | None |

No Chinese commission-based claims service with a current public rate was found. This matches the finance pack. SellerHow calls 25% "这个品类的公价" (the going rate) for Western services.

### (c) Into a skill / Read at run time

- **Into a skill:** a pointer to the finance pack's tools reference (P-tool-17, P-ref-31) for the fee models and vendors, with this reading's additions offered to it (the report-only and zero-commission models; that a marketing rate and a contract rate can differ; the contract points that move the cost: commission on reversed money, on automatic payments, rate-change notice, termination tail). From this file itself: that a service's look-back does not widen what can be claimed, since each kind is bounded by Amazon's window for it (EC4).
- **Read at run time:** each vendor's current rate, from its own page and the seller's contract. The rates in the table above are evidence as read on 2026-11-13, not facts for a skill. No SP-API operation or Amazon page gives them (P-tool-17).

---

## 3. What happened to the paid services after 2024: a listed company's numbers

### (a) Amazon's rule

The changes behind this market are dated, and each is held elsewhere:
- shorter windows from 2024-10-23 (US post 81c3235d; the later window posts and the 2026-08-13 US staff post are in P-ref-16 and each area file);
- automation, with its start date per store (see fc-lost-damaged FC3, FC4, FC5 and its post-to-store table; finance P-ref-13);
- sourcing-cost value from 2025-03-31 (P-ref-14).

### (b) What SPS Commerce says about its own business [opinion: a vendor's statements and filings; the figures are the company's]

- **Purchase.** Announced 2025-01-02 at about $210M (Nasdaq / RTT News; the "about 40% in stock" split was not re-read). The 10-Q for the quarter to 2025-09-30 gives "total consideration transferred was $210.2 million, net of cash acquired": $142.5M in cash and 378,100 shares valued at $67.7M (about a third in stock), with "The acquisition became effective on February 4, 2025" (SEC EDGAR, Note B). The SPS press release of 2026-06-30 says the acquisition "closed on February 7, 2025". The two dates are the company's own and differ. Carbon6 was expected to add "approximately $40.0 million in revenue" in fiscal 2025, across its 1P and 3P products [not re-read 2026-11-13; the Q4 2025 transcript gives no Carbon6 revenue figure].
- **Q4 2025 call** (2026-02-12, Motley Fool transcript):
  - CFO Kimberly Nelson: "with the take rate model that we have there, we did see more to the lower end of what our expectation would be … along with the Amazon policy changes that have occurred"; "the number of 3P customers declined by 350".
  - CEO Chad Collins: "on the 3P side, these are much smaller businesses, they do have a higher churn rate".
- **Q1 2026 call** (MarketBeat via Yahoo Finance, 2026-04-30):
  - CFO Joe Del Preto: the Amazon portion "continues on a negative trajectory"; it "probably troughs somewhere in the middle of this year, towards the end of this year" (the article's summary: "trough mid-to-late 2026"); the CEO spoke of "the headwinds from Amazon's policy changes";
  - a subscription fee "quite modest at $19.99 a month" for what Del Preto called "the very smallest of our 3P take rate only Amazon customers" and "very, very low revenue customers";
  - the article (not a quote) says the company projected losing "as many as 4,000 3P suppliers in 2026" as the fee rolled out.
- **Sale.** On 2026-06-30 SPS announced it "has completed the sale" of its 3P Revenue Recovery business for "a cash payment of $9.5 million at closing" (the headline says "Agreement to Sell"). The press release gives "an estimated loss on sale of approximately $20 million in Q2 2026" and, as its reason, that the divestiture "focuses SPS on the strategic opportunity with 1P suppliers"; it does not mention Amazon's policy changes. The Q2 call gave $23.5 million (finance pack, P-ref-32; the Q2 transcript was not re-read here). The buyer is not named.
- **Q3 2026 call** (Investing.com transcript, 2026-10-29), CFO Joe Vruwink:
  - "The divestiture reduced our total customer count by approximately 7,300 3P customers";
  - "we expect divestiture to reduce second half 2026 revenue by approximately $10.5 million";
  - "Amazon has implemented certain policy changes which have been unfavorable to recovery yields".

  CEO Collins says these new changes concern "when one of our suppliers makes a short shipment to Amazon" and "our ability to redispute … a submission". These are 1P (vendor) recovery rules: a supplier's shipment to Amazon Retail, not an FBA seller's claim [inferred from "suppliers" and SPS's 1P/3P split].

### (c) Into a skill / Read at run time

- **Into a skill:** the dated history. One recovery business, bought for about $210M in early 2025, was sold for $9.5M in cash about 17 months later; its owner named Amazon's policy changes on its earnings calls, and the 1P focus in the sale's press release. This is a fact about a market, not about a seller's store.
- **Read at run time:** nothing. No seller data bears on this.

---

## 4. Published figures versus marketing

### (a) Amazon's rule

None. See §1(a), last point.

### (b) What is published, sorted by what stands behind it

| Figure | Who, date | What stands behind it |
|---|---|---|
| 1–3% of annual revenue | GETIDA (Yoni Mazor, ~2023, MWQHJ #449, via the finance pack); sellerboard 2026-07-14; Threecolts; ecomEngine (Bob Norberg, 2026-10-19: "Industry audits suggest"); Titan 2025; Sellerview 2026-06-06 ("Every recovery service quotes the same number"); Modern Retail 2024-12-20 (quoting Joel MacPherson of TrueOps, a recovery service) | No method. Sources cite each other or "industry audits" |
| up to 1% | Helium 10 MRS (finance pack); Seller Investigators' calculator example (1.0%); 亿数通 via 雨果网 2020 (1%) | A calculator default and a worked example |
| 3% | SELLERLOGIC (finance pack); 船长BI ("每1000万营业额…30万") | No method |
| 3.5% | Seller 365 estimator | "assumed" |
| $1,500–$3,000 a year; $2,500 average per seller | Nova Data 2025/2026 | No method |
| "40% of what they're owed" / "approximately 40%" left by automation | Threecolts; ecommerceparadise (finance pack) | No method |
| 98.5% of FBA customer-return issues auto-paid within 64 days | GETIDA (finance pack, P-ref-31) | "over 2 million Getida sample data points": the only figure with a stated sample |
| FC loss 0.3–1.0% of throughput value (labelled "Documented US FBA range"); lost inbound 0.5–1.0% and adjustments 0.05–0.15% of on-hand value (in its worked example only); return rate "Category average 5–10%. Apparel can be 15–25%" | ecomcalctools reimbursement calculator, updated 2026-06-17 | Says "Loss rates are documented US FBA defaults" and cites only Amazon's help page G200684750 for the 18-month window. No source for the rates |
| 99.943% inbound accuracy (70 units short of 123,228 shipped in 2023) | Seller ASV_Vites, sellersasksellers.com, 2024-01-30 | One seller's own count: shipments expected versus received, over-receipts discounted |
| "over 1300 units" lost "since May 2023" (2023-08-25, lost-inbound thread); "the 1500 units Amazon lost on FC transfer" (2024-01-30) | Seller packetfire, sellersasksellers.com | One seller's reports, in two threads |
| ~$2,900 revenue per 3P customer a year, so roughly $11,500 recovered per customer a year | Inferred from SPS (§3) | A vendor's audited-company figures, divided by this seat (held under *Seat's own*; EC12 withdrawn) |

**Published research** [research]:
- No peer-reviewed or industry study of FBA loss, damage or reimbursement rates was found (searches 2026-11-13; the finance pack's search of 2026-11-09 agrees).
- Adjacent studies, none measuring FBA:
  - DeHoratius & Raman, "Inventory Record Inaccuracy: An Empirical Analysis", *Management Science* 54(4):627–641 (2008): inaccuracies in 65% of 369,567 inventory records at a US retailer. Read from abstracts and a 2022 M&SOM citation; the paper itself was not opened.
  - NRF National Retail Security Survey 2023: average shrink 1.6% of sales in FY2022, about two-thirds of it theft. Store retail; not comparable to a fulfilment centre.
  - NRF / Happy Returns, 2025-10-15: 19.3% of US online sales expected to be returned in 2025 (15.8% of all retail). Consumer and retailer surveys. This is all e-commerce, not Amazon.

### (c) Into a skill / Read at run time

- **Into a skill:**
  - Every "% of revenue owed" figure is a vendor's, without method.
  - Several of them predate 2024-10-23 or 2025-03-31 and so measure a pool Amazon has since changed.
  - Vendors contradict each other on customer returns: GETIDA reports 98.5% auto-paid, while sellerboard says unreturned returns are "almost entirely seller-initiated".
- **Read at run time:** the seller's own split, which is the only figure that holds for their store.
  - `GET_FBA_REIMBURSEMENTS_DATA` (Pricing or Amazon Fulfillment): sum `amount-total` by `reason`, and by blank versus filled `case-id`. A blank `case-id` read as "Amazon paid on its own" is a seat reading until a live account confirms it (P-ref-20).
  - `GET_LEDGER_DETAIL_VIEW_DATA` (Amazon Fulfillment) for the units the losses came from.

---

## 5. An inferred estimate per kind, per unit volume (the seat's illustration)

Everything in this section is **[inferred]**, and its totals are the seat's own: they rest on incidences the seat chose and enter no skill (see *Seat's own*). Only the model's form (EC19) and the value basis by kind (EC10) are positions. No seller's data is used.

**GL's size is not on record for this seat.** Brief item 6 asks what a seller of GL's size plausibly recovers. Neither the brief nor any page this seat may read states GL's units, revenue, stores or SKU count, and no seller data may be read here. So the illustration is parameterised per volume: per 1,000, 10,000 and 100,000 units inbound a year, and GL's figure is the row its own ledger puts it in at the first live-account run (open question 10).

**Model.** For each kind:

  owed by claim = units through the stage × incidence × value per unit × (1 − share Amazon pays without a claim in that store)

The window for the kind then cuts what can still be claimed by the time anyone looks.

**Base parameters** [seat; replaced by the seller's own at run time]:

| Parameter | Value | Read at run time from |
|---|---|---|
| U, units inbound a year (≈ units sold) | 10,000 (and ×0.1, ×10 below) | `GET_LEDGER_SUMMARY_VIEW_DATA` receipts (Amazon Fulfillment); Fulfillment Inbound v0 `getShipmentItems` `QuantityReceived` (Amazon Fulfillment) |
| P, average sale price | $30 | Finances `listTransactions` (Finance and Accounting) |
| C, sourcing cost | $8 (27% of P) | Seller Central Manage Your Sourcing Cost (no API); else the seller |
| Fees on a sale (referral 15% + fulfilment) | $4.50 + $4.50 | `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` / `getMyFeesEstimates` (Pricing) |
| V_post, post-order value = P − fees | $21 | as above |
| Store | US unless the row says UK | the seller's marketplace participations |

Revenue on these numbers is about $300,000 a year. Dollar figures are illustrative; a UK store's money is in GBP.

| Kind | Incidence (source) | Units | Value/unit | Owed in total | Amazon pays unasked | Left for a claim |
|---|---|---|---|---|---|---|
| **A. FC lost or damaged before an order** (fc-lost-damaged), US | 0.1–1.0% of units. The upper end is ecomcalctools' unsourced 0.3–1.0%; the lower end is [seat], given ASV_Vites' 0.06% inbound | 10–100 | C = $8 | $80–$800 | "almost all" (US post 81c3235d; P-ref-13); a vendor says ~60% ("40% left behind", unsourced) | **$0–$320** |
| **A-UK. The same kind in a UK store** | as A; the lost/damaged split is unknown [seat: shown as all lost for the upper bound] | 10–100 | C | £-denominated, as A | Amazon's UK posts disagree for lost units: automatic from 2025-01-15 (d0fc997e, UK) against "requires manual claim submission (automatic reimbursement disabled since August 2022)" (2f44617d, UK staff, 2026-04-06); sellable warehouse damage "Automatically reimbursed within 21 days" (2f44617d). See fc-lost-damaged FC5 | **up to the full lost value: $80–$800 equivalent** if the staff post holds; as A if the 2025 post holds |
| **B. Inbound shortfall** (inbound-shortfalls) | 0.06% (ASV_Vites, measured, one seller) to 1.0% (ecomcalctools, unsourced) | 6–100 | C = $8 | $48–$800 | None through the IDR portal (P-ref-13) | **$48–$800** |
| **C. Customer return not returned, wrong item, or damaged by Amazon** (customer-returns) | Return rate 5–20% (ecomcalctools; NRF online 19.3%) × faulty share 2–10% [seat] | 10–200 | V_post = $21 (basis contested: value-and-reversals VR27 against customer-returns RT42) | $210–$4,200 | 98.5% (GETIDA, sample) to "almost entirely seller-initiated" (sellerboard) | **$3–$4,200** |
| **D. Removal lost or damaged** (removals-disposals) | Removals 2–10% of inbound × loss 0.5–3% [seat; no published rate] | 1–30 | C = $8 | $8–$240 | None ("all removal claims … manually") | **$8–$240** |
| **E. Itemised fee overcharge: fulfilment fee on a mismeasured SKU** (fee-overcharges) | 0–10% of units on a mis-tiered SKU [seat] × $0.35–$0.89 a unit (sellerboard's hypothetical $0.35; an EU forum case of Small→Large standard, $2.81→$3.70) | 0–1,000 | $0.35–$0.89 | $0–$890 | Not stated by Amazon for the US; an automatic look-back true-up exists under the EU certification regime (fee-overcharges FE7) | **$0–$890**, of which only charges inside the itemised window are claimable (EC21) |
| **E′. Wrong referral-fee category** (fee-overcharges) | Rare, but large when it happens: GETIDA's example is 8% vs 15% | e.g. one SKU of 1,000 units | 7% × $30 = $2.10 | e.g. $2,100 | — | a tail, not a rate |
| **E″. Non-itemised fee error: removal or disposal order fees, prep and labelling** (fee-overcharges) | No published rate [seat: not estimated] | — | — | — | — | not estimated; claimable inside the non-itemised window, which is longer than the itemised one (EC21) |
| **F. Under-valued reimbursement** (value-and-reversals) | Units paid at Amazon's estimate where the seller entered no cost | 10–100 (from A) | gap $0–$4 [seat] | $0–$400 | — | **$0–$400**; $0 by definition once the seller's own cost is entered |
| **G. Reversal with no unit found** (value-and-reversals) | Unknown. One case of "$1,100" (My Amazon Guy, finance pack P-ref-18) | — | — | — | — | not estimable |

**Totals per volume** (A–F, US, excluding E′, E″ and G) [seat's own; linear scaling is itself a seat assumption, and a seller's incidences need not scale with volume]:

| Units inbound a year | Low | Central [seat picks] | High |
|---|---|---|---|
| 1,000 | ≈ $6 | ≈ $64 | ≈ $685 |
| 10,000 | ≈ $60 | ≈ $635 | ≈ $6,850 |
| 100,000 | ≈ $600 | ≈ $6,350 | ≈ $68,500 |

The 10,000-unit central case is built from: A 50 units, 10% unpaid = $40; B 0.2% = 20 units = $160; C 1,000 returns × 5% = 50 units × $21 = $1,050 owed, at a 90% auto-paid share $105 left; D 10 units = $80; E 300 units × $0.50 = $150; F 50 units × $2 = $100.

**For a UK store** [seat's own]: if the UK staff post of 2026-04-06 holds, the A-UK row replaces A. On the central picks, the 50 lost-or-damaged units carry up to $400 to a claim instead of $40 (all lost; less by the damaged share, which the staff post says is paid within 21 days when sellable). The 10,000-unit central case then reads up to about $995, and the warehouse-lost kind is the **largest** central row, not the smallest. Which statement holds for a store is read at run time: whether `Lost_Warehouse` rows with blank `case-id` arrive in that store's `GET_FBA_REIMBURSEMENTS_DATA` (fc-lost-damaged open question 1). The UK staff post also lists "Items not returned within 45 days (UK/WW) when returnable" under reimbursable events in a post about manual claims; whether UK returns are paid unasked is customer-returns'.

**Before the 2024–2025 changes**, on the same parameters [seat's own]: A, B and D were valued near the sale price (about $21 rather than $8 a unit, ×2.6); A and C were not auto-paid (US); and the windows were longer than the 2024–2025 posts' (each area file holds them). The same model then gives A $210–$2,100 and C $210–$4,200 claimable in full, and a central case of about $3,000 per 10,000 units, or 1% of revenue. This is consistent with vendors' 1–3% being a pre-2024 figure [inferred].

**Cross-check against the SPS numbers**: held under *Seat's own* (formerly EC12, EC13).

**Into a skill:** the model's form (EC19), each value basis by kind (EC10), that the share paid unasked is a per-store fact (EC27), and where each input is read.

**Read at run time:** every input, from the reads named in the parameter table, and the seller's own history of reimbursements by `reason` and `case-id` (EC26).

---

## 6. What a seller's choice changes (no recommendation)

The choices, side by side, each with what it changes:
- **File in Seller Central themselves.** No commission. Costs the seller's own time, and every kind has its window.
- **A commission service.** It files for the seller, usually via its own Seller Central access. It takes a share of what is paid (the rates are evidence in §2 and P-tool-17), and possibly of money Amazon would have paid anyway, depending on the contract. Its look-back does not reopen closed windows (EC4).
- **A subscription or ERP tool** (sellerboard, Refund Genie, 领星, 积加, 易仓, 船长BI). These find candidates and the seller files. A fixed fee or none.
- **Enter a sourcing cost on Manage Your Sourcing Cost.** Once Amazon approves it, eligible pre-order reimbursements issued after the approval date are valued at the seller's own cost instead of Amazon's estimate. It does not revalue earlier reimbursements (value-and-reversals VR8); a declined entry leaves the previously approved amount or Amazon's estimate in force (VR9); units unsellable when lost, damaged or removed are reimbursed at a reduced estimated cost (VR25). The seller shares that cost with Amazon, under the spokesperson's data statement in §1.
- **Do nothing for a kind.** The money in that kind lapses when its window closes. Amazon's automatic payments continue regardless.

Practitioners weigh these choices with worked examples of their own (SellerHow's is under *Seat's own* as evidence); none is a threshold this pack holds.

---

## 7. The survey's "about 30%": two readings, each answered

The SP-API plugins survey (2026-11-09) gave the claims job "Size: 2–3 skills (`claim-windows`, `reimbursement-value`, `ledger-reading`), about 4 references, no script. **About 30%.**", where size "is measured against the listing playbook, counted at its head: 5 skills, 19 references (about 23,500 words …)". Brief item 5 asks where "about 30%" holds "after Amazon automated most warehouse-lost and return cases", which invites a second reading. Both are answered; both answers are the seat's own and enter no skill.

**(a) As the survey wrote it: a size against the listing playbook.** The tree's files call for references the survey did not count: windows by store with the post-to-store table; evidence by claim kind; report columns and pitfalls (returns, removals, reimbursements, ledger); valuation and reversals; fee-overcharge detection including the EU certification regime; filing, conduct and the steps only Seller Central can do; the API surface. That is about 6–8 references against the listing playbook's 19, about 32–42% by reference count, before skills and words are counted. So "about 30%" holds as a size only if valuation, reversals and the vendor material stay in the finance pack's `refunds-and-reimbursements` skill and are pointed to; kept here, the size is nearer 35–45% (the completeness review's count agrees). Automation does not shrink the size much: an automated kind still needs its reads to show what Amazon paid beside what was lost, and the UK case (EC27) keeps warehouse-lost a live claim kind for at least one store.

**(b) Read as a share: what part of the old recovery pool is left after automation.** No source supports a percentage. Amazon publishes no loss rate, automation share or total (EC6). Every vendor percentage states no method, and several predate 2024-10-23 or 2025-03-31 (EC7). The per-unit value on pre-order kinds fell by 1 − C ÷ (P − fees) (EC8). One listed company's 3P recovery business sold for $9.5M about 17 months after the purchase of its parent for about $210M (EC11). The seat's own illustration gives a post-change central case of about $635 against about $3,000 before, about 21%, but that ratio rests entirely on the seat's picks and on US automation; for a UK store it is higher. A share for any store, GL's included, is read from that store's own reimbursements over 2023–2026 (EC28; open questions 1–7, 10).

**The survey's "15–25%" service range** is too narrow as read today: 0% (Seller 365 under $1M, Captain BI) to 30% (Refund Retriever), plus 8% for report-only (2020). Held as a correction to the survey.

---

## Positions

Tags: [read in official docs], [command-verified], [opinion], [inferred]. A value that differs by store or date sits in *Values that move*; a position states the rule and where the value is read.

- **EC1.** (withdrawn: vendor fee models are the finance pack's, P-tool-17 and P-ref-31; this reading's additions are offered there under *Corrections to other packs*.)
- **EC2.** (withdrawn: a vendor's terms are not Amazon's rule; the marketing-against-contract rate evidence moves to *Corrections to other packs* as an addition to P-tool-17, with §2 as evidence.)
- **EC3.** (withdrawn: contract terms are not Amazon's rule; held in §2 as evidence and offered to the finance tools reference.)
- **EC4.** What an audit can still claim is bounded by each kind's window in the seller's store, not by the service's look-back. Services advertise look-backs (values in *Values that move*); Amazon's windows differ by kind, by store and by date (see each area file, and fc-lost-damaged's post-to-store table for which store each post addresses; finance P-ref-16). So whether a look-back exceeds the window depends on the kind and on which statement governs the seller's store. Read at run time: the store's FBA inventory reimbursement policy (G200213130) as the seller's store shows it, and the latest News or staff post issued for that store. Sources: vendor pages (§2) [opinion]; P-ref-16 [read in official docs]; the bound is [inferred].
- **EC5.** Amazon's 2024 posts under the one title *Update on Reimbursement Automation and Eligibility Window to file reimbursement claims* give two customer-returns windows, and on the post-object store reading they are two stores' rules, not one store's contradiction: the US post (81c3235d) gives a window counted "after the customer refund or replacement date" whose bounds differ from those of the Canadian (6605eede) and UK (d0fc997e) posts. For the US store a contradiction remains in time: the 2026-08-13 US staff post (0e07abc1) states a different window again. Values in *Values that move*. Which governs a store today is customer-returns'; read at run time as in EC4. Sources: 81c3235d, 6605eede, d0fc997e, 0e07abc1 (read 2026-11-13); store per §1(d) and fc-lost-damaged's table [read in official docs; store reading command-verified against one control, otherwise inferred].
- **EC6.** Amazon publishes no fulfilment-centre loss rate, no share of cases paid without a claim, and no reimbursement total. Every "% of revenue owed" figure found (1%, 1–3%, 3%, 3.5%) is a recovery vendor's or a tool maker's and states no method. Sources: searches 2026-11-13 and §4 table [opinion for the figures]. The absence is the seat's finding over the searches named, extending finance pack P-ref-31 [inferred].
- **EC7.** Vendors' figures that predate 2024-10-23 (shorter windows), 2024-11-01 or 2025-01-15 (automation) or 2025-03-31 (sourcing-cost value) measure a pool Amazon has since changed. Examples: the 2020 "1000W→10W" of 亿数通 via 雨果网, and GETIDA's "1% to 3%" (~2023). The dates are in finance pack P-ref-13, P-ref-14 and P-ref-16 [read in official docs]. Sources: §4 table [opinion]; the reading is [inferred].
- **EC8.** For a unit lost or damaged before a customer order, the per-unit fall from the 2025-03-31 value change is 1 − sourcing cost ÷ (sale price − fees). Practitioners report falls of 50–75% (Nova Data: "$18.50 to $6.20 per unit"; AMZ123 2026-11-02), and sellers interviewed before the change forecast 42%, 50% and 70%. Read at run time: the seller's cost (Manage Your Sourcing Cost; no API), and price and fees as in §1(c). Sources: finance pack P-ref-14 [read in official docs]; Nova Data; AMZ123 tg6kPptK; Modern Retail 2024-12-20 [opinion]; the formula is [inferred].
- **EC9.** Amazon's spokesperson gave the value change's purpose as "a more consistent approach as more sellers are using our supply chain services". The spokesperson also stated that "Specific cost data is not shared with any other seller in Amazon's store, including Amazon Retail". Source: Mira Dix, quoted in Modern Retail, 2024-12-20 [read in official docs, relayed by press].
- **EC10.** By kind, value per unit follows the moment of loss. A loss before an order (FC lost or damaged, inbound, removals) is valued at sourcing cost (P-ref-14). A customer-return claim is valued after fees on a post-order basis, refund or sale price: the exact basis is contested inside this pack (see value-and-reversals VR27 against customer-returns RT42; finance P-ref-40 quotes the US PDF of 2024-12-18 as "the refund amount or the sales price of the replacement item on the original order minus applicable fees"). Whenever the post-order value exceeds sourcing cost, a returns unit is worth more per unit than a warehouse unit. Sources: finance pack P-ref-14 and P-ref-40 [read in official docs]; the comparison is [inferred].
- **EC11.** SPS Commerce:
  - bought Carbon6 (Seller Investigators, ChargeGuard) for about $210M; announced 2025-01-02; closed 2025-02-07 per the 2026-06-30 press release, "effective February 4, 2025" per the 10-Q; "$210.2 million, net of cash acquired"; about $40M of fiscal-2025 revenue expected (not re-read);
  - announced on 2026-06-30 the completed sale of its 3P Revenue Recovery business for $9.5M in cash, at an estimated loss of about $20M (press release) or $23.5M (Q2 call); the press release's stated reason is the 1P focus;
  - cited Amazon's policy changes and the take-rate model on its Q4 2025, Q1 2026 and Q3 2026 calls.

  Sources: SPS press release 2026-06-30; SEC 10-Q (quarter to 2025-09-30); Nasdaq / RTT News 2025-01-02; Motley Fool Q4 2025 transcript 2026-02-12; MarketBeat via Yahoo 2026-04-30; Investing.com Q3 2026 transcript 2026-10-29 [opinion: a vendor's statements; extends finance pack P-ref-32].
- **EC12.** (withdrawn: its substance, about $11,500 recovered per customer a year, is the seat's division of SPS figures; moved under *Seat's own*. The SPS figures themselves stay in EC11 and §3.)
- **EC13.** (withdrawn: its substance, recoveries of about $960 a year or less, is the seat's inference from a fee SPS charged; moved under *Seat's own*. The quotes stay in §3.)
- **EC14.** The "short shipment" and "redispute" changes that SPS said hurt recovery yields in Q3 2026 concern suppliers' shipments to Amazon Retail (1P vendor recovery), not FBA seller claims. They are not evidence about FBA reimbursement. Sources: Investing.com Q3 2026 transcript (Chad Collins: "when one of our suppliers makes a short shipment to Amazon") [opinion]; the scope reading is [inferred].
- **EC15.** On customer returns, vendors contradict each other:
  - GETIDA reports that Amazon auto-pays 98.5% of FBA customer-return issues within 64 days, from "over 2 million" data points;
  - sellerboard says unreturned customer returns are "almost entirely seller-initiated".

  Amazon's post says "almost all … customer returns cases" are reimbursed proactively. For a given store, the split is read at run time from `GET_FBA_REIMBURSEMENTS_DATA` (Pricing or Amazon Fulfillment): customer-return rows (the `reason` value seen in sellers' reports is `CustomerReturn`; Amazon publishes no list of `reason` values, P-ref-19, P-ref-35) with blank versus filled `case-id`. Joining those rows to the refunds in Finances `listTransactions` (Finance and Accounting) and to `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` (Amazon Fulfillment or Pricing) shows how many refunds were paid unasked and how many were paid at all. Sources: finance pack P-ref-31 (GETIDA), P-ref-13, P-ref-20; sellerboard 2026-07-14 [opinion; official for P-ref-13].
- **EC16.** One seller measured inbound accuracy at 99.943% for 2023: 70 units short of 123,228 shipped, counted as shipments expected versus received, over-receipts discounted. Another reported "over 1300 units" lost "since May 2023" (2023-08-25) and, later, "the 1500 units Amazon lost on FC transfer" (2024-01-30). These are single sellers' counts, not rates for FBA. Sources: sellersasksellers.com, ASV_Vites 2024-01-30; packetfire 2023-08-25 and 2024-01-30 [opinion].
- **EC17.** The loss-rate inputs that recovery calculators use are not sourced:
  - ecomcalctools: FC 0.3–1.0% of throughput value ("Documented US FBA range"; "Loss rates are documented US FBA defaults"), and, in its worked example only, lost inbound 0.5–1.0% of inbound value and adjustments 0.05–0.15% of on-hand value;
  - Captain BI: "会有1%-3%的出错率" (there is an error rate of 1–3%).

  The seller's own rate is read at run time from `GET_LEDGER_DETAIL_VIEW_DATA` (Amazon Fulfillment), the adjustment events against receipts, and from Fulfillment Inbound v0 `getShipmentItems` (`QuantityShipped` versus `QuantityReceived`, Amazon Fulfillment). Sources: ecomcalctools (2026-06-17); m.captainbi.com [opinion].
- **EC18.** No peer-reviewed or industry study of FBA loss, damage or reimbursement rates was found. The nearest published research measures other things:
  - store record inaccuracy (DeHoratius & Raman 2008: 65% of 369,567 records);
  - store shrink (NRF NRSS 2023: 1.6% of FY2022 sales, mostly theft);
  - online return rates (NRF / Happy Returns 2025: 19.3% of US online sales).

  None measures an Amazon fulfilment centre. Sources: as named [research; DeHoratius & Raman read from abstracts only].
- **EC19.** What an amount owed is made of, by kind: units through the stage × incidence × value per unit × the share Amazon does not pay unasked. The window then cuts what can still be claimed. Each input is the seller's own and is read at run time from the reads in §5's parameter table. Source: seat's model over P-ref-13, P-ref-14 and P-ref-40 [inferred].
- **EC20.** (withdrawn: its substance, the $60–$6,850 range and the $635 central case, rests on the seat's own incidences; moved under *Seat's own* with §5. EC19 keeps the model's form.)
- **EC21.** An FBA fee-reimbursement request has a window counted from the date of the disputed charge, and Amazon states two: one for itemised fees (tied to an ASIN or FNSKU, typically weight or dimension errors: fulfilment, customer-returns, monthly and long-term storage fees) and a longer one for non-itemised fees (removal or disposal order fees, prep and labelling). So what a seller can still recover on a mismeasured SKU is the per-unit overcharge times the units charged inside the itemised window, while a non-itemised error reaches further back. The windows are fee-overcharges' (see fee-overcharges FE9); values in *Values that move*. Read at run time: *FBA fees reimbursement policy: Weight and dimensions* (GL7U4JFSDXUTQAJ) as the store shows it and the latest staff guide on disputing charges for that store; the charge date from `listTransactions` `postedDate`. Sources: FE9; Roberto_Amazon ce0bea71 (US, 2026-04-17, re-read 2026-11-13) [read in official docs]; the consequence is [inferred].
- **EC22.** Services' published success rates:
  - GETIDA: "more than 90% of claims we open"; "63% of previously unsuccessful claims"; "roughly 40% of claims require Proof of Inventory Ownership or Proof of Delivery";
  - Seller Investigators: "95.9%", relayed by AmpliSell;
  - Nova Data: "90%+" with documentation and "Under 40%" without.

  None states a denominator or method. Sources: getida.com/pricing; AmpliSell 2026-11-09; Nova Data guide [opinion].
- **EC23.** No Chinese tool or service found files claims for a commission at a current public rate. A Chinese "0 commission" claim assistant exists: 船长BI ("船长索赔0抽佣"; its comparison table puts other services at "25% 佣金"), which in its current version covers FC lost or damaged only. 亿数通 (2020) offered a claims tool, but the article read states no fee for it. ERPs (领星, 积加, 赛狐, 易仓) estimate at no extra charge, and the seller files. 马帮 and 店小秘 show no claims service. Sources: m.captainbi.com/amz_claim.html; cifnews 81125; mabangerp news 4114; finance pack P-ref-39 [opinion].
- **EC24.** Chinese claim assistants read back a fixed span (船长BI: "首次索赔可追溯到18个月之前", the first claim reaches back a stated span; values in *Values that move*). Items in that span outside the window Amazon applies to their kind are not claimable. The window is read as in EC4. Source: m.captainbi.com [opinion]; the consequence is [inferred].
- **EC25.** Whether to file oneself, pay a share to a service, use a subscription or ERP tool, enter a sourcing cost, or leave a kind alone is the seller's choice. §6 lists the choices side by side with what each changes: commission, time, who files, the value basis of eligible pre-order reimbursements issued after an approved cost (value-and-reversals VR8, with VR9 for a declined entry and VR25 for unsellable units), and money lapsing at the window. Sources: §2 vendor pages, SellerHow 2026-08-16 [opinion]; P-ref-14 [read in official docs].
- **EC26.** A seller's own history of what Amazon paid, by kind and by whether a case was filed, is in `GET_FBA_REIMBURSEMENTS_DATA`. Sum `amount-total` by `reason`, split `quantity-reimbursed-cash` from `-inventory`, and net reversals through `original-reimbursement-id`. It needs Pricing or Amazon Fulfillment, and it is the only "recovery figure" that holds for that store. Sources: finance pack P-ref-17, P-ref-19, P-ref-20 [read in official docs]; the use is [inferred].
- **EC27.** The share Amazon pays without a claim is a fact of the seller's store, not one figure for every store: what a kind leaves for a claim depends on whether Amazon pays it unasked there. For UK warehouse-lost units Amazon's own UK posts disagree (fc-lost-damaged FC5: the UK automation post d0fc997e against the UK staff post 2f44617d saying the claim is manual), so for a UK store the warehouse-lost kind can carry its whole lost value to a claim. Read at run time: whether `Lost_Warehouse` and `Damaged_Warehouse` rows with blank `case-id` arrive in that store's `GET_FBA_REIMBURSEMENTS_DATA` (Pricing or Amazon Fulfillment) after the store's automation date, against the ledger's lost and damaged adjustments (`GET_LEDGER_DETAIL_VIEW_DATA`, Amazon Fulfillment). Sources: d0fc997e, 2f44617d (read 2026-11-13; store per §1(d)) [read in official docs]; blank `case-id` as "paid unasked" is a reading (P-ref-20) [inferred].
- **EC28.** No page read gives the share of a seller's former recoveries that remains claimable after Amazon's 2024–2025 changes. Amazon publishes none (EC6); the nearest vendor figures ("sellers recover 40% of what they're owed", Threecolts; "40% left behind" relayed in the finance pack) state no method or date base. For a store the share is read at run time from its own `GET_FBA_REIMBURSEMENTS_DATA`: amounts by `reason` and by blank against filled `case-id`, before and after the store's automation date and 2025-03-31. Sources: §4 table [opinion]; P-ref-31 [opinion]; the read is [inferred].

---

## Values that move

Each value differs by store, vendor or date. A position names the rule and where it is read; the value sits here.

| Value | Store | Value as read | Date read | Source |
|---|---|---|---|---|
| Customer-returns claim window | US | "60-120 days after the customer refund or replacement date" | 2026-11-13 | News 81c3235d (2024-07-24, eff. 2024-10-23) |
| Customer-returns claim window | US | "no sooner than 60 days after the customer refund … and within 18 months" | 2026-11-13 | Staff 0e07abc1 (2026-08-13; quote re-read; also finance P-ref-16) |
| Customer-returns claim window | Canada | "between 45-105 days" | 2026-11-13 | News 6605eede (2024-07-24) |
| Customer-returns claim window | UK | "between 45-105 days" | 2026-11-13 | News d0fc997e (2024-10-10, windows from 2025-01-09) |
| Warehouse-lost automation | US | from 2024-11-01 | 2026-11-13 | News 81c3235d |
| Warehouse-lost automation | UK | from 2025-01-15 (d0fc997e) against "requires manual claim submission (automatic reimbursement disabled since August 2022)", window "18 months of the event" (2f44617d, 2026-04-06) | 2026-11-13 | as named; home fc-lost-damaged FC4, FC5 |
| Sellable warehouse damage | UK | "Automatically reimbursed within 21 days" | 2026-11-13 | Staff 2f44617d |
| FBA fee window, itemised | US | "within 90 days of the disputed charge" | 2026-11-13 | Staff ce0bea71 (2026-04-17); home fee-overcharges FE9 (EU twin ff7c3c15) |
| FBA fee window, non-itemised | US | "an 18-month statute of limitations" | 2026-11-13 | Staff ce0bea71; home FE9 |
| Service look-back | all | GETIDA 18 months; Helium 10 MRS 18 months; Margin Pro "up to 9 months"; 船长BI 18 months back, ledger "前18个月~前45天" | 2026-11-13 | vendor pages (§2) |
| Service fee | all | §2 table (0% to 30%; 8% report-only, 2020) | 2026-11-13 | vendor pages; home finance P-tool-17 |
| Recovery-service contract periods | GETIDA | rate-change notice 45 days (clause 5.2); termination 60 days with a tail (clause 6.3) | 2026-08-16 (SellerHow's reading) | SellerHow |
| Per-unit cap; valuation-dispute window; sourcing-cost limits | by store | see value-and-reversals | — | value-and-reversals |

---

## Seat's own (no source; enters no skill)

- **The §5 illustration and its totals** (formerly EC20): the [seat] incidences (faulty share of returns 2–10%, removals 2–10% of inbound with 0.5–3% loss, mis-tiered units 0–10%, under-valuation gap $0–$4, the UK lost/damaged split), the central-case picks, linear scaling by volume, and the results: per 10,000 units a year roughly $60–$6,850 with a central $635 (about 0.2% of $300k revenue) in a US store; up to about $995 central in a UK store if warehouse-lost is manual; about $3,000 (1%) on the pre-2024 rules. Vendors' 1–3% is reached only when returns automation is as weak as sellerboard says and fee errors are present.
- **GL's size.** Not on record for this seat; the illustration is per 1,000 / 10,000 / 100,000 units, and GL's row is read from its own ledger at the first run.
- **The SPS cross-check** (formerly EC12, EC13): $10.5M a half-year over about 7,300 3P customers is about $1,440 a half-year, ~$2,900 a year per customer; if all of it were a 25% take, customers recovered at most about $11,500 a year on average (an upper bound, subscription revenue included; a mean pulled up by large accounts; inside §5's range only for about 20,000 units a year or more at high-end incidences). The $19.99-a-month fee aimed at the smallest accounts, with "as many as 4,000" expected to leave (the article's words), implies many paid under about $240 a year in commission, i.e. recovered under about $960 a year at 25%.
- **SellerHow's break-even** (formerly in EC25), kept as evidence of a practitioner's way of weighing the choice, not as a threshold: 3 hours a month at $30 an hour is about $1,080 a year, equal to a 25% fee on about $4,320 of recoveries (SellerHow, 2026-08-16) [opinion]. Other practitioners weigh the same choice by success rate (EC22) or by look-back (EC4); the three are ways of weighing side by side, none the pack's.
- **The answers to the survey's "about 30%"** (§7): as a size, about 32–42% by reference count unless valuation and reversals stay in the finance pack; as a share, no percentage supported, the seat's own ratio about 21% (US picks).
- **The pack's shape.** The "two skills" (units owed; value and fees) and "which kinds are too small or too automated to earn a skill" are the seat's packaging, chosen on money, and bind nothing. On this revision: warehouse-lost is not "mostly automated" for a store where Amazon's UK staff post holds (EC27), and C (customer returns) carries the widest uncertainty. The completeness review counts three skills by trigger (inventory held by Amazon; customer orders; charges) with valuation, reversals, windows and filing as shared references; this file's money arithmetic does not decide between two and three.

### Corrections to other packs

- **Finance pack P-tool-17** (vendor rates as read 2026-11-09; owner: finance pack). Additions from §2: Seller 365 has a second page reading "0% … under $1M … 10% above", conflicting with the "5% to 15%" P-tool-17 holds; GETIDA's contract is read as 25% against "starting at 20%" on its page (SellerHow; Titan; AmpliSell); Helium 10's two pages still conflict; add Refully 18%, TrueOps 10%, AMZRefund 25% (relayed by AmpliSell); Eva 10% rests on a search snippet only; add the report-only (AMZ Refund 8%, 2020) and zero-commission (船长BI) models and the contract points that move a seller's cost (§2(b)).
- **Finance pack P-ref-32** (owner: finance pack). Extended with: the purchase price ($210.2M, 10-Q) and the two close dates (2025-02-04 per the 10-Q; 2025-02-07 per the press release); the press release's estimated loss (~$20M) beside the call's $23.5M; ~7,300 customers and ~$10.5M of revenue a half-year; the 2026 $19.99 fee on small accounts.
- **Finance pack P-ref-13** (owner: finance pack; home of the table: fc-lost-damaged). "No page says which store each addresses" no longer holds on the post-object reading: 6605eede (the 2024-11-01 copy P-ref-13 cites) carries Canada's id, the US copy is 81c3235d, and d0fc997e (2025-01-15) carries the UK's id (§1(d), one control).
- **Finance pack P-ref-16 and P-tool-22** (owner: finance pack). P-tool-22's "Amazon's US notices give 45–105 days" is wrong on the post-object reading: the US post 81c3235d gives 60–120, and the 45–105 posts are Canada's (6605eede) and the UK's (d0fc997e). P-tool-22 also calls d8f9a56c (effective 2025-10-15) "US"; its post object carries Australia's id (A39IBJ37TRP1C6). P-ref-16 lists these posts without their stores. Evidence: §1(d), read 2026-11-13.
- **Stock pack** (cx-amazon-stock-playbook) skills/stock-inbound/references/shortages.md, "Proactive reimbursement (US from 2024-11-01; UK from 2025-01-15)" (owner: stock pack). This file's earlier note called the UK date "a reading, not Amazon's words"; that note is withdrawn: d0fc997e's post object carries the UK's id. What the stock line lacks is the UK staff post of 2026-04-06 (2f44617d, UK id) saying UK warehouse-lost reimbursement is manual, "disabled since August 2022" (fc-lost-damaged FC5); both are Amazon's words and the conflict is unresolved.
- **The earlier survey (the SP-API plugins report, §2.3 and §5b; owner: the office):**
  - "Effective March 10, 2025" is outdated; it became 2025-03-31 (P-ref-15).
  - "the services … sell this at 15–25%" is too narrow as read today: 0% (Seller 365 under $1M; 船长BI) to 30% (Refund Retriever).
  - "about 30%" was a size measure against the listing playbook, not a share recovered; as a size it is low unless valuation and reversals are pointed to the finance pack (§7).

---

## Open questions for a first run on a real account

1. What share of the seller's `GET_FBA_REIMBURSEMENTS_DATA` amount over the last 12 months has a blank `case-id`, and does blank mean Amazon paid unasked (P-ref-20)?
2. For refunds from 105–120 days ago, how many have a matching `CustomerReturn` reimbursement or a return in `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA`, and how many have neither? This settles GETIDA's 98.5% against sellerboard's view for this store.
3. The seller's measured inbound accuracy: closed shipments, `QuantityShipped` against `QuantityReceived`. How does it compare with 99.943%?
4. The ledger's lost/damaged adjustment rate per unit received, and its reimbursed share (finance pack P-ref-36 join).
5. Has the seller entered sourcing costs? Compare `amount-per-unit` on `Lost_Warehouse` and `Damaged_Warehouse` rows before and after 2025-03-31 against the seller's own cost.
6. Removal shipments in the window: units requested versus delivered (`GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA`).
7. Are any SKUs' Amazon-measured tiers in `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA` different from the seller's packaging? How many units were charged in the last 90 days?
8. Has the seller ever used a recovery service? Its commission invoices would be a direct measure of what was recovered, but only the seller holds them.
9. Which returns window does the seller's store's G200213130 show today: for a US store, the 2024 post's or the 2026 staff post's (EC5)?
10. GL's size: units received a year from `GET_LEDGER_SUMMARY_VIEW_DATA`, its stores, and revenue from `listTransactions`. Which row of §5's per-volume table it falls in, and how its own incidences compare with the seat's picks.
11. For a UK store: do `Lost_Warehouse` rows with blank `case-id` arrive after 2025-01-15, or are UK warehouse-lost units paid only on a case (EC27; fc-lost-damaged FC5)?
12. Over 2023–2026, what share of the store's reimbursement amount came on filed cases before and after its automation date and 2025-03-31 (EC28)?

---

## Pages read

| Title | Address | Publisher | Page date | Read on | Used for |
|---|---|---|---|---|---|
| Update on Reimbursement Automation and Eligibility Window to file reimbursement claims | https://sellercentral.amazon.com/seller-forums/discussions/t/81c3235d-4c44-47ba-96c5-883cecab3244 | Amazon (News_Amazon; post object: US) | 2024-07-24 | 2026-11-13 | EC5; §1(d) |
| Same title (Canada) | https://sellercentral.amazon.com/seller-forums/discussions/t/6605eede-df8e-4498-803f-cb612d95d7ce | Amazon (News_Amazon; post object: Canada) | 2024-07-24 | 2026-11-13 | EC5; §1(d); corrections |
| Same title (UK; 2025-01-15 start) | https://sellercentral.amazon.com/seller-forums/discussions/t/d0fc997e-de50-4100-9803-76b7993b66df | Amazon (News_Amazon; post object: UK) | 2024-10-10 | 2026-11-13 | EC5, EC27; §1(d); corrections |
| Update on eligibility window to file reimbursement claims (UK) | https://sellercentral.amazon.com/seller-forums/discussions/t/9a92846d-41f8-4ad7-b59a-f946efdcc2b4 | Amazon (News_Amazon; post object: UK) | 2025-01-15 | 2026-11-13 | §1(d) (store only) |
| Update to FBA inventory reimbursement claim windows | https://sellercentral.amazon.com/seller-forums/discussions/t/d8f9a56c-882f-437c-ad34-cccd11cfa465 | Amazon (News_Amazon; post object: Australia) | 2025-08-14 | 2026-11-13 | §1(d); corrections (store only) |
| [April FBA Series] Recover Your Lost FBA Inventory: UK Reimbursement Claims Explained | https://sellercentral.amazon.com/seller-forums/discussions/t/2f44617d-9e1c-413e-94b0-d427524ceb82 | Amazon staff (Jameson_Amazon; post object: UK) | 2026-04-06 | 2026-11-13 | EC27; §1(d) control; §5 A-UK |
| FBA Lost Your Inventory? Steps to File a Reimbursement Claim | https://sellercentral.amazon.com/seller-forums/discussions/t/0e07abc1-9026-4540-a005-153d9e78bf04 | Amazon staff (Indy_Amazon; post object: US) | 2026-08-13 | 2026-11-13 | EC5; §1(d) |
| A Seller's Guide to Disputing Incorrect Charges on Amazon | https://sellercentral.amazon.com/seller-forums/discussions/t/ce0bea71-dd81-4a08-808a-893ecc1572dd | Amazon staff (Roberto_Amazon; post object: US) | 2026-04-17 | 2026-11-13 | EC21 (itemised 90 days, non-itemised 18 months) |
| Amazon sellers are in revolt over a new policy they say hurts profits and gives up guarded business data (Allison Smith) | https://www.modernretail.co/?p=113702 | Modern Retail | 2024-12-20 | 2026-11-13 | EC8, EC9 |
| GETIDA pricing | https://www.getida.com/pricing | GETIDA | undated, © 2026 | 2026-11-13 | §2; EC4, EC22; corrections |
| GETIDA 中文: 亚马逊自动索赔，自动化获得FBA赔偿 | https://getida.cn/%E4%BA%9A%E9%A9%AC%E9%80%8A%E8%87%AA%E5%8A%A8%E7%B4%A2%E8%B5%94%EF%BC%8C%E8%87%AA%E5%8A%A8%E5%8C%96%E8%8E%B7%E5%BE%97fba%E8%B5%94%E5%81%BF/ | GETIDA (CN) | 2024-12-14 | 2026-11-13 | §2 (no rate stated in Chinese) |
| Seller Investigators home | https://www.sellerinvestigators.com/ | Carbon6 | undated | 2026-11-13 | §2; EC22 |
| Helium 10 Managed Refund Service | https://www.helium10.com/tools/operations/managed-refund-service/ | Helium 10 | undated | 2026-11-13 | §2; EC4; corrections |
| Amazon FBA Inventory Reimbursement Policy Update (blog) | https://www.helium10.com/blog/amazon-fba-inventory-reimbursement-policy-update/ | Helium 10 (Josh VanAkker) | 2024-07-24, mod. 2024-10-01 | 2026-11-13 | EC5 |
| Margin Pro FBA reimbursement service | https://www.threecolts.com/margin-pro/marketplace-seller-reimbursements/fba-reimbursement-service | Threecolts | © 2026 | 2026-11-13 | §2; EC4 |
| Seller 365 reimbursements | https://www.threecolts.com/seller-365/reimbursements | Threecolts | © 2026 | 2026-11-13 | §2; corrections |
| Seller 365 reimbursements, pro sellers | https://www.threecolts.com/seller-365-reimbursements-pro-sellers | Threecolts | undated | 2026-11-13 | corrections |
| 9 Best Amazon Reimbursement Services for FBA Brands | https://amplisell.com/blog-posts/best-amazon-reimbursement-services-for-fba-brands | AmpliSell (Josh Rawe) | 2026-11-09 | 2026-11-13 | §2; EC22; corrections |
| Amazon Reimbursement Service 2026 | https://titannetwork.com/amazon-reimbursement-service/ | Titan Network (Dan Ashburn) | 2025-07-01, reviewed 2026-04-25 | 2026-11-13 | §2, §4 |
| Amazon FBA Reimbursements 2026 (guide) | https://novadata.io/resources/blog/amazon-reimbursement-guide | Nova Data | 2025-10-15, upd. 2026-10-08 | 2026-11-13 | §4; EC22 |
| Amazon reimbursement policy: manufacturing cost (news) | https://novadata.io/resources/news/amazon-reimbursement-policy-manufacturing-cost | Nova Data | 2025-11-28, upd. 2025-12-01 | 2026-11-13 | §1(b); EC8 ("50-75%", "$18.50 to $6.20") |
| Amazon Reimbursement Recovery: How Much Are You Owed? | https://sellerview.ai/blog/amazon-reimbursement-recovery | Sellerview (Himanshu Gaba) | 2026-06-06 | 2026-11-13 | §1(b), §4 |
| Amazon FBA Reimbursements: What You're Owed… | https://blog.sellerboard.com/2026/07/14/amazon-fba-reimbursements-what-youre-owed-and-why-most-sellers-never-collect-it/ | sellerboard | 2026-07-14 | 2026-11-13 | EC15; §5 E |
| Amazon Reimbursement Services: What Can You Really Recover? | https://www.sellersprite.com/en/blog/amazon-reimbursement-services | SellerSprite (卖家精灵) Content Team | 2026-10-23 | 2026-11-13 | §2 context (illustrative 25%, "not an industry average") |
| Amazon FBA reimbursement audit | https://www.ecomengine.com/blog/amazon-fba-reimbursement-audit | eComEngine (Bob Norberg) | 2026-10-19 | 2026-11-13 | §4 |
| Amazon Reimbursement Calculator 2026 | https://ecomcalctools.com/amazon/amazon-reimbursement-calculator/ | ecomcalctools | 2026-06-17 | 2026-11-13 | EC17; §5 |
| Amazon's 2025 Reimbursement Policy Update | https://www.sellerlabs.com/blog/amazon-2025-fba-reimbursement-policy-change/ | Seller Labs (Nhan Dinh) | 2025-05-29 | 2026-11-13 | §1(b) |
| Amazon FBA Seller Refunds | https://www.junglescout.com/resources/articles/amazon-fba-seller-refunds/ | Jungle Scout (Brian Connolly) | 2023-11-29 | 2026-11-13 | §2 |
| 亚马逊 FBA 索赔要不要外包：25% 抽成的算账模型与五家服务商对比 | https://www.sellerhow.com/amazon-fba-reimbursement-service-zh/ | SellerHow | 2026-08-16 | 2026-11-13 | §2, EC25, Seat's own |
| 亚马逊FBA索赔助手 | https://m.captainbi.com/amz_claim.html | 船长BI | © 2016–2026 | 2026-11-13 | EC17, EC23, EC24 |
| 学会亚马逊FBA索赔，让你的店铺增加1%净利润 | https://www.cifnews.com/article/81125 | 雨果网 (from 亿卖大学) | 2020-10-28 | 2026-11-13 | EC7, EC23 |
| 被亚马逊FBA错误收费该怎么办？ | https://www.mabangerp.com/main_newsDetail.htm?id=4114 | 马帮ERP (from 雨果网) | 2020-06-29 | 2026-11-13 | §2 Chinese table; EC23 |
| 亚马逊FBA索赔时限缩短，卖家有解决方案了！ | https://m.mjzj.com/article/du2ckgmjnthc | 卖家之家 (招单猫) | 2024-08-07 | 2026-11-13 | §2 Chinese table |
| (FBA policy roundup, 2026-11-02) | https://www.amz123.com/t/tg6kPptK | AMZ123 (老虎站外推广) | 2026-11-02 | 2026-11-13 | EC8 |
| SPS Commerce announces agreement to sell 3P revenue recovery business | https://www.spscommerce.com/press/sps-commerce-announces-agreement-to-sell-3p-revenue-recovery-business/ | SPS Commerce | 2026-06-30 | 2026-11-13 | EC11 |
| SPS Commerce Form 10-Q (quarter to 2025-09-30) | https://www.sec.gov/Archives/edgar/data/1092699/000109269925000064/spsc-20250930.htm | SEC EDGAR / SPS Commerce | 2025 (Q3 FY2025) | 2026-11-13 | EC11 |
| SPS Commerce to buy Carbon6 Technologies for $210 mln | https://www.nasdaq.com/articles/sps-commerce-buy-carbon6-technologies-210-mln ; https://www.rttnews.com/3500354/sps-commerce-to-buy-carbon6-technologies-for-210-mln.aspx | Nasdaq / RTT News (via search) | 2025-01-02 | 2026-11-13 | EC11 |
| SPS Commerce Q4 2025 earnings call transcript | https://www.fool.com/earnings/call-transcripts/2026/02/12/sps-commerce-spsc-q4-2025-earnings-transcript/ | Motley Fool | 2026-02-12 | 2026-11-13 | EC11 |
| SPS Commerce Q1 earnings call highlights | https://finance.yahoo.com/markets/stocks/articles/sps-commerce-q1-earnings-call-024206977.html | MarketBeat via Yahoo Finance | 2026-04-30 | 2026-11-13 | §3; Seat's own |
| Earnings call transcript: SPS Commerce Q3 2026 | https://www.investing.com/news/transcripts/earnings-call-transcript-sps-commerce-beats-q3-2026-eps-forecast-shares-fall-after-hours-93CH-4985375 | Investing.com | 2026-10-29 | 2026-11-13 | EC11, EC14; Seat's own |
| 2023 FBA accuracy inbound, just sayin | https://sellersasksellers.com/t/2023-fba-accuracy-inbound-just-sayin/3268 | Sellers Ask Sellers (ASV_Vites et al.) | 2024-01-30 | 2026-11-13 | EC16; §5 B |
| Keeping Amazon honest on lost inbound | https://sellersasksellers.com/t/keeping-amazon-honest-on-lost-inbound/1896 | Sellers Ask Sellers (packetfire) | 2023-08-25 | 2026-11-13 | EC16 |
| Consumers expected to return nearly $850 billion in merchandise in 2025 | https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025 | NRF / Happy Returns (via search) | 2025-10-15 | 2026-11-13 | EC18; §5 C |
| National Retail Security Survey 2023 | https://nrf.com/research/national-retail-security-survey-2023 | NRF (via search) | 2023-09-26 | 2026-11-13 | EC18 |
| Inventory Record Inaccuracy: An Empirical Analysis (abstract records) | https://econpapers.repec.org/RePEc:inm:ormnsc:v:54:y:2008:i:4:p:627-641 | Management Science 54(4) (DeHoratius & Raman) | 2008 | 2026-11-13 (abstract) | EC18 |
| Finance pack research and skills (P-ref-13/14/15/16/17/18/19/20/29/31/32/36/39/40; P-tool-17/18/22) | the finance pack (cx-amazon-finance-playbook) research/areas/refunds-reimbursements-adjustments.md; research/beyond/sellers-tools-and-research.md; skills/refunds-and-reimbursements/ | ComChatX | 2026-11-09/10 | 2026-11-13 | cited throughout |
| Stock pack shortages reference | the stock pack (cx-amazon-stock-playbook) skills/stock-inbound/references/shortages.md | ComChatX | 2026-11 | 2026-11-13 | correction note |
| The SP-API plugins survey report (§2.3, §5) | the office's completed inbox, sp-api-plugins report of 2026-11-09 | ComChatX CEO office | 2026-11-09 | 2026-11-13 | "about 30%"; correction note |

**Unread or only relayed:**
- Amazon's FBA inventory reimbursement policy (G200213130): a JavaScript shell. Its text is relayed in the finance pack.
- GL7U4JFSDXUTQAJ: not read; the fee windows now rest on the US staff post ce0bea71 (read) and fee-overcharges FE9.
- Threecolts DimeTydSellers "Fee Protector": redirects to threecolts.support. A search snippet relays "250,000 SKUs averaged 3 dimensional changes in the last 6 months"; not used as a position.
- Refunds Manager's current page: the finance pack says it now pitches 1P and Walmart.
- Refully, TrueOps and AMZRefund own pages: rates relayed by AmpliSell. Eva: rate from a search snippet only; AmpliSell's page does not name it.
- SellerLegend, Prestozon, Turbo/Seller Hub, AMZ Reimbursement, Payability recovery: no page with a reimbursement fee found.
- 知乎 563632006: 403.
- The CSDN piece on 速易特 (SellingExpress) 索赔助手: socket closed.
- Jungle Scout State of the Amazon Seller 2025: no reimbursement figure in the excerpt.
- The ecommercebytes article on found inventory (2025-06-29): the site has closed.
- The DeHoratius & Raman full text.

---

## Verification (2026-11-13)

An adversarial re-read of this file's load-bearing statements against their cited sources, the same day. Public pages only; no SP-API call, no login, no seller data. SP-API operations were checked in a local clone of amzn/selling-partner-api-models at commit db2936aa; GitHub main's newer commit (b13d1d10, 2026-11-11, "Update Analytics Economics Schema") touches no operation named here.

**Confirmed as written:**
- News 81c3235d: title; "Starting November 1, 2024"; "October 23"; FC lost/damaged 60 days; customer returns "60-120 days"; removal lost in transit "15-75 days"; other removals 60 days after delivery back. The page shows "2 years ago".
- Helium 10 blog (Josh VanAkker, 2024-07-24, modified 2024-10-01): 60–120 days; "over 90% of reimbursement claims are currently made within 60 days"; effective 2024-10-23.
- Modern Retail 2024-12-20: Mira Dix's three quotes; the 42% ($108,000), 70% and "cut in half" forecasts; Rawe's half a million to $250,000; TrueOps "2,000 Amazon sellers".
- GETIDA pricing: "starting at 20%", the first $400, the 18-month audit, the claim list, "more than 90%" and "63%".
- Seller Investigators: "25% commission only after you've been paid"; "within Amazon's Terms of Service"; the $2,000,000 GMV → $20,000 calculator example; "99% of our new customers"; the customer-returns categories.
- Helium 10 MRS: Diamond 15%, Platinum 18%; "last 18 months"; Emerald Program.
- Threecolts Margin Pro: 15–25%; "up to 9 months"; "$500M+"; "40% of what they're owed"; 1–3%; "auto-credits only the most obvious". Seller 365: "5% to 15%"; the pro-sellers page's "0% … under $1M" and "10% above $1M"; the $115,500 / $3.3M / 3.5% estimator.
- sellerboard 2026-07-14: 1–3%; $10,000–$30,000 on $1M; "almost entirely seller-initiated" (about refunded items never returned); does not file.
- Nova Data: "50-75%" and "$18.50 to $6.20" (news page, 2025-11-28); the guide's $1,500–$3,000, $2,500, $4,200 in 90 days, 90%+ / under 40%, nine categories.
- Titan Network: $1,000–$3,000 per $100K; $1M → $10,000–$30,000, $7,500–$22,500 after 25%; the vendor fees listed.
- AmpliSell 2026-11-09: GETIDA 25%, Refully 18%, TrueOps 10%, AMZRefund 25%, sellerboard $19–$79/month, Seller Investigators "Over $100 million" and "95.9%".
- SellerHow 2026-08-16: GETIDA clause 1.10 (25%), 5.2 (45 days), 6.3 (60 days and the tail); Seller Investigators reverses its fee on a reversal; the $1,080 / $4,320 break-even; "25% 是这个品类的公价".
- 船长BI: "0抽佣", other services at 25%, the eight cases, current version FC lost/damaged only, 18 months back, ledger 18 months to 45 days, 30万 per 1000万.
- AMZ123 2026-11-02: "现在赔的是12美元"; "50%到75%".
- SPS press release 2026-06-30: $9.5M cash; ~$20M estimated loss in Q2 2026; Carbon6 closed 2025-02-07; buyer not named. 10-Q: "$210.2 million, net of cash acquired". Q4 2025 call: Kimberly Nelson's take-rate and policy quote, "declined by 350"; Chad Collins's churn quote. Q1 2026 article: $19.99, "very smallest", "very, very low revenue", up to 4,000 (the article's words). Q3 2026 call: Joe Vruwink's 7,300, $10.5M and policy quotes; Collins's short-shipment and redispute quotes.
- sellersasksellers: ASV_Vites 123,228 / 70 / 99.943% and its method.
- SP-API: Fulfillment Inbound v0 `getShipmentItems` and `getShipmentItemsByShipmentId` exist and carry `QuantityShipped` / `QuantityReceived`; Finances v2024-06-19 `listTransactions` and Product Fees v0 `getMyFeesEstimates` exist; no operation in the models reads or writes a sourcing cost. The `GET_FBA_REIMBURSEMENTS_DATA` columns and the roles are as the finance pack records them (P-ref-19, P-tool-26; product-profit).
- Finance pack P-ref-13, -14, -15, -16, -19, -20, -29, -31, -32, -40 say what this file cites them for.

**Corrected:**
- Summary and §3: the sale's press release gives the 1P focus as its reason and does not mention Amazon's policy changes; those are named on the calls. "Sold" is the press release's "has completed the sale"; the headline says "Agreement to Sell".
- Carbon6 close: the 10-Q says "effective February 4, 2025"; the press release says closed February 7, 2025. Both now stated. The "about 40% in stock" split was replaced by the 10-Q's $142.5M cash and $67.7M stock.
- Q1 2026 quotes: "remains on a negative trajectory due to policy changes" was not the wording; replaced by the CFO's "continues on a negative trajectory" and the CEO's "headwinds from Amazon's policy changes". The CFO is Joe Del Preto in that article.
- EC4, EC5, §3(a), §5, §2(c): P-ref-16 holds a staff post of 2026-08-13 giving 18 months for customer returns and removals and 9 months for missing-from-inbound. "Look-backs are longer than Amazon's current windows" and "the windows were 18 months, not 60 days" were not true across Amazon's pages; rewritten to the rule (bounded by the window for the kind, read at run time) with the values as dated evidence.
- Modern Retail's 1–3% is a quote from Joel MacPherson of TrueOps, a recovery service, not background.
- Seller 365 "30+ claim categories": not on the reimbursements page; replaced by the page's own list. Its estimator wording corrected to "Based on an estimated 3.5% of annual FBA revenue".
- Eva 10%: AmpliSell's page does not name Eva; marked as a search snippet, unsupported by a page read.
- 亿数通 "0 commission (2020)": the cifnews article states no fee; removed from EC23 and the table.
- ecomcalctools: only the FC 0.3–1.0% is labelled a documented range; lost inbound and adjustments come from its worked example.
- packetfire: "over 1300 units" since May 2023 (2023-08-25, lost inbound) and "the 1500 units Amazon lost on FC transfer" (2024-01-30), not one range on FC transfers.
- GETIDA's proof figure is "approximately 40%", not "roughly 40%"; 船长BI's error-rate and recovery quotes put in their exact words.
- `CustomerReturn` is a `reason` value seen in sellers' reports; Amazon publishes no list (P-ref-19, P-ref-35).
- Role for `getMyFeesEstimates` is Pricing or Product Listing; for `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA`, Amazon Fulfillment or Pricing.
- Nova Data's 50–75% and $18.50→$6.20 are on its news page, now listed in Pages read; the Modern Retail row now carries the article's title.

**Moving values moved out of positions:** EC3 (GETIDA's 45- and 60-day contract periods), EC4 (look-back and window lengths), EC21 (the 90-day fee window, with its page title and address), EC24 (the 18-month span), and the summary's "90-day window" now state the rule and where it is read, with the value as dated evidence.

**Forbidden positions:** no threshold of ours, fixed sequence, when-to-ask or ceiling was found among the positions; §6 already states choices and what each changes. The "too small to earn a skill" list, the "two skills" shape and "A and C enter as reads" are relabelled the seat's own packaging for the office, not anything a seller is told.

**Not re-read today:** the Q2 2026 call ($23.5M), the RTT/Nasdaq announcement (~$210M, "$40.0 million in revenue"), Seller Labs, Sellerview, Jungle Scout, ecomEngine, SellerSprite, the NRF and DeHoratius & Raman items, 马帮 and 招单猫, GL7U4JFSDXUTQAJ (relayed only). The SP-API report-type page redirected to a different host and was not followed; report columns rest on the finance pack's reading.

**Remaining doubts:**
- Which customer-returns window governs a store today (45–105, 60–120, or 60 days to 18 months) is unresolved; the model's pre/post comparison in §5 assumes the shorter 2024–2025 windows.
- SPS's two close dates (4 and 7 February 2025) are both the company's own.
- The §5 model's incidences are partly seat's own; its totals are an illustration, not a measurement.
- "Blank `case-id` means Amazon paid unasked" stays a seat reading until a live account confirms it (P-ref-20).

---

## Revision (2026-11-13)

After the completeness review of the same day. Routes used: plain GET of Seller Forums threads on the .com host (post object read with curl), web search in English and Chinese; no POST, no help-hub content call, no SP-API host, no sign-in, no seller data.

- **Positions withdrawn (ids kept):** EC1, EC2, EC3 (vendor fee models and contract terms: the finance pack's tools reference P-tool-17 is their home; the new material stays in §2 as evidence and is offered under *Corrections to other packs*); EC12, EC13, EC20 (their substance is the seat's own inputs: moved under *Seat's own*; EC19's formula stays).
- **Positions changed:** EC4 (values moved to *Values that move*; windows pointed to the area files and fc-lost-damaged's post-to-store table); EC5 (restated on the post-object store reading: the 60–120 post is the US's, the 45–105 posts Canada's and the UK's; the US conflict that remains is with the 2026-08-13 staff post); EC10 (customer-return basis pointed to value-and-reversals VR27 and customer-returns RT42, which disagree); EC21 (points to fee-overcharges FE9; two windows, itemised and non-itemised, instead of one "however long the error ran"; re-read the US staff post ce0bea71); EC24 (look-back value moved to the table); EC25 (SellerHow's break-even moved under *Seat's own*; the choices stay side by side).
- **Positions added:** EC27 (the share paid unasked is a per-store fact; UK warehouse-lost may be wholly left for a claim); EC28 (no page gives the share of former recoveries left after the 2024–2025 changes; read per store).
- **Sections:** §1(a) now points to P-ref-13/-14/-15, fc-lost-damaged and value-and-reversals instead of restating them; new §1(d) re-checks the post-object store reading against a post whose title names its store (2f44617d, UK id) and records eight posts' stores; §2 and §3(a) point to their homes; §5 is parameterised per 1,000 / 10,000 / 100,000 units, states that GL's size is not on record for this seat, adds a UK row (A-UK) and a non-itemised fee row (E″), and moves its totals under *Seat's own*; §6 drops the break-even; new §7 states and answers both readings of the survey's "about 30%"; new *Values that move*; *Seat's own* expanded; *Corrections to other packs* renamed, with owners named, the stock-pack note reversed (d0fc997e carries the UK's id) and new corrections to finance P-ref-13, P-ref-16 and P-tool-22.
- **Open questions added:** 10 (GL's size), 11 (UK warehouse-lost automation in the store's own report), 12 (filed share before and after the changes); 9 restated.
- **Pages read added:** 6605eede, d0fc997e, 9a92846d, d8f9a56c, 2f44617d, 0e07abc1, ce0bea71.
- **Not done here:** the completeness review's other items (B, C, G, H, the route ruling in A2 and K) concern other files or the office.
