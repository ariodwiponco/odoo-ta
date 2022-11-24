# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Business(models.Model):
    _inherit = 'business'
    _description = 'Business Model'

    product_ids = fields.One2many('product', 'business_id', string='Products')
