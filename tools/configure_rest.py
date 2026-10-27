import frappe

def setup():
    property_name = "SR Continental"
    
    # Create POS Outlets
    outlets = [
        {"doctype": "POS Outlet", "outlet_name": "Main Restaurant", "property": property_name, "gst_rate": 5, "tables": "T1\nT2\nT3"},
        {"doctype": "POS Outlet", "outlet_name": "In-Room Dining", "property": property_name, "gst_rate": 5}
    ]
    
    for outlet in outlets:
        if not frappe.db.exists("POS Outlet", {"outlet_name": outlet["outlet_name"]}):
            try:
                frappe.get_doc(outlet).insert(ignore_permissions=True)
                print(f"Created POS Outlet: {outlet['outlet_name']}")
            except Exception as e:
                print(e)
                
    # Create Laundry Rates
    laundry_rates = [
        {"doctype": "Laundry Rate", "item_name": "Shirt - Wash & Iron", "rate": 100, "property": property_name},
        {"doctype": "Laundry Rate", "item_name": "Trouser - Wash & Iron", "rate": 120, "property": property_name},
        {"doctype": "Laundry Rate", "item_name": "Suit - Dry Clean", "rate": 350, "property": property_name}
    ]

    for lr in laundry_rates:
        if not frappe.db.exists("Laundry Rate", {"item_name": lr["item_name"]}):
            try:
                frappe.get_doc(lr).insert(ignore_permissions=True)
                print(f"Created Laundry Rate: {lr['item_name']}")
            except Exception as e:
                print(e)
                
    frappe.db.commit()
    print("Restaurant and Laundry configuration complete!")
