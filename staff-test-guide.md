# Kamra Test Guide for SR Continental

This guide tells you what to do in Kamra for each hotel task. To test a task, follow the flow written for it and check that the screen shows what the guide says. Hotel staff can also use it as a quick training sheet.

## Before you start

- Open Kamra at `http://127.0.0.1:8001/kamra` and sign in.
- Names in **bold** are buttons, fields or menu items on the screen.
- All names, phone numbers and GST numbers in the examples are made up. Use your own when you train real staff.
- The top right corner of every screen has two buttons: **Walk in** and **New booking**.
- The left menu changes with the app you pick on the **Your apps** page. The apps are Front Desk, Housekeeping, Operations, F&B, Banquets and Groups, Revenue, Finance, Booking Engine and Admin.
- The hotel date can differ from the calendar date. The night audit moves the hotel date forward.
- A list of known problems is in the separate file `issues-found`. Where this guide says "see the issues list", read that file before you rely on the feature.

---

## Part 1. Front Desk

### 1.1 Make a booking
Use this when a guest asks for a room on a future date or for today.
1. Click **New booking**.
2. Type the **Guest name** and the **Phone** (ten digits).
3. Pick the **Room type**. The price for one night shows next to each type.
4. Check **Check in**, then set **Nights**, **Adults** and **Children**.
5. Pick a **Meal plan**. European Plan means room only.
6. If the guest has a code, type it in **Voucher**.
7. Read the **Quote** on the right side. It shows room price, meals, GST and the total.
8. Click **Confirm booking**.
9. The next screen shows the booking number (for example RES-2026-00061) and the room given. Click **Done**.

You should see: the booking under **Arrivals** on the **Today** page for the check in date.

If the room type is full for those dates the screen says it is sold out. Use **Waitlist** (see 1.12).

### 1.2 Check in a booking
1. Click **Today** in the left menu.
2. Under **Arrivals** find the guest and click **Check In**.
3. A panel opens. It shows chips for Online check in, ID on file, Address proof, Phone and Email. Missing papers do not stop the check in, but the register must be complete before the night audit.
4. Make sure the room line says the room is assigned and Clean.
5. Click **Check in to 101** (the button shows the room number).

You should see: Arrivals goes down by one, **In house** goes up by one, and the room on the room board turns dark.

### 1.3 Walk in guest (booking and check in in one step)
1. Click **Walk in**.
2. Type the guest name and phone.
3. Pick the **ID type** (Aadhaar, Passport, Driving License, Voter ID, PAN or Other) and type the **ID number**. An Aadhaar number has 12 digits.
4. Check the **Nationality**. India is the default.
5. Pick the **Room type** and the **Room**. Choose a room that shows Clean.
6. Set **Nights**, **Adults**, **Children** and the **Meal plan**.
7. In **Payment** pick Cash, Card, UPI or Bank Transfer. The amount fills with the full total. Change it if the guest pays less.
8. Click **Check in & collect** (the button shows the amount).
9. Click **Open bill** to see the bill, or **Done**.

### 1.4 Change or upgrade a room after check in
1. On **Today**, click the guest under **In house guests**. The registration card opens.
2. Click **Change room**.
3. Click **Same type** to see rooms of the same type, or **All types (upgrade)** to see every free room.
4. Click the new room. The line under the list shows the price change and says the old room will be marked Dirty.
5. Pick a reason (the default is Guest request). Add a note if you want.
6. Click **Move to 202** (the button shows the new room).

You should see: the registration card shows the new room and the new stay total. Example: Deluxe 101 to Premier 202 changes a 7,350 stay to 9,450.

### 1.5 Charges and payments on the bill
Open the bill from the registration card with **Open bill**.

To add a charge:
1. In **Post a charge** pick the type (Food & Beverage, Minibar, Laundry, Spa, Early Check in, Late Checkout, Discount or Misc).
2. Type a description, the amount before tax, and the GST rate.
3. Click **Post**. The bill shows the amount, the GST and the CGST and SGST split.

