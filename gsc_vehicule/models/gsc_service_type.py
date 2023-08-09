from odoo import fields, models


class GscServiceType(models.Model):
    _name = 'service.type'
    _description = 'Type de service pour les véhicules'

    name = fields.Char(required=True, translate=True)