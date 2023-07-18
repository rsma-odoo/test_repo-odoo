{
    'name':"K'awiil Motors Motorcycle Registration",
    'version':'0.1',
    'summary':"Motorcycle registration for K'awiil Motors",
    'description':'App for Motorcycle registration.',
    'author':'Odoo',
    'website':'odoo.com',
    'category':'tools',
    'license':'OPL-1',
    'depends':['base'],
    'data':[
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
    ],
    'demo':[
        'data/demo.xml',
    ],
    'assets':[],
    'installable':True,
    'auto_install':False,
    'application':True
}