To take a payment:
1. In **Record a payment** pick **Payment**, **Advance** or **Security Deposit**.
2. Pick the mode: Cash, Card, UPI, Bank Transfer or Payment Link.
3. Type the amount. The box fills with the full balance, so change it for a part payment.
4. Click **Record**.

Use only Cash, Card, UPI and Bank Transfer for ordinary guests. Payment Link is for a link that was really sent.

To reduce a bill, use **Pass an allowance** and type a reason. Do not post a charge with a minus amount.

### 1.6 Check out and make the invoice
Follow this order every time.
1. Open the bill and take the full stay amount from the guest with **Record a payment**.
2. Click **Reservations** in the left menu and click the booking row. A panel opens on the right.
3. Click **Check out**. The status changes to **Checked Out**. The billing box now shows the room charge and all other charges together.
4. Click **Open folio** in the billing box, check the balance is zero, then click **Close & generate invoice**.
5. The bill becomes a TAX INVOICE with a number and the status Closed.

Messages you may see:
- "Cannot check out: 9,450 is still owed. Collect payment or transfer it to the city ledger before departure." Take the payment, then check out again.
- "Cannot check out: the guest is owed 735. Issue the refund before departure." The guest paid too much. Use **Refund money** on the bill, then check out.
- "Invoice is issued, its charges are frozen." You made the invoice too early. Use 1.7 to cancel it, check out, then make the invoice again.

### 1.7 Cancel an invoice
1. Open the bill. Click **Cancel invoice**. A yellow bar opens.
2. Type the reason (it is required).
3. Click **Confirm cancel**.

The number goes to the cancelled register and the bill shows PROVISIONAL BILL again, so you can correct it.

### 1.8 Cancel a booking before arrival
The hotel gives free cancellation if the guest cancels two or more days before arrival. Inside two days the fee is the first night plus GST. Example: a Deluxe booking for tomorrow, cancelled today, costs 2,500 plus GST, and the fee shows on a bill for that guest. A manager can waive the fee. Each cancel gets a number such as CXL-2026-00001.

Only a booking in Confirmed status can be cancelled. A guest who has checked in must check out.

### 1.9 Extend or shorten a stay
Change the **Check out** date in the reservation panel (Reservations, click the row). The price is worked out again. Example: a Deluxe stay changed from 2 nights to 4 nights shows 10,500. The system refuses a check out date on or before the check in date, and a check in date in the past.

### 1.10 Vouchers
Type the code in **Voucher** when you make a booking.
- WELCOME10 gives 10 percent off and needs at least 2 nights.
- FLAT500 takes 500 rupees off.
- A code that does not exist shows "Voucher does not exist."
- A code on too few nights shows "needs a stay of at least 2 nights."
- Check the **Valid to** date of every voucher yourself. See the issues list.

### 1.11 Room blocks, tape chart and calendar
- **Room Blocks** takes a room out of sale: click **New**, pick the room, the reason (House Use, VIP Hold, Owner, Maintenance, Other), the **From** and **To** dates and Status **Active**, then **Save**. To free the room set Status to **Released**.
- **Tape Chart** shows every room for 14 days. **Calendar** shows availability and price for each room type for 14 days; click a cell to start a booking.
- Before you promise the last room of a type, look at the tape chart for blocked rooms. See the issues list.

### 1.12 Waitlist
Use **Waitlist** on the New booking panel when a room type is full. The booking is kept with no room. When a room is free open the booking and click **Promote to a room**.

### 1.13 Group booking
A group booking makes one booking for every room. Example: 2 Deluxe and 1 Premier from 5 to 7 March 2027 for a wedding family. If a room type is full the system makes the group with the rooms it can and lists the rooms it skipped with a reason. Read that list so no room is forgotten. Groups are listed under **Banquets and Groups**, then **Groups & Blocks** (click **New**: Group name, Company, Arrival, Departure, Block cutoff, Status, Notes).

