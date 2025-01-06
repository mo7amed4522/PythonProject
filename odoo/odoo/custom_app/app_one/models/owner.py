from odoo import models, fields

class Owner(models.Model):
    _name = 'owner'
    _description = 'Owner'

    name = fields.Char(string='Name', required=True)  # Add this line if missing
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    property_ids = fields.One2many('property', 'owner_id',string='Properties')