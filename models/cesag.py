from odoo import fields, models, api


class module(models.Model):
    _name = 'cesag.module'
    _description = 'Model cesag'

    name = fields.Char(required=True)
    description = fields.Text(required=True)
