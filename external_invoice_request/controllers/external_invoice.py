from odoo import http
from odoo.http import request

class ExternalInvoiceController(http.Controller):

    @http.route('/external/sale-invoice/<string:token>', type="http", auth="public", website=True)
    def external_sale_invoice(self, token, **kwargs):
        partner = request.env["res.partner"].sudo().search([("external_token", "=", token)], limit=1)
        if not partner:
            return "Invalid token"

        sale_orders = request.env["sale.order"].sudo().search([
            ("partner_id", "=", partner.id),
            ("state", "=", "sale"),
            ("invoice_status", "=", "to invoice")
        ])

        partner_data = {
            "id": partner.id,
            "name": partner.name,
            "external_token": partner.external_token,
        }
        sale_orders_data = [
            {"id": so.id, "name": so.name, "amount_total": so.amount_total}
            for so in sale_orders
        ]

        return request.render("external_invoice_request.external_invoice_page", {
            "partner": partner_data,
            "sale_orders": sale_orders_data,
        })

    @http.route('/external/request-invoice', type="json", auth="public", website=True, csrf=False)
    def request_invoice(self, sale_order_id, token):
        partner = request.env["res.partner"].sudo().search([("external_token", "=", token)], limit=1)
        if not partner:
            return {"error": "Invalid token"}

        sale_order = request.env["sale.order"].sudo().browse(int(sale_order_id))
        if not sale_order or sale_order.partner_id.id != partner.id:
            return {"error": "Sale order not found"}

        inv_req = request.env["invoice.request"].sudo().create({
            "partner_id": partner.id,
            "sale_id": sale_order.id,
        })

        return {"success": True, "request_id": inv_req.id}
