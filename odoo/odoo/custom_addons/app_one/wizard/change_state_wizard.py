# noinspection PyUnresolvedReferences
from odoo import models, fields

class ChangeStateWizard(models.TransientModel):
    _name = 'changestate'
    _description = 'Change State Wizard'


    property_id = fields.Many2one('property', string='Property')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed')
    ], string='New State')
    reson=fields.Char(string='Reson')


    def action_confirm(self):
        if self.property_id.state == 'closed':
            self.property_id.state = self.state
            self.property_id.crate_history_record(self.property_id.state, self.state, self.reson)