### 1.14 Company and travel agent bookings
- A booking for a company that has credit goes to the city ledger when the guest checks out. Pay what the company owes from **Finance**, then **Ledgers**.
- A company that has no credit must pay at check out.
- When a booking has a travel agent the commission is worked out by itself. Example: Sunrise Travels at 10 percent on a 2 night Deluxe stay (5,000 before tax) gives 500.

### 1.15 Split a bill and move a charge
1. Open the bill and click **Split folio**. Two tabs appear: **Guest** and **Company**.
2. Click **Move** on the line to move. A bar opens.
3. Under **Send to** click **Company**, **New Company folio** or **New Extra folio**.

### 1.16 Voiding a charge
Click **Void** on the line, then **Confirm void**. The system asks for a reason, but this screen has no box for it. See the issues list. Until it is fixed, use **Pass an allowance**.

### 1.17 Deposit, refund and credit note
- **Security deposit:** in **Record a payment** pick **Security Deposit** and type the amount (the sample is 5,000). It counts against the bill during the stay. To give it back use **Refund money** on the bill. The system refuses a refund bigger than the money taken.
- **Credit note:** after the invoice is made click **Credit note**, type the amount and the reason. The system gives a number such as CN-SR Con-20261012-0002. Amount zero is refused. A closed bill is not refunded in cash. Check the amount yourself, see the issues list.
- **Early check in and late check out:** use **Post a charge** and pick the type.

### 1.18 Send the self check in link to a guest
1. Click **Today**. Under **Arrivals** click **copy check in link** next to the guest. The link shows only for guests who have not submitted the form.
2. Paste it into WhatsApp, SMS or email.
3. The link looks like `<site address>/kamra/checkin/<a long code>`. Opening `/kamra/checkin/` without the code shows Page not found.
4. The guest fills the form on a phone: ID type and number, optional ID photo and address proof, email, nationality, address, city, arrival time and notes. The guest reads the house rules, signs, ticks **I accept the registration declaration** and taps **Sign & complete check in**.
5. At the desk open the guest's registration card to see the signed card. The ID photo is deleted at check out.

The link needs the hotel's public site address, not `127.0.0.1`. Automatic sending before arrival needs a connected WhatsApp channel and the scheduler switched on.

### 1.19 Guests
**Guests** lists every guest with phone, bookings, stays, nights and lifetime value. Click a guest to see the guest journey. Two profiles for the same person can be merged. A profile cannot be merged into itself.

---

## Part 2. Housekeeping

### 2.1 Room board
1. Pick **Housekeeping**, then **Room Board**.
2. Each room box shows the number, the state (Dirty, Clean, Inspected, Out of order) and the guest name.
3. Use the top buttons (All, Dirty, Clean, Inspected, Out of Order, Due out, Has task) to filter.
4. Click a room and pick **Mark Clean**, **Mark Inspected** or **Mark Out of Order**.

Marking a room Clean here does not close its task. Close the task as well (2.2).

### 2.2 Tasks
1. Click **Tasks**, then click a task row (or **New** to make one).
2. The form has **Room**, **Assigned To** (the housekeeper, shown to a user with full access), **Type** (Checkout Clean, Stayover Clean, Deep Clean, Inspection, Maintenance), **Priority**, **Status** and **Notes**. A user with full access also sees **Delete**.
3. Set **Assigned To**, then **Save**.
4. Change **Status** to **In Progress**, **Save**, then **Done**, **Save**.
5. When a clean task is Done the room turns Clean and an **Inspection** task is made. The supervisor sets the inspection to **Verified**.

By itself the system makes a task when a guest changes room (old room Dirty) and when a guest checks out (a Checkout Clean task).

### 2.3 Housekeeper phone app
1. The housekeeper signs in and opens `/kamra/hk`. It shows tasks given to that person only. With none it says "Available, waiting for assignments".
2. The housekeeper accepts a task, sets **In Progress**, then **Done**.
3. A found item can be logged (it goes to Lost & Found).
4. A minibar charge can be added to a room that has a guest. A room with no guest shows "No checked in guest in that room to bill."

