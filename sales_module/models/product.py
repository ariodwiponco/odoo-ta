# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Product(models.Model):
    _name = 'product'
    _description = 'Product Model'

    name = fields.Char()