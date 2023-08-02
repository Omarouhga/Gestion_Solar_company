{
    'name': 'vente (gsc)',
    'version': '1.0',
    'category':'GSC',
    'sequence': '-100',
    'summary': "Gestion des ventes à Solar company",
    'description': "",
    'depends': 
    [
        'base','sale_management'
    ],
    'data':[
        'views/gsc_vente_menu.xml',
        'views/gsc_devis_view.xml',
        # 'views/gsc_client_view.xml'

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
     'author': "OUHAGUA Omar"
     
    
}