### 2.4 Lost & Found
Click **Lost & Found**, then **New**. Fields: Kind (Found, Missing, Damaged), Item, Room, Logged on, Logged by, Status (In Storage, Returned, Disposed), Guest, Returned on, Notes.

### 2.5 Laundry
Click **Laundry**. It has Pickup requests, In hand, a Price menu and Billing.
1. **Log pickup request** for a room that has a guest (an empty room shows "No checked in guest in that room.").
2. **Collect now**: count the items, for example 3 shirts Wash & Iron, which prices at 300 rupees. Quantity must be above zero. An item not on the price menu is refused.
3. Move the bag in order: Collected, In Process, Ready. It cannot skip a step.
4. **Deliver**. Type a shortage note if something is missing. The charge goes to the guest bill with GST.
5. A delivered order cannot be cancelled. A house order (staff uniforms) needs no room and is never billed.

---

## Part 3. Restaurant (F&B)

### 3.1 Take a table order
1. Pick **F&B**, then **Restaurant POS**.
2. At the top pick the outlet **Main Restaurant**. The page goes back to In Room Dining each time you open it, so pick the outlet again.
3. Keep **Dine In** selected and pick a table (T1, T2 or T3).
4. Click menu items to add them. Click again for one more. Use plus and minus to change the number.
5. Check the total. GST is split into CGST and SGST.
6. Click **Send to kitchen**.

Example: Butter Chicken plus 2 Garlic Naan comes to 570 plus 28.50 GST, a total of 598.50.

### 3.2 Kitchen screen
1. Click **Kitchen Display**. Each ticket shows the table, items and the minutes waited.
2. Click **Start / accept**. The button changes to **All ready**.
3. Click **All ready** when the food is done, or **Mark ready** on each item.

### 3.3 Settle a table
1. Go to **Restaurant POS**, pick the outlet and click the table.
2. Click **Settle** and pick **Cash**, **Card** or **UPI**. **Complimentary, close at 0** is for free orders.
3. The order shows as Delivered. An order cannot be paid twice or cancelled after it is paid.

### 3.4 Room service
1. On the POS click **Room Service** and pick the outlet **In Room Dining**.
2. Add the item, pick the **Room** (only choose a room with a guest), click **Send to kitchen**.
3. Click **Settle**, then **Deliver & post to Room 102** (the room number changes). The charge appears on the guest bill.

### 3.5 Discount and cancel
- **Add discount**: type the amount and the reason. A discount of 50 on a bill of 900 gives 850. Keep the amount between zero and the bill. See the issues list.
- **Cancel**: type a reason (required), click **Cancel order**.

### 3.6 Menu, recipes and stock
- **Menu** lists dishes with outlet, category, price and availability. Buttons: **Recipes** (how much of each ingredient a dish uses), **Bulk upload** (many dishes from a file), **New**, **Export**, **Columns**.
- Bulk upload: give item name, price, category and veg. The preview says how many dishes are new, how many are updated and which rows are skipped. A dish already on the menu has its price changed, so read the preview.
- When an order is delivered, the stock of each ingredient in its recipe goes down. Example: 2 Butter Chicken at 0.25 kg each takes 0.5 kg of chicken.
- **Kitchen Inventory**: pick the outlet. **Receive** records goods in (supplier and invoice number; quantity above zero). **Stock take** sets the counted quantity (a note is required). **Wastage** needs the ingredient, a quantity above zero and "What happened". Each ingredient has a **Ledger** button. Tabs: All, Negative, Out, Low, OK. A par level is the stock that should always be there.
- **F&B Dashboard** shows gross sales, average bill, covers, open bills, complimentary, fire to ready time, sales by order type and tender, top items and voided lines for an outlet.
- **Outlets**: Outlet name, Type, GST percent, Disabled.

---

## Part 4. Finance

