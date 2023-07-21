from odoo import models,fields,api


class ProductTemplate(models.Model):
    _inherit ='product.template'

    detailed_type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle'),], ondelete={'motorcycle': 'set product'})
    type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle'),], ondelete={'motorcycle': 'set product'})

    horsepower = fields.Char(string='Horse Power')
    top_speed = fields.Char(string='Top Speed')
    torque = fields.Char(string='Torque')
    batt_cap = fields.Char(string='Battery Capacity')
    batt_charge_time = fields.Char(string='Battery Charge Time')
    batt_range = fields.Char(string='Battery Range')
    curb_weight = fields.Char(string='Curb Weight')
    make = fields.Char(string='Make')
    model = fields.Char(string='Model')

  
