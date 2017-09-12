# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models
from odoo import fields
from odoo import api

class res_partner(models.Model):
    _inherit="res.partner"
    
    order_block = fields.Boolean(string="Blocked from orders")