from odoo import fields, models

class Voiture(models.Model):
    _inherit = 'fleet.vehicle'
    _description = 'Modèle pour la gestion des voitures de service'
    

    # name = fields.Char(string="Plaque d'immatriculation", required=True)
    # model_id = fields.Many2one('vehicle.model', 'Modèle',
    #     tracking=True, required=True, help='Modèle de véhicule')    
    # kilometrage_actuel = fields.Float(string="Kilométrage actuel", compute="compute_kilometrage_actuel")
    # image_128 = fields.Image(related='model_id.image_128', readonly=True)
    # etat_general = fields.Selection([
    #     ('excellent', 'Excellent'),
    #     ('bon', 'Bon'),
    #     ('moyen', 'Moyen'),
    #     ('mauvais', 'Mauvais')
    # ], string="État général")
    # vidanges_ids = fields.One2many('gsc.vidange', 'voiture_id', string="Opérations de vidange")
    # gasoil_ids = fields.One2many('gsc.gasoil', 'voiture_id', string="Transactions de carburant")
   
    # def compute_kilometrage_actuel(self):
    #     for voiture in self:
    #         total_kilometrage = 0.0
            
    #         for vidange in voiture.vidanges_ids:
    #             total_kilometrage = vidange.kilometrage
            
    #         for gasoil in voiture.gasoil_ids:
    #             total_kilometrage = gasoil.kilometrage
                
    #         voiture.kilometrage_actuel = total_kilometrage