### 4.1 Night audit
1. Pick **Finance**, then **Billing**.
2. Click **Run night audit** one time at the end of the day.
3. A message shows what was posted. Example: 1 room night, 2,500 rupees, 0 folios opened, 0 no shows.

It posts the room charge for every guest in the house and flags guests who did not arrive. Every click moves the hotel date forward one day with no question, so do not click twice. The system also runs it at 3 AM when the scheduler is on.

### 4.2 Cashier till
1. Click **My Till**. Type the **Opening float** (example 2000) and click **Open session**. Opening again returns the same till.
2. The page shows Float, Cash in, Card, UPI, Paid outs, Drops, Petty cash and Expected cash.
3. **Paid out**: amount and reason, then **Post**. Example: 200 for a guest taxi gives Expected cash 1,800.
4. **Cash drop** moves cash to the safe.
5. At the end of the shift type the **Counted cash**. The page shows the variance. Click **Close session**.

Keep amounts below the cash in the till. Write any shortage in the shift handover. Open the till before the shift starts, because payments taken before it opens are not counted in it.

### 4.3 Petty cash
Click **Petty Cash**, then **New voucher**: Payee, Category (Supplies, Maintenance, Transport, Staff Welfare, Miscellaneous), Amount, Reason. Click **Post voucher**. Amount zero or no payee is refused.

### 4.4 Currency desk
Click **Currency Desk**. Use the calculator (EUR or USD, Buy or Sell, **Calculate**, **Post exchange**). **Set rate** with **Save** changes the rate for the day. Sample rates: USD 83.20 buy and 84.50 sell, EUR 90.10 and 91.80, tax 18 percent. One exchange above 50,000 is refused ("Exceeds per transaction FX limit"). A currency with no rate is refused.

### 4.5 Sessions, shift report and shift handover
- **Sessions**: one row for every till with cashier, status, float, cash, expected, counted and variance.
- **Shift Report**: cash, card, UPI and variance for each till, and a journal by kind (Drop, Paid Out, Petty Cash) and mode.
- **Shift Handover**: every closed till makes a shift record (example SHIFT-2026-10-12-Morning). Use **New** to pass cash count and follow ups to the next shift.

### 4.6 Folio History, Ledgers, Reports and Accounting Export
- **Folio History**: every bill with tabs All, Open and Closed, **Batch print**, invoice number, total, balance and reprints.
- **Ledgers**: Guest, Deposit, AR and Package ledgers and the city ledger aging. If debit and credit differ a red line says "Out of balance". Ask the accountant to check it.
- **Reports**: occupancy, ADR, RevPAR, RevPAX and revenue split into room, food and other, with a table for 14 days.
- **Accounting Export**: pick Generic CSV, Tally, Zoho Books or ERPNext and click **Download CSV**. Each closed invoice shows SAC code, taxable amount, CGST, SGST and total. Example: INV-SC-26-00004, taxable 10,000, GST 500, total 10,500.

---

## Part 5. Operations

### 5.1 Guest requests (tickets)
1. Pick **Operations**, then **Guest Requests**, then **New ticket**.
2. Type what the guest needs. Pick the **Department** (Housekeeping, Room Service, Maintenance, Front Desk, Concierge, Complaint, Other), the **Priority** and the **Room**. Add a note if needed.
3. Click **Create ticket**.
4. Click **Start** when work begins and **Resolve** when it is done. Tick **Show closed** to see old tickets.

Priority sets the time allowed: Urgent 15 minutes, High 30 minutes, Medium 1 hour, Low 4 hours. The due time shows on the ticket.

### 5.2 SLA Report
Shows how many requests were solved in time: tickets, resolved, breach rate and average time, by category and by priority.

---

## Part 6. Banquets

