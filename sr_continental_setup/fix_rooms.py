import frappe

def setup():
    property_name = "SR Continental"
    
    # 30 Rooms configuration as specified
    rooms_data = [
        # Floor 1
        {"room_number": "101", "floor": "1", "room_type": "SR Continental-SPRM"},
        {"room_number": "102", "floor": "1", "room_type": "SR Continental-PRM"},
        {"room_number": "103", "floor": "1", "room_type": "SR Continental-PRM"},
        {"room_number": "104", "floor": "1", "room_type": "SR Continental-PRM"},
        # Floor 2
        {"room_number": "201", "floor": "2", "room_type": "SR Continental-DLX"},
        {"room_number": "202", "floor": "2", "room_type": "SR Continental-DLX"},
        {"room_number": "203", "floor": "2", "room_type": "SR Continental-DLXT"},
        {"room_number": "204", "floor": "2", "room_type": "SR Continental-SPRM"},
        {"room_number": "205", "floor": "2", "room_type": "SR Continental-PRM"},
        {"room_number": "206", "floor": "2", "room_type": "SR Continental-PRM"},
        {"room_number": "207", "floor": "2", "room_type": "SR Continental-PRM"},
        {"room_number": "208", "floor": "2", "room_type": "SR Continental-PRMT"},
        # Floor 3
        {"room_number": "301", "floor": "3", "room_type": "SR Continental-DLX"},
        {"room_number": "302", "floor": "3", "room_type": "SR Continental-DLX"},
        {"room_number": "303", "floor": "3", "room_type": "SR Continental-DLXT"},
        {"room_number": "304", "floor": "3", "room_type": "SR Continental-SPRM"},
        {"room_number": "305", "floor": "3", "room_type": "SR Continental-PRM"},
        {"room_number": "306", "floor": "3", "room_type": "SR Continental-PRM"},
        {"room_number": "307", "floor": "3", "room_type": "SR Continental-PRM"},
        {"room_number": "308", "floor": "3", "room_type": "SR Continental-PRMT"},
        # Floor 4
        {"room_number": "401", "floor": "4", "room_type": "SR Continental-DLX"},
        {"room_number": "402", "floor": "4", "room_type": "SR Continental-DLX"},
        {"room_number": "403", "floor": "4", "room_type": "SR Continental-DLXT"},
        {"room_number": "404", "floor": "4", "room_type": "SR Continental-SPRM"},
        {"room_number": "405", "floor": "4", "room_type": "SR Continental-PRM"},
        {"room_number": "406", "floor": "4", "room_type": "SR Continental-PRM"},
        {"room_number": "407", "floor": "4", "room_type": "SR Continental-PRM"},
        {"room_number": "408", "floor": "4", "room_type": "SR Continental-PRMT"},
        # Floor 5
        {"room_number": "501", "floor": "5", "room_type": "SR Continental-STE"},
        {"room_number": "502", "floor": "5", "room_type": "SR Continental-STE"},
    ]

    for r in rooms_data:
        room_name = f"{property_name}-{r['room_number']}"
        if not frappe.db.exists("Room", room_name):
            doc = frappe.get_doc({
                "doctype": "Room",
                "room_number": r["room_number"],
                "floor": r["floor"],
                "room_type": r["room_type"],
                "property": property_name,
                "housekeeping_status": "Clean",
                "occupancy_status": "Vacant"
            })
            doc.insert(ignore_permissions=True)
            print(f"Created Room: {r['room_number']}")
        else:
            frappe.db.set_value("Room", room_name, {
                "room_type": r["room_type"],
                "floor": r["floor"]
            })
            print(f"Updated Room: {r['room_number']}")

        # Ensure Sellable Unit exists
        unit_name = f"{property_name}-Room {r['room_number']}"
        if not frappe.db.exists("Sellable Unit", unit_name):
            su = frappe.get_doc({
                "doctype": "Sellable Unit",
                "unit_name": f"Room {r['room_number']}",
                "property": property_name,
                "room_type": r["room_type"],
                "unit_kind": "individual",
                "is_active": 1,
                "is_auto_assignable": 1,
                "base_occupancy": 2,
                "competition_group": f"{property_name}::{r['room_type']}",
                "physical_rooms": [{"room": room_name}]
            })
            su.insert(ignore_permissions=True)
            print(f"Created Sellable Unit for Room {r['room_number']}")
        else:
            frappe.db.set_value("Sellable Unit", unit_name, {
                "room_type": r["room_type"],
                "is_active": 1,
                "competition_group": f"{property_name}::{r['room_type']}"
            })

    frappe.db.commit()
    print("All 30 Rooms & Sellable Units configured successfully!")
