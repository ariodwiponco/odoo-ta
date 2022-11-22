# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Material(models.Model):
    _name = 'material'
    _description = 'Material Model'

    name = fields.Char()
    product_id = fields.Many2one('product', string='Product')
    cost = fields.Float(string='Cost')
