# Issues found while testing Kamra at SR Continental

Test date: 10 October 2026. Site: http://127.0.0.1:8001/kamra. Tested on a local test copy.

How to read this list
- Each issue has a number and a severity. High means money or legal papers can go wrong. Medium means staff get confused or wrong data is saved. Low means it is a nuisance.
- Under each issue: **How to repeat it** (what to click), **What happens**, and **What should happen**.
- Sign in as Administrator unless the steps say another user. Left menu names are written in **bold**.
- Some issues were found by calling the system directly because the screen has no way to do the step. These are marked "No screen". They are still real, because other tools (the AI assistant, the API) can reach them.
- No Kamra files were changed during testing. The fix for issue 39 was made later in a separate fork of Kamra.

---

## High

### 1. The tax invoice can be made while money is still owed
How to repeat it
1. Click **Walk in** (top right). Type a name and phone, pick ID type and number, pick Cash, set the amount collected to 1000, click **Check in & collect**.
2. Click **Open bill**.
3. In **Post a charge** pick Food & Beverage, type Dinner, amount 1000, GST 5%, click **Post**.
4. In **Record a payment** type 500 and click **Record**. Paid is 500 and balance is 550.
5. Click **Close & generate invoice** (top right).
What happens: The page shows TAX INVOICE (for example INV-SC-26-00002) with Closed and balance 550. There is no warning.
What should happen: A warning or a block while the balance is not zero.

### 2. A credit note can be bigger than the bill
How to repeat it
1. Open a bill with an invoice (see issue 1, steps 1 to 5, and pay the balance first).
2. Click **Credit note** (top right).
3. A small browser box asks for the amount. Type 999999 and press OK. Type a reason.
What happens: The credit note number is made (example CN-SR Con-20261012-0001).
What should happen: The amount cannot be more than the invoice.

### 3. A company payment can be bigger than what the company owes (No screen)
How to repeat it: There is no button for this. Open **Finance**, **Ledgers** and look at the table **City ledger aging**. It shows the balance. The system call for settling a city ledger account accepted 999,999 on an account that owed 2,675, and the balance became minus 997,324.
What should happen: The amount cannot be more than the balance. Also add a screen to receive company payments.

### 4. A charge with a minus amount, or a wrong GST rate, is accepted
How to repeat it (minus amount)
1. Open any open bill. In **Post a charge** pick Misc, type a description.
2. Type `-50` in the amount box. Pick GST 5%. Click **Post**.
What happens: A line of minus 50 is added and the bill total goes down.
How to repeat it (wrong GST): No screen. The GST list on the screen has only 0, 5, 12, 18 and 28. The system call accepted GST 99 and added 99 rupees of tax to a 100 rupee charge.
What should happen: Amount above zero. GST only 0, 5, 12, 18 or 28.

### 5. A charge cannot be voided from the screen
How to repeat it
1. Open a bill that has a charge line.
2. Click **Void** at the end of the line. The button changes to **Confirm void**.
3. Click **Confirm void**.
What happens: A red message "A reason code or reason text is required." There is no box to type a reason, so the void never works.
What should happen: A reason box next to **Confirm void**.

### 6. The Ledgers page says Out of balance
How to repeat it: Click **Finance**, then **Ledgers** (left menu, under Books).
What happens: A red line "Out of balance, debit 1,581 vs credit 26,040". The test day included cancelled invoices and payments on closed bills, so an accountant must check whether the system or the test caused it.

### 7. A booking is accepted for a room type whose only room is blocked
How to repeat it
1. Click **Front Desk**, then **Room Blocks**, then **New**.
2. Pick room SR Continental 301 (the only Suite), reason Maintenance, From 20 Oct 2026, To 22 Oct 2026, Status Active. Click **Save**.
3. Click **New booking**. Type a name and phone. Pick Suite Room. Set Check in 2026 10 20 and Nights 2. Click **Confirm booking**.
What happens: The booking is saved as Confirmed, but with no room.
What should happen: The system says the room type is sold out.

