import frappe

def setup():
    property_name = "SR Continental"
    outlet_name = "Main Restaurant"
    
    # 1. Detailed Menu Items
    menu_items = [
        # Starters
        {"doctype": "Menu Item", "item_name": "Paneer Tikka", "category": "Starters", "price": 250, "is_veg": 1, "prep_station": "Tandoor", "property": property_name, "outlet": outlet_name, "available": 1},
        {"doctype": "Menu Item", "item_name": "Chicken Tikka", "category": "Starters", "price": 350, "is_veg": 0, "prep_station": "Tandoor", "property": property_name, "outlet": outlet_name, "available": 1},
        {"doctype": "Menu Item", "item_name": "Crispy Corn", "category": "Starters", "price": 180, "is_veg": 1, "prep_station": "Fryer", "property": property_name, "outlet": outlet_name, "available": 1},
        
        # Main Course
        {"doctype": "Menu Item", "item_name": "Butter Chicken", "category": "Main Course", "price": 450, "is_veg": 0, "prep_station": "Kitchen", "property": property_name, "outlet": outlet_name, "available": 1},
        {"doctype": "Menu Item", "item_name": "Dal Makhani", "category": "Main Course", "price": 280, "is_veg": 1, "prep_station": "Kitchen", "property": property_name, "outlet": outlet_name, "available": 1},
        {"doctype": "Menu Item", "item_name": "Paneer Butter Masala", "category": "Main Course", "price": 320, "is_veg": 1, "prep_station": "Kitchen", "property": property_name, "outlet": outlet_name, "available": 1},
        
        # Breads
        {"doctype": "Menu Item", "item_name": "Garlic Naan", "category": "Breads", "price": 60, "is_veg": 1, "prep_station": "Tandoor", "property": property_name, "outlet": outlet_name, "available": 1},
        {"doctype": "Menu Item", "item_name": "Tandoori Roti", "category": "Breads", "price": 30, "is_veg": 1, "prep_station": "Tandoor", "property": property_name, "outlet": outlet_name, "available": 1},
        
        # Beverages
        {"doctype": "Menu Item", "item_name": "Fresh Lime Soda", "category": "Beverages", "price": 120, "is_veg": 1, "prep_station": "Bar", "property": property_name, "outlet": outlet_name, "available": 1},
        {"doctype": "Menu Item", "item_name": "Cold Coffee", "category": "Beverages", "price": 150, "is_veg": 1, "prep_station": "Bar", "property": property_name, "outlet": outlet_name, "available": 1},
    ]

    for item in menu_items:
        if not frappe.db.exists("Menu Item", {"item_name": item["item_name"]}):
            try:
                frappe.get_doc(item).insert(ignore_permissions=True)
                print(f"Created Menu Item: {item['item_name']}")
            except Exception as e:
                print(f"Error creating {item['item_name']}: {e}")

    # 2. Detailed Laundry Rates
    laundry_rates = [
        {"doctype": "Laundry Rate", "item_name": "Shirt - Wash Only", "rate": 80, "property": property_name},
        {"doctype": "Laundry Rate", "item_name": "Shirt - Iron Only", "rate": 50, "property": property_name},
        {"doctype": "Laundry Rate", "item_name": "Trouser - Wash Only", "rate": 90, "property": property_name},
        {"doctype": "Laundry Rate", "item_name": "Trouser - Iron Only", "rate": 60, "property": property_name},
        {"doctype": "Laundry Rate", "item_name": "Undergarments - Wash", "rate": 40, "property": property_name},
        {"doctype": "Laundry Rate", "item_name": "Socks (Pair) - Wash", "rate": 30, "property": property_name},
        {"doctype": "Laundry Rate", "item_name": "Jacket - Dry Clean", "rate": 400, "property": property_name},
        {"doctype": "Laundry Rate", "item_name": "Dress - Dry Clean", "rate": 450, "property": property_name},
    ]

    for lr in laundry_rates:
        if not frappe.db.exists("Laundry Rate", {"item_name": lr["item_name"]}):
            try:
                frappe.get_doc(lr).insert(ignore_permissions=True)
                print(f"Created Laundry Rate: {lr['item_name']}")
            except Exception as e:
                print(e)

    frappe.db.commit()
    print("Detailed Menu and Laundry configurations complete!")
