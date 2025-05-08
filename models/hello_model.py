# odoo-docker/addons/hello_world/models/hello_model.py

from odoo import models, fields, api, exceptions

class HelloWorld(models.Model):
    _name = 'hello.world'
    _description = 'Hello World Model'


    # Add a uniqueness constraint for the username
    _sql_constraints = [
        ('username_unique',
         'UNIQUE(username)',
         'The username must be unique!'),
    ]

    name = fields.Char(string='Message')
    quantity = fields.Integer(string='Quantity')  # New Numeric Field (Integer)
    event_timestamp = fields.Datetime(string='Event Timestamp', default=fields.Datetime.now) # New Datetime Field

    # Add a state field
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
    ], string='Status', default='draft', required=True)

    # Add the new username field
    username = fields.Char(string='Username', required=True, copy=False) # required and copy=False are good practices for unique fields


    # Add the new date fields
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')


    # Add a method to confirm the record
    def action_confirm(self):
        """ Changes the state to confirmed """
        self.ensure_one() # Ensures the method is called on a single record
        self._check_dates() # Call the date validation method
        self.write({'state': 'confirmed'})


    # Add a constraint method to validate the date range
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise exceptions.ValidationError("Error: Start Date must be before End Date.")
