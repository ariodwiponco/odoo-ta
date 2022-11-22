# -*- coding: utf-8 -*-
{
    'name': "Inventory",

    'summary': """
        Basic inventory module for UMKM ERP""",

    'description': """
        This module will be a major module that will become master data for supporting sales module
    """,

    'author': "Ario Dwiponco",
    'website': "",

    'category': 'Uncategorized',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/product_views.xml',
    ],
}
