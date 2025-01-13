from  odoo import  fields,models

class Tags(models.Model):
    _name = 'tags'
    _description = 'Tags'

    name = fields.Char(string='Name', required=True)
    #property_ids = fields.Many2many('property', string='Properties')