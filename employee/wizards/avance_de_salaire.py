from odoo import models,fields,api
from odoo import exceptions

class GSCAvanceWizard(models.TransientModel):
    _name="gsc.avance.wizard"
    _description="avance de salaire"
   
    avancement=fields.Integer("Avancement")
    
    def avancement_salaire(self):
        employee=self.env['hr.employee'].browse(self.env.context.get('active_id'))    
        employee.avance+=self.avancement