### 26. Banquet: any amount can be received, and the invoice and close out work before the event
How to repeat it
1. Click **Banquets and Groups**, **Banquets**, **All Functions**, open a confirmed function (example EVT-2026-0168, event on 20 November 2026).
2. In the Money step use **Record money in**. Type 99999999 and save.
3. Open the **Invoice** tab and click **Issue**. Click **Close out the function**.
What happens: The receipt is accepted (balance due becomes minus 9,96,94,659). The invoice and the close out work 40 days before the event. The function becomes Completed.
What should happen: A receipt cannot be bigger than what is due. Close out only on or after the event day.

---

## Medium

### 8. Checkout is refused after the invoice is made
How to repeat it
1. Check a guest in. Open the bill. Click **Close & generate invoice**.
2. Click **Reservations** (left menu), click the booking row, click **Check out**.
What happens: Red message "Invoice is issued, its charges are frozen. Post adjustments on a new folio." The guest stays checked in.
What should happen: Tell the staff the right order, or make the invoice automatically at check out.
Fix for staff: On the bill click **Cancel invoice**, type a reason, click **Confirm cancel**. Check out first, then make the invoice.

### 9. The night audit button moves the date on every click
How to repeat it
1. Click **Finance**, then **Billing**.
2. Click **Run night audit**. Wait for the message.
3. Click **Run night audit** again.
4. Click **My Till** and look at **Business date**.
What happens: Each click moves the hotel date one day forward (two clicks moved it from 10 to 12 October). There is no question to confirm.
What should happen: A confirm question, and one run for each day.
Note: running the system call again for a date that already ran is safe ("already ran"). Only the screen button moves the date on every click.

### 10. The till closes with missing cash and asks nothing
How to repeat it
1. Click **My Till**. Opening float 2000, click **Open session**.
2. In **Paid out** type 200 and a reason, click **Post**. Expected cash is 1,800.
3. In **Close till** type 1700 in **Counted cash**. The page shows the variance minus 100.
4. Click **Close session**.
What happens: The till closes. No warning, no reason box.

### 11. A till accepts cash amounts bigger than the cash in it
How to repeat it
1. Open the till with 3000 (steps above).
2. Click **Petty Cash** in the left menu and post 99999 with a payee and reason. Or in **My Till**, in **Cash drop**, type 999999 and click **Drop to safe**.
What happens: Both are accepted. Expected cash becomes minus 2,107,614.
What should happen: Refuse an amount bigger than the cash in the till, or ask a manager.

### 12. Room service order can be sent without a room
How to repeat it
1. Click **F&B**, then **Restaurant POS**. Click **Room Service** (top). The outlet is In Room Dining.
2. Click Coffee to add it. Do not pick a room.
3. Click **Send to kitchen**.
What happens: The order (for example ORD-2026-00163) is sent with no room. The Room list also shows empty rooms.
What should happen: Block the order until a room with a guest is chosen.

### 13. A restaurant discount has no limit
How to repeat it
1. Open an order in Restaurant POS (pick a table, add Butter Chicken twice, bill is 900).
2. Click **Add discount**. Type 99999 and apply. The total goes to 0.
3. Click **Add discount** again, type -10 and apply. The total becomes 910.
What should happen: A discount from 0 up to the bill, and a manager PIN above a set percent.

### 14. A housekeeper can mark their own task Verified
How to repeat it
1. As Administrator click **Housekeeping**, **Tasks**, open a task, set the person (assigned to) to housekeeping@srcontinental.com, **Save**.
2. Sign out. Sign in as housekeeping@srcontinental.com. Open `http://127.0.0.1:8001/kamra/hk` (phone app).
3. Accept the task. Set it In Progress, then Done, then Verified.
What happens: Every step is accepted.
What should happen: Only a supervisor can set Verified.

### 15. A booking with the same check in and check out day is accepted
How to repeat it
1. Click **New booking**. Type a name and phone.
2. Set Check in to a day and Nights to 0 (or use the system call with the same day for both).
3. Click **Confirm booking**.
What happens: It is saved and charged one night. Changing an existing stay to the same day is refused, so the two screens do not agree.
Note: this was found through the system call. The screen has Nights, and 0 should be tested again by hand.

