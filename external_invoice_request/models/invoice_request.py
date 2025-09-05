from odoo import models, fields, api
import uuid

class InvoiceRequest(models.Model):
    _name = "invoice.request"
    _description = "Invoice Request"

    partner_id = fields.Many2one(
        "res.partner",
        string="Partner"
    )

    sale_id = fields.Many2one(
        "sale.order",
        string="SO"
    )
    
    invoice_id = fields.Many2one(
        "account.move",
        string="Invoice"
    )

    status = fields.Selection([
        ("pending", "Pending"), 
        ("approved", "Approved")
        ],default="pending",
    )

    def action_approve(self):
        for rec in self:
            if rec.status == "pending":
                invoice = rec.sale_id._create_invoices()
                invoice.action_post()
                rec.write({
                    "invoice_id": invoice.id,
                    "status": "approved"
                })
