# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models
from odoo import fields
from odoo import api
import datetime


class account_invoice(models.Model):
    _inherit="account.invoice"
    partner_id = fields.Many2one(domain=[('order_block','=',False)])
    
    def _cron_check_invoice_due_dates(self):
        today = datetime.date.today()
    
        day_5_before = today + datetime.timedelta(days=6)
        day_5_before = day_5_before.strftime('%Y-%m-%d')        
#         5 days before payment due
        day_1_before = today + datetime.timedelta(days=2)
        day_1_before = day_1_before.strftime('%Y-%m-%d')
#         1 day after payment due
        day_10_after = today + datetime.timedelta(days=-9)
        day_10_after = day_10_after.strftime('%Y-%m-%d') 
#         10 days after payment due
        day_30_after = today + datetime.timedelta(days=-29)    
        day_30_after = day_30_after.strftime('%Y-%m-%d')    
#         30 days after the payment due

        target_dates={day_5_before:'customer_dunning.dunning_5_day_before',
                      day_1_before:'customer_dunning.dunning_1_day_before',
                      day_10_after:'customer_dunning.dunning_10_day_after',
                      day_30_after:'customer_dunning.dunning_30_day_after',
                      }
#         target_states=['draft','paid','cancel']        
        target_states=[]
#         domain=[('date_due','in',target_dates.keys()),('state','not in',target_states)]
        domain=[]
        temp_res = self.search(domain)
        for target_invoice in temp_res:
            if target_dates.get(target_invoice.date_due):
                template = self.env.ref(target_dates[target_invoice.date_due])            
                self.env['mail.template'].browse(template.id).send_mail(target_invoice.id)
                if target_invoice.date_due == day_30_after:
                    target_invoice.partner_id.order_block=True
    
    @api.onchange('partner_id')
    def onchange_partner_id_dunning(self):
        if self.partner_id.order_block:
            self.partner_id = False    
        self._cron_check_invoice_due_dates()
            
    @api.multi
    def write(self, vals):
        if vals and 'state' in vals and vals['state']=='paid':
            if self.partner_id.order_block:
                self.partner_id.order_block = False
        res = super(account_invoice, self).write(vals)
        return res            
    