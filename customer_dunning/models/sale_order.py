# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models
from odoo import fields
from odoo import api
from odoo.exceptions import UserError, ValidationError



class sale_order(models.Model):
    _inherit="sale.order"    
        
    @api.onchange('partner_id')
    def onchange_partner_id_dunning(self):
        if self.partner_id.order_block:
            self.partner_id = False    
    