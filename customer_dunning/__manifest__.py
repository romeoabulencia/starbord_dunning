# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Customer Dunning",
    'summary': """
        Customer Dunning and filtering through orders""",
    'version': '1.0',
    'category': 'Uncategorized',
    'license': 'AGPL-3',
    'installable': True,
    'depends': [
        'account',
        'sale',
        'purchase',
    ],
    'data': [
        #partner view alteration
        'views/res_partner_views.xml',
                
        #email templates
        'data/dunning_email_templates.xml',
        
        #cron
        'data/dunning_cron.xml',
        

    ],
}
