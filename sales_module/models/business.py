# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Business(models.Model):
    _inherit = 'business'
    _description = 'Business Model'

    sales_ids = fields.One2many('sales', 'business_id', string='Sales')
