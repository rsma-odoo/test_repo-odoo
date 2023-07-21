"""
Training Exercise
Specifications

"""
from odoo.models import env
def main():
    
    #Create one record from the Motorcycle Registry Model. This Registry should have more than 1000 miles and no license plate.
    reg = env['motorcycle.registry'].create({
        'registry_number':'005',
        'first_name':'jorge',
        'last_name':'perez',
        'vin':'vino blanco',
        'current_mileage':1500.2})
    
    #Search for all Motorcycles Registries with less than 1000 miles.
    env['motorcycle.registry'].search_read([('current_mileage','>',1000)])
    
    #Search for all Motorcycle Registries with a VIN Number but no License Plate. Only show the fields: registry_number, vin, license_plate, and lastname
    env['motorcycle.registry'].search_read([('vin','!=',False),('license_plate','=','False')],['registry_number','vin','license_plate','last_name'])
    
    #Search for all Motorcycle Registries with a VIN Number or a License Plate.
    env['motorcycle.registry'].search_read(['|',('vin','!=',False),('license_plate','!=','False')])
    
    #Update the Name and Lastname of the record you created to John Wick
    reg.write({'first_name':'john','last_name':'wick'})
    
    #Delete the Record.
    reg.unlink()
if __name__ == '__main__':
    main()
