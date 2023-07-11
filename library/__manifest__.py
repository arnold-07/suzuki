# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """ 
 Gestion libros en Odoo 
 """,

    'description': """ 
 Gestion libros en Odoo 
 """,

    'author': "Juan Carlos Montoya",
    'website': "http://www.cursosodoo.net",

    'category': 'Tools',
    'version': '14.0.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],
    'application': True,

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book_view.xml',
        'views/library_author_view.xml',
        'views/menus.xml',

    ],
    # only loaded in demonstration mode
    # 'demo': [
    # 'demo/demo.xml',
    # ],
}