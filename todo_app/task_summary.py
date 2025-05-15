def execute(filters=None):
    from frappe import db

    data = db.sql("""
        SELECT status, COUNT(*) as total
        FROM `tabTask`
        GROUP BY status
    """, as_dict=True)

    columns = [
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 150},
        {"label": "Total Tasks", "fieldname": "total", "fieldtype": "Int", "width": 100},
    ]

    return columns, data

