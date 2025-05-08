# odoo-docker/addons/hello_world/models/hello_model.py

from odoo import models, fields, api

class HelloWorld(models.Model):
    _name = 'hello.world'
    _description = 'Hello World Model'

    name = fields.Char(string='Message')
    quantity = fields.Integer(string='Quantity')  # New Numeric Field (Integer)
    event_timestamp = fields.Datetime(string='Event Timestamp', default=fields.Datetime.now) # New Datetime Field


    # Add a state field
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ], string='Status', default='draft', required=True)

    # Add a method to confirm the record
    def action_confirm(self):
        """ Changes the state to confirmed """
        self.ensure_one() # Ensures the method is called on a single record
        self.write({'state': 'confirmed'})