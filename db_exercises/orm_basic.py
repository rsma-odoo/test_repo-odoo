from odoo import env
def main():
    reg = env['motorcycle.registry'].create({
        'registry_number':'005',
        'first_name':'jorge',
        'last_name':'perez',
        'vin':'vino blanco',
        'current_mileage':1500.2})
    env['motorcycle.registry'].search_read([('current_mileage','>',1000)])
    env['motorcycle.registry'].search_read([('vin','!=',False),('license_plate','=','False')],['registry_number','vin','license_plate','last_name'])
    env['motorcycle.registry'].search_read(['|',('vin','!=',False),('license_plate','!=','False')])
    reg.write({'first_name':'john','last_name':'wick'})
    reg.unlink()
if __name__ == '__main__':
    main()
    