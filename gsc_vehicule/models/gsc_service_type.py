from odoo import fields, models


class GscServiceType(models.Model):
    _inherit= 'fleet.service.type'
    _description = 'Type de service pour les véhicules'

    category = fields.Char(readonly=True, store=False)
