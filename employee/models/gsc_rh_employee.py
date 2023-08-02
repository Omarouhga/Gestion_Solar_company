from odoo import models,fields,api
from odoo.exceptions import ValidationError
import re


class GSCRhemployee(models.Model):
    _name="hr.employee"
    _inherit = ["hr.employee", "resource.resource"]
    _rec_name="name"
    _check_company_auto = True
    
    name=fields.Char(string='Nom complet')
    nom=fields.Char(string="Nom",required=True)
    prenom = fields.Char(string="Prénom", required=True)
    nom_ar=fields.Char(string="إسم العائلي")
    prenom_ar = fields.Char(string="إسم الشخصي")
    
    company_id=fields.Many2one("res.company",required=True,string="Etablissement",default=lambda self:self.env.user.company_id)

    gendre=fields.Selection([('F','Femme'),('M','Homme'),('u','autre')],string="Genre")
    tel = fields.Char(string="Télephone")
    email=fields.Char(string="Email")
    date_naiss = fields.Date(string='Date de naissance')
    Lieu_Naissance=fields.Char(string="Lieu de naissance")
    cin = fields.Char(string="CIN")
    adresse=fields.Char(string="Adresse")
    situation_familiale=fields.Selection(string="situation familiale", selection=([('m','marié'),('c','célibataire')]))
    
    salaire = fields.Integer(string="Salaire")
    avance = fields.Integer(string="Avance")
    rest_salaire = fields.Integer(string="Reste du salaire", compute="_compute_reste_salaire")
    
    @api.onchange("nom","prenom","name")
    def compute_name(self):
        for rec in self:
            rec.name=""
            if  rec.nom :
                rec.name=rec.name+rec.nom.upper()+" "
            if rec.prenom :
                rec.name=rec.name+rec.prenom.title()+" "  

    @api.depends('salaire', 'avance')
    def _compute_reste_salaire(self):
        for rec in self:
            rec.rest_salaire = rec.salaire - rec.avance