import frappe

def setup():
    users = [
        {"email": "reception@srcontinental.com", "first_name": "Reception", "role": "Front Desk"},
        {"email": "restaurant@srcontinental.com", "first_name": "Restaurant", "role": "Kamra Agent"},
        {"email": "housekeeping@srcontinental.com", "first_name": "Housekeeping", "role": "Housekeeping"},
        {"email": "finance@srcontinental.com", "first_name": "Finance", "role": "Finance"}
    ]
    
    for u in users:
        if not frappe.db.exists("User", u["email"]):
            try:
                user = frappe.get_doc({
                    "doctype": "User",
                    "email": u["email"],
                    "first_name": u["first_name"],
                    "send_welcome_email": 0,
                    "roles": [{"role": u["role"]}]
                })
                user.insert(ignore_permissions=True)
                print(f"Created user {u['email']} with role {u['role']}")
            except Exception as e:
                print(e)

    frappe.db.commit()
    print("Users configured.")
