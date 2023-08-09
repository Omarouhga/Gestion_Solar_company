from odoo import _, api, fields, models

FUEL_TYPES = [
    ('diesel', 'Diesel'),
    ('gasoline', 'Gasoline'),
    ('hybrid', 'Hybrid Diesel'),
    ('full_hybrid_gasoline', 'Hybrid Gasoline'),
    ('plug_in_hybrid_diesel', 'Plug-in Hybrid Diesel'),
    ('plug_in_hybrid_gasoline', 'Plug-in Hybrid Gasoline'),
    ('cng', 'CNG'),
    ('lpg', 'LPG'),
    ('hydrogen', 'Hydrogen'),
    ('electric', 'Electric'),
]
class VehicleModel(models.Model):
    _name = 'vehicle.model'
    _description = 'Model of a vehicle'
    _order = 'name asc'

    name = fields.Char('Model name', required=True)
    brand_id = fields.Many2one('vehicle.model.brand', 'Fabriquant', required=True, help='fabriquant de  véhicule')
    image_128 = fields.Image(related='brand_id.image_128', readonly=True)
    model_year = fields.Integer(string="Année de modèle")
    default_fuel_type = fields.Selection(FUEL_TYPES, 'Fuel Type', default='diesel')
    active = fields.Boolean(default=True)

