from odoo import fields,models,api

class Property(models.Model):
    _name = 'property'
    _description = "New Description Picking"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref= fields.Char(default='New' , readonly=1, translate=True)
    name = fields.Char(required=1 , size=16 ,translate=True)
    expire_price = fields.Integer()
    description = fields.Text(required=1,tracking=1,translate=True)
    area = fields.Float()
    expected_price = fields.Integer()
    expected_date = fields.Date()
    is_late= fields.Boolean()
    diff = fields.Integer(compute='_compute_diff_')
    postcode = fields.Integer()
    area_oration= fields.Selection([
        ('north','North'),
        ('west','West'),
        ('east','East'),
        ('west','West')
    ],default='north')
    owner_id = fields.Many2one('owner', string='Owner')
    tag_ids = fields.Many2many('tags', string='Tags')

    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
        ('closed','Closed')
    ], default="draft")
    line_ids= fields.One2many('property.liens','property_id')

    _sql_constraints = [
        ('unique_name','unique("name")','The name of new property is Existing!!')
    ]

    @api.depends('expected_price','expire_price','owner_id.name')
    def _compute_diff_(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.expire_price

    @api.onchange('expected_price')
    def _onchange_expected_price_(self):
        for _ in self:
            return {
                'warring':{'title':'Warring','message':'Negative Value .','type':'notification'}
            }
    @api.constrains('name')
    def _check_name(self):
        for record in self:
            if record.name == 'New Property' or record.name == '':
                raise models.ValidationError('Name cannot be "New Property"')

    def action_draft(self):
        for rec in self:
            rec.crate_history_record(rec.state,'draft')
            rec.state = 'draft'
    def action_pending(self):
        for rec in self:
            rec.crate_history_record(rec.state,'pending')
            rec.state='pending'
    def action_sold(self):
        for rec in self:
            rec.crate_history_record(rec.state,'sold')
            rec.state= 'sold'
    def action_closed(self):
        for rec in self:
            rec.crate_history_record(rec.state,'closed')
            rec.state='closed'

    def check_expected_date(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.expected_date and rec.expected_date < fields.Date.today():
                rec.is_late = True

    def change_wizard_state(self):
        action= self.env['ir.actions.actions']._for_xml_id('app_one.change_wizead_action_state')
        action['context']={'default_property_id':self.id}
        return  action


    @api.model
    def create(self,vals):
        res = super(Property, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('property_seq')
        return  res
    def crate_history_record(self,old_state,new_state,reson=""):
        for rec in self:
            rec.env['history'].create({
                'user_id':self.env.uid,
                'property_id':rec.id,
                'old_state':old_state,
                'new_state':new_state,
                'reson':reson or '',
            })

    #SMART BUTTON
    def action_open_related_owner(self):
        action = self.env['ir.actions.actions']._for_xml_id('app_one.owner_action')
        view_id = self.env.ref('app_one.owner_view_form').id
        action['res_id'] = self.owner_id.id
        action['views'] = [(view_id,'form')]
        return action


    def property_xlsx_report(self):
        return {
            'type': 'ir.actions.act_url',
            'url': f'/property/excel/report/{self.env.context.get("active_ids")}',
            'target': 'new',
        }
        


class PropertyLiens(models.Model):
    _name = 'property.liens'
    _description = "Property Liens"

    area= fields.Float()
    description= fields.Text()
    side = fields.Char(string='Side')
    property_id = fields.Many2one('property', string='Property')
