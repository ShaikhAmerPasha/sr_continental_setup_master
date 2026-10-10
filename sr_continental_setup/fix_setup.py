import frappe

def setup():
    property_name = "SR Continental"
    
    # 2. Create Room Types
    room_types = [
        {"doctype": "Room Type", "room_type_name": "Deluxe Room", "room_type_code": "DLX", "type_name": "Deluxe Room", "base_price": 2500, "base_capacity": 2, "property": property_name},
        {"doctype": "Room Type", "room_type_name": "Premier Room", "room_type_code": "PRM", "type_name": "Premier Room", "base_price": 3500, "base_capacity": 2, "property": property_name},
        {"doctype": "Room Type", "room_type_name": "Suite Room", "room_type_code": "STE", "type_name": "Suite Room", "base_price": 5000, "base_capacity": 2, "property": property_name}
    ]
    
    for rt in room_types:
        if not frappe.db.exists("Room Type", {"room_type_name": rt["room_type_name"]}):
            try:
                frappe.get_doc(rt).insert(ignore_permissions=True)
                print(f"Created Room Type: {rt['room_type_name']}")
            except Exception as e:
                print(e)

    # 3. Create Rooms
    rooms = [
        {"doctype": "Room", "room_number": "101", "room_type": "Deluxe Room", "property": property_name},
        {"doctype": "Room", "room_number": "102", "room_type": "Deluxe Room", "property": property_name},
        {"doctype": "Room", "room_number": "103", "room_type": "Deluxe Room", "property": property_name},
        {"doctype": "Room", "room_number": "201", "room_type": "Premier Room", "property": property_name},
        {"doctype": "Room", "room_number": "202", "room_type": "Premier Room", "property": property_name},
        {"doctype": "Room", "room_number": "301", "room_type": "Suite Room", "property": property_name},
    ]
    
    for r in rooms:
        if not frappe.db.exists("Room", {"room_number": r["room_number"]}):
            try:
                frappe.get_doc(r).insert(ignore_permissions=True)
                print(f"Created Room: {r['room_number']}")
            except Exception as e:
                print(e)

    frappe.db.commit()
    print("Room configuration complete!")
