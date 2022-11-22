# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Product(models.Model):
    _name = 'product'
    _description = 'Product Model'

    name = fields.Char()
    cost_type = fields.Selection([('single', 'Single Cost'), ('material', 'Material Cost')], string='Product Cost Type',
                                 default='material')
    material_ids = fields.One2many('material', 'product_id', string='Materials')