### 6.1 Enquiry to confirmed function
1. Pick **Banquets and Groups**, **Banquets**, then **New enquiry**.
2. Type the customer name and phone. Pick a company for a corporate event.
3. Pick the event type, date, expected guests (pax) and session.
4. In **Which hall** pick a hall. A hall too small for the guests shows an orange warning. A hall already used at that time is grey and shows who has it.
5. Click **Open the enquiry**. The function opens with a number such as EVT-2026-0168 and a quote. Example: Grand Ballroom 80,000 plus 18 percent GST is 94,400.
6. Click **Confirm**. Use **Tentative** to hold the date, **Cancelled** or **Lost** to close it.

An empty customer name shows "Whose function is this?". The page has six steps: Enquiry, Quote, Margin, Money, Documents, The night.

### 6.2 Menus, services and payments
1. On the function add a menu from **Menus & Services** (Classic Veg Buffet is 1,200 a guest) and add services (Projector and Screen is 3,000). With 150 guests the sample function totals 3,10,340 including 47,340 GST.
2. Set the payment terms. The default is a 25 percent advance, 50 percent before the function and 25 percent on completion.
3. Record each receipt with **Record money in**. A receipt must be above zero. Do not record more than is due.
4. Click the document tabs: **Quotation**, **Contract**, **Event order**, **Pack list**, **Invoice**, **Menu card**, **Print**.
5. Make the invoice and **Close out** on or after the event day. Close out marks the function Completed.

### 6.3 Other banquet screens
**Month Availability**, **Function Diary**, **Registers**, **All Functions**, **Halls & Venues**. Click an open slot in the month view to start an enquiry.

---

## Part 7. Rates and setup (Revenue and Admin)

### 7.1 Price checks
Make these bookings and compare the quote. If a figure differs, check Rate Plans, Seasons, Meal Plans and Room Types.

| Booking | Quote should show |
|---|---|
| Deluxe, 2 nights, normal days | 5,250 (2,500 a night plus 5 percent GST) |
| Deluxe, 2 nights from 24 Dec 2026 (Peak Season, plus 30 percent) | 6,825 |
| Deluxe, 2 nights in June 2027 (Monsoon, minus 15 percent) | 4,462.50 |
| Deluxe, 4 and 5 January 2027 | 6,825 (both nights are in the peak) |
| Suite, 1 night | 5,250 |
| Premier, 1 night, Modified American Plan, 2 adults | 5,775 |
| Deluxe, 1 night, 1 child | 3,045 |
| Deluxe, 2 nights, Non Refundable plan (minus 15 percent) | 4,462.50 |
| Deluxe with 3 adults | Refused (limit 2) |
| Corporate Rate plan | 10 percent off the room |

### 7.2 Forms (click **New** on each list)
A star (*) means the field must be filled.
- **Rooms**: Room number*, Room type*, Floor, Housekeeping status, Notes.
- **Room Types**: Name*, Code*, Public listing URL slug, Category, Base price a night*, Adults included in base price, Single occupancy price, Extra adult a night, Child a night, Max adults, Max children, GST percent, Bed type, Air Conditioning, site name, site URL slug, site address, Google Maps link, Latitude, Longitude, Disabled. The sample types show GST 0 because the property uses the slab rule (5 percent up to 7,500 a night, 12 percent above).
- **Rate Plans**: Name*, Code*, Modifier type (Percent, Amount, Absolute), Modifier value (minus 10 means 10 percent off), Cancellation policy, Default plan, Disabled.
- **Seasons**: Name*, Room type (blank means all), Start date*, End date (inclusive)*, Adjustment, Value (20 means plus 20 percent), Days of week (example fri, sat), Priority (highest wins), Disabled.
- **Guardrails**: Room type (blank means all), Floor price a night*, Ceiling price a night*, Disabled.
- **Vouchers**: Code*, Type, Value*, Valid from, Valid to, Minimum nights, Max uses (0 means no limit), Times used, Disabled.
- **Meal Plans**: Code*, Label, Price per adult a night, Price per child a night, Default, Disabled. Only one plan should be the default (EP).
- **Companies**: Company name*, GSTIN, Contact name, Contact phone, Contact email, Negotiated rate plan, Credit allowed (city ledger), Disabled.
- **Travel Agents**: Agent name*, Type, Commission percent, Contact name, Contact phone, Contact email, Disabled.
- **Halls & Venues**: Venue name*, Code, Type, Seats, Minimum pax, Area, Day rental, Hourly rental, Minimum hours, Rental GST percent, Layouts it takes, Amenities, Disabled.
- **Banquet Menus & Services**: tabs Menus, Services and Dishes. **New menu** adds a package with a price for each guest.

