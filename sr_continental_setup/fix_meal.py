import frappe

def setup():
    property_name = "SR Continental"
    
    # Create Meal Plans with correct fields
    meal_plans = [
        {"doctype": "Meal Plan", "code": "CP", "label": "Continental Plan", "property": property_name},
        {"doctype": "Meal Plan", "code": "MAP", "label": "Modified American Plan", "property": property_name}
    ]
    
    for mp in meal_plans:
        if not frappe.db.exists("Meal Plan", {"code": mp["code"], "property": property_name}):
            try:
                frappe.get_doc(mp).insert(ignore_permissions=True)
                print(f"Created Meal Plan: {mp['code']}")
            except Exception as e:
                print(e)
                
    # Fix the existing EP one to have a label
    if frappe.db.exists("Meal Plan", {"code": "EP", "property": property_name}):
        doc = frappe.get_doc("Meal Plan", {"code": "EP", "property": property_name})
        if not doc.label:
            doc.label = "European Plan"
            doc.save(ignore_permissions=True)
            
    frappe.db.commit()
    print("Meal Plans Fixed!")
