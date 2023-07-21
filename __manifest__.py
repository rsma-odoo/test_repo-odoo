{
    'name':'Motorcycle Registry',
    'summary':"Manage Registration of Motorcycles",
    'license':'LGPL-3',
    'description':"""Motorcycle Registry
        ====================
        This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    'author':'rsma-odoo',
    'website':'https://github.com/rsma-odoo',
    'category':'kawiil',
    'depends':['base','contacts','stock',],
    'data':[
        'security/kawiil_motors_motorcycle_registration_groups.xml',
        'security/ir.model.access.csv',
        #'security/kawiil_motors_motorcycle_registration_security.xml',
        'data/motorcycleRegistry_data.xml',
        'views/registry_menuitems.xml',
        'views/motorcycleRegistry_views.xml',
    ],
    'demo':[],#"demo/registry_demo.xml",],
    'installable':True,
    'application':True,
}
