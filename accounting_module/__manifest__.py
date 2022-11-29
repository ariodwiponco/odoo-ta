# -*- coding: utf-8 -*-
{
    'name': "Accounting",

    'summary': """
        Basic accounting module for UMKM ERP""",

    'description': """
        This module will help to manage accounting record
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
        'views/account_views.xml',
    ],
}
