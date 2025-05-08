# odoo-docker/addons/hello_world/__manifest__.py

{
    'name': 'Hello World',
    'version': '1.0',
    'summary': 'A simple Hello World module',
    'author': 'Your Name',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'views/hello_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
