# -*- coding: utf-8 -*-
{
    'name': "Sales",

    'summary': """
        Basic sales module for UMKM ERP""",

    'description': """
        This module will be a major module that will hold sales that can afford to record sales
    """,

    'author': "Ario Dwiponco",
    'website': "",

    'category': 'Uncategorized',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'accounting_module'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/sales_views.xml',
    ],
}