### 16. A bill cannot be moved to the city ledger from the screen
How to repeat it
1. Check in a guest who has a bill. Do not pay.
2. Click **Reservations**, click the row, click **Check out**.
3. The message says "Collect payment or transfer it to the city ledger before departure."
4. Look on the bill and on **Ledgers** for a button to transfer. There is none.
What should happen: A button on the bill: **Move to city ledger** with a company.

### 17. Restaurant sample user has too many rights
How to repeat it
1. Sign in as restaurant@srcontinental.com. Open `http://127.0.0.1:8001/kamra/billing`.
2. Try **Run night audit**, give a refund on a bill, or make a booking.
What happens: All work. The user has the Kamra Agent role, which is made for the AI assistant.
What should happen: Give restaurant staff a smaller role.

### 18. Reception and Finance can refund and run the night audit with no manager
How to repeat it: Sign in as reception or finance. On a bill with a payment, use **Refund money** and give a small refund. Also click **Run night audit**.
What happens: Both work with no supervisor step.

### 19. A staff user can open a page the role should not use
How to repeat it
1. Sign in as housekeeping@srcontinental.com.
2. Type `http://127.0.0.1:8001/kamra/billing` in the address bar.
What happens: The page opens with the Night audit button and the Folios heading. The server blocks the data, but the screen should not open.

### 27. A corporate booking can be made with no company
How to repeat it: Click **New booking**. Open **Company, add ons & arrival details**. Leave Company empty and choose booking type Corporate if the list has it (the system call accepted it). Click **Confirm booking**.
What happens: The booking is saved as Corporate with no company, so no company bill or city ledger can follow.

### 28. A guest can be checked in 46 days before the arrival date
How to repeat it
1. Click **New booking**, pick a Premier Room, Check in 25 November 2026, 1 night, **Confirm booking**.
2. Open **Reservations**, click the booking row.
3. Click **Check in** (or use the Check In button on Today if it shows).
What happens: The guest is checked in today and the room is taken from today on. No warning about the date.
What should happen: A warning that arrival is on another date, with a choice to change the dates first.

### 29. The phone number is not checked for length
How to repeat it: **New booking**, type the name, type `123` in **Phone**, click **Confirm booking**. Also try a 15 digit number, or leave the phone empty.
What happens: The booking is saved. Only a phone number with letters is refused.

### 30. A negative number of children is accepted
How to repeat it: Make a booking through the system with children minus 1 (the screen field may stop it; try typing `-1` in **Children**).
What happens: Saved at the normal price.

### 31. There is no longest stay
How to repeat it: **New booking**, Suite Room, **Nights** 365, **Confirm booking**.
What happens: Saved for 19,21,500 rupees. No warning.

### 32. All three meal plans were set as Default (setup data, now fixed)
How to repeat it: Click **Revenue**, **Meal Plans**. The column **Default** showed 1 for CP, EP and MAP.
What should happen: Only one plan (EP) is the default. This was fixed in the test data and in the setup app.

### 33. Some messages are wrong
- Cancel a booking that is already cancelled (Reservations, click a Cancelled booking, use the cancel option). The message says "Only confirmed bookings can be cancelled, checked in stays check out." It should say the booking is already cancelled.
- Click **Check out** on a booking that is still only Confirmed. The message talks about money owed, not that the guest has not checked in.

### 34. Wastage can be more than the stock, and a stock take can be minus
How to repeat it
1. Click **F&B**, **Kitchen Inventory**. Pick the outlet **Main Restaurant**.
2. Click **Wastage**. Pick Rice. Type 500 in the quantity. Type a reason. Click **Write it off**.
3. Click **Stock take**. Type a count of -3 for Rice and a note. Save.
What happens: Both are accepted. Rice went to minus 505 and then minus 3. The **Negative** tab then shows it.
What should happen: Wastage cannot be more than the stock on hand. A count cannot be below zero.

