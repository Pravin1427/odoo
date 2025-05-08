# odoo-docker/addons/hello_world/models/hello_model.py

from odoo import models, fields

class HelloWorld(models.Model):
    _name = 'hello.world'
    _description = 'Hello World Model'

    name = fields.Char(string='Message')
