from odoo import models, fields
import uuid

class ResPartner(models.Model):
    _inherit = "res.partner"

    external_token = fields.Char("External Token", readonly=True)

    def action_generate_token(self):
        for partner in self:
            if not partner.external_token:
                partner.external_token = str(uuid.uuid4())
