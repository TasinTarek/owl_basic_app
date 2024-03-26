# -*- coding: utf-8 -*-
{
    'name': "OWL Basic App",

    'summary': "Owl Basic App",

    'description': """
        Basic Struture for OWL
    """,

    'author': "Tasin Tarek",
    'website': "https://www.tasintarek-odoo.com",
    'category': 'Tools',
    'version': '17.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data':[
        'views/ir_actions_client.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'owl_basic_app/static/src/components/**/*.scss',
            'owl_basic_app/static/src/components/**/*.xml',
            'owl_basic_app/static/src/components/**/*.js',
        ],
        'web.assets_frontend': [
            
        ],
        'web.assets_common': [
            
        ],
    },
    'demo': [],
    'icon': '/owl_basic_app/static/description/icon.png',
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 0,
    'currency': 'EUR',
    'license': 'OPL-1',
    'contributors': [
        'Tasin Tarek <https://github.com/TasinTarek>',
    ],
}

