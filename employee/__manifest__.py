{
    'name': 'employee (gsc)',
    'version': '1.0',
    'category':'GSC',
    'sequence': '-100',
    'summary': "Gestion des ventes à Solar company",
    'description': "GSC RH",
    'depends': 
    [
        'base','sale_management', 'hr'
    ],
    'data': [
        'wizards/avance_de_salaire.xml',
        'views/gsc_employee_view.xml',
        'views/gsc_employee_menu.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'author': "Ibrahim ESSAKINE"

}