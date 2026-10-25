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
	"""Fixture sync blanks the hotel date, so remember it first."""
	prop = frappe.db.get_value("Property", {}, "name")
	if prop:
		date = frappe.db.get_value("Property", prop, "business_date")
		frappe.db.set_default("sr_saved_business_date", str(date) if date else "")


def after_migrate():
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
