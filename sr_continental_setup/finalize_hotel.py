import frappe

def setup():
    property_name = "SR Continental"
    
    # 1. Update Property details (GST, Policies, Check-in/out)
    if frappe.db.exists("Property", property_name):
        doc = frappe.get_doc("Property", property_name)
        # GST Setup (from 2025 guidelines in prompt)
        doc.gstin = "29SRCON1234HOTL"
        doc.gst_mode = "Slab"
        doc.gst_slab_threshold = 7500
        doc.gst_rate_low = 5
        doc.gst_rate_high = 12
        doc.rates_include_tax = 0
        
        # Policies
        doc.checkin_time = "12:00:00"
        doc.checkout_time = "11:00:00"
        doc.free_cancel_days = 2
        doc.cancellation_fee = "First Night"
        doc.advance_percent = 50
        
        doc.save(ignore_permissions=True)
        print("Updated Property GST and Policies.")
        
    # 2. Create Standard Rate Plan
    rate_plan = {
        "doctype": "Rate Plan",
        "code": "STD",
        "rate_plan_name": "Standard Rate",
        "property": property_name,
        "is_default": 1
    }
    
    if not frappe.db.exists("Rate Plan", {"code": "STD", "property": property_name}):
        frappe.get_doc(rate_plan).insert(ignore_permissions=True)
        print("Created Standard Rate Plan.")
        
    frappe.db.commit()
    print("Hotel configuration completely finalized.")
