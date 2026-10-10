# SR Continental Setup

Frappe app that loads the starter master data for SR Continental (a Kamra PMS hotel) when it is installed on a new site.

## Install on a new site
```
bench get-app kamra <kamra repo url>
bench get-app sr_continental_setup <this repo url>
bench new-site <site> 
bench --site <site> install-app payments kamra sr_continental_setup
bench --site <site> enable-scheduler
```
Kamra must be installed first (`required_apps` enforces it).

## What loads
- `fixtures/*.json`: property, room types, rooms, sellable units, rate plans, meal plans, transaction codes, POS outlets, menu items, laundry rates, reason codes, seasons, turnover profiles, guardrails, hurdle rates, exchange rates, vouchers, revenue budgets, corporate account, city ledger account, travel agent, venues, banquet dishes, menus, services and checklists, experiences.
- `install.py` creates the 4 staff users (reception, restaurant, housekeeping, finance), the 2 cashiers, and sets the hotel date to today.
- Staff users get **no password**. Set one for each user after install.

## Notes
- Fixtures load again on every `bench migrate` and overwrite edits made on the site.
- Ingredients, ingredient stock and menu recipes are left out on purpose (their names are numbered by the site).
- After `bench export-fixtures`, run `python3 clean_fixtures.py`. It removes test leftovers (business date, recipes, city ledger balance, voucher use counts, dirty rooms, duplicate checklists).
- Only master data is in the app. No reservations, bills, orders, guests, tills or housekeeping tasks are installed.
- Payment gateway, channel connections and ZATCA are not set up.
