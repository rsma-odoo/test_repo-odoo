from odoo import models,fields,api
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number'
    registry_number = fields.Char(
            string='Registry Number',
            required=True,
            default='MRN0000',
            copy=False,
            readonly=True)
    
    vin = fields.Char(string='', required=True)
    first_name = fields.Char(string='First Name',required=True)
    last_name = fields.Char(string='Last Name',required=True)
    picture = fields.Image(string='Profile Pic')
    current_mileage = fields.Float(string='Mileage')
    license_plate = fields.Char(string='License Plate',copy=False,)
    certificate_title = fields.Binary(string='Certificate Title')
    register_date = fields.Date(string='Register Date')

    @api.model_create_multi
    def create(self,vals):
        for val in vals:
            if val.get('registry_number',('MRN0000')) == ('MRN0000'):
                val['registry_number'] = self.env['ir.sequence'].next_by_code('motorcycle.registry.registry_number_sequence')
        return super().create(vals)
    
    @api.constrains('vin')
    def check_vin(self):
        """
        VIN
        Make - 2 Capital Letters
        Model - 2 Capital Letters
        Year - 2 Digits
        Battery Capacity - 2 Capital Letters or Numbers
        Serial Number - 6 Digits
        """
    
        error = ''
        error += ('\nVIN must be 14 characters long.','')[len(self.vin) == 14]
        error += ('\nFirst two characters must be capital letters.','')[self.vin[0:2].isalpha() and self.vin[0:2].isupper()]
        error += ('\nCharacters 3 and 4 must be capital letters.','')[self.vin[2:4].isalpha() and self.vin[2:4].isupper()]
        error += ('\nCharacters 5 and 6 must be numeric.','')[self.vin[4:6].isnumeric()]
        error += ('\nCharacters 7 and 8 must be capital letters or numbers.','')[all([(ch.isnumeric() or ch.isupper()) for ch in self.vin[6:8]])]
        error += ('\nLast 6 characters must be numeric.','')[self.vin[8:14].isnumeric()]
        error += ("\nVIN must not be the same as someone else's.",'')[len(self.env['motorcycle.registry'].search_read([('vin','=',self.vin)])) < 2]
        if(len(error) > 0):
            error = 'VIN field has some mistakes:\n'+error
            raise ValidationError(error)
        return

    @api.constrains('license_plate')
    def check_license_plate(self):
        """
        The License Plate should follow the following Pattern:

        1 - 4 Capital Letters
        1 - 3 Digits
        Optional 2 Capital Letters

        For example KLV453, KLR3453L
        """
        if(self.license_plate):
            conditions = [
                self.license_plate.isalnum(),
                len([ch for ch in self.license_plate if ch.isupper()]) > 0,
                len([ch for ch in self.license_plate if ch.isupper()]) <= 4,
                len([ch for ch in self.license_plate if ch.isnumeric()]) > 0,
                len([ch for ch in self.license_plate if ch.isnumeric()]) <= 3,
            ]
        else:
            conditions = [True]

        if(all(conditions) != True):
            raise ValidationError("""
The License Plate should follow the following Pattern:

        1 - 4 Capital Letters
        1 - 3 Digits""")
        return

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