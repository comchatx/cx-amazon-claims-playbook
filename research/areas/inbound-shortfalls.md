# Inbound: units lost, damaged or short on the way into Amazon

Date read for every page: 2026-11-13 (the research seat for brief 548, area "inbound").

Units a seller sends to Amazon can go missing in three places: with the seller's own carrier or forwarder before Amazon signs for them, with a carrier operated by or for Amazon (Amazon Global Logistics included, under its own freight terms), or inside the receiving dock between delivery and the final count. Amazon pays for the last two under the *Shipment to Amazon* part of its FBA inventory reimbursement policy; the first is a matter between the seller and the carrier it engaged (section M). Amazon's proactive-reimbursement announcements cover warehouse lost and damaged and customer returns and leave out inbound loss and removals; which store each announcement was issued for, and the 2026 UK staff post that says UK warehouse-lost claims are still manual, are fc-lost-damaged's (see fc-lost-damaged, post-to-store table in § 2, and FC5). Amazon pays inbound loss only after the shipment is closed and only when the seller asks through the shipment's Contents ("Reconcile") tab, with proof of ownership and proof of delivery; submitting the request creates a Selling Partner Support case. The filing window is a per-store rule read from the store's *Shipment to Amazon claims* help page and its forum News (values read, with dates, are in *Values that move*). For the EU, UK and JP stores no Amazon statement of the inbound window's length was read; Amazon's UK and EU redlines show that the 2025 window changes left the shipment-to-Amazon window out (IN35, IN36). The "MCF inventory reimbursement policy" that the AWD terms name is, by the terms' own link, the Supply Chain Portal reimbursements page (IN34). No SP-API operation returns the delivery date the window runs from or the shipment's eligibility (IN10, IN29); what the case API can and cannot do is sp-api-claims-surface's (SU8–SU12). This file builds on the stock pack's I8, I14, I21–I23 and I26 and its reference `stock-inbound/references/shortages.md`, and corrects facts held by the stock and finance packs (*Corrections to other packs*).

## How to read this file

Tags:
- **[read in official docs]**: Amazon's own words, on a page opened in this session or in the local clone of `amzn/selling-partner-api-models` (commit `db2936aa`, 2026-10-29). Amazon's own words include Seller Central help, Seller Forums posts by `News_Amazon` or `*_Amazon` staff, sell.amazon.com, supplychain.amazon.com, gs.amazon.cn, developer-docs.amazon and Amazon's policy PDFs on m.media-amazon.com.
- **[read in official docs, via X]**: Amazon's text as a third party quotes it.
- **[command-verified]**: something run locally: a grep or parse of a model file, a PDF text extraction, or a page's embedded data.
- **[opinion]**: a named practitioner, a tool vendor or a seller.
- **[inferred]**: this seat's reading of sources that are cited.
- **seat's own**: a point with no source. It enters no skill.

How pages were reached:
- **Seller Central help pages** (`/help/hub/reference/external/<ID>`, `/gp/help/external/<ID>`, in the `.com` and `.co.uk` forms) returned a script shell of about 171 KB with no article text to a plain GET, through curl and through WebFetch. They stay unread here: the help hub's content call is a route the office closed on 2026-11-10, and this file does not use it. Their content comes from three routes, each marked where used: Amazon's own Chinese articles on gs.amazon.cn, which restate them; Amazon staff forum posts; and Amazon's policy PDFs on m.media-amazon.com.
- **Amazon's policy PDFs** are redlines: struck and inserted text share one text layer. In the revision of 2026-11-13 the pages that carry valuation sentences were rendered to images and read, so struck text is told apart from live text (value-and-reversals VR28 holds the pitfall).
- **Seller Forums threads** were read with a plain GET. The store each thread was issued for is the thread-level `"marketplaceId"` that sits beside `"pinnedToCategory"` in the page's embedded JSON. That is a different field from the `selectedMarketplaceId` and `ue_mid` values, which follow the host you fetch from [command-verified]. A WebFetch summary that names the store from the host is wrong for threads posted to other stores. This file read the thread-level field. The post-to-store table for the whole pack is fc-lost-damaged's (§ 2); this file's own readings stay below as evidence. A control check on 2026-11-13, all fetched from the `.com` host: Jameson_Amazon's *UK Reimbursement Claims Explained* (`2f44617d-…`, whose text names the UK) reads `A1F83G8C2ARO7P` (UK); Jameson_Amazon's prep reply (`5c63f045-…`, whose text names "the US store") reads `ATVPDKIKX0DER` (US); a US seller's thread (`3354bdd4-…`) fetched from the `.co.jp` host reads `ATVPDKIKX0DER`. The field follows the thread, not the host [command-verified].
- **The web search budget for the session ran out** during the revision of 2026-11-13 as well. Pages still to be searched for are listed under *Open questions* and *Unread pages*.

Already held elsewhere, and not repeated here:
- **The stock pack (cx-amazon-stock-playbook)** holds these, and they are cited by ID:
  - research/README.md I8 (`CLOSED` is not proof of receipt; research only after `CLOSED`)
  - I14 (the Inbound Performance report)
  - I21 (the US nine-month line; the UAE 15–60 post; proactive reimbursement leaves inbound out)
  - I22 (sourcing-cost valuation; `GET_FBA_REIMBURSEMENTS_DATA`)
  - I23 (labels can defeat eligibility)
  - I26 (wait instructions during backlogs)
  - I3 (received quantity only in v0 and the ledger)
  - I9 (auto-closure 45/75 days and the 2026 peak relaxation)
  - I17 (the 5% / six-unit edit tolerance)
  - I19 (US prep and label service ended 2026-01-01)
  - I5, I7 and W38 (AWD not readable on the five roles)
- **The finance pack (cx-amazon-finance-playbook), research/areas/refunds-reimbursements-adjustments.md** holds:
  - P-ref-12 (what the policy covers, including the 2026 prep exclusion)
  - P-ref-13 (automation and the IDR portal leave out missing-from-inbound)
  - P-ref-14 and P-ref-15 (sourcing cost)
  - P-ref-16 (windows page by page)
  - P-ref-33 and P-ref-35 (`MISSING_FROM_INBOUND`, `Lost_Inbound`, `Damaged_Inbound`)
  - P-ref-37 (gs.amazon.cn: nine months, US)
  - P-ref-40 (the US policy PDF)
- **The finance pack, research/areas/fulfilment-charges.md** holds the billing side of Amazon Global Logistics: who bills and when, the estimate against the charge, the overcharge notice window, and that no SP-API operation reads AGL bookings (P-ful-29 to P-ful-31, P-ful-37). Section K adds only the loss and claim side of the same terms.
- **The stock pack's reference `skills/stock-inbound/references/shortages.md`** says "The claim itself is outside this pack"; inbound claims are this file's.
- **The door (cx-amazon-sp-api)** says how a call and a report are made. That is not repeated here.
- **Other files of this pack** own the following. Pointers only:
  - *fc-lost-damaged*: units lost after receipt; the post-to-store table for News posts (§ 2); the automation dates and the UK contradiction (FC3–FC5).
  - *value-and-reversals*: valuation and reversal of what an inbound claim pays; the per-unit cap (VR29); the valuation-dispute window (VR20); the struck "estimated proceeds" text (VR1, VR28); MYSC proof and limits (VR11, VR13, VR14).
  - *sp-api-claims-surface*: roles and reports in general; the Support API's reads and its restricted role (SU8–SU11); "no operation files a claim" (SU12); the removed reconciliation reports (SU42).
  - *filing-and-conduct*: case routes, limits and conduct: one claim per shipment (FL7), shipment-to-Amazon evidence as a filing list (FL24), the Supply Chain page as a source pitfall (FL27), staff review times (FL30), the "premature requests" sentence (FL11).
  - *recovery-economics*: what inbound claims are worth a year.
  - *removals-disposals*: the removal-lost windows that appear in the same News posts.

---

## A. Whose loss it is: the policy's scope at the door

**(a) Amazon's rule.**
- **The policy's opening sentence.** *FBA inventory reimbursement policy*, US redlined PDF (Word metadata created 2024-12-18; https://m.media-amazon.com/images/G/01/rainier/help./PC__Kiwi_Comms_redlined_policy_US_clean.pdf; read 2026-11-13):

  > "If an item you send to us as part of the Fulfillment by Amazon (FBA) service is lost or damaged at a facility or by a carrier operated by Amazon or on behalf of Amazon, we replace that item with a new item of the same FNSKU or reimburse you for it."

  Among the eligibility conditions: "You have sent us the exact items and quantities stated in your shipping plan" and "The shipment for the item is not in canceled or deleted status". The German store's version (*FBA lost and damaged inventory reimbursement policy*, DE redlined PDF created 2025-02-24, https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_DE.pdf, read 2026-11-13) has the same opening sentence and conditions. It omits the cancelled/deleted condition. [read in official docs; text extracted with pypdf, command-verified]
- **Damage found on arrival.** An Amazon staff reply (NR_Amazon, US forum, thread `0d6e8a48-4095-4e90-bf84-7bb3a88a9fbc`, thread posted 2025-03-19, reply dated 2025-04-11, read 2026-11-13):

  > "Inventory labeled as "distributor damaged" or "damaged by inbound carrier" indicates that the shipment was received by Amazon already damaged, and are classified as unfulfillable, meaning that they will need to be removed."

  The reply sends the seller to their carrier with proof of the damage once the units come back. [read in official docs]
- **Delivered but never received.** An Amazon Seller Support email of 2023-08-07, quoted by the seller in US thread `0fc75622-4221-4548-9254-977d5f034aeb`:

  > "The partnered carrier proof of delivery is a confirmation that the shipment described by the carrier has been delivered to Amazon. The contents of the shipment were not inspected at the time of drop off by the partnered carrier."

  The thread's staff reply (TaylorR_Amazon, 2023-08-10) took the case up, and the seller then reported a refund in progress. [read in official docs, via the seller's quotation; outcome: opinion, the seller]

**(b) What practitioners add.**
- 深圳美辰物流 (a freight forwarder), AMZ123, 2023-10-27, https://www.amz123.com/t/0JE2nztt: "查询物流单号，判断是物流问题还是亚马逊仓库问题；物流问题：与货代协商赔偿；亚马逊仓库问题：开Case调查" (look up the tracking number to tell a carrier problem from a warehouse problem; a carrier problem is negotiated with the forwarder; a warehouse problem goes to a case). [opinion]
- GETIDA lists "Damaged Inbound" for units "damaged by an Amazon Partnered Carrier on the way to Amazon's Fulfillment Center". GETIDA's claim types were seen in the survey's money notes and in search results only. [opinion]

**(c) Into a skill:** the scope sentence as Amazon wrote it: Amazon pays for loss or damage at its facilities or by a carrier it operates or uses. Arrivals classed as distributor-damaged or damaged by the inbound carrier are unfulfillable and are routed to the seller's carrier.

**Read at run time:** whether the shipment travelled on an Amazon-partnered option is on its transportation option, `shippingSolution` `AMAZON_PARTNERED_CARRIER` or `USE_YOUR_OWN_CARRIER` (Fulfillment Inbound v2024-03-20 `listTransportationOptions`, role Amazon Fulfillment). The disposition of damaged arrivals is in the Inventory Ledger detail (`GET_LEDGER_DETAIL_VIEW_DATA`, Amazon Fulfillment).

---

## B. The window, store by store

**(a) Amazon's statements, each with its store and date.** The store is the thread-level `marketplaceId` for forum posts [command-verified].

| Store | Statement | Source and date | Tag |
|---|---|---|---|
| US | "Shipment to Amazon (MFI) claims: File after your shipment is closed/finalized (allow time for reconciliation) and within 9 months" | Indy_Amazon, *🆘FBA Lost Your Inventory? Steps to File a Reimbursement Claim*, thread `0e07abc1-9026-4540-a005-153d9e78bf04`, posted 2026-08-13, thread store `ATVPDKIKX0DER` | read in official docs |
| US | "您必须在货件送达 亚马逊 运营中心后的9个月内提交索赔。逾期提交的索赔将无法获得赔偿" ("*美国适用"); and "必须在货件送达亚马逊运营中心的确切日期后最迟九个月内（美国站）提交索赔" (the claim must be filed no later than nine months after the exact date the shipment reached the fulfilment centre, US) | Amazon 全球开店, gs.amazon.cn article-250305-3 ("发布时间为2025年3月") and article-250807-3 ("发布时间为2025年8月") | read in official docs |
| US | "the window for filing a claim for shipments to Amazon is nine months after the verified delivery date", quoting help page `GEYPWTSQRTXXXMVB` | seller post, thread `2b32f5d5-28e2-4445-8318-17793237a735`, 2024-09-26. Dominic_Amazon's reply did not address the window | read in official docs, via a seller |
| MCF / Supply Chain Portal (not FBA) | "Once a shipment is shown as eligible for investigation in the Status column on the Contents tab… You must submit your claim no later than nine months after the verified date of a shipment delivery to an Amazon fulfillment center or to a third-party facility operated on Amazon's behalf" | *Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS)*, https://supplychain.amazon.com/support/reimbursements, no page date (footer © 2026); eligibility requires "Your Multichannel Fulfillment (MCF) account is in Active state". The AWD terms link their words "MCF inventory reimbursement policy" to this page (IN34) | read in official docs; link command-verified |
| AWD | Shipment claims follow "the specified claim window for lost or damaged shipments in the MCF inventory reimbursement policy, with the claim window starting on the verified date that the shipment was delivered to an AWD site or to a third-party facility operated on Amazon's behalf" | *Amazon Warehousing and Distribution* service terms, "Dated: January 14, 2026", https://supplychain.amazon.com/legal/service-terms/warehouse-and-distribution | read in official docs |
| UK | "Note: Starting on January 9, 2025, the FBA inventory reimbursement policy for the eligibility claim windows, except for shipment to Amazon claims, will be updated from 18 months to 60 days." The length of the shipment-to-Amazon window is not on the page | UK policy redline `_PC__Kiwi_Comms_redlined_policy_UK_clean_version.pdf` (created 2024-12-11), https://m.media-amazon.com/images/G/01/rainier/help./_PC__Kiwi_Comms_redlined_policy_UK_clean_version.pdf | read in official docs |
| EU | Amazon's EU redline set of 2024-08-20 redlines three sub-pages (FBA customer return claims, Fulfilment centre operations, Removals claims) and carries no *Shipment to Amazon* sub-page | `EU_Policy_Redline.pdf` (created 2024-08-20), https://m.media-amazon.com/images/G/02/rainier/help/EU_Policy_Redline.pdf | read in official docs; page list command-verified |
| JP | The JP policy ("※This Help page is as of 02/19", PDF created 2025-02-19) names "Shipment to Amazon" among claim kinds and states no window for it | https://m.media-amazon.com/images/G/09/rainier/help/redline_FBA_reimbursement_policy__EN_version.pdf | read in official docs |
| UK | Spencer_Amazon, *FBA Inventory Protection: Amazon's Lost & Damaged Policies*: "Time limit: File within 60 days", for lost or damaged inventory in general, naming no claim kind and no start | thread `e236599d-210d-455f-a601-5dbee8fc95c7`, posted 2025-06-06, store `A1F83G8C2ARO7P` | read in official docs; store command-verified; whether it covers shipments to Amazon is not stated |
| UAE, Saudi Arabia, Egypt | "Starting September 5, 2024 … Units missing from shipments sent to Amazon fulfillment centers: No sooner than 15 calendar days from the shipment delivery date but no later than 60 calendar days." | News_Amazon, *Update on reimbursement claim window eligibility on FBA*, posted 2024-08-06, three threads: `96a05f4a-537a-49d2-a918-703c47716bc0` (store `A2VIGQ35RCS4UG`, UAE), `c6da88ce-b14f-4ae1-95a5-1c6482b5c565` (`A17E79C6D8DWNP`, Saudi Arabia), `e62a8ace-3875-433c-8ef1-bb27a29b17c4` (`ARBP9OOSHTCHU`, Egypt; this one also lists carrier-damaged returns and customer returns) | read in official docs; store command-verified |
| US, Canada, UK, Sweden, Australia | The News posts on claim windows (US `81c3235d-…` and Canada `6605eede-…`, both 2024-07-24; UK `d0fc997e-…` 2024-10-10; UK `9a92846d-…` and Sweden `1101821c-…`, both 2025-01-15; Australia `d8f9a56c-…` 2025-08-14) name no window for shipments to Amazon | finance pack P-ref-16; thread stores command-verified here (`1101821c` reads `A2NODRKZP88ZB9`, Sweden); the pack's post-to-store table is fc-lost-damaged's | read in official docs |
| UK | A seller writes that Seller Central told him "not eligable for reimbursement as over 6 months since arrived at the fba warehouse" | thread `c3831651-3056-4bf9-87e7-e51f40bd43d0`, store `A1F83G8C2ARO7P`, 2025-01-08 | opinion, the seller relaying a Seller Central message |

