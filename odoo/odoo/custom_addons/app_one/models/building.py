from odoo import fields,models

class Building(models.Model):
    _name = 'building'
    _description = "Building Description"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    no = fields.Integer()
    address = fields.Char(required=1, size=64)
    city = fields.Char()
    state = fields.Char()
    zipcode = fields.Integer()
    country = fields.Char()
    floors = fields.Integer()
    total_units = fields.Integer()
    description = fields.Text()
    active=fields.Boolean(default=True)