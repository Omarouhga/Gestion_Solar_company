{
    'name': 'Vehicule',
    'version': '1.0',
    'category':'GSC',
    'sequence': '-1000000',
    'summary': "Gestion des véhicules",
    'description': "",
    'depends': 
    [
        'base','fleet'
    ],
    'data':[
        'views/gsc_voiture_view.xml',
        'views/gsc_vehicule_menu.xml',
        # 'views/gsc_model_view.xml',
        'views/gsc_service_type_view.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
     'author': "OUHAGUA Omar"
     
    
}