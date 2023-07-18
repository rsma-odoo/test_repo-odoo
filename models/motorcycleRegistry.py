from odoo import models

class MotorcycleRegistry(models.Model):
    _name='motorcycle.registry'
    _order = 'registry_number char required, vin char required, first_name char required, last_name char required, picture image, current_mileage float, license_plate char, certificate_title binary, register_date date '