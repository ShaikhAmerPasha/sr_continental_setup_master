import frappe

def setup():
    property_name = "SR Continental"
    rooms = [
        {"doctype": "Room", "room_number": "101", "room_type": "SR Continental-DLX", "property": property_name},
        {"doctype": "Room", "room_number": "102", "room_type": "SR Continental-DLX", "property": property_name},
        {"doctype": "Room", "room_number": "103", "room_type": "SR Continental-DLX", "property": property_name},
        {"doctype": "Room", "room_number": "201", "room_type": "SR Continental-PRM", "property": property_name},
        {"doctype": "Room", "room_number": "202", "room_type": "SR Continental-PRM", "property": property_name},
        {"doctype": "Room", "room_number": "301", "room_type": "SR Continental-STE", "property": property_name},
    ]
    
    for r in rooms:
        if not frappe.db.exists("Room", {"room_number": r["room_number"]}):
            try:
                frappe.get_doc(r).insert(ignore_permissions=True)
                print(f"Created Room: {r['room_number']}")
            except Exception as e:
                print(e)
    frappe.db.commit()
    print("Rooms created!")