### 7.3 Where each screen is
| App | Left menu |
|---|---|
| Front Desk | Today, Dashboard, Kamra Agent, Reservations, Central Reservations, Tape Chart, Calendar, Guests, Room Blocks |
| Housekeeping | Room Board, Tasks, Laundry, Lost & Found, Phone App |
| Operations | Guest Requests, WhatsApp, Channels, SLA Report |
| F&B | Restaurant POS, F&B Dashboard, Kitchen Display, Menu, Kitchen Inventory, Outlets |
| Banquets and Groups | Banquets, Month Availability, Function Diary, Registers, Menus & Services, All Functions, Groups & Blocks, Halls & Venues |
| Revenue | Revenue Reports, Channel Manager, OTA Room Mappings, Rate Plans, Seasons, Guardrails, Vouchers, Meal Plans, Travel Agents, Companies |
| Finance | My Till, Sessions, Petty Cash, Shift Report, Shift Handover, Currency Desk, Billing, Folio History, Laundry, Ledgers, Reports, Accounting Export |
| Booking Engine | Hotel Profile, Amenities, Photos, Policies, Payments, FAQ, SEO |
| Admin | Settings, System Health, Rooms, Room Types, Activity Log, Marketplace, Developers, New Property, Manage Users, Frappe Desk |

### 7.4 Other admin screens
- **Booking Engine**: the guest booking page is at `/kamra/book`. A guest picks dates and sees each room type with the stay total, rooms left and the 5,000 rupee refundable deposit. The console has seven tabs. A switch shows **Engine Live** and **Preview Page** opens the page.
- **Activity Log**: everything done on the property, newest first, with who did it. Tabs: Everyone, People only, AI only.
- **System Health**: version, database, scheduler, disk space and time zone. Turn the scheduler on, or the night audit and reminders do not run by themselves.
- **Kamra Agent**: the AI helper. It needs an AI key before it works.
- **Revenue Reports**: month against the targets set in Revenue Budget. **Edit targets** changes them.
- **Central Reservations**: search one date range across every property.
- Channel Manager, OTA Room Mappings, WhatsApp and Payments are not set up for this hotel test.

---

## Part 8. Who can do what

| Task | Reception (Front Desk) | Restaurant (Kamra Agent) | Housekeeping | Finance |
|---|---|---|---|---|
| See bookings and bills | Yes | Yes | Bookings only | Yes |
| Make a booking | Yes | Yes | No | No |
| Cancel a booking | Yes | Yes | No | No |
| Post a charge on a bill | Yes | Yes | No | Yes |
| Refund money on a bill | Yes | Yes | No | Yes |
| Open a cashier till | Yes | Yes | No | Yes |
| Run the night audit | Yes | Yes | No | Yes |
| Change room notes | Yes | Yes | Yes | No |
| Change Property or Rate Plan | No | No | No | No |

- A housekeeping user sees only the Housekeeping app.
- The restaurant sample user has the role Kamra Agent, which is made for the AI helper and allows far more than a restaurant needs. Give restaurant staff a smaller role before real use.
- The four sample users have no password yet. Set one for each user before they sign in.

---

## Part 9. Before real use

- Turn the scheduler on: `bench --site <site> enable-scheduler`.
- Set a password for each staff user.
- Replace the sample company, agent, seasons and prices with the hotel's own.
- Connect WhatsApp and the payment gateway if the hotel wants automatic links and online payment.
- Read the file `issues-found` and decide which items must be fixed first.
