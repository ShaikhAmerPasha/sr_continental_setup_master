import frappe

def setup():
    # 1. Create Property
    property_name = "SR Continental"
    if not frappe.db.exists("Property", property_name):
        try:
            frappe.get_doc({
                "doctype": "Property",
                "property_name": property_name,
                "country": "India",
                "currency": "INR",
                "timezone": "Asia/Kolkata",
                "check_in_time": "14:00:00",
                "check_out_time": "11:00:00",
                "booking_payment_mode": "Advance percent",
                "advance_percent": 50
            }).insert(ignore_permissions=True)
            print("Created Property: SR Continental")
        except Exception as e:
            print(f"Property might already exist or error: {e}")

    # 2. Create Room Types
    room_types = [
        {"doctype": "Room Type", "type_name": "Deluxe Room", "base_price": 2500, "base_capacity": 2, "property": property_name},
        {"doctype": "Room Type", "type_name": "Premier Room", "base_price": 3500, "base_capacity": 2, "property": property_name},
        {"doctype": "Room Type", "type_name": "Suite Room", "base_price": 5000, "base_capacity": 2, "property": property_name}
    ]
    
    for rt in room_types:
        if not frappe.db.exists("Room Type", rt["type_name"]):
            try:
                frappe.get_doc(rt).insert(ignore_permissions=True)
                print(f"Created Room Type: {rt['type_name']}")
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
        if not frappe.db.exists("Room", r["room_number"]):
            try:
                frappe.get_doc(r).insert(ignore_permissions=True)
                print(f"Created Room: {r['room_number']}")
            except Exception as e:
                print(e)

    # 4. Create Meal Plans
    meal_plans = [
        {"doctype": "Meal Plan", "plan_name": "EP", "property": property_name},
        {"doctype": "Meal Plan", "plan_name": "CP", "property": property_name},
        {"doctype": "Meal Plan", "plan_name": "MAP", "property": property_name}
    ]
    
    for mp in meal_plans:
        if not frappe.db.exists("Meal Plan", mp["plan_name"]):
            try:
                frappe.get_doc(mp).insert(ignore_permissions=True)
                print(f"Created Meal Plan: {mp['plan_name']}")
            except Exception as e:
                print(e)

    frappe.db.commit()
    print("Configuration complete!")
