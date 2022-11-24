# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Sales(models.Model):
    _name = 'sales'
    _description = 'Sales Model'

    name = fields.Char()
    sales_date = fields.Datetime(string='Sales Date')
    line_ids = fields.One2many('sales.line', 'sales_id', string='Sales Lines')
    business_id = fields.Many2one('business', string='Business')

class SalesLine(models.Model):
    _name = 'sales.line'
    _description = 'Sales Lines'

    product_id = fields.Many2one('product', string='Product')
    sales_id = fields.Many2one('sales.model')
    sales_qty = fields.Integer(string='Sale Qty')

    _sql_constraints = [('product_id_uniq', 'unique(product_id)', "Cannot add same product")]