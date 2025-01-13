from odoo import fields,models

class ResPartener(models.Model):
    _inherit = 'res.partner'
    _description=''

    property_id= fields.Many2one('property')
    price = fields.Integer(related='property_id.diff')