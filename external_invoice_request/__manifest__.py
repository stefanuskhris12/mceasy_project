{
    "name": "External Invoice Request",
    "version": "1.0",
    "depends": ["sale", "account", "website"],
    "data": [
        "views/external_invoice_template.xml",
        "views/res_partner_views.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "external_invoice_request/static/src/components/external_invoice_form.js",
            "external_invoice_request/static/src/components/external_invoice_form.xml",
        ],
    },
    "installable": True,
    "license": "LGPL-3",
}