### 35. Menu bulk upload makes a dish with a minus price and quietly changes old prices
How to repeat it
1. Click **F&B**, **Menu**, **Bulk upload**. Paste rows: `Negative Dish,-50,Snacks,yes` and `Dal Makhani,300,Main Course,yes` (columns item name, price, category, veg). Pick the outlet Main Restaurant. Click preview, then import.
What happens: The dish with minus 50 is created. Dal Makhani is updated from 280 to 300 with no question. Rows with a price like `abc` or with no name are skipped correctly.
What should happen: A price of zero or less is skipped. Changed prices are listed in the preview and need a tick.

### 36. Online check in accepts a short ID number and (on the server) a missing signature
How to repeat it
1. Open the guest check in link (see section 9.9 of the guide).
2. Pick ID type Aadhaar. Type `12345` as the ID number. Fill the other fields, draw a signature, tick the declaration, tap **Sign & complete check in**.
What happens: It is saved. An Aadhaar number has 12 digits.
Also: the button stays grey without a signature on the screen, but the server accepted a request with an empty signature. Only the declaration tick is checked by the server.

### 37. Any bill can take "Company Credit", "OTA Prepaid" or "Payment Link" as a payment mode
How to repeat it
1. Open the bill of a normal guest (no company, no booking site).
2. In **Record a payment** pick the mode **Payment Link** (the list shows it). Type 1 and click **Record**.
What happens: A payment is recorded as if paid by link, though no link was sent and no money arrived. The same happens for Company Credit and OTA Prepaid through the system call.
What should happen: These modes only for a company booking, a booking from a booking site, or a real paid link.

### 38. The Billing box says 0 owed, but check out says 5,145 is owed, and the booking total is a third number
How to repeat it
1. Click **New booking**. Pick Deluxe Room, 2 adults, Meal plan Continental Plan, 1 night, today. Click **Confirm booking**.
2. Click **Today**, then **Check In**, then **Check in to 103** (the room given).
3. Click **Reservations**, click the booking row.
4. Look at the **Billing** box: Total 0, Paid 0, Balance due 0.
5. Click **Check out**.
What happens: A red message "Cannot check out: 5,145.00 is still owed." The Billing box shows 0 because the room charge is posted to the bill only at check out. The booking total in the system is 5,407.50, a different figure from the 5,145 owed. The same kind of gap showed on other bookings (a guest who paid the booking total then had to be refunded 367.50 and 735.00 before check out).
What should happen: One total. The Billing box should show the room charge the guest will owe, and the booking total should equal the amount asked at check out.
Workaround for staff: Before check out open the bill and take the amount the check out message asks for.

---

### 25. A voucher is checked against today, not the stay date
How to repeat it
1. Click **Revenue**, then **Vouchers**. Note WELCOME10 is valid until 31 March 2027.
2. Click **New booking**. Type a name and phone. Pick Deluxe Room.
3. Set **Check in** to 10 June 2027 and **Nights** to 2.
4. Type `WELCOME10` in **Voucher**. Read the **Quote** on the right.
What happens: The quote shows 10 percent off, because today is before 31 March 2027. A voucher that has really expired (end date in the past) is refused with "Voucher ... expired on ...". So the check works, but it uses today and not the check in date.
What should happen: The owner decides. Either a voucher is valid when you book (as now) or valid for the stay dates. This is a policy question, not a fault.

### 39. A saved booking cannot be amended when its voucher is used up or expired
How to repeat it
1. Click **Revenue**, then **Vouchers**, then **New**. Make a voucher with **Max Uses** set to 1 and save.
2. Click **New booking**, type the voucher code and confirm the booking.
3. Open that booking and click **Amend stay**. Change the nights and save.
What happens: The error "Voucher ... has been fully redeemed" appears, because the booking's own use counts against the limit. The same error type appears when the voucher end date passes after the booking was made, or when the voucher is disabled.
What should happen: A booking keeps the voucher it was made with. The dates and use limit are checked only when the voucher is first added.
Status: Fixed in the fork branch `fix/voucher-recheck-on-existing-booking`.

## Low

### 20. Marking a room Clean on the board leaves its task Pending
How to repeat it
1. Click **Housekeeping**, **Room Board**. Click a dirty room that shows a task. Click **Mark Clean**.
2. Click **Tasks** in the left menu.
What happens: The room is Clean but the task is still Pending.

