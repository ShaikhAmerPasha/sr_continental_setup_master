import json

import frappe
from frappe.utils import today

USERS_AND_CASHIERS = (("CSH-REC", "reception@srcontinental.com"),
                      ("CSH-RST", "restaurant@srcontinental.com"))


def after_install():
	"""Bench runs this before it loads the fixtures, so load them first.
	Users and cashiers link to the fixtures, so they come after."""
	from frappe.utils.fixtures import sync_fixtures
	sync_fixtures("sr_continental_setup")
	ensure_users_and_cashiers()
	set_business_date_if_blank()


def before_migrate():
	"""Fixture sync blanks the hotel date and resets every room, so remember
	both first."""
	save_room_status()
	prop = frappe.db.get_value("Property", {}, "name")
	if prop:
		date = frappe.db.get_value("Property", prop, "business_date")
		frappe.db.set_default("sr_saved_business_date", str(date) if date else "")


def after_migrate():
	restore_room_status()
	ensure_users_and_cashiers()
	saved = frappe.db.get_default("sr_saved_business_date")
	prop = frappe.db.get_value("Property", {}, "name")
	if saved and prop and not frappe.db.get_value("Property", prop, "business_date"):
		frappe.db.set_value("Property", prop, "business_date", saved)
	set_business_date_if_blank()


def ensure_users_and_cashiers():
	from sr_continental_setup.configure_users import setup
	setup()
	prop = frappe.db.get_value("Property", {}, "name")
	if not prop:
		return
	for cashier_id, user in USERS_AND_CASHIERS:
		if frappe.db.exists("User", user) and not frappe.db.exists("Cashier", cashier_id):
			frappe.get_doc({"doctype": "Cashier", "cashier_id": cashier_id,
			                "user": user, "property": prop}).insert(ignore_permissions=True)
	frappe.db.commit()


def set_business_date_if_blank():
	"""The hotel date starts at today on a new site and is moved by the
	night audit after that. The fixture file leaves it out on purpose."""
	prop = frappe.db.get_value("Property", {}, "name")
	if prop and not frappe.db.get_value("Property", prop, "business_date"):
		frappe.db.set_value("Property", prop, "business_date", today())
		frappe.db.commit()


ROOM_STATUS_DEFAULTS = {"occupancy_status": "Vacant", "housekeeping_status": "Clean"}


def save_room_status():
	"""Fixture sync deletes and re-inserts each room, which would free
	occupied rooms and undo housekeeping. Keep the live values."""
	rows = frappe.get_all("Room", fields=["name", *ROOM_STATUS_DEFAULTS], limit=0)
	frappe.db.set_default("sr_saved_room_status", json.dumps(
		{r.name: {k: r[k] for k in ROOM_STATUS_DEFAULTS} for r in rows}))


def restore_room_status():
	"""Put the live status back after the fixture sync. A room with no
	status gets the default, because the Front Desk screen fails on a blank."""
	saved = json.loads(frappe.db.get_default("sr_saved_room_status") or "{}")
	rooms = frappe.get_all("Room", fields=["name", *ROOM_STATUS_DEFAULTS], limit=0)
	for current in rooms:
		name = current.name
		values = {k: saved.get(name, {}).get(k) or current[k] or default
		          for k, default in ROOM_STATUS_DEFAULTS.items()}
		if any(values[k] != current[k] for k in values):
			frappe.db.set_value("Room", name, values, update_modified=False)
	frappe.db.set_default("sr_saved_room_status", "")
	frappe.db.commit()
