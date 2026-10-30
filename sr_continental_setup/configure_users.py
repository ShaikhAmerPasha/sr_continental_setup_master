import frappe

ALL_ROLES = ["System Manager", "Hotel Admin", "Front Desk", "Kamra Agent",
             "Housekeeping", "Finance", "Accounts Manager"]


def setup():
    users = [
        {"email": "reception@srcontinental.com", "first_name": "Reception", "roles": ["Front Desk"]},
        {"email": "restaurant@srcontinental.com", "first_name": "Restaurant", "roles": ["Kamra Agent"]},
        {"email": "housekeeping@srcontinental.com", "first_name": "Housekeeping", "roles": ["Housekeeping"]},
        {"email": "finance@srcontinental.com", "first_name": "Finance", "roles": ["Finance"]},
        {"email": "kavita@srcontinental.com", "first_name": "Kavita", "roles": ALL_ROLES, "keep_roles": True},
    ]

    for u in users:
        try:
            if not frappe.db.exists("User", u["email"]):
                user = frappe.get_doc({
                    "doctype": "User",
                    "email": u["email"],
                    "first_name": u["first_name"],
                    "send_welcome_email": 0,
                    "user_type": "System User",
                    "roles": [{"role": r} for r in u["roles"]],
                })
                user.insert(ignore_permissions=True)
                print(f"Created user {u['email']} with roles {', '.join(u['roles'])}")
            elif u.get("keep_roles"):
                # a user made by hand may have no roles and be a Website User
                user = frappe.get_doc("User", u["email"])
                have = {r.role for r in user.roles}
                missing = [r for r in u["roles"] if r not in have]
                if missing or user.user_type != "System User":
                    user.user_type = "System User"
                    for r in missing:
                        user.append("roles", {"role": r})
                    user.save(ignore_permissions=True)
        except Exception as e:
            print(e)

    frappe.db.commit()
    print("Users configured.")