### 21. The POS forgets the outlet
How to repeat it: Click **F&B**, **Restaurant POS**. Pick the outlet Main Restaurant at the top. Click **Kitchen Display**, then click **Restaurant POS** again.
What happens: The outlet is In Room Dining again.

### 22. A print window can freeze the browser tab
How to repeat it: In Restaurant POS add an item, click **Send to kitchen** with **KOT printer on**, or settle an order.
What happens: The print window opens and the page stops answering until the window is closed (press Esc).

### 23. Two clocks for the date
How to repeat it: Run the night audit once. Open **Tape Chart** and note the first date. Open **My Till** and note the Business date.
What happens: The tape chart and the banquet form show the calendar date. The till shows the hotel date. They differ after the audit.

### 24. An old page asks for a file that no longer exists
How to repeat it: After the frontend is rebuilt, open **Kitchen Display** in a tab that was already open.
What happens: "Something broke in the UI. Failed to fetch dynamically imported module". A hard reload (Ctrl plus Shift plus R) fixes it.

---

## Retest after Administrator got full access
On 10 October 2026 the hotel manager gave the Administrator user all hotel roles (Front Desk, Finance, Housekeeping, Housekeeping Supervisor, Hotel Admin, Revenue Manager, Kamra Agent, System Manager). The areas below were tested again with the full access. Nothing changed, so the earlier results stand.

| Area | Test | Result with full access |
|---|---|---|
| Invoice | Close invoice with 550 owed | Still made, no warning (issue 1) |
| Check out | Check out after the invoice | Still refused (issue 8) |
| Void | Void a charge | Works only with a reason (issue 5) |
| Till | Open, paid out 200, petty cash 300 | Works |
| Till | Petty cash 99,999, drop 999,999, paid out 999,999 | Still accepted. Expected cash minus 2,097,497 (issue 11) |
| Till | Close with 0 counted when cash is missing | Still closes with no warning (issue 10) |
| Night audit | Run again for a date already done | Safe: the system says "already ran" and does not post twice or move the date. Only the button on the screen (which has no date) moves the date on every click (issue 9) |
| Restaurant | Discount 99,999 | Still accepted, total 0 (issue 13) |
| Restaurant | Discount minus 10 | Still accepted, total goes up (issue 13) |
| Restaurant | Pay an order twice | Refused: "Already paid." |
| Restaurant | Room service with no room | Still accepted (issue 12) |
| Housekeeping | Assign, accept, In Progress, Done, Verified | All accepted (Administrator is allowed to verify; for the housekeeper user see issue 14) |
| Housekeeping | Status "Flying" | Refused: "Status must be In Progress, Done or Verified." |
| Banquet | Same hall, same date as a confirmed function | Still blocked: "Taken: Meera Iyer" |
| Apps page | Which apps show | All 10 apps show |

## Tests that could not be finished
- **Company credit limit:** the test company (Acme Travels) had a minus balance of 9,97,324 from issue 3, and its only Suite was already booked, so the limit of 1,00,000 could not be crossed. Test again after the balance is fixed. A company with credit **not** allowed (Bharat Tech) was correctly made to pay at check out.
- **Payment link:** the link is made from the bill screen only. The system call is not open directly, so it was not run. The gateway is off on purpose.
- **Printing on paper:** needs a printer and a person to look at the paper.

## Setup notes (not product faults)
- **Scheduler is off.** Open **System Health** (`/kamra/health`). It says "Scheduler is off, night audit and reminder jobs will not run". The automatic 3 AM night audit does not run on this site. Turn it on with `bench --site <site> enable-scheduler`.
- Administrator had no hotel roles at first. Tests as Administrator before the manager gave full access may have passed because Administrator skips some checks.
- A role test ran one more night audit (hotel date is now 13 October 2026), opened and closed three tills, made two bookings and cancelled booking RES-2026-00074 (Ameer). These are test data only.
- Many sample bookings and bills were added to the local database by testing. A fresh install from the setup app starts clean.
