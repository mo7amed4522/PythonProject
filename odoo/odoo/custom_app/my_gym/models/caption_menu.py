# noinspection PyUnresolvedReferences
from odoo import fields, models,api

class CaptionMenu(models.Model):
    _name = 'caption.menu'
    _description = 'Caption Menu'

    ref = fields.Char(default='Reference', readonly=1)
    name = fields.Char(string='Caption')

    @api.model
    def create(self, vals):
        res = super(CaptionMenu, self).create(vals)
        if res.ref == "Reference":
            res.ref = self.env['ir.sequence'].next_by_code('cap_sequence')
        return res