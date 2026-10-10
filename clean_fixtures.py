"""Run after `bench export-fixtures --app sr_continental_setup`.
Removes test leftovers so a new site starts with master data only:
python3 clean_fixtures.py
"""
import json
import os

FX = os.path.join(os.path.dirname(__file__), "sr_continental_setup", "fixtures")


def edit(name, fn):
	path = os.path.join(FX, name + ".json")
	if not os.path.exists(path):
		return
	data = json.load(open(path))
	data = fn(data)
	json.dump(data, open(path, "w"), indent=1, ensure_ascii=False)


def drop(keys):
	def f(rows):
		for r in rows:
			for k in keys:
				r.pop(k, None)
		return rows
	return f


def setval(**vals):
	def f(rows):
		for r in rows:
			r.update(vals)
		return rows
	return f


edit("property", drop(["business_date"]))              # set to today on install
edit("menu_item", drop(["recipe"]))                    # ingredient names differ per site
edit("city_ledger_account", setval(balance=0))         # no money owed on a new site
edit("discount_voucher", setval(times_used=0))         # no vouchers used yet
edit("room", setval(housekeeping_status="Clean"))      # all rooms start clean
edit("banquet_checklist_template",
     lambda rows: [r for r in rows if r.get("event_type")])  # drop the unnamed copies made by confirming a function
for stale in ("ingredient", "ingredient_stock"):
	p = os.path.join(FX, stale + ".json")
	if os.path.exists(p):
		os.remove(p)
print("fixtures cleaned")
