# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models
from odoo import fields
from odoo import api


class invoice_payment_followup_line(models.Model):
    _name="invoice.payment.followup.line"
    date_duration_type = fields.Selection([('before','Day/s Before'),('after','Day/s After')],string="Duration type",required=True)
    date_duration= fields.Integer(string="# of days")    

class invoice_payment_followup(models.Model):
    _name="invoice.payment.followup"
    
    active = fields.Boolean('Active')
    company_id = fields.Many2one('res.partner',string="Company",domain=[('company_type','=','company')])
    line_ids = fields.Many2many('invoice.payment.followup.line','followup_id','followup_line_id',string="Lines")
    
    