**The start date is not in the API.** No Fulfillment Inbound operation returns a delivery, check-in, receiving or closed date [command-verified: every `date-time` field of `fulfillmentInbound_2024-03-20.json` was listed]:
- Its dates are plan `createdAt` and `lastUpdatedAt`, option expirations, delivery-window and appointment start and end times, the shipment's `dates.readyToShipWindow` (when the seller expects to ship), `editableUntil` and `voidableUntil`.
- v0 `InboundShipmentInfo` carries no date except `ConfirmedNeedByDate` (pre-orders); v0 `InboundShipmentItem` carries `ReleaseDate` (a pre-order item's on-sale date). `LastUpdatedAfter`/`LastUpdatedBefore` are query filters, not returned fields.

The AWD `InboundShipment` has `createdAt`, `updatedAt` and `shipBy` [command-verified].

**(b) What practitioners add.**
- **Helium 10**, Managed Refund Service FAQ (https://kb.helium10.com/hc/en-us/articles/30482681645339, 403 to a fetch; search snippet only): inbound lookback "9 months (US), 6 months (EU)", inbound cases submitted "30 days after Amazon receives the goods". [opinion, snippet]
- **SELLERLOGIC** (snippet of post 20856): an inbound request must be filed "within six months of the date Amazon received the shipment". Its other pages state 18 months and 60 days. [opinion, snippet]
- **百运网** (https://m.by56.com/news/59431.html, 2026-05-27): "Receiving 状态下差异索赔需在货件创建后 90 天内发起" (discrepancy claims in Receiving status within 90 days of shipment creation). No Amazon page read says this. It matches the auto-closure clock of 2020–2023 (90 days), not a claim window. [opinion]
- **Refunzo** (Jimi Patel, 2026-01-18, https://www.refunzo.com/blog/amazon-lost-inbound-claims-guide-2026/): "usually have a 60 to 90 day window to file lost inbound claims". [opinion; at odds with every US Amazon statement read]
- **Marketplace Valet** (Justin W. Boggs, updated 2026-10-24): "nine months after verified delivery", with a warning to confirm in Seller Central. [opinion]
- **A search summary of gs.amazon.cn** (2026-11-13) said an Amazon Chinese article on the inbound process gives "欧洲站为六个月" (six months for Europe). No gs.amazon.cn page fetched in this session carries that sentence: article-250305-3 and article-250807-3 say nine months and mark it US only, and the article the summary appeared to name (news-brand-230829) now redirects to globalselling.amazon.com and serves no article body. [unverified lead; not evidence]
- **AMZ123** (1KqAXyXG, 2025-05-19): "需注意亚马逊规定的180天索赔有效期" (Amazon's 180-day claim period). No Amazon page read states 180 days for inbound. [opinion; unsupported]

**(c) Into a skill:**
- The window is a per-store rule, read from the store's *Shipment to Amazon claims* help page and its forum News; its length is not fixed in a skill. The table above is the evidence: the US statements read (2024-09 to 2026-08) count it from delivery to the fulfilment centre, with the request filed only after the shipment is closed; three Middle East stores were given a minimum and a maximum count of calendar days from delivery, effective 2024-09-05.
- For the UK, Amazon's 2024-12-11 redline excludes shipment-to-Amazon claims from the 2025-01-09 change to 60 days, and Amazon's EU redline set of 2024-08-20 carries no shipment-to-Amazon page; the length for the UK, the EU stores and JP was not read on any Amazon page.
- The API carries no delivery date to count from.

**Read at run time:**
- **The rule:** the store's help page *FBA inventory reimbursement policy: Shipment to Amazon claims*, `https://sellercentral.amazon.<store>/help/hub/reference/external/GEYPWTSQRTXXXMVB` (a script shell to a plain fetch), and the latest News post on the store's forum. No operation states a window.
- **Proxies for the shipment's delivery date:**
  - the earliest `Receipts` event for the shipment's Reference ID in `GET_LEDGER_DETAIL_VIEW_DATA` (Amazon Fulfillment);
  - the selected delivery window or carrier appointment (`getShipment`, `listTransportationOptions`, Amazon Fulfillment);
  - the carrier's own tracking.

  None of these is Amazon's "verified delivery date" [inferred].

---

## C. When a shipment can be researched, and what the Contents tab says

**(a) Amazon's rule.**
- **Eligibility.** sell.amazon.com, *How to track FBA shipments* (https://sell.amazon.com/blog/fba-shipment-tracking; shown "Jan 7, 2025"; the stock pack read a modified date of 2025-10-03): "Once the shipment status is "Closed," eligible products will have an Action required dropdown menu". The options are to "confirm you sent a different number of units compared to the number of units listed for the shipment" or "request that we research the difference". After submission "a case number will display on the Contents tab of the Shipment summary", and a reply to a request is due "within five business days". Page JSON-LD: `datePublished` 2025-01-07, `dateModified` 2025-10-03. [read in official docs; held in substance by stock I8]
- **The request is a support case.** Bryce_Amazon (2024-09-05): submitting "will create a case with Selling Partner Support, and you'll receive a case number to track the progress". TaylorR_Amazon (2023-10-10): "After you have submitted your request, a case with Seller Support will be created". [read in official docs]
- **The eligibility date.** Amazon's Chinese article of 2025-03 (gs.amazon.cn article-250305-3) names two self-checks:
  - the 货件一览 → 物品信息 tab's 状态 column;
  - the 查询货件差异 (Missing inbound FBA inventory) tool, which "会显示货件做好准备进行调查的预计日期" (shows the estimated date the shipment is ready for investigation).

  It adds "只有状态为【已完成】的货件才符合货件差异查询的要求" (only shipments in Closed status qualify). [read in official docs]
- **Amazon on the date.** Angie_Amazon (US thread `ecbb2ef1-398c-4686-9e80-89b28eb383c9`, thread posted 2026-04-03, reply dated 2026-04-09): "The reconciliation eligibility date of May 15, 2026 is standard procedure", "Amazon requires shipments to be finalized before they become eligible for investigation", and "discrepancies can auto-correct during the receiving process, but it's not guaranteed". [read in official docs]
- **"Investigation completed".** Amazon's Chinese article (2025-03) and Julia_Amzn (UK thread `25ab2e15-8c9b-4ead-82d4-75a35ffd719a`, thread posted 2024-08-16, reply dated 2024-08-20) both explain the status 已完成调查 - 已清点并确认货件内商品 / "Investigation completed – shipment contents counted and confirmed". It means Amazon matched the delivered boxes against the plan and physically counted the units. "These products are no longer eligible for research. If you have any information that will help locate any of these missing units, contact Selling Partner Support. If we locate the missing units, we will add them to your inventory. Otherwise, we will deem the units short-shipped and a reimbursement cannot be issued." [read in official docs]
- **How long research takes.** "Typically, this process takes anywhere from 2 to 30 days, though in some cases it can extend up to 60 days… not all discrepancies result in reimbursement" (Christine_Amazon, US thread `83caf79b-4ca1-4e1c-9564-9f328739e0f7`, posted 2025-11-14). Bryce_Amazon (US thread `e0a6f096-f8a0-4d4d-8fbe-2b65b05b5e8f`, posted 2024-09-05) gives "2 to 60 days" and names the options "Units not shipped" and "Research missing units". Christine_Amazon names "Units not shipped" where "Amazon received fewer units than you shipped" and "Extra units shipped" for overages, adding "There might be other options". [read in official docs]
- **Investigation leaves stock alone.** gs.amazon.cn article-250807-3 (2025-08): "亚马逊将确认收到的数量，并尽力对漏发与多发的商品进行货件差异查询。进行此类货件差异查询不会影响卖家现有库存" (Amazon confirms the quantity received and researches both short- and over-shipped units; the research does not affect existing inventory). It advises filing on the 物品信息 page rather than with Seller Support, which "很可能…也会指导回到“物品信息页面”" (will likely send the seller back to that page). [read in official docs]

**Amazon's pages disagree on what `CLOSED` means** (stock I8 holds the 45/75-day reading):
- sell.amazon.com (2025): all units confirmed received, or open more than 45 days (domestic) or 75 days (international).
- gs.amazon.cn article-250807-3 (2025-08): "亚马逊已根据发货数量确认收到货件的所有商品，或者卖家的货件自创建之日起已打开超过90天（以时间较早者为准）" (all units received, or open more than 90 days from creation, whichever is earlier).
- TaylorR_Amazon (US thread `0c8e8239-9cd4-444f-9253-673a487b0039`, posted 2023-10-10): "open more than 90 days".
- The v0 model's `ShipmentStatus` `CLOSED`: "arrived at the fulfillment center and all items have been marked as received", with no timeout [command-verified].

The dating of the two forms (90 days from 2020-12-16; 45/75 days in the US from 2024-02-01) is stock I9's and was not re-read here. That the 2025-08 Chinese page carries the older figure is this seat's reading. The same 2025-08 page uses 45/75 days elsewhere, for the inbound defect fee on shipments not delivered within those days of creation. [read in official docs; dating via stock I9; reading inferred]

**(b) What practitioners add.**
- **Waiting is a common practitioner instruction.** My Amazon Guy reports that a case opened during a backlog gets a wait instruction (stock I26). Indy_Amazon's own post says that "filing prematurely is the #1 reason claims get denied". [read in official docs]
- **The status line forecloses filing.** Sellers on UK and EU threads report that "Investigation completed – shipment contents counted and confirmed" removes the Reconcile option. The European forum has at least four threads with that title. [opinion]
- **Two ways practitioners count a shortfall, side by side** (see section F for what each rests on):
  - per shipment and SKU: PrepVia (Bernardo Campelo, 2026-08-25, https://www.prepvia.com/blogs/amazon-fba-overage-received-more-than-shipped) writes "Reconcile shipment by shipment, never on the net number" and "receive counts can be revised"; 优麦云's claim assistant flags a completed shipment whose declared quantity differs from the received quantity (2024-06-05). [opinion]
  - across shipments: sellers report a fulfilment centre under-counting one shipment and over-counting a later one by the same number (thread `111de1aeacb3b8e67c5d845949bf8c02`, search result only), and a 2018 thread relays an Amazon "leader" saying overages may be used against shortages. No practitioner read recommends netting for a claim. [opinion]

**(c) Into a skill:**
- A shipment can be researched only once it is `CLOSED`.
- Seller Central shows an estimated eligibility date per shipment, and that date can move.
- "Investigation completed – shipment contents counted and confirmed" ends the research route in Seller Central. Amazon then treats the units as not shipped unless Selling Partner Support locates them.
- How long research takes is an Amazon staff statement, not a rule (see filing-and-conduct FL30; the figures read are in *Values that move*).
- Submitting the request creates a Selling Partner Support case whose number shows on the Contents tab.

**Read at run time:**
- The shipment's status: v0 `getShipments` (`ShipmentStatus`) or v2024-03-20 `getShipment` (`status`), Amazon Fulfillment.
- The shipped and received quantities per SKU: v0 `getShipmentItemsByShipmentId` (`QuantityShipped`, `QuantityReceived`), Amazon Fulfillment (stock I3).
- The case the request created: through the Support API, on a restricted role outside the five (see sp-api-claims-surface SU8–SU11). Whether a reconciliation case's `subject` names the shipment is unread.
- **Only in Seller Central:** the eligibility status, the estimated eligibility date, the "Investigation completed" line, and the Action required menu.

---

## D. Evidence Amazon asks for

**(a) Amazon's rule.**
- **The list.** The fullest English text read is the SCP page's *Shipment to Amazon claims* (https://supplychain.amazon.com/support/reimbursements). Its "Before you submit a claim" and "Submit your claim" steps match the FBA page as Amazon's Chinese restatements give it (gs.amazon.cn 2025-03 and 2025-08) and as Hopted's undated copy gives it:
  - "Amazon shipment ID";
  - "Proof of inventory ownership… an invoice from a supplier, a receipt from another seller, or a signed packing slip if you are a manufacturer", showing "Date of purchase, Product names matching the lost or damaged items, Quantity";
  - "Proof of delivery: For less-than-truckload (LTL) or full-truckload (FTL) shipments, a proof of delivery document showing the number of boxes in the shipment and the total weight when it was picked up by the carrier. The document must be stamped by Amazon, confirming that the shipment was received and signed for at the fulfillment center… For small-parcel shipments, Amazon needs the active tracking ID, which the carrier can confirm for each package shipped. If you did not use an Amazon partnered carrier and did not provide the tracking information at the time you created the shipment, you must enter it before you can be reimbursed."
  - "To submit a claim for lost units, use the Contents tab. To submit a claim for damaged units, open a claim through the Contact Us page."
  - "Note: You may file only one claim per shipment. Additional claims for the same shipment will be declined."
  - "Merchants who generate a high number of shipping problems affecting Amazon receiving operations may be subject to additional investigation and monitoring."

  [read in official docs; the "one claim per shipment" sentence is SCP's text and Hopted's copy of the FBA page: official for MCF, official-via-third-party for FBA. For FBA, Indy_Amazon's US post (2026-08-13) also says "Don't submit duplicate claims — One claim per shipment or event": read in official docs]
- **Format and what Amazon refuses.** gs.amazon.cn article-250305-3 (2025-03):
  - a packing slip must carry "装箱单日期、货件编号或采购订单编号、缺少商品的名称、已发货数量、制造商签名或印戳" (date, shipment or PO number, item names, quantity shipped, maker's signature or stamp);
  - editable formats are refused: "不接受可编辑格式：如Excel、Word等。接受的文件格式：PDF、JPG、JPEG、PNG或TIFF";
  - "您可以隐藏或遮挡为购买商品支付的价格" (you may hide the price paid);
  - "亚马逊不接受形式发票或类似合同作为所有权证明" (pro forma invoices and contracts are not accepted as proof of ownership).

  [read in official docs]
- **What an invoice must name.** KJ_Amazon (US thread `2c97b436-bc0f-41bc-8246-c4509716d7a8`, thread posted 2025-02-11, reply dated 2025-02-13: "Full name and address of the invoice issuer", "Full name and address of the buyer (seller)"; a manufacturer's signed packing slip "in non-editable format") and TaylorR_Amazon (2023-10-10: "the full name and address of the invoice issuer and of the purchaser") add the issuer and buyer. [read in official docs]
- **The staff checklist.** Indy_Amazon (2026-08-13) lists "Tracking IDs and proof of delivery for inbound shipments" and "Amazon-stamped delivery documents (for LTL/FTL shipments)". The path is "Inventory > Shipments > Shipping Queue… click the Reconcile tab", and damaged inbound units go to "Help > Get Support with your Shipment ID". [read in official docs]
- **The model's tracking check.** In the v2024-03-20 model, `SpdTrackingItem.trackingNumberValidationStatus` is `VALIDATED`, `NOT_VALIDATED` or `NOT_SUPPORTED` ("Amazon is unable to find tracking information for the provided tracking ID"); "If more than 24 hours have passed and the status is not yet 'VALIDATED' or `NOT_SUPPORTED`, verify the number and update it if necessary." `LtlTrackingDetail` carries `billOfLadingNumber` and `freightBillNumber` [command-verified]. Tracking is written with `updateShipmentTrackingDetails` and needs Amazon Fulfillment (role table). v0 `getBillOfLading` returns the BOL PDF for a partnered LTL/FTL shipment (Amazon Fulfillment). [read in official docs]

**Two of Amazon's own requirements pull against each other** [inferred]:
- Amazon's 2025-03 Chinese page lets the seller hide the price on the ownership invoice.
- Since 2025-03-31 the shortfall is paid at sourcing cost (finance P-ref-14; stock I22), and the SCP text asks for "Proof of item cost". Without it, it estimates "40% of the estimated sale price".

A redacted invoice proves ownership but not cost. Where a sourcing cost was entered on *Manage Your Sourcing Cost* the two are separate documents (value-and-reversals owns the valuation).

**(b) What practitioners add.**
- **百运网** (2026-05-27):
  - for factories, a signed English packing list with carton numbers;
  - a forwarder's stamped delivery receipt with carton count, total weight and delivery time;
  - carton-label photos, pre-seal photos, weight records and tracking screenshots, "形成完整闭环" (to close the loop);
  - inconsistent quantities across invoice, packing list and POD are a common rejection.

  [opinion]
- **AMZ123 / 深圳美辰物流** (2023-10-27): for LTL/FTL "可以像物流商索要PRO和ISA截图" (ask the carrier for the PRO and ISA screenshots); per shipment, list each FNSKU, carton tracking number, expected and received quantity. [opinion]
- **Marketplace Valet** (2026-10-24): "An invoice for 500 units doesn't prove a shipment of 600." [opinion]
- **Forum sellers on partnered LTL.** In US forum threads, sellers report that the partnered carrier releases a POD only against the PRO number, which was missing from the BOL Amazon generated (TForce Freight, thread `d6e43b25-2e85-43c5-8400-2c2f2ba13648`, seen in search results only). [opinion, snippet]

**(d) Chinese sellers' evidence for inbound, as Amazon's Chinese pages and Chinese practitioners name it.**
- **Amazon's Chinese words** (gs.amazon.cn article-250305-3, "以上信息发布时间为2025年3月", and article-250807-3, "2025年8月"; read 2026-11-13):
  - 库存所有权证明: "供应商提供的发票、其他卖家提供的收据；如果您是商品的制造商，也可提供已签字的装箱单" (a supplier invoice, another seller's receipt, or a manufacturer's signed packing list);
  - an invoice must carry "购买日期 / 与缺少的商品一致的商品名称 / 购买数量"; a manufacturer's 装箱单 must carry "装箱单日期 / 货件编号或采购订单编号 / 缺少商品的名称 / 已发货数量 / 制造商签名或印戳";
  - 交货证明 for LTL/FTL: "显示承运人取件时货件箱数和总重量的提货单。该文件须经亚马逊盖章确认运营中心已签收货件" (a bill of lading showing carton count and total weight at pickup, stamped by Amazon to confirm the fulfilment centre signed for it), obtained from the carrier;
  - before filing, "建议卖家先与仓库发货人员、承运商等确认是否漏发或多发了商品" (confirm with the warehouse dispatch staff and the carrier whether units were short- or over-shipped) (article-250807-3).

  [read in official docs]
- **What Chinese practitioners call the delivery proof.** The words differ from Amazon's:
  - 百运网 (https://m.by56.com/news/59431.html, 2026-05-27): "交货证明(POD)：货代出具的带公章的签收单，含箱数、总重量、送达时间" (a signed receipt issued and company-stamped by the forwarder, with carton count, total weight and delivery time); a rejection cause is "发票、装箱单、POD 数量 / 信息矛盾，或无公章、无签字". [opinion]
  - AMZ123 (ask 7xKCTk0F, 2024-05-12): "现在很多亚马逊仓库在签收时已经不再盖章或签字，尤其是在旺季时"; "卖家在发货时应当尽量要求货代提供POD单" (many Amazon warehouses no longer stamp or sign at receipt, especially at peak; ask the forwarder for the POD when shipping). [opinion; an aggregated Q&A page, author not named]
  - AMZ123 (ask 1KqAXyXG, 2025-05-19): the POD "需包含仓库接收章、收货人签名、完整货物件数" (warehouse receiving stamp, receiver's signature, full carton count). [opinion; same caveat]
  - AMZ123 (ask 02AvE5QA, 2024-11-02, a seller's account): a truckload the forwarder delivered to the wrong FC, where "提供签收证明也没用" (the signed receipt did not help). [opinion]
- **The gap between the two** [inferred]: Amazon's text asks for a document stamped by Amazon; the practitioners' 签收单 is the forwarder's, stamped by the forwarder, and the practitioners report that Amazon warehouses often do not stamp. Whether Amazon accepts a forwarder-stamped 签收单 without an Amazon stamp for an LTL/FTL inbound claim is unread (open question 13).
- **Invoices from Chinese suppliers** (Chinese-language invoices, 1688 order receipts, 发票/fapiao, a buyer entity that differs from the selling entity): Amazon's inbound pages read name the issuer and the buyer ("Full name and address of the buyer (seller)", KJ_Amazon 2025-02-13) and refuse pro forma invoices and contracts; none read says whether a Chinese-language invoice or a 1688 receipt is accepted for an inbound claim. The proof-of-value side (MYSC) is value-and-reversals' (VR13); for inbound the question stays open (open question 14).

**(c) Into a skill:**
- The evidence list: shipment ID; an ownership document carrying date, product names and quantity, with issuer and buyer named, in a non-editable format, and not a pro forma.
- Proof of delivery depends on mode: an Amazon-stamped BOL with carton count and weight for LTL/FTL; for small parcel, the "active tracking ID" (Amazon's words; the model's `VALIDATED` status is the API's own field, and no Amazon page read ties the claim to that status [inferred]).
- One claim per shipment (see filing-and-conduct FL7).
- Lost units go through the Contents tab; damaged units go through a support case.
- Amazon's Chinese pages name the same documents in Chinese; the LTL/FTL delivery proof they name is an Amazon-stamped 提货单, which is not the forwarder's 签收单 that Chinese practitioners name.

**Read at run time:**
- The shipment's mode and solution: `listTransportationOptions` (`shippingMode`, `shippingSolution`).
- Box IDs and tracking IDs with their validation status: `getShipment` → `trackingDetails`; `listShipmentBoxes`.
- The BOL: v0 `getBillOfLading`.
- Box content source: `listShipmentBoxes` → `contentInformationSource`; v0 `BoxContentsSource`.

All of these need Amazon Fulfillment. The invoice and the carrier's signed POD are the seller's documents and are not in any API.

---

## E. Amazon-partnered carrier against the seller's own carrier; small parcel against LTL/FTL

**(a) Amazon's rule.**
- **Amazon's carrier.** The policy covers loss "by a carrier operated by Amazon or on behalf of Amazon" (section A). For a UPS partnered small-parcel shipment that UPS marked "damaged and destroyed", TaylorR_Amazon replied: "you can file a claim with Amazon directly, in accordance with the FBA inventory reimbursement policy… You will just need proof of inventory ownership and proof of delivery. See reconcile your shipment" (US thread `10816b8f-963d-4d07-a4e2-9480206f9c22`, thread posted 2024-11-12, reply dated 2024-11-29). The seller's question had said "Amazon is the shipper of record, so I can't file the claim myself"; the staff reply neither confirms nor denies that. [read in official docs for the reply; the shipper-of-record sentence is the seller's: opinion]
- **The seller's own carrier.** The tracking sentence in D applies ("If you did not use an Amazon partnered carrier and did not provide the tracking information… you must enter it before you can be reimbursed"). Loss before delivery with the seller's own carrier is outside the policy's opening sentence; section M holds the first mile. TaylorR_Amazon (2023-10-10) asks for "drop-off receipt or proof of pick-up from the carrier" where loss in transit is suspected. [read in official docs; the "outside the policy" reading is inferred from the opening sentence]
- **Who carries arrival data.** Amazon's Chinese article (2025-08): with a partnered carrier the shipment shows 已发货 (Shipped) once the carrier picks up; with a non-partnered carrier it shows Shipped once valid tracking is entered. "承运人将货件运至运营中心后，货件可能需要长达10天时间才能进入“已登记”状态，在高峰时段可能需要更长时间" (after delivery it can take up to 10 days to reach Checked-in, longer at peak). [read in official docs]
- **The partnered-carrier charge.** Confirming a partnered-carrier transportation option agrees to the charge, which can be voided within 24 hours (small parcel) or one hour (LTL/FTL). This is stock I16 and is not repeated. Unused partnered labels are a fee question (fee-overcharges).

**(b) What practitioners and sellers report on outcomes.**
- Partnered UPS losses end in reimbursement in some threads (thread `0fc75622-…`, 2023: "this is in the process of being refunded") and in an "Amazon has no evidence the units were received" denial in others. [opinion: sellers; the denial wording is an Amazon Seller Support email]
- UPS tells sellers that "Due to Amazon's agreement with UPS Amazon has to open any investigation or claim regarding this shipment" (same thread). [opinion, the seller relaying UPS]
- A French-store seller (thread `30b0589d-36ad-47ef-a280-c481fd59551d`, store `A13V1IB3VIYZZH`, 2025-03-17) reports 148 units marked "CARRIER DAMAGED" in the ledger, an automatic disposal order he could not cancel, and repeated "wait" answers. Maya_Amazon asked for the case ID. [opinion; staff reply official]
- 百运网 (2026-05-27) and a VIPON / 百佬汇 article report that Amazon may answer that a quantity difference at the sender's end is not the warehouse's responsibility. [opinion, search snippet]

**(c) Into a skill:**
- A partnered-carrier loss is filed with Amazon under the same Shipment to Amazon route (staff reply, 2024-11-29). That the seller cannot claim from the partnered carrier is what a seller and UPS (as relayed by a seller) say, not an Amazon page [opinion].
- For the seller's own carrier, tracking must be on the shipment before Amazon pays.
- A carrier POD proves delivery of boxes, not their contents.

**Read at run time:** `shippingSolution` and `shippingMode` per shipment (`listTransportationOptions`); the tracking IDs and their validation (`getShipment`); the ledger disposition `CARRIER_DAMAGED` or `DISTRIBUTOR_DAMAGED` rows (`GET_LEDGER_DETAIL_VIEW_DATA`; the disposition spellings are to be confirmed on a live file).

---

## F. Overages: more received than shipped

**(a) Amazon's rule.**
- Christine_Amazon (2025-11-14) names "Extra units shipped" as an Action required option for overages.
- Amazon's Chinese article (2025-08) says the research covers "漏发与多发" (short and over) and "不会影响卖家现有库存".
- Angie_Amazon (reply dated 2026-04-09) told a seller whose system over-counted a box to wait for the eligibility date and keep the air invoice as evidence.
- No Amazon page read says that an overage of one SKU or shipment offsets a shortage of another.

[read in official docs]

**(b) What practitioners add.**
- A 2018 US thread (`a6ed7c414c1dc77c9c37a29068557802`) reports an Amazon "leader" saying it is "within Amazons policy to use overages and unexpected units that are received on shipments". A reply answers "There is nothing in any policy, anywhere that allows substitution." [opinion; the "leader" statement is relayed, not Amazon's page]
- Sellers report a fulfilment centre under-counting one shipment and over-counting a later one by the same number (thread `111de1aeacb3b8e67c5d845949bf8c02`, search result only). [opinion, snippet]
- PrepVia (2026-08-25): extra units "post as Receipts on the shipment; after it closes they post as a found Adjustment in the ledger". The inbound placement fee "is billed on units received", so an overage also carries fee. In PrepVia's view, netting "launders four process failures into one reassuring number". [opinion; the placement-fee basis agrees with stock P-inbound-22, which says the fee is charged "on the inbound location and the quantities received"]
- 百运网 (2026-05-27): 多收 (overage) means "调查多余商品" (research extra units) and cooperating with removal of the excess. [opinion]

**(c) Into a skill:**
- Overages are a discrepancy Amazon researches through the same menu ("Extra units shipped").
- Amazon's pages state no netting rule.
- The placement fee is charged on received quantities (stock pack).

**Read at run time:** per SKU `QuantityShipped` against `QuantityReceived` (v0) with its sign. Ledger `Receipts` against the shipment, and later `Found` adjustments (`GET_LEDGER_DETAIL_VIEW_DATA`, `GET_LEDGER_SUMMARY_VIEW_DATA`, Amazon Fulfillment).

---

## G. What an inbound claim pays (pointer to value-and-reversals)

**(a) Amazon's rule, as it touches inbound only.**
- **Pre-order losses.** The US PDF (2024-12-18) says "For shipment to Amazon claims, removals claims, and fulfillment center operations claims that occur before fulfillment, we will reimburse you the manufacturing cost of the item. This also covers lost and damage claims during inventory replenishment handled by Amazon or on behalf of Amazon to fulfillment centers or non-Amazon buildings in marketplaces where we provide the service." The DE PDF (2025-02-24) says the same with "sourcing cost".
- **The "estimated proceeds" sentence is struck.** The PDFs' text layer also carries "If we elect to reimburse you for a shipment to Amazon claim, we reimburse you for the estimated proceeds of a sale of that item." Rendered, that sentence is struck through, with the whole price-indicator block and the "Estimated proceeds" note, in the US PDF of 2024-12-18 (page 3), the US PDF of 2025-02-24 (page 2) and the JP policy of 2025-02-19 (page 3), where the pre-order clause above is inserted text (red, underlined). It is the pre-2025 basis, not a live second one (see value-and-reversals VR1, VR28). The earlier reading of this file, that both sentences stand, was a text-layer reading and is withdrawn. [read in official docs; pages rendered and read, command-verified]
- **Caps.** The per-unit cap is a per-store value (see value-and-reversals VR29). The Supply Chain Portal page has its own cap, preference for unit reimbursement and fallback (see filing-and-conduct FL27; fc-lost-damaged FC40). Values read are in *Values that move*.
- **The IDR portal.** It "doesn't include defects under missing from inbound" (finance P-ref-13; filing-and-conduct FL5).

[read in official docs]

**(b) What practitioners add.** AMZ123 老虎站外推广 (2026-11-02, quoted in finance pack): "入仓短装…自动赔付基本不覆盖" (inbound shortages are basically not auto-paid). [opinion]

**(c) Into a skill:** inbound shortfalls are pre-order losses, paid at sourcing cost where the seller entered one and otherwise at Amazon's estimate (valuation is value-and-reversals'). Replenishment loss (for example AWD → FBA) is inside the policy's pre-order clause.

**Read at run time:** what was paid: `GET_FBA_REIMBURSEMENTS_DATA` (`reason` `Lost_Inbound` / `Damaged_Inbound`, `case-id`, `amount-per-unit`, `quantity-reimbursed-cash` / `-inventory`; Amazon Fulfillment or Pricing). The money line: Finances `listTransactions` (Finance and Accounting) or the settlement row `MISSING_FROM_INBOUND` (finance P-ref-33). Valuation detail belongs to value-and-reversals.

---

## H. Prep and labels: the 2026-01-01 exclusion

**(a) Amazon's rule.** Jameson_Amazon, reply in US thread `5c63f045-b956-447b-9e6d-410b1e2a05bb` (thread posted 2025-11-25, reply dated 2025-12-01, store `ATVPDKIKX0DER`):
- "Starting January 1, 2026, we'll no longer offer prep and item labeling services for Fulfillment by Amazon (FBA) shipments in the US store. This change applies to all inventory that is sent to our US FBA service".
- The change includes inventory from AWD, AGL, Amazon SEND and Supply Chain Portal, "when that inventory goes through FBA".
- "For shipments created before January 1, we'll continue to provide prep and item labeling services, even if inventory arrives after that date".
- Shipments "created after January 1, that arrive without proper prep and item labeling won't be eligible for reimbursement if damaged or untraceable."

Where a shipment created on 2026-01-01 itself falls is not stated in the reply; "on or after" below is this seat's reading of "created before January 1" [inferred].

[read in official docs; the finance pack's P-ref-12 holds the exclusion; this adds the creation-date boundary and the word "untraceable"]

Before the exclusion, Amazon already refused where labels broke the tie to the shipment (stock I23, a moderator reply of 2025-12). Amazon's Chinese article (2025-08), on the labels themselves:
- "每个单独售卖的产品外包装，必须使用“X00”开头的FNSKU标签… 不能用ASIN或UPC标签代替" (for units that are not commingled, each unit needs an FNSKU label starting X00; not an ASIN or UPC label);
- labels can fall off in transit;
- labels inside the packaging cannot be scanned;
- other barcodes should be removed rather than covered.

[read in official docs]

The SP-API changelog (stock I19) records that `AMAZON` is no longer accepted as `prepOwner` or `labelOwner` in the US. A third party gives 2026-07-01 for Canada (stock pack, snippet).

**(b) What practitioners add.** 百运网 (2026-05-27) names mixed cartons with unclear or missing carton labels as "无法溯源" (untraceable) and a rejection cause. [opinion]

**(c) Into a skill:**
- For US shipments created on or after 2026-01-01, units that arrive without proper prep and item labels are not reimbursed if damaged or untraceable.
- The boundary is the shipment's creation date, not its arrival.

**Read at run time:**
- **Creation date:** v2024-03-20 `InboundPlan.createdAt` (`getInboundPlan` / `listInboundPlans`, Amazon Fulfillment). v0 carries no creation date [command-verified].
- **Prep and label owner the plan declared:** `listInboundPlanItems` / `listShipmentItems` (`prepOwner`, `labelOwner`), and `listPrepDetails` for SKUs whose prep was set through the API (stock G3).
- **Unplanned prep problems:** the Inbound Performance report (stock I14).

---

## I. End of commingling (2026-03-31) and what it changes for tracing a unit

**(a) Amazon's rule.** News_Amazon, *Commingling practices will end effective March 31, 2026*, posted 2025-12-08 to the UK forum (thread `06778c12-539e-478a-8f67-00592c4c5cca`, store `A1F83G8C2ARO7P`) and the Canada forum (thread `cd352647-7a0d-426f-83e7-e3dd4add6c5c`, store `A2EUQ1WTGCTBG2`) [store command-verified]. The text read (via WebFetch of the UK thread):
- Amazon "will end commingling practices across its supply chain" for inventory shipped on or after March 31, 2026.
- Brand owners with the Brand Representative role no longer need Amazon barcode stickers for products carrying a manufacturer barcode.
- Resellers who are not Brand Representatives must use Amazon barcode stickers.
- Products without a manufacturer barcode need stickers.

The post says nothing about reimbursement or tracing. No US thread for the announcement was located before the search budget ran out. [read in official docs]

**(b) What practitioners add.**
- PPC Land (2026-03-24, https://ppc.land/amazon-ends-fba-commingling-on-march-31-what-really-changes-for-sellers/) dates the announcement to about November 2025 and says inventory already held is "grandfathered". It also says "Units arriving at fulfillment centers without required barcodes after March 31 will be flagged as defective" and "Defective units are not eligible for reimbursement under Amazon's FBA policies".
- PPC Land quotes Ivan Raineri: "With returns now routed back to your specific inventory, the traceability is improved."

[opinion; no Amazon page read says the defect and reimbursement sentences]

**(c) Into a skill:** commingling ended for inventory shipped on or after 2026-03-31, and Amazon's announcement names the label each kind of seller must use. Amazon's announcement states no effect on inbound claims. That an arrival on the wrong label after the cut-off cannot be reimbursed is practitioner opinion. [inferred: before the cut-off, units received under a manufacturer barcode in a commingled pool were not tied to the seller's own unit, which is one reason a shipped-against-received count could not be traced to a box; seat's own beyond that]

**Read at run time:** the label type the plan declared per SKU (`labelOwner`; the item's `msku` and `fnsku` in `listShipmentItems`). Whether an ASIN may use the manufacturer barcode: `getItemEligibilityPreview` with `program` `COMMINGLING` (FBA Inbound Eligibility v1, Amazon Fulfillment; reason codes `FBA_INB_0342` and `FBA_INB_0465` concern manufacturer-barcode ineligibility, stock pack G5).

---

## J. AWD inbound and AWD → FBA replenishment

**(a) Amazon's rule.**
- **AWD service terms** ("Dated: January 14, 2026", https://supplychain.amazon.com/legal/service-terms/warehouse-and-distribution, read 2026-11-13), section 4:
  - eligibility needs "a valid AWD appointment for the shipment";
  - "Amazon will only accept one lost or damaged shipment claim per shipment and one AWD facility operations claim per box";
  - shipment claims follow the MCF policy's Shipment to Amazon provisions, with the window starting at verified delivery to the AWD site (section B);
  - "AWD transportation: Units that are lost or damaged in transit to an Amazon fulfillment center will be replaced or reimbursed pursuant to the MCF inventory reimbursement policy";
  - "Inventory reimbursement calculation: If we determine that your AWD inventory reimbursement claim is valid, we will reimburse you according to the valuation methodology described in the MCF inventory reimbursement policy";
  - AWD fee claims for box dimensions, counted from the date the fee was charged (value in *Values that move*);
  - claims go "by submitting a case to Amazon Support".

  [read in official docs]
- **Which page "the MCF inventory reimbursement policy" is.** Every one of the five places the AWD terms name it is a hyperlink, and all five point to https://supplychain.amazon.com/support/reimbursements ("MCF inventory reimbursement policy: Shipment to Amazon claims", "…: Fulfillment center operations claims", "…: Removals claims", and twice the bare name). That page is titled *Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS)*; its eligibility list requires "Your Multichannel Fulfillment (MCF) account is in Active state", and its sections are Shipments to Amazon, Fulfillment center operations, MCF order fulfillment, Removals, MCF Order Returns and Fee Reimbursements. So the MCF policy the AWD terms name and the Supply Chain Portal page are one page; filing-and-conduct FL27 (the page is the ASCS programme's, for an active MCF account, and its figures are not FBA's) and this file's IN26 describe the same page and do not conflict. No separate Seller Central "MCF inventory reimbursement policy" page was found by a permitted route. [read in official docs; link targets command-verified from the terms' HTML, 2026-11-13]
- **What the page says for shipments to Amazon** (read 2026-11-13): the claim may be filed "Once a shipment is shown as eligible for investigation in the Status column on the Contents tab"; a window counted from "the verified date of a shipment delivery to an Amazon fulfillment center or to a third-party facility operated on Amazon's behalf"; valuation "based on the cost of the eligible item", first "the commercial value if you provide ASIN-specific commercial values … with invoice samples", else a percentage of the retail price, else "lesser of the listing price provided by you and the estimated category average value"; for items damaged in inbound shipments Amazon may "reimburse a partial amount based on the extent of damage"; a valuation dispute goes through the Supply Chain Portal Contact Us within a stated period. Values are in *Values that move*. [read in official docs]
- **The FBA policy** (US PDF, 2024-12-18) brings "inventory replenishment handled by Amazon or on behalf of Amazon to fulfillment centers" into its pre-order clause (section G). [read in official docs]
- **The AWD API model** (v2024-05-09, local clone) [command-verified]:
  - `InboundShipment` carries `receivedQuantity` ("Quantity received (at the receiving end)") and, with `skuQuantities=SHOW`, per-SKU `expectedQuantity` and `receivedQuantity`, each as `InventoryQuantity` with `unitOfMeasurement` `PRODUCT_UNITS`, `CASES` or `PALLETS`;
  - its statuses are `CREATED`, `SHIPPED`, `IN_TRANSIT`, `RECEIVING`, `DELIVERED`, `CLOSED` ("No more actions required… final state") and `CANCELLED`.

  The release note says `skuQuantities` lets a seller "reconcile and compare expected and received inventory for each SKU in a shipment". The tutorial *Track an inbound shipment with expected and received SKU details* (updatedAt 2026-09-09) says: "Currently, there are no reports for AWD available in the API. You can use Seller Central to manually download Inbound Shipment report, Inventory Ledger report and Fee Reports." [read in official docs]
- **Every AWD operation needs the Amazon Warehousing and Distribution role** (stock W38; P-inbound-41), which is outside the five roles the door's application holds.
- **Staff answers.**
  - For AWD inbound (US thread `f72ae6d7-9041-444c-9605-c4a5ebdaea7f`, thread posted 2025-01-17, staff reply dated 2025-01-21), a seller wrote that "There does not appear to be a process by which we can request reconciliation of an inbound shipment to an AWD warehouse". Topher_Amazon asked for case IDs "for our AWD partners to look into any missing units and discrepancies".
  - For AWD → FBA (US thread `2c97b436-…`, thread posted 2025-02-11, reply dated 2025-02-13), KJ_Amazon had a "partner team" open cases for the replenishment shipments (IDs of the form `FBA18…`) and asked for proof of ownership. It did not ask for proof of delivery, which the seller could not hold because AWD books the carrier.
  - In US thread `ed108c90-…` (2024-10-14), Topher_Amazon found that a shipment a seller took for an AWD replenishment had been sent "using AGL directly to FBA in the CA Marketplace".

  [read in official docs]

**(b) What practitioners add.**
- The seller of `f72ae6d7-…`: support asked for "invoices that cover AWD to FBA FC replenishment shipments", which do not exist. [opinion]
- 赛狐 counts AWD in transit from statuses `SHIPPED`, `IN_TRANSIT`, `DELIVERED`, `CHECKED_IN`, `RECEIVING` (stock P6). [opinion]

**(c) Into a skill:**
- **AWD inbound:** a loss is claimed by support case under the AWD terms; the window counts from verified delivery to the AWD site, one claim per shipment.
- **AWD → FBA replenishment:** loss is covered by the FBA policy's replenishment clause and the AWD terms. The replenishment shipment carries an FBA shipment ID, and Amazon staff have asked for proof of ownership, not proof of delivery, for it.
- AWD shipments are not readable on the door's five roles.

**Read at run time:**
- **AWD inbound:** `getInboundShipment` with `skuQuantities=SHOW` (role Amazon Warehousing and Distribution, outside the five: it would open expected against received per SKU for AWD inbound; nothing is built on it). Otherwise Seller Central's AWD Inbound Shipment report and ledger, which have no API.
- **AWD → FBA:** the FBA shipment through the Fulfillment Inbound reads, if it is returned there (open question 3).

---

## K. Amazon Global Logistics (AGL)

**(a) Amazon's rule.**
- The help page *Claims and reimbursements through Amazon Global Logistics* (`GR384ESWC8HH8667`, https://sellercentral.amazon.com/gp/help/external/GR384ESWC8HH8667) is a script shell. Its text reached this seat only as a search summary: for missing units, go to the Shipping Queue → Track shipment → Summary → Reconcile, and under Status/Action required choose "Missing – please research"; for damaged inventory, contact Amazon with the shipment ID. [read in official docs, via search snippet; page unread]
- AGL inventory to US FBA falls under the 2026-01-01 prep exclusion (section H). [read in official docs]
- **The ocean and air legs: *Amazon Global Logistics Freight Service Terms*** ("Dated: January 14, 2026", https://supplychain.amazon.com/legal/service-terms/global-logistics-freight, read 2026-11-13 by plain GET; the finance pack holds the billing clauses, P-ful-29 to P-ful-31):
  - Who "we" is: "For China origin, domestic, and international outbound Services, "us" or "we" will mean BCJ. For international ocean carriage originating in China, "us" or "we" will mean BCJ" (Beijing Century Joyo Courier Co., Limited).
  - Risk of loss, §1.4: "We assume risk of loss for Cargo transported through the AGL Freight Program only from receipt at Origin until delivery at Destination." §19: "“Destination” means an Amazon facility in an Eligible Country"; "“Origin” means a pick-up location in an Eligible Country".
  - Sealed cargo, §3.5: where the seller loads and seals a container and "we cannot count or weigh the Cargo being loaded and the seal is intact upon delivery, we will not be liable for shortages or any damage to the Cargo unless proximately caused by our independent action".
  - Packaging, §5.5: "we are not liable for any loss or damage caused by inadequately packaged Cargo".
  - Limits, §10.1, §10.6, §10.8: a per-shipment limit for an ocean bill of lading to the US, unless a higher liability is agreed in writing at booking for a higher rate; "you must prove that the negligence of us, our contractor, or the carrier actually performing the transportation service caused damage to the Cargo"; otherwise the limit of the applicable convention (CMR, Montreal 1999, Hague-Visby, COGSA) "or a lesser amount corresponding to the value of the Cargo declared in relevant customs documents at the point of export or the point of import, whichever is less"; and a cumulative cap per 12-month period. §7.7: a per-pound limit while Amazon holds cargo as a warehouseman or cross-docks it.
  - Whom to claim from, §10.3: "You will pursue any claims regarding the AGL Freight Program or Cargo exclusively against the Amazon Contracting Party (not the carrier)".
  - Insurance, §8: the seller "must maintain insurance coverage … including (a) all marine risk, air Cargo risk, and property insurance for Cargo covering the entire shipment".
  - Claims, §11.1: "Notice of claims for loss or damage to Cargo must be filed in writing by you with us within [a stated period] from date of delivery, or scheduled date of delivery for lost Cargo"; legal action within a stated period of the written disallowance. §11.3: a credited amount may be contested in writing within a stated period of the decision, after which it "will constitute a complete settlement of the claim".

  Values are in *Values that move*. [read in official docs]
- **Where AGL freight ends and FBA receiving begins** [inferred]: the freight terms' risk ends at "delivery at Destination", an Amazon facility; the Seller Central AGL help text (snippet above) sends missing units to the shipment's Reconcile route. A shortfall found at receiving therefore reads as a Shipment to Amazon matter, and loss or damage before delivery as an AGL Freight claim; no Amazon page read draws the line in one sentence.
- **AGL proof of delivery.** A search summary of gs.amazon.cn (2026-11-13) says Shipper Central orders completed after 2024-04-01 let the seller download the proof of delivery from the Shipper Central account. The article was not identified or read. [read in official docs, via search summary; page unread]

**(b) What practitioners add.** EU forum sellers report AGL pallets "delivered" in tracking and stuck for months while Amazon and AGL point at each other (thread `4af0d38f-b970-4f5f-aedf-7fb99a755da3`, search result only). [opinion, snippet]

**(c) Into a skill:** AGL shortages at receiving go through the same Reconcile route. Loss or damage to AGL cargo before delivery to the Amazon facility is claimed in writing against the Amazon contracting party (BCJ for China-origin ocean carriage) under the AGL Freight Service Terms, within their notice period and liability limits; sealed-container shortages are excluded unless Amazon's own act caused them.

**Read at run time:** the AGL Freight Service Terms as dated on supplychain.amazon.com (public), and the bill of lading for the booking; the AGL help page in the seller's store (a script shell, unread here). No SP-API operation creates or reads AGL bookings (stock I18; finance P-ful-37).

---

## L. What the SP-API shows for an inbound claim, and what it cannot do

Reads, with the role Amazon's Role Mappings name (the roles table at commit `db2936aa`; report roles from *Role Mappings for Types*) [command-verified]:

| Read | What it gives a claim | Role |
|---|---|---|
| Fulfillment Inbound v0 `getShipments` | status, destination FC, `BoxContentsSource`, `LabelPrepType` | Amazon Fulfillment |
| v0 `getShipmentItemsByShipmentId`, `getShipmentItems` | `QuantityShipped`, `QuantityReceived`, `QuantityInCase` per SKU | Amazon Fulfillment |
| v0 `getBillOfLading`, `getLabels` | partnered LTL BOL PDF; box labels | Amazon Fulfillment |
| v2024-03-20 `listInboundPlans`, `getInboundPlan` | plan `createdAt` (the prep-exclusion boundary) | Amazon Fulfillment |
| v2024-03-20 `getShipment` | status, `trackingDetails` (SPD tracking IDs with validation status; LTL BOL and freight-bill numbers), `selectedDeliveryWindow`, `amazonReferenceId` (partnered LTL) | Amazon Fulfillment |
| v2024-03-20 `listShipmentBoxes`, `listShipmentItems`, `listShipmentPallets` | box IDs, box content source, planned items, prep and label owner | Amazon Fulfillment |
| v2024-03-20 `listTransportationOptions` | `shippingSolution` (partnered or own), `shippingMode` | Amazon Fulfillment |
| `GET_LEDGER_DETAIL_VIEW_DATA` | `Receipts` per FC and date, reconciled and unreconciled quantities, dispositions | Amazon Fulfillment |
| `GET_FBA_FULFILLMENT_INBOUND_NONCOMPLIANCE_DATA` | problem rows with expected and received quantity (stock I14) | Amazon Fulfillment or Pricing |
| `GET_FBA_REIMBURSEMENTS_DATA` | what Amazon paid, with `case-id` and reason | Amazon Fulfillment or Pricing |
| Finances `listTransactions` | the money line | Finance and Accounting |
| AWD `getInboundShipment` / `listInboundShipments` | expected against received for AWD inbound | Amazon Warehousing and Distribution (outside the five) |
| Support API (cases) | the support case a reconciliation request or a damaged-unit/AWD claim creates | restricted role outside the five (see sp-api-claims-surface SU8–SU11) |

Writes that touch a claim's evidence: `updateShipmentTrackingDetails` (Amazon Fulfillment) enters SPD tracking IDs or the LTL BOL and freight-bill numbers. This is the API side of "you must enter it before you can be reimbursed". [read in official docs; the link to the policy sentence is inferred]

Transport mode and carrier as the plan declared them: `ShippingConfiguration.shippingMode` lists `GROUND_SMALL_PARCEL`, `FREIGHT_LTL`, `FREIGHT_FTL_PALLET`, `FREIGHT_FTL_NONPALLET`, `OCEAN_LCL`, `OCEAN_FCL`, `AIR_SMALL_PARCEL`, `AIR_SMALL_PARCEL_EXPRESS`; `Carrier` carries `alphaCode` and `name`; partnered freight quotes take `FreightInformation.declaredValue` and `freightClass`. Nothing in the model names AGL or a forwarder's legs before the carrier that delivers to Amazon [command-verified, `fulfillmentInbound_2024-03-20.json` at `db2936aa`].

Removed reports that older guides still name: see sp-api-claims-surface SU42.

**No SP-API operation reads any of the following for an inbound shipment** [command-verified: no such operation in the models at `db2936aa`; upstream `main` has one later commit, `b13d1d10` of 2026-11-11, which touches only the Analytics Economics schema]. That no operation files or answers a claim is sp-api-claims-surface's (SU12):
- **The shipment's research eligibility:** the eligibility status, the estimated eligibility date and the "Investigation completed" line.
- **The answer, on the shipment:** the "units located" detail on hover and the shipment's own reconciliation status.
- **The rule itself:** the claim window, and Amazon's verified delivery date.

The seller does these by hand in Seller Central's Shipping Queue → Contents/Reconcile tab, or through a support case for damaged units and AWD.

---

## M. The first mile: loss before Amazon signs, with the seller's own carrier or forwarder

**(a) Amazon's rule.**
- **Scope.** The policy covers loss or damage "at a facility or by a carrier operated by Amazon or on behalf of Amazon" (section A). A carrier or forwarder the seller engaged is neither; its loss before delivery is outside that sentence. Arrivals already damaged are routed back to the seller's carrier (IN2). [read in official docs; the scope reading is inferred]
- **Amazon names the first mile as a cause of short counts.** gs.amazon.cn article-250807-3 (2025-08), under "为什么会出现箱内商品数量不准确的情况？": "① 发货前可能因清点疏忽导致少装。② 第三方/仓库/货代在打包时库存短缺且未及时更新货件计划。③ 运输过程中也可能因箱体破损造成商品遗失。④ 在海关、货代检查时出现数量误差。" (short packing before dispatch; a third party, warehouse or forwarder short of stock at packing that did not update the plan; units lost from broken cartons in transit; counting errors at customs or forwarder inspection). The same page tells the seller to confirm with "仓库发货人员、承运商" before requesting research. [read in official docs]
- **What Amazon asks of a non-partnered shipment.** The tracking must be on the shipment (IN5); for LTL/FTL the delivery proof is a document stamped by Amazon (IN15); TaylorR_Amazon (2023-10-10) asks for "drop-off receipt or proof of pick-up from the carrier" where loss in transit is suspected. [read in official docs]
- **AGL is not the seller's own carrier.** A shipment booked on Amazon Global Logistics travels under the AGL Freight Service Terms until delivery to the Amazon facility (section K).

**(b) What practitioners add** (all [opinion]):
- 深圳美辰物流 (AMZ123, 2023-10-27): look up the tracking to tell a carrier problem from a warehouse problem; a carrier problem is "与货代协商赔偿" (negotiated with the forwarder).
- 百运网 (https://m.by56.com/news/64618.html, 2026-11-09, on air freight): a written exception noted on the delivery document ("外箱破损、内件损坏、数量短缺，保留索赔权利") keeps the claim; hidden damage is usually to be notified "收货后 7 日内书面"; without cargo insurance "航司是按重量限额赔付，往往远低于货值" (the airline pays by a weight-based limit, often far below the goods' value); the claim goes in writing to the forwarder or airline with AWB, commercial invoice, packing list, photos and a damage count.
- AMZ123 (ask 02AvE5QA, 2024-11-02, a seller's account): a forwarder delivered a truckload to the wrong FC, and support passed the case around despite a signed receipt; for a whole shipment that never appeared, the forwarder said other sellers' cartons on the same truck had been received.
- Each forwarder's own contract sets its compensation basis, notice period and whether freight is refunded; a search summary (2026-11-13) described one forwarder's terms as per kilogram with a 60-day notice period. That page was not read. [snippet]

**(c) Into a skill:** Amazon's inbound policy does not pay for loss before Amazon or a carrier acting for it takes the goods; that loss is claimed from the carrier or forwarder under the seller's own contract, and its terms are the seller's documents. Amazon itself names forwarder and customs counting errors and broken cartons as causes of short counts.

**Read at run time:** the transport the plan declared (`listTransportationOptions`: `shippingSolution`, `shippingMode`, `carrier`; Amazon Fulfillment) tells a partnered from an own-carrier shipment. The forwarder contract, its POD and its tracking are the seller's documents; no API carries them.

---

## Positions

Each is one fact. "Read at" names where cx reads it for a seller's own store.

**IN1.** Amazon's FBA reimbursement policy covers items lost or damaged "at a facility or by a carrier operated by Amazon or on behalf of Amazon"; one of its conditions is that the seller sent "the exact items and quantities stated in your shipping plan". Sources: US policy PDF (2024-12-18); DE policy PDF (2025-02-24). [read in official docs]

**IN2.** Arrivals classed "distributor damaged" or "damaged by inbound carrier" were damaged before Amazon received them. They are unfulfillable, are removed, and the reimbursement route Amazon names is the seller's carrier. Source: NR_Amazon, US thread `0d6e8a48-…` (thread 2025-03-19, reply dated 2025-04-11). [read in official docs] Read at: ledger dispositions, `GET_LEDGER_DETAIL_VIEW_DATA` (Amazon Fulfillment).

**IN3.** For a loss by an Amazon-partnered carrier, Amazon staff told the seller to file with Amazon under the Shipment to Amazon policy, with proof of ownership and proof of delivery. Source: TaylorR_Amazon, US thread `10816b8f-…` (thread 2024-11-12, reply dated 2024-11-29) [read in official docs]. That Amazon is the shipper of record and the seller cannot claim from the partnered carrier is the seller's statement in the same thread and UPS's answer as relayed by a seller in thread `0fc75622-…`; no Amazon page read says it [opinion].

**IN4.** A carrier's proof of delivery shows that boxes arrived, not what was in them. An Amazon Seller Support email of 2023-08-07 declined a partnered-carrier loss "at this time" on that ground ("Amazon has no evidence the units were received"); the seller later relayed a refund in progress. Source: the email, quoted in US thread `0fc75622-…`. [read in official docs, via the seller; the later outcome: opinion]

**IN5.** For a small-parcel shipment with the seller's own carrier, the tracking ID must be on the shipment before Amazon pays. Source: SCP *Shipment to Amazon claims* (supplychain.amazon.com/support/reimbursements), and Hopted's undated copy of the FBA page. [read in official docs (MCF); via third party (FBA)] For FBA, Amazon's own pages read say less: Indy_Amazon (2026-08-13) lists "Tracking IDs and proof of delivery for inbound shipments" among what to have ready, and gs.amazon.cn article-250807-3 (2025-08) says Amazon requires a unique tracking code per box for small-parcel shipments and shows a non-partnered shipment as Shipped once valid tracking is entered; neither ties payment to it in words [read in official docs]. Read at: `getShipment` → `trackingDetails.spdTrackingDetail` (Amazon Fulfillment); written with `updateShipmentTrackingDetails`.

**IN6.** In the v2024-03-20 model each SPD tracking ID carries `trackingNumberValidationStatus` (`VALIDATED`, `NOT_VALIDATED`, `NOT_SUPPORTED` = Amazon cannot find tracking for it), and the model says to verify and update a number that is not validated after 24 hours. Source: `fulfillmentInbound_2024-03-20.json` at `db2936aa`. [command-verified]

**IN7.** The claim window for units missing from an inbound shipment is a per-store length, counted from the verified delivery to the fulfilment centre, and the request is filed after the shipment is closed. Read at: the help page *FBA inventory reimbursement policy: Shipment to Amazon claims* (`GEYPWTSQRTXXXMVB`) in the seller's store (script shell; unread here) and the store's forum News. No operation states it. Evidence, US store: Indy_Amazon's post (2026-08-13), gs.amazon.cn article-250305-3 (2025-03, "*美国适用") and article-250807-3 (2025-08, "（美国站）"), and a seller quoting `GEYPWTSQRTXXXMVB` (2024-09-26, thread store US); all read 2026-11-13; the value is in *Values that move*. This extends stock I21. [read in official docs]

**IN8.** Amazon's post *Update on reimbursement claim window eligibility on FBA* (2024-08-06; "Starting September 5, 2024"), which sets a minimum and a maximum count of calendar days from the shipment delivery date for units missing from shipments to Amazon, was issued as three threads, for the UAE, Saudi Arabia and Egypt stores, not for the US or the UK. Source: thread-level `marketplaceId` of `96a05f4a-…`, `c6da88ce-…`, `e62a8ace-…` (the pack's post-to-store table is fc-lost-damaged's); the day counts are in *Values that move*. [read in official docs; store command-verified] Read at: each store's forum News.

**IN9.** None of Amazon's News posts on claim windows for the US (2024-07-24), Canada (2024-07-24), UK (2024-10-10, 2025-01-15), Sweden (2025-01-15) or Australia (2025-08-14) names a window for shipments to Amazon. No Amazon statement of the length of an EU, UK or JP inbound window was read (see IN35, IN36 for what Amazon's redlines do say). Sources: the threads' stores, command-verified here; their content as in finance P-ref-16. [read in official docs]

**IN10.** No Fulfillment Inbound operation (v0 or v2024-03-20) returns a delivery, check-in, receiving or closed date. The window's start date ("verified delivery date") cannot be read from the API. Source: every `date-time` field of both models at `db2936aa`. [command-verified] Read at: proxies only: the first `Receipts` event in `GET_LEDGER_DETAIL_VIEW_DATA`, the selected delivery window or carrier appointment (`getShipment`, `listTransportationOptions`), and the carrier's tracking.

**IN11.** Seller Central shows, per shipment, whether it is eligible for investigation and an estimated date it will be. Amazon staff call that date standard procedure and say discrepancies "can auto-correct during the receiving process, but it's not guaranteed". Sources: gs.amazon.cn article-250305-3 (2025-03); Angie_Amazon, US thread `ecbb2ef1-…` (thread 2026-04-03, reply dated 2026-04-09). [read in official docs] Read at: Seller Central only (Contents tab; *Missing inbound FBA inventory* tool, `G201214140`).

**IN12.** "Investigation completed – shipment contents counted and confirmed" means Amazon matched boxes to the plan and physically counted the units. The units are then no longer eligible for research. Selling Partner Support adds units it locates, and otherwise Amazon deems them short-shipped and pays nothing. Sources: Julia_Amzn, UK thread `25ab2e15-…` (thread 2024-08-16, reply dated 2024-08-20); gs.amazon.cn article-250305-3. [read in official docs] Read at: Seller Central only.

**IN13.** Submitting a research request creates a Selling Partner Support case whose number shows on the Contents tab. Amazon staff give the research's duration as a range, not a rule, and say not all discrepancies result in reimbursement (review times: see filing-and-conduct FL30; figures in *Values that move*). Sources: sell.amazon.com *How to track FBA shipments* (modified 2025-10-03); TaylorR_Amazon 2023-10-10; Christine_Amazon, US thread `83caf79b-…`, 2025-11-14; Bryce_Amazon, US thread `e0a6f096-…`, 2024-09-05. [read in official docs] Read at: the case through the Support API, on a restricted role outside the five (see sp-api-claims-surface SU8).

**IN14.** Amazon's pages define `CLOSED` as all units received or, where they disagree, a timeout counted from shipment creation whose length the pages state differently; the v0 model gives no timeout ("arrived at the fulfillment center and all items have been marked as received"). Read at: the store's shipment-status help page and sell.amazon.com's tracking guide. Evidence: sell.amazon.com (modified 2025-10-03); gs.amazon.cn article-250807-3 (2025-08); TaylorR_Amazon (2023-10-10); v0 `ShipmentStatus`; the timeouts each states are in *Values that move*. Their dating is stock I9's, not re-read here. [read in official docs; command-verified for the model]

**IN15.** For a lost-unit claim on an inbound shipment, Amazon asks for:
- the shipment ID;
- proof of ownership (a supplier invoice, another seller's receipt, or the manufacturer's signed packing slip) showing purchase date, product names and quantity, with issuer and buyer named;
- proof of delivery: for LTL/FTL an Amazon-stamped document with box count and total weight at pickup; for small parcel, active tracking IDs.

Lost units are filed on the shipment's Contents tab, damaged units through a support case. Sources: SCP page; Indy_Amazon 2026-08-13; KJ_Amazon reply 2025-02-13; gs.amazon.cn 2025-03 and 2025-08. [read in official docs] (filing-and-conduct FL24 restates the list for filing; the Chinese wording is IN41.)

**IN16.** Amazon accepts ownership documents only in a non-editable format (PDF, JPG, JPEG, PNG, TIFF). It refuses pro forma invoices and contracts, and it lets the seller hide the price paid. Source: gs.amazon.cn article-250305-3 (2025-03). [read in official docs]

**IN17.** One claim is allowed per shipment; further claims for the same shipment are declined (see filing-and-conduct FL7, which holds the limit). This file's added evidence: the AWD terms (2026-01-14) apply the same to AWD, with one shipment claim per shipment and one facility claim per box. [read in official docs]

**IN18.** Amazon advises submitting the request on the shipment's item page rather than to Seller Support, which will likely send the seller back there. It also says the research does not change the seller's existing inventory. Source: gs.amazon.cn article-250807-3 (2025-08). [read in official docs]

**IN19.** Overages are researched through the same Action required menu ("Extra units shipped"; shortages: "Units not shipped" or "Research missing units" in staff posts). No Amazon page read states that an overage offsets a shortage. Sources: Christine_Amazon 2025-11-14; gs.amazon.cn 2025-08 [read in official docs]; the 2018 thread's relayed "leader" claim and its rebuttal [opinion].

**IN20.** Amazon's Contents tab and v0 items list shipped against received per SKU, so an overage on one SKU and a shortage on another are separate lines; no Amazon page read states a netting rule. Practitioners count a shortfall in two ways, side by side: per shipment and SKU (PrepVia, 2026-08-25; 优麦云's claim assistant, 2024-06-05), or across shipments, which sellers report fulfilment centres doing (thread `111de1ae…`, snippet; the 2018 thread's relayed "leader"); no practitioner read recommends netting for a claim. [the per-SKU lines: command-verified in the v0 model; the practices: opinion] Read at: per-SKU `QuantityShipped` against `QuantityReceived` (v0, Amazon Fulfillment).

**IN21.** Amazon's policy puts shipment-to-Amazon claims, and loss during replenishment handled by or for Amazon, in its pre-order class, reimbursed at manufacturing or sourcing cost. The "estimated proceeds" sentence for shipment-to-Amazon claims that a text extraction of the same PDFs shows is struck through in the rendered pages (US 2024-12-18, US 2025-02-24, JP 2025-02-19); it is the pre-2025 basis. Valuation itself is value-and-reversals' (see VR1, VR2, VR4, VR28). Sources: those PDFs, rendered and read 2026-11-13. [read in official docs; command-verified] Read at: *FBA inventory reimbursement policy* (`G200213130`) in the seller's store; the payment in `GET_FBA_REIMBURSEMENTS_DATA`.

**IN22.** (withdrawn: the per-unit cap is value-and-reversals' (see VR29), and the Supply Chain Portal page's own cap and fallback are filing-and-conduct's (FL27) and fc-lost-damaged's (FC40); values this file read are kept in *Values that move*.)

**IN23.** For US shipments created on or after 2026-01-01, units arriving without proper prep and item labelling are not reimbursed if damaged or "untraceable". Shipments created before that date keep Amazon's prep service even if they arrive later. This covers inventory reaching US FBA through AWD, AGL, Amazon SEND and Supply Chain Portal. Source: Jameson_Amazon, US thread `5c63f045-…` (thread 2025-11-25, reply dated 2025-12-01); the reply says "created before January 1" and "created after January 1", and "on or after" is this seat's reading. [read in official docs; boundary day inferred] Read at: plan `createdAt` (`getInboundPlan`/`listInboundPlans`, Amazon Fulfillment); `prepOwner`/`labelOwner` per item.

**IN24.** Amazon announced on 2025-12-08 (UK and Canada forum threads) that commingling ends for inventory shipped on or after 2026-03-31. Brand Representatives with a manufacturer barcode need no Amazon sticker, and resellers and products without a manufacturer barcode must use Amazon stickers. The announcement says nothing about reimbursement. Sources: threads `06778c12-…` (UK), `cd352647-…` (Canada). [read in official docs; store command-verified]

**IN25.** A practitioner reports that after 2026-03-31, units arriving without the required barcode are flagged defective and not reimbursed. Source: PPC Land, 2026-03-24. [opinion]

**IN26.** AWD shipment claims use the claim window of the MCF inventory reimbursement policy, counted from verified delivery to the AWD site, with one claim per shipment and one AWD facility claim per box, filed by support case; units lost in AWD transit to an FBA centre are reimbursed under the MCF policy, and AWD claims are valued by its methodology. The MCF policy is the Supply Chain Portal reimbursements page (IN34), so the window, cap and valuation an AWD claim takes are read there, not on the FBA policy. Source: AWD service terms, dated 2026-01-14, read 2026-11-13; the window value is in *Values that move*. [read in official docs] Refines stock I21 (see corrections).

**IN27.** The AWD model returns expected and received quantity per SKU for an AWD inbound shipment (`getInboundShipment` with `skuQuantities=SHOW`), counted in `PRODUCT_UNITS`, `CASES` or `PALLETS`. Amazon's tutorial says no AWD report is available in the API. Sources: AWD model at `db2936aa` [command-verified]; *Track an inbound shipment with expected and received SKU details* (2026-09-09) [read in official docs]. Role: Amazon Warehousing and Distribution, outside the five.

**IN28.** AWD → FBA replenishment shipments carry FBA shipment IDs. For missing units on them, Amazon staff opened cases and asked for proof of ownership, not proof of delivery. Source: KJ_Amazon, US thread `2c97b436-…`, reply dated 2025-02-13. [read in official docs]

**IN29.** No SP-API operation exposes an inbound shipment's research eligibility or eligibility date, the "Investigation completed" line, the shipment's reconciliation result, the claim window or Amazon's verified delivery date. These are Seller Central views (Shipping Queue → Contents/Reconcile). That no operation files or answers a claim, and what the Support API reads of the case, are sp-api-claims-surface's (SU8–SU12). Source: the Fulfillment Inbound, AWD and reports models at `db2936aa` (no later upstream commit touches them). [command-verified]

**IN30.** (withdrawn: the removed reconciliation and receipts reports are sp-api-claims-surface's; see SU42.)

**IN31.** Practitioners state inbound windows that no Amazon page read supports: 60–90 days (Refunzo, 2026-01-18); 90 days from creation for Receiving-status claims (百运网, 2026-05-27); 6 months for EU (Helium 10 FAQ and SELLERLOGIC, snippets). [opinion] (AMZ123 / 深圳美辰物流, 2023-10-27, states 18 months for fulfilment-centre operations claims, not for inbound.) AMZ123 (ask 1KqAXyXG, 2025-05-19) states a 180-day claim period; no Amazon page read supports it. [opinion]

**IN32.** A shipment can sit Delivered for some days before it reaches Checked-in, longer at peak; the lag is a stated maximum that Amazon may change (gs.amazon.cn article-250807-3, 2025-08, read 2026-11-13; value in *Values that move*). With a partnered carrier the shipment shows Shipped at pickup; with the seller's own carrier, once valid tracking is entered. [read in official docs]

**IN33.** The AWD terms set a filing window for fee claims on box dimensions, counted from the charge date (section 4.2). Source: AWD terms dated 2026-01-14, read 2026-11-13; value in *Values that move*. [read in official docs] fee-overcharges does not hold it as of 2026-11-13; it stays here until that file does.

**IN34.** The "MCF inventory reimbursement policy" that the AWD service terms name is the page https://supplychain.amazon.com/support/reimbursements, titled *Supply Chain Portal (SCP) Reimbursements policy - Amazon Supply Chain Services (ASCS)*: each of the five mentions in the terms is a hyperlink to that page. Its eligibility requires an MCF account "in Active state", and its windows, cap and valuation are its own, not the FBA policy's (as filing-and-conduct FL27 states). Sources: AWD terms dated 2026-01-14 (link targets read from the page's HTML, 2026-11-13); the SCP page read 2026-11-13. [read in official docs; links command-verified]

**IN35.** Amazon's UK policy redline of 2024-12-11 states that from 2025-01-09 the claim windows change "except for shipment to Amazon claims"; the UK shipment-to-Amazon window was not part of that change, and the page does not state its length. Source: `_PC__Kiwi_Comms_redlined_policy_UK_clean_version.pdf` (m.media-amazon.com, created 2024-12-11), read 2026-11-13. [read in official docs] Read at: `GEYPWTSQRTXXXMVB` on the UK host (script shell; unread here).

**IN36.** Amazon's EU redline set of 2024-08-20 changes the customer-return, fulfilment-centre-operations and removals pages and carries no Shipment to Amazon page, and Amazon's JP policy of 2025-02-19 names Shipment to Amazon claims with no window. No Amazon page read by a permitted route states the length of the inbound window for an EU store, the UK or JP; a UK staff post of 2025-06-06 says "File within 60 days" for lost or damaged inventory without naming a claim kind or a start, and a UK seller relayed a Seller Central refusal at "over 6 months since arrived" (2025-01-08). Sources: `EU_Policy_Redline.pdf` (created 2024-08-20); `redline_FBA_reimbursement_policy__EN_version.pdf` (G/09, created 2025-02-19); Spencer_Amazon, thread `e236599d-…` (store UK); thread `c3831651-…` (store UK); all read 2026-11-13. [read in official docs; the seller's relay: opinion] Read at: `GEYPWTSQRTXXXMVB` on the store's host, and the store's forum News.

**IN37.** Under the *Amazon Global Logistics Freight Service Terms* (dated 2026-01-14), Amazon assumes risk of loss "only from receipt at Origin until delivery at Destination", and Destination "means an Amazon facility". For China-origin ocean carriage the contracting party is Beijing Century Joyo Courier Co., Limited (BCJ), and claims go "exclusively against the Amazon Contracting Party (not the carrier)". For a sealed container Amazon could not count, with the seal intact on delivery, Amazon is "not liable for shortages or any damage … unless proximately caused by our independent action", and it is not liable for loss caused by inadequate packaging. Source: those terms, §§ preamble, 1.4, 3.5, 5.5, 10.3, 19, read 2026-11-13. [read in official docs] Read at: the terms as dated on supplychain.amazon.com, and the booking's bill of lading.

**IN38.** An AGL Freight loss or damage claim is a written notice to Amazon within a period counted from delivery, or from the scheduled delivery date for lost cargo; legal action has its own period from Amazon's written disallowance, and a credited amount the seller does not contest in writing within a stated period is a complete settlement. Recovery is limited per shipment for an ocean bill of lading to the US unless higher liability was agreed in writing at booking, otherwise by the applicable convention or the customs-declared value, whichever is less, with a cumulative cap per 12 months; the seller must prove negligence of Amazon, its contractor or the performing carrier, and must itself insure the cargo. Source: AGL Freight Service Terms §§ 7.7, 8, 10.1, 10.6, 10.8, 11.1, 11.3, read 2026-11-13; the periods and limits are in *Values that move*. [read in official docs] The billing clauses are the finance pack's (P-ful-29 to P-ful-31).

**IN39.** Amazon's FBA policy covers loss "at a facility or by a carrier operated by Amazon or on behalf of Amazon"; loss before delivery while the goods are with a carrier or forwarder the seller engaged is outside that sentence and is claimed under the seller's contract with that carrier. Amazon's Chinese article names forwarder, warehouse and customs counting errors and cartons broken in transit as causes of in-box shortfalls, and tells the seller to confirm with its dispatch staff and carrier before requesting research. Sources: US policy PDF (2024-12-18); gs.amazon.cn article-250807-3 (2025-08), read 2026-11-13. [read in official docs; the scope reading is inferred]

**IN40.** Practitioners describe first-mile recovery as a claim against the forwarder or airline under its contract: an exception written on the delivery document at receipt, a short written notice for hidden damage, weight-based convention limits unless the cargo was insured, and a document set of AWB or bill of lading, commercial invoice, packing list and photos (百运网, 2026-11-09); 深圳美辰物流 (AMZ123, 2023-10-27) tells a carrier problem from a warehouse problem by the tracking and negotiates the former with the forwarder. [opinion]

**IN41.** Amazon's Chinese pages name inbound evidence as 库存所有权证明 (a supplier invoice, another seller's receipt, or a manufacturer's signed 装箱单 with date, shipment or PO number, item names, quantity shipped and signature or stamp) and, for LTL/FTL, a 交货证明 that is the carrier's 提货单 "须经亚马逊盖章". Chinese practitioners instead name the forwarder's company-stamped 签收单 as the POD (百运网, 2026-05-27) and report that Amazon warehouses often do not stamp at receipt (AMZ123, 2024-05-12). Whether a forwarder-stamped 签收单 alone satisfies Amazon's LTL/FTL requirement is unread. Sources: gs.amazon.cn article-250305-3 (2025-03), article-250807-3 (2025-08) [read in official docs]; the practitioners [opinion].

### The seat's own (no source; enters no skill)

- A shortage on a shipment that is not yet `CLOSED` and whose eligibility date has not passed is not yet a claim. A shortage whose shipment reads "Investigation completed" has no claim route left in Seller Central.
- A skill that quotes a window quotes Amazon's statement for the store and its date, not a practitioner's figure (moved here from IN31 on verification: a discipline, not a fact).
- The join that finds an inbound claim is per shipment and SKU: `QuantityShipped` > `QuantityReceived` on a `CLOSED` shipment, with no `Lost_Inbound`/`Damaged_Inbound` row in the Reimbursements report for that shipment and FNSKU, and the window not past for the store.

---

## Open questions for a first run on a real account

1. Does the Reimbursements report carry the inbound shipment ID for `Lost_Inbound` / `Damaged_Inbound` rows (the documented columns do not include one), or only `case-id` and FNSKU? Which column ties a payment to a shipment?
2. In the ledger, is the Reference ID of a `Receipts` event the `shipmentConfirmationId` (`FBA…`)? Is the earliest `Receipts` date of a shipment ever earlier than Amazon's "verified delivery date"?
3. Are AWD → FBA replenishment shipments returned by v0 `getShipments` and v2024-03-20 `listInboundPlans` on the five roles, with `QuantityShipped` and `QuantityReceived`?
4. Does v0 `getShipments` still return shipments closed more than nine months ago, or is there a retention limit that cuts below the US window?
5. Does `GET_LEDGER_DETAIL_VIEW_DATA` show `CARRIER_DAMAGED` and `DISTRIBUTOR_DAMAGED` as dispositions, with what exact spelling?
6. What window does Seller Central enforce today for the UK, DE, FR, IT, ES and JP stores? Amazon's redlines show only that the 2025 changes left it out (IN35, IN36). A UK seller relayed "over 6 months"; practitioners say six months for the EU; a gs.amazon.cn search summary said "欧洲站为六个月" but no page carrying it was found. Settles by: `GEYPWTSQRTXXXMVB` as each store's host shows it, read by a route the office allows, or a store's News post.
7. Does `GEYPWTSQRTXXXMVB`, as the US store shows it today, still read "nine months after the verified date of a shipment delivery", and does it state the one-claim-per-shipment rule? It was not readable here (script shell).
8. (narrowed 2026-11-13) The "estimated proceeds" sentence is struck in the rendered PDFs (IN21), so the policy text gives Amazon's own cost estimate when no sourcing cost was entered. Does a 2026 US `Lost_Inbound` line on a live account match that estimate (value-and-reversals' question for every pre-order kind)?
9. Is there a US-forum thread for the commingling announcement, and does its text differ from the UK and Canada posts?
10. A web roundup (news.seonib.com, 2026-09-05) says Amazon changed the FBA reimbursement policy in "late May 2026". It cites a press article that could not be found, and no Amazon post was located before the search budget ran out. Did Amazon post any 2026 change to the shipment-to-Amazon claim?
11. For a partnered LTL (Amazon Freight) shortage, where does the seller get an Amazon-stamped POD? Does `getBillOfLading` carry the PRO number?
12. For an AGL shipment, where is a loss between "delivery at Destination" under the AGL Freight terms and the FBA receiving count handled: as an AGL Freight claim or as a Shipment to Amazon research? The Seller Central AGL help page (`GR384ESWC8HH8667`) and *Amazon Global Logistics Freight Terms and related Program Policies* (`G5N72FX7B37YJ3AT`) are script shells. Where is the gs.amazon.cn article that says AGL proofs of delivery download from Shipper Central from 2024-04-01?
13. Does Amazon accept a forwarder-stamped 签收单, without an Amazon stamp, as the LTL/FTL proof of delivery for an inbound claim? Settles by: a staff reply on the US or a Chinese-language forum thread, or a first claim on a live account.
14. Does Amazon accept a Chinese-language supplier invoice, a 1688 order receipt or a 发票 (fapiao) as proof of ownership for an inbound claim, and a buyer entity other than the selling account (for example a Hong Kong or mainland company buying for a US LLC)? No page read says. The MYSC side is value-and-reversals' (VR13).
15. Are the Seller Central inbound pages for JP (`GEYPWTSQRTXXXMVB` on `.co.jp`) and Japanese practitioners (FBA補填 blogs) consistent with the US rule? None was read; the search budget ran out.

## Unread pages

- *FBA inventory reimbursement policy: Shipment to Amazon claims*, `GEYPWTSQRTXXXMVB` (`.com`). Script shell. Text reached via gs.amazon.cn (2025-03, 2025-08), a seller's quotation (2024-09-26), Hopted's copy (undated), and the SCP twin.
- *Reconcile your shipment* / *Missing inbound FBA inventory*, `201214140` / `G201214140` (`.com`, `.co.uk`). Script shell. Text reached via gs.amazon.cn and staff posts.
- *FBA inventory reimbursement policy*, `G200213130`. Script shell. Text reached via the US and DE PDFs.
- *Claims and reimbursements through Amazon Global Logistics*, `GR384ESWC8HH8667`. Script shell. Search summary only. The freight claim side is read on the public *AGL Freight Service Terms* instead (section K).
- *Amazon Global Logistics Freight Terms and related Program Policies*, `G5N72FX7B37YJ3AT`. Help page; not fetched (script shell expected).
- The help hub's content call for any of these pages: not used; the office closed that route on 2026-11-10.
- Helium 10 KB *FAQs for Managed Refund Service* (403). Search snippet only.
- 知乎 p/719529228 and p/443601737 (403). Not used.
- sellermetrics.app (bot wall). Not used.
- (read 2026-11-13; moved to *Pages read*) The UK redlined policy PDFs and the Chinese US PDF.
- A JP redline under the G/01 name `Redlined_FBA_Reimbursement_policy_JP.pdf` returns 404; the JP policy is read at its G/09 address.
- The gs.amazon.cn article that a search summary said gives "欧洲站为六个月"; not located.
- A forwarder's compensation terms (per kilogram, 60-day notice) seen in a search summary only.

## Values that move

Each value differs by store, programme or date. Positions state the rule and where it is read; the value sits here.

| Value | Store / programme | Figure as read | Date of the statement | Read on | Source |
|---|---|---|---|---|---|
| Inbound (shipment to Amazon) claim window | US FBA | within 9 months; after the shipment is closed or finalized | 2026-08-13 | 2026-11-13 | Indy_Amazon, thread `0e07abc1-…` |
| Inbound claim window | US FBA | "9个月" / "九个月" after delivery to the FC | 2025-03; 2025-08 | 2026-11-13 | gs.amazon.cn article-250305-3; article-250807-3 |
| Inbound claim window | US FBA | nine months after the verified delivery date (help page as a seller quoted it) | 2024-09-26 | 2026-11-13 | thread `2b32f5d5-…` (store US) |
| Inbound claim window | UAE, Saudi Arabia, Egypt FBA | no sooner than 15 and no later than 60 calendar days from the shipment delivery date; effective 2024-09-05 | 2024-08-06 | 2026-11-13 | News_Amazon `96a05f4a-…`, `c6da88ce-…`, `e62a8ace-…` |
| Inbound claim window | UK FBA | not stated; excluded from the 2025-01-09 change to 60 days | 2024-12-11 | 2026-11-13 | UK redline PDF |
| Generic lost/damaged filing limit (claim kind not named) | UK FBA | "File within 60 days" | 2025-06-06 | 2026-11-13 | Spencer_Amazon, `e236599d-…` |
| Inbound claim window | EU stores, JP | not stated on any Amazon page read | — | 2026-11-13 | EU redline 2024-08-20; JP policy 2025-02-19 |
| Shipment-to-Amazon window | Supply Chain Portal (MCF), and AWD by reference | nine months after verified delivery | page © 2026; AWD terms 2026-01-14 | 2026-11-13 | supplychain.amazon.com/support/reimbursements |
| Per-unit cap | Supply Chain Portal (MCF) and AWD | $300.00; fallback 40% of the retail price (valuation) or of the estimated sale price (shipment proof of cost) | © 2026 | 2026-11-13 | same page |
| Valuation dispute window | Supply Chain Portal (MCF) | 90 days after the reimbursement, via SCP Contact Us | © 2026 | 2026-11-13 | same page |
| Per-unit cap | FBA, by store | US $5,000; CA CAD 5,000; UK £2,000; DE, FR, IT, ES €2,000; JP 675,000 JPY | US 2024-12-18 and 2025-02-24; others 2025-02-24; JP 2025-02-19 | 2026-11-13 | policy PDFs (home: value-and-reversals VR29) |
| AWD box-dimension fee claim window | AWD (US) | within 90 days of the date the fee was charged | 2026-01-14 | 2026-11-13 | AWD service terms § 4.2 |
| `CLOSED` timeout from creation | US FBA | 45 days domestic / 75 days international | modified 2025-10-03 | 2026-11-13 | sell.amazon.com tracking guide |
| `CLOSED` timeout from creation | (store not named) | 90 days | 2025-08; 2023-10-10 | 2026-11-13 | gs.amazon.cn article-250807-3; TaylorR_Amazon |
| Delivered → Checked-in lag | US FBA (Chinese page) | up to 10 days, longer at peak | 2025-08 | 2026-11-13 | gs.amazon.cn article-250807-3 |
| Research duration (staff range) | US FBA | 2 to 30 days, up to 60; 2 to 60 days | 2025-11-14; 2024-09-05 | 2026-11-13 | Christine_Amazon; Bryce_Amazon (home: filing-and-conduct FL30) |
| Reply to an Action required request | US FBA | within five business days | modified 2025-10-03 | 2026-11-13 | sell.amazon.com tracking guide |
| AGL Freight claim notice | AGL Freight | in writing within nine (9) months from date of delivery, or scheduled delivery for lost cargo | 2026-01-14 | 2026-11-13 | AGL Freight Service Terms § 11.1 |
| AGL legal action | AGL Freight | within one (1) year of the written disallowance | 2026-01-14 | 2026-11-13 | § 11.1 |
| AGL contest of a credited amount | AGL Freight | thirty (30) days from the decision | 2026-01-14 | 2026-11-13 | § 11.3 |
| AGL liability, ocean bill of lading to the US | AGL Freight | 500 USD per shipment unless higher liability agreed in writing at booking | 2026-01-14 | 2026-11-13 | § 10.1 |
| AGL liability as warehouseman / cross-dock | AGL Freight | $0.25 per pound unless greater liability agreed | 2026-01-14 | 2026-11-13 | § 7.7 |
| AGL cumulative cap | AGL Freight | no more than 80,000 USD in any 12-month period | 2026-01-14 | 2026-11-13 | § 10.8 |
| AGL overcharge notice | AGL Freight | 180 days of receipt of the invoice (home: finance P-ful-31) | 2026-01-14 | 2026-11-13 | § 11.2 |

## Corrections to other packs

1. **Finance P-ref-13 and P-ref-16 (store of each News post).** P-ref-13 says of 6605eede and d0fc997e that "no page says which store each addresses". Each thread's own `marketplaceId` does: `6605eede-…` is Canada (`A2EUQ1WTGCTBG2`), `d0fc997e-…` is the UK (`A1F83G8C2ARO7P`), `81c3235d-…` is the US, `1101821c-…` is Sweden (`A2NODRKZP88ZB9`), `d8f9a56c-…` is Australia; the field follows the thread, not the host, by the control check in *How to read this file*. The pack's post-to-store table is fc-lost-damaged's; this is this file's evidence for it. Owner after publication: the finance pack's reimbursement reference, pointing to the claims pack's table.
2. **Stock I21 / `shortages.md` (UK automation), and finance P-ref-13.** The stock pack says proactive reimbursement covers fulfilment-centre losses in the UK from 2025-01-15; finance P-ref-13 says Amazon reimburses most warehouse-lost cases without a claim, naming no store. Amazon's UK staff post of 2026-04-06 (`2f44617d-…`, store UK) says UK warehouse-lost claims "Currently [require] manual claim submission (automatic reimbursement disabled since August 2022)". The two Amazon statements contradict each other; neither can be stated alone for the UK (see fc-lost-damaged FC5).
3. **Stock I21 / `shortages.md` (the 2024-08-06 post).** They say the 15-to-60-day post "was issued on the UAE forum". It was issued as three threads, for the UAE, Saudi Arabia and Egypt (IN8).
4. **Stock I21 (Supply Chain page).** I21's correction of 2026-11-10 (the page is MCF's, not an FBA home) stands. Add: the AWD terms link their "MCF inventory reimbursement policy" to that page, so it is also the AWD claim rule (IN26, IN34).
5. **This file's earlier note "corrects the finance pack's 'SCP/AWD' label".** On re-reading the finance pack on 2026-11-13 no "SCP/AWD" label was found in it; that correction is withdrawn.

## Pages read

| Title | Address | Publisher | Page date | Read on | Used for |
|---|---|---|---|---|---|
| FBA inventory reimbursement policy (US redlined PDF) | https://m.media-amazon.com/images/G/01/rainier/help./PC__Kiwi_Comms_redlined_policy_US_clean.pdf | Amazon | created 2024-12-18 | 2026-11-13 (US page 3 rendered in the revision) | A, G, IN1, IN21, values |
| FBA lost and damaged inventory reimbursement policy (DE redlined PDF) | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_DE.pdf | Amazon | created 2025-02-24 | 2026-11-13 (US page 3 rendered in the revision) | A, G, IN1, IN21, values |
| Supply Chain Portal (SCP) Reimbursements policy | https://supplychain.amazon.com/support/reimbursements | Amazon Supply Chain Services | none (© 2026) | 2026-11-13 (re-read) | B, D, G, J, IN5, IN15, IN26, IN34, values |
| Amazon Warehousing and Distribution service terms | https://supplychain.amazon.com/legal/service-terms/warehouse-and-distribution | Amazon | "Dated: January 14, 2026" | 2026-11-13 (re-read; link targets parsed from the HTML) | B, J, IN26, IN33, IN34 |
| 你最关心的亚马逊库存管理问题，这次全解决！ (article-250305-3) | https://gs.amazon.cn/zhishi/article-250305-3 | Amazon 全球开店 | 2025-03 | 2026-11-13 | B, C, D, IN7, IN11, IN12, IN16 |
| 亚马逊FBA货件状态怎么查？丢件能不能赔偿？一次讲清 (article-250807-3) | https://gs.amazon.cn/zhishi/article-250807-3 | Amazon 全球开店 | 2025-08 | 2026-11-13 | B, C, E, H, IN7, IN14, IN18, IN32 |
| 🆘FBA Lost Your Inventory? Steps to File a Reimbursement Claim (Indy_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/0e07abc1-9026-4540-a005-153d9e78bf04 | Amazon Seller Forums (US) | 2026-08-13 | 2026-11-13 | B, D, G, IN7, IN15 |
| Update on reimbursement claim window eligibility on FBA (UAE) | https://sellercentral.amazon.com/seller-forums/discussions/t/96a05f4a-537a-49d2-a918-703c47716bc0 | News_Amazon (UAE) | 2024-08-06 | 2026-11-13 | B, IN8 |
| Update on reimbursement claim window eligibility on FBA (Saudi Arabia) | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/c6da88ce-b14f-4ae1-95a5-1c6482b5c565 | News_Amazon (Saudi Arabia) | 2024-08-06 | 2026-11-13 | B, IN8 |
| Update on reimbursement claim window eligibility on FBA (Egypt) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/e62a8ace-3875-433c-8ef1-bb27a29b17c4 | News_Amazon (Egypt) | 2024-08-06 | 2026-11-13 | B, IN8 |
| Update on Reimbursement Automation and Eligibility Window (US) | https://sellercentral.amazon.com/seller-forums/discussions/t/81c3235d-4c44-47ba-96c5-883cecab3244 | News_Amazon (US) | 2024-07-24 | 2026-11-13 | IN9; store check |
| Update on Reimbursement Automation and Eligibility Window (Canada) | https://sellercentral.amazon.com/seller-forums/discussions/t/6605eede-df8e-4498-803f-cb612d95d7ce | News_Amazon (Canada) | 2024-07-24 | 2026-11-13 | IN9; correction to finance P-ref-13 |
| Update on Reimbursement Automation and Eligibility Window (UK) | https://sellercentral.amazon.com/seller-forums/discussions/t/d0fc997e-de50-4100-9803-76b7993b66df | News_Amazon (UK) | 2024-10-10 | 2026-11-13 | IN9; correction to finance P-ref-13 |
| Update on eligibility window to file reimbursement claims (UK) | https://sellercentral.amazon.com/seller-forums/discussions/t/9a92846d-41f8-4ad7-b59a-f946efdcc2b4 | News_Amazon (UK) | 2025-01-15 | 2026-11-13 | IN9 |
| Update to the FBA lost and damage inventory reimbursement policy (UK) | https://sellercentral.amazon.com/seller-forums/discussions/t/a941ac02-d389-409a-9d62-00ab9db5bc4a | News_Amazon (UK) | 2024-12-18 | 2026-11-13 | store check only |
| Temporary peak season extensions for international FBA shipments | https://sellercentral.amazon.com/seller-forums/discussions/t/f25ba535-e06e-4fa3-8bb0-cb3a095fd696 | News_Amazon (US) | 2026-10-30 | 2026-11-13 | store check (stock I9) |
| Clarification on the claim window… shipment to Amazon | https://sellercentral.amazon.com/seller-forums/discussions/t/2b32f5d5-28e2-4445-8318-17793237a735 | Seller Forums (US) | 2024-09-26 | 2026-11-13 | B, IN7 |
| FC Transfer shipping question & Inventory over-count (Angie_Amazon reply) | https://sellercentral.amazon.com/seller-forums/discussions/t/ecbb2ef1-398c-4686-9e80-89b28eb383c9 | Seller Forums (US) | 2026-04-03 | 2026-11-13 | C, F, IN11 |
| How to Resolve FBA Shipment Discrepancies (Christine_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/83caf79b-4ca1-4e1c-9564-9f328739e0f7 | Seller Forums (US) | 2025-11-14 | 2026-11-13 | C, F, IN13, IN19 |
| Mastering Shipment Reconciliation (Bryce_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/e0a6f096-f8a0-4d4d-8fbe-2b65b05b5e8f | Seller Forums (US) | 2024-09-05 | 2026-11-13 | C, IN13 |
| What to do if you have a lost or delayed FBA Shipment (TaylorR_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/0c8e8239-9cd4-444f-9253-673a487b0039 | Seller Forums (US) | 2023-10-10 | 2026-11-13 | C, D, E, IN14 |
| Investigation completed – shipment contents counted and confirmed // How to appeal (Julia_Amzn) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/25ab2e15-8c9b-4ead-82d4-75a35ffd719a | Seller Forums (UK) | 2024-08-16 | 2026-11-13 | C, IN12 |
| How to get reimbursed for inbound SPD shipment that was destroyed by UPS? (TaylorR_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/10816b8f-963d-4d07-a4e2-9480206f9c22 | Seller Forums (US) | 2024-11-12 | 2026-11-13 | E, IN3 |
| Does Amazon reimburse for items that their partnered carrier loses? | https://sellercentral.amazon.com/seller-forums/discussions/t/0fc75622-4221-4548-9254-977d5f034aeb | Seller Forums (US) | 2023-08-07 | 2026-11-13 | A, E, IN3, IN4 |
| CHANGING FROM WAREHOUSE TO DISTRIBUTER DAMAGE (NR_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/0d6e8a48-4095-4e90-bf84-7bb3a88a9fbc | Seller Forums (US) | 2025-03-19 | 2026-11-13 | A, IN2 |
| Amazon Delaying Reimbursement for Carrier-Damaged Inventory… | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/30b0589d-36ad-47ef-a280-c481fd59551d | Seller Forums (France) | 2025-03-17 | 2026-11-13 | E |
| Amazon Prep Service (Jameson_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/5c63f045-b956-447b-9e6d-410b1e2a05bb | Seller Forums (US) | 2025-11-25 | 2026-11-13 | H, IN23 |
| Commingling practices will end effective March 31, 2026 (UK) | https://sellercentral.amazon.com/seller-forums/discussions/t/06778c12-539e-478a-8f67-00592c4c5cca | News_Amazon (UK) | 2025-12-08 | 2026-11-13 | I, IN24 |
| Commingling practices will end effective March 31, 2026 (Canada) | https://sellercentral.amazon.ca/seller-forums/discussions/t/cd352647-7a0d-426f-83e7-e3dd4add6c5c | News_Amazon (Canada) | 2025-12-08 | 2026-11-13 | I, IN24 (store and date only) |
| Is there a documented process to reconcile… AWD (Topher_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/f72ae6d7-9041-444c-9605-c4a5ebdaea7f | Seller Forums (US) | 2025-01-17 | 2026-11-13 | J |
| AWD to FBA automated shipment discrepancy (KJ_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/2c97b436-bc0f-41bc-8246-c4509716d7a8 | Seller Forums (US) | 2025-02-11 | 2026-11-13 | D, J, IN28 |
| AWD to FBA units not received – Reimbursement error (Topher_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/ed108c90-2629-4708-b43d-447507f70fcb | Seller Forums (US) | 2024-10-14 | 2026-11-13 | J |
| AWD delivery issues? (Topher_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/8ebecbc9-a4e5-4619-b631-8c9b6d227f58 | Seller Forums (US) | 2024-08-06 | 2026-11-13 | J (context) |
| Amazon FBA Shortage Overage Reimbursement Policy | https://sellercentral.amazon.com/seller-forums/discussions/t/a6ed7c414c1dc77c9c37a29068557802 | Seller Forums (US) | 2018-03-29 | 2026-11-13 | F, IN19 |
| Missing Shipment to FBA | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/c3831651-3056-4bf9-87e7-e51f40bd43d0 | Seller Forums (UK) | 2025-01-08 | 2026-11-13 | B |
| Reimbursement for Lost Items Lower Than Before | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/b84f90fe-4751-4cd4-b338-a268d22322fc | Seller Forums (UK) | not shown | 2026-11-13 | checked; no inbound content |
| How to track FBA shipments | https://sell.amazon.com/blog/fba-shipment-tracking | sell.amazon.com | "Jan 7, 2025" (stock read modified 2025-10-03) | 2026-11-13 | C, IN14 |
| FBA inventory reimbursement policy (US redline, regenerated) | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_US.pdf | Amazon | created 2025-02-24 | 2026-11-13 (page 2 rendered) | G, IN21 |
| FBA lost and damaged inventory reimbursement policy (UK redline) | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_UK.pdf | Amazon | created 2025-02-24 | 2026-11-13 (text layer) | values (cap) |
| FBA lost and damaged inventory reimbursement policy (UK, first draft) | https://m.media-amazon.com/images/G/01/rainier/help./_PC__Kiwi_Comms_redlined_policy_UK_clean_version.pdf | Amazon | created 2024-12-11 | 2026-11-13 | B, IN35 |
| FBA inventory reimbursement policy (CA, FR, IT, ES redlines) | https://m.media-amazon.com/images/G/01/rainier/help./Redlined_FBA_Reimbursement_policy_CA.pdf (…_FR, …_IT, …_ES) | Amazon | created 2025-02-24 | 2026-11-13 (text layer) | values (cap); no inbound window in any |
| 亚马逊物流库存赔偿政策 (US, Chinese redline) | https://m.media-amazon.com/images/G/01/rainier/help./PC__Kiwi_Comms_redlined_policy_US_clean-zh_cn.pdf | Amazon | created 2024-12-20 | 2026-11-13 (text layer) | values (cap $5,000) |
| FBA lost and damaged inventory reimbursement policy (JP, English) | https://m.media-amazon.com/images/G/09/rainier/help/redline_FBA_reimbursement_policy__EN_version.pdf | Amazon | "as of 02/19"; created 2025-02-19 | 2026-11-13 (page 3 rendered) | B, G, IN21, IN36, values |
| EU policy redline (customer returns, FC operations, removals pages) | https://m.media-amazon.com/images/G/02/rainier/help/EU_Policy_Redline.pdf | Amazon | created 2024-08-20 | 2026-11-13 | B, IN36 |
| Amazon Global Logistics Freight Service Terms | https://supplychain.amazon.com/legal/service-terms/global-logistics-freight | Amazon Supply Chain Services | "Dated: January 14, 2026" | 2026-11-13 (plain GET, full text) | K, M, IN37, IN38, values |
| FBA Inventory Protection: Amazon's Lost & Damaged Policies (Spencer_Amazon) | https://sellercentral.amazon.co.uk/seller-forums/discussions/t/e236599d-210d-455f-a601-5dbee8fc95c7 | Seller Forums (UK) | 2025-06-06 | 2026-11-13 | B, IN36 |
| [April FBA Series] UK Reimbursement Claims Explained (Jameson_Amazon) | https://sellercentral.amazon.com/seller-forums/discussions/t/2f44617d-9e1c-413e-94b0-d427524ceb82 | Seller Forums (UK) | 2026-04-06 | 2026-11-13 | store control check; correction 2 |
| Update on eligibility window (Sweden) | https://sellercentral.amazon.com/seller-forums/discussions/t/1101821c-7ff1-495a-b8a5-71ff01e3afc3 | News_Amazon (Sweden) | 2025-01-15 | 2026-11-13 | B, IN9 (store) |
| FBA receiving short (US seller; fetched from the .co.jp host) | https://sellercentral.amazon.co.jp/seller-forums/discussions/t/3354bdd4-022e-4667-b5cc-f7cd6fd46cc6 | Seller Forums (US) | 2024-02-29 | 2026-11-13 | store control check |
| Missing FBA items | https://sellercentral-europe.amazon.com/seller-forums/discussions/t/1e2113b5-735e-4b38-ad70-7e10b993af0a | Seller Forums (UK) | 2025-03-05 | 2026-11-13 | checked; no window |
| 我的货件上架了，为什么还不可售？ (news-brand-230829) | https://gs.amazon.cn/news/news-brand-230829 | Amazon 全球开店 | — | 2026-11-13 (302 to globalselling.amazon.com; no article body) | open question 6 |
| 国际空运货物破损怎么索赔（签收前要拍哪些证据） | https://m.by56.com/news/64618.html | 百运网 | 2026-11-09 | 2026-11-13 | M, IN40 |
| 亚马逊签收单 (ask 7xKCTk0F) | https://www.amz123.com/ask/7xKCTk0F | AMZ123 (aggregated Q&A) | 2024-05-12 | 2026-11-13 | D(d), IN41 |
| 亚马逊卡派进仓丢件 (ask 1KqAXyXG) | https://www.amz123.com/ask/1KqAXyXG | AMZ123 (aggregated Q&A) | 2025-05-19 | 2026-11-13 | B, D(d), IN31 |
| fba仓库丢件怎么处理 (ask 02AvE5QA) | https://www.amz123.com/ask/02AvE5QA | AMZ123 (aggregated Q&A) | 2024-11-02 | 2026-11-13 | D(d), M |
| 亚马逊FBA货运代理：2026完整指南 | https://suaidglobal.com/zh-cn/insights/amazon-fba-freight-forwarder/ | Suaid Global | 2026-04-18 | 2026-11-13 | checked; no compensation terms |
| Fulfillment Inbound API models v0 and v2024-03-20 | github amzn/selling-partner-api-models, `models/fulfillment-inbound-api-model/` at `db2936aa` | Amazon | 2026-10-29 (commit) | 2026-11-13 | B, D, L, IN6, IN10, IN14 (and `ShippingConfiguration`, `Carrier`, `FreightInformation` for L and M) |
| AWD API model v2024-05-09 | same repository, `models/amazon-warehousing-and-distribution-model/` at `db2936aa` | Amazon | 2026-10-29 (commit) | 2026-11-13 | J, IN27 |
| Track an inbound shipment with expected and received SKU details | https://developer-docs.amazon/sp-api/docs/track-an-inbound-shipment-with-sku-details.md | Amazon SP-API docs | updatedAt 2026-09-09 | 2026-11-13 | J, IN27 |
| SP-API Release Notes | https://developer-docs.amazon/sp-api/docs/sp-api-release-notes.md | Amazon SP-API docs | rolling | 2026-11-13 | J (`skuQuantities`, `replenishmentQuantity`) |
| SP-API Deprecation Schedule | https://developer-docs.amazon/sp-api/docs/sp-api-deprecations.md | Amazon SP-API docs | updatedAt 2026-09-09 | 2026-11-13 | L (pointer to SU42) |
| FBA Reports (report type values) | https://developer-docs.amazon/sp-api/docs/report-type-values-fba.md | Amazon SP-API docs | updatedAt 2026-10-13 | 2026-11-13 | L |
| SP-API roles table (survey extract of Role Mappings for operations and report types) | the survey's roles extract (not a public page) | Amazon (extracted by the survey) | 2026-11-09 | 2026-11-13 | L, roles |
| Amazon FBA Inventory Reimbursement Policy (copy) | https://www.hopted.com/integrations/amazon-sp-api/amazon-help-articles/fba-inventory-reimbursement-policy | Hopted | undated (© 2026) | 2026-11-13 | D, IN5, IN17 (FBA wording via third party) |
| FBA 入仓 "数量差异"：Receiving 状态如何快速索赔 | https://m.by56.com/news/59431.html | 百运网 | 2026-05-27 | 2026-11-13 | B, D, F, IN31 |
| 亚马逊FBA货件丢失，卖家如何进行索赔？ | https://www.amz123.com/t/0JE2nztt | AMZ123 / 深圳美辰物流 | 2023-10-27 | 2026-11-13 | A, D, IN31 |
| 亚马逊FBA货物损坏或丢失怎么办？ | https://www.amz123.com/ask/2pxdwDvH | AMZ123 | 2024-10-31 | 2026-11-13 | D (context) |
| 优麦云 索赔助手使用指南 | https://www.sellerspace.com/help/doc/claim-indemnity-assistant-use-guide | 优麦云 SellerSpace | 2024-06-05 | 2026-11-13 | claim rule as a tool reads it (declared ≠ received on a completed shipment); cited in finance pack too |
| Amazon lost inbound claims Guide 2026 | https://www.refunzo.com/blog/amazon-lost-inbound-claims-guide-2026/ | Refunzo (Jimi Patel) | 2026-01-18 | 2026-11-13 | B, IN31 |
| How to Build a Timeline for Disputing Inbound Receiving Shortages | https://marketplacevalet.com/how-to-build-a-timeline-for-disputing-inbound-receiving-shortages/ | Marketplace Valet (Justin W. Boggs) | updated 2026-10-24 | 2026-11-13 | B, D |
| Amazon Received More Than You Shipped: FBA Overages | https://www.prepvia.com/blogs/amazon-fba-overage-received-more-than-shipped | PrepVia (Bernardo Campelo) | 2026-08-25 (modified 2026-10-17) | 2026-11-13 | C, F, IN20 |
| Amazon ends FBA commingling on March 31 | https://ppc.land/amazon-ends-fba-commingling-on-march-31-what-really-changes-for-sellers/ | PPC Land | 2026-03-24 | 2026-11-13 | I, IN25 |
| Sending FBA goods to Amazon… | https://www.sellerlogic.com/en/blog/sending-fba-goods-to-amazon-how-to-ensure-your-inbound-shipment-arrives-safely-at-the-warehouse/ | SELLERLOGIC (Robin Bals) | 2022-04-26, updated 2025-08-29 | 2026-11-13 | B (no six-month text on this page) |
| Amazon FBA 2026: 5 Policy Changes… | https://news.seonib.com/articles/2026-09-05/amazon-fba-2026-5-policy-changes-reshaping-seller-profitabil.html | seonib | 2026-09-05 | 2026-11-13 | open question 10 |
| FAQs for Managed Refund Service | https://kb.helium10.com/hc/en-us/articles/30482681645339 | Helium 10 | unknown | 2026-11-13 (403; snippet) | B, IN31 |
| Claims and reimbursements through Amazon Global Logistics | https://sellercentral.amazon.com/gp/help/external/GR384ESWC8HH8667 | Amazon | unknown | 2026-11-13 (shell; snippet) | K |
| FBA inventory reimbursement: Shipment to Amazon claims | https://sellercentral.amazon.com/help/hub/reference/external/GEYPWTSQRTXXXMVB | Amazon | unknown | 2026-11-13 (shell) | B (unread) |
| Reconcile your shipment / Missing inbound FBA inventory | https://sellercentral.amazon.com/help/hub/reference/external/G201214140 | Amazon | unknown | 2026-11-13 (shell) | C (unread) |

## Verification (2026-11-13)

An adversarial pass re-opened the sources behind the positions on 2026-11-13. Public pages only; no SP-API call, no login, no seller data.

**What was checked (36 positions or load-bearing facts), and the verdict:**
- *Confirmed from the source:* the policy's opening sentence and the "exact items and quantities" condition in both PDFs, and the cancelled/deleted condition in the US PDF only (IN1; PDF metadata creation dates 2024-12-18 and 2025-02-24); the manufacturing/sourcing-cost clause with replenishment, and the "estimated proceeds" sentence in both PDFs (IN21); the caps $5,000 / €2,000 and the SCP $300, unit-first and 40% text (IN22); the NR_Amazon quote (IN2); the 2023-08-07 Seller Support email and the UPS relay (IN4); TaylorR_Amazon's "file a claim with Amazon directly" (IN3); the SCP evidence list, tracking sentence, Contents-tab sentence and one-claim note, and the same sentences in Hopted's copy (IN5, IN15, IN17); the `trackingNumberValidationStatus` text and enum (IN6); Indy_Amazon's "within 9 months", "closed/finalized", Reconcile path and "filing prematurely" (IN7, C); both gs.amazon.cn articles' nine-month, US-only, eligibility-date, "Investigation completed", format, pro forma, price-hiding, no-effect-on-stock, item-page and 10-day text, and their "发布时间" notes 2025-03 and 2025-08 (IN7, IN11, IN12, IN16, IN18, IN32); the store of all three 2024-08-06 threads and their 15/60-day text (IN8); the US, Canada and two UK News posts, which name no shipment-to-Amazon window (IN9); the date fields of both Fulfillment Inbound models (IN10); Julia_Amzn's, Angie_Amazon's, Christine_Amazon's and Bryce_Amazon's quotes (IN11–IN13, IN19); sell.amazon.com's 45/75-day `CLOSED`, Action required and five-business-day text, `datePublished` 2025-01-07, `dateModified` 2025-10-03 (IN14); the v0 `CLOSED` description (IN14); KJ_Amazon's ownership list (IN15, IN28); Jameson_Amazon's prep-exclusion text (IN23); the commingling post's body and the UK and Canada stores (IN24); PPC Land's sentences (IN25); AWD terms sections 4.1–4.3 (IN26, IN33); the AWD model's fields, statuses and units, and the tutorial's no-AWD-reports sentence (IN27); the deprecation dates of the two removed reports (IN30); Refunzo's 60–90 days (IN31); the `COMMINGLING` program and reason codes `FBA_INB_0342` / `FBA_INB_0465` in the inbound-eligibility model; the `GET_FBA_REIMBURSEMENTS_DATA` columns (no inbound shipment ID column, per the FBA report-type page, updatedAt 2026-10-13).
- *Upstream models:* `amzn/selling-partner-api-models` `main` has one commit after `db2936aa` (`b13d1d10`, 2026-11-11, Analytics Economics schema only); no Fulfillment Inbound, AWD or Support model changed.

**What changed:**
- IN29, IN13, section C, section L and the opening paragraph: corrected. Submitting a research request creates a Selling Partner Support case (sell.amazon.com guide; Bryce_Amazon 2024-09-05; TaylorR_Amazon 2023-10-10), and the Support API v2025-02-01 (`listCases`, `getCase`, `listContacts`; restricted Selling Partner Support role, outside the five) reads that case's status, `resolvedDate` and messages. The earlier "no operation exposes the research outcome" was too broad; no operation creates or answers a case.
- Opening paragraph: "inbound loss is the one large kind of FBA loss that automatic reimbursement does not cover" corrected: the US, Canada and UK proactive-reimbursement posts also leave removal claims manual.
- IN3: "Amazon is the shipper of record, and the seller cannot claim from the partnered carrier" downgraded from an Amazon statement to the seller's and UPS's words [opinion]; the staff reply only says to file with Amazon.
- IN31: AMZ123 / 深圳美辰物流 does not give 18 months for inbound; its 18 months is for fulfilment-centre operations claims. Removed from the inbound list.
- Staff reply dates corrected, where the file had given the thread's date as the reply's: NR_Amazon 2025-04-11, TaylorR_Amazon (`10816b8f`) 2024-11-29 and (`0fc75622`) 2023-08-10, Julia_Amzn 2024-08-20, Angie_Amazon 2026-04-09, KJ_Amazon 2025-02-13, Topher_Amazon (`f72ae6d7`) 2025-01-21, Jameson_Amazon 2025-12-01.
- IN23: the boundary day ("on or after") marked as this seat's reading of "created before January 1"; "when that inventory goes through FBA" added to the scope.
- IN14: the dating of the 90-day and 45/75-day timeouts marked as stock I9's, not re-read; the same 2025-08 Chinese page uses 45/75 days for the inbound defect fee.
- IN10 / section B: added `dates.readyToShipWindow` (v2024-03-20) and v0 `InboundShipmentItem.ReleaseDate` to the date list. Neither is a delivery date, so IN10 stands.
- IN17: Indy_Amazon's "One claim per shipment or event" added as an Amazon-staff FBA source beside Hopted's copy.
- IN19 / section C: the shortage options "Units not shipped" and "Research missing units" added as the staff posts name them.
- Moving values: IN7, IN8, IN14, IN26, IN32, IN33, section B's "Into a skill" and the opening paragraph now state the rule and where it is read, and keep nine months, 15/60 days, 45/75/90 days, 10 days and 90 days as dated evidence. IN13's research duration is restated as a staff range, not a rule.
- Forbidden positions: IN31's "A skill quoting a window quotes Amazon's statement" moved to the seat's own list; IN20's "a seller cannot reconcile on a net figure" rewritten as a fact (per-SKU lines, no Amazon netting rule) plus PrepVia's advice tagged opinion; "fact or discipline" in the Positions header changed to "fact". Section D's "validated tracking IDs" restated, because Amazon's words are "active tracking ID" and no page ties the claim to the API's `VALIDATED` status.

**Remaining doubts:**
- The FBA help page `GEYPWTSQRTXXXMVB` is still a script shell. The US nine-month value rests on staff posts, Amazon's Chinese restatements and a third-party copy, not on the page itself.
- Whether a reconciliation case's Support API `subject` or messages name the shipment ID and the per-unit outcome is unread (no account); the Support API's role is restricted and outside the five.
- The Australia News post (`d8f9a56c-…`, 2025-08-14) was not re-opened in this pass; IN9 relies on the original read for it.
- Practitioner snippets (Helium 10, SELLERLOGIC, GETIDA, TForce thread) were not re-opened. They are tagged opinion and carry no position on their own.
- The stock and finance pack IDs cited (I8, I9, I19, I21–I23, P-ref-12 to P-ref-16) were not re-verified here.
- Staff "thread posted" dates were read from the first post's `createdAt` in the page JSON (UTC); a reply's own date is its post's `createdAt`.

## Revision (2026-11-13)

A revision after the completeness critic's first round. Routes: plain GET of public pages (Seller Forums threads, gs.amazon.cn, supplychain.amazon.com, m.media-amazon.com PDFs, third-party sites) and grep of the model clone at `db2936aa`. No POST to any Amazon host, no help-hub content call, no SP-API host, no sign-in, no seller data. The web search budget ran out partway; what it left unread is under *Open questions* (6, 12–15) and *Unread pages*.

**Critic items acted on, and how:**
- **A1 (post-to-store table).** The table's home is fc-lost-damaged (§ 2); this file points there and keeps its readings as evidence. A control check added: two threads whose text names the store (UK `2f44617d-…`, US `5c63f045-…`) read the matching `marketplaceId` from the `.com` host, and a US thread fetched from `.co.jp` reads the US. `1101821c-…` read as Sweden. Tag kept as command-verified.
- **A2, H (help pages).** The office closed the help-hub content call on 2026-11-10; this file does not use it. `GEYPWTSQRTXXXMVB`, `G201214140`, `G200213130`, `GR384ESWC8HH8667` stay unread, and their facts are carried by the routes named and tagged.
- **A8 (UK automation).** The opening paragraph no longer states UK automation from 2024-10-10 as fact; it points to fc-lost-damaged FC5 (UK staff, 2026-04-06: UK warehouse-lost claims manual). Correction 2 records the stock and finance packs' statements against FC5.
- **A9 (MCF policy).** Settled: the AWD terms link each of their five mentions of "MCF inventory reimbursement policy" to supplychain.amazon.com/support/reimbursements, the *Supply Chain Portal (SCP) Reimbursements policy - ASCS* page (new IN34). FL27 and IN26 describe the same page; IN26 restated to say the AWD window, cap and valuation are read there.
- **B, Chinese evidence and first mile.** New § D(d), § M and IN39–IN41: Amazon's Chinese wording of the evidence (an Amazon-stamped 提货单 for LTL/FTL), Chinese practitioners' forwarder-stamped 签收单, the gap between them, Amazon's Chinese list of first-mile causes of short counts, first-mile claims against the forwarder or airline. Chinese-invoice acceptance and the buyer-entity question are open question 14, pointing to value-and-reversals VR13 for MYSC.
- **B, AGL ocean leg.** § K rewritten from the public *AGL Freight Service Terms* (2026-01-14): risk of loss to delivery at an Amazon facility, BCJ as contracting party for China-origin ocean carriage, sealed-container and packaging exclusions, liability limits, insurance duty and the claim notice periods (new IN37, IN38). Billing clauses point to finance P-ful-29 to P-ful-31.
- **C, H (EU/UK/JP windows).** Read: the UK redline of 2024-12-11 (the 2025-01-09 change excludes shipment-to-Amazon claims; new IN35), the EU redline set of 2024-08-20 (no shipment-to-Amazon page), the JP policy of 2025-02-19 (claim kind named, no window), a UK staff post of 2025-06-06 ("File within 60 days", no claim kind) (new IN36). No length for the EU, UK or JP inbound window was found on any Amazon page; a gs.amazon.cn "欧洲站为六个月" lead from a search summary could not be located and is not evidence.
- **D (homes).** IN22 withdrawn (cap → VR29; SCP cap → FL27, FC40). IN30 withdrawn (→ SU42). IN29 narrowed to what the inbound reads lack; "no operation files a claim" and the Support API → SU8–SU12. IN17 points to FL7. IN13's durations point to FL30. Section L's Support API row and removed-reports line are pointers. Added pointers to stock `shortages.md` and to finance P-ful-29 to P-ful-31 and P-ful-37.
- **E (forbidden kinds).** IN20 and § C(b) restated as two practitioner ways of counting a shortfall, side by side, with no method picked.
- **F (moving values).** New *Values that move* table; IN7, IN8, IN13, IN14, IN26, IN32, IN33 and §§ C, G, J, K now state the rule and where it is read, with the figures in the table.
- **G (weak sources).** IN5 now names the Amazon FBA statements that exist (Indy_Amazon; gs.amazon.cn on per-box tracking) beside the Hopted copy, and says they do not tie payment to tracking in words. IN31 adds AMZ123's unsupported 180 days. IN25 and the other snippets stay tagged opinion.

**Correction found in this revision:** IN21 and § G said the US and DE PDFs carry both a sourcing-cost and an "estimated proceeds" basis for shipment-to-Amazon claims. Rendered, the "estimated proceeds" sentence is struck in the US PDFs (2024-12-18, 2025-02-24) and the JP policy (2025-02-19); it is the pre-2025 basis (value-and-reversals VR1, VR28). IN21 restated; open question 8 narrowed. For value-and-reversals (its home, not edited here): the JP policy of 2025-02-19 carries the same sourcing-cost text with "After April 1, 2025" for the estimate refresh, and a JP cap of 675,000 JPY.

**Positions now:** IN1–IN41; IN22 and IN30 withdrawn (39 standing). Added IN34–IN41. Changed IN5, IN7, IN8, IN9, IN13, IN14, IN15, IN17, IN20, IN21, IN26, IN29, IN31, IN32, IN33.

**Corrections to other packs** (new section): finance P-ref-13/-16 store attribution; stock I21 and `shortages.md` on UK automation (against FC5) and on the 2024-08-06 post's three stores; stock I21 extended (the SCP page is also the AWD claim rule); this file's own earlier "SCP/AWD" correction to the finance pack withdrawn, as no such label was found.
