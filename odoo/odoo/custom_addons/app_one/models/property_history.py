from odoo import  fields,models

class PropertyHistory(models.Model):
    _name = 'history'
    _description = "Property History"

    user_id = fields.Many2one('res.users',string='User')
    property_id = fields.Many2one('property',string='Property')
    old_state = fields.Char(string='Old State')
    new_state = fields.Char(string='New State')
    reson= fields.Char(string='Reson')
    line_ids= fields.One2many('history.line','history_id')
    line_idss= fields.One2many('history.lines','history_id')

class PropertyHistoryLine(models.Model):
    _name = 'history.line'
    _description = "Property History Line"

    history_id = fields.Many2one('history',string='History')
    area = fields.Char(string='Area')
    description = fields.Char(string='Description')
    side = fields.Char(string='Side')
    old_state = fields.Char(string='Old State')
    new_state = fields.Char(string='New State')


class HistoryLines(models.Model):
    _name = 'history.lines'
    _description = "Property History Line"

    history_id = fields.Many2one('history',string='History')
    area = fields.Char(string='Area')
    description = fields.Char(string='Description')
    side = fields.Char(string='Side')
