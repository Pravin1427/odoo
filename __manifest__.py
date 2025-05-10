{
    'name': 'Appointment Management',
    'version': '1.0',
    'summary': 'A module for managing appointments',
    'author': 'Pravin Timalsina',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'views/appointment_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}