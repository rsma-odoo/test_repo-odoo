from odoo import models,fields

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number'
    registry_number = fields.Char(string='',required=True)
    vin = fields.Char(string='', required=True)
    first_name = fields.Char(string='',required=True)
    last_name = fields.Char(string='',required=True)
    picture = fields.Image(string='')
    current_mileage = fields.Float(string='')
    license_plate = fields.Char(string='')
    certificate_title = fields.Binary(string='')
    register_date = fields.Date(string='')


"""registry_number - char, required, this field should be the name of the record.
Hint: use the _rec_nameattribute in the Model to define this.
vin - char, required
first_name - char, required
last_name - char, required
picture - image
current_mileage - float
license_plate - char
certificate_title - binary
register_date - date
"""

#env['motorcycle.registry'].search_read([])