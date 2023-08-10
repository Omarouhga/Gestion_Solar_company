from odoo import models,fields,api

class Vidange(models.Model):
    _name = 'gsc.vidange'
    _description = 'Modèle pour le suivi des opérations de vidange'
    _rec_name="name"

    STATE_SELECTION = [
        ('impaye', 'Vidange impayée'),
        ('paye', 'Vidange payée')
    ]
    name = fields.Char(compute='_compute_name', store=False)
    voiture_id = fields.Many2one('fleet.vehicle', string="Voiture",required=True)
    date_vidange = fields.Date(string="Date de vidange")
    kilometrage = fields.Float(string="Kilométrage au moment de la vidange")
    montant = fields.Float(string="Montant de la vidange")
    kilometrage_huile = fields.Float(string="Kilométrage d'huile")
    state = fields.Selection(STATE_SELECTION, string="État de vidange", default='impaye')
    
    @api.depends('voiture_id', 'date_vidange')
    def _compute_name(self):
        for record in self:
            if record.voiture_id and record.date_vidange:
                record.name = f"Vidange {record.voiture_id.name} - {record.date_vidange}"
            else:
                record.name = "Vidange non défini"

    
   
    def mark_as_paid(self):
        self.state = 'paye'

    def mark_as_unpaid(self):
        self.state = 'impaye'


class Gasoil(models.Model):
    _name = 'gsc.gasoil'
    _description = 'Modèle pour le suivi des transactions de carburant'
    _rec_name="name"

    STATE_SELECTION = [
        ('impaye', 'Gasoil impayée'),
        ('paye', 'Gasoil payée')
    ]
    name = fields.Char(compute='_compute_name', store=False)
    voiture_id = fields.Many2one('fleet.vehicle', string="Voiture",required=True)
    date_ravitaillement = fields.Date(string="Date")
    quantite_carburant = fields.Float(string="Quantité de carburant ajoutée")
    prix_carburant = fields.Float(string="Prix du carburant")
    kilometrage = fields.Float(string="Kilométrage")
    state = fields.Selection(STATE_SELECTION, default='impaye')
    chauffeur_id=fields.Many2one('res.users',string='Chauffeur')
    def mark_as_paid(self):
        self.state = 'paye'

    def create_invoices(self):
        sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))

        if self.advance_payment_method == 'delivered':
            sale_orders._create_invoices(final=self.deduct_down_payments)
    

    @api.depends('voiture_id', 'date_ravitaillement')
    def _compute_name(self):
        for record in self:
            if record.voiture_id and record.date_ravitaillement:
                record.name = f"Gasoil {record.voiture_id.name} - {record.date_ravitaillement}"
            else:
                record.name = "Gasoil non défini"

class GscVehiculeService(models.Model):
    _inherit = 'fleet.vehicle.log.services'
    
    TYPE_SELECTION = [
        ('service', 'Service'),
        ('gasoil', 'Gasoil'),
        ('vidange','Vidange')
    ]
    
    service_type_id=fields.Selection(TYPE_SELECTION,string='Type',default='service')
    km_huil=fields.Float(string="Km huil")
    code_sortie=fields.Char(string="Code de sortie",placeholder="14-130723")
