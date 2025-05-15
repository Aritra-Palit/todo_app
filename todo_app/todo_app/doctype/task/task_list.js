frappe.listview_settings['Task'] = {
    add_fields: ["status", "due_date", "priority"],

    get_indicator: function (doc) {
        const colors = {
            "To-Do": "gray",
            "In Progress": "orange",
            "Done": "green"
        };
        return [__(doc.status), colors[doc.status], "status,=," + doc.status];
    }
};

