from odoo import fields,models

class AccountMove(models.Model):
    _inherit="sale.order"


    def do_somthing(self):
        print("hello")