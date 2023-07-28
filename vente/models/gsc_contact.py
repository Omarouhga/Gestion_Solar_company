from odoo import models,fields,api,_
from odoo import exceptions
import re
import datetime


class GSCContatct(models.Model):
    _inherit=["res.partner"]

    