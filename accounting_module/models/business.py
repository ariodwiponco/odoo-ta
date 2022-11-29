# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Business(models.Model):
    _name = 'business'
    _description = 'Business Model'

    name = fields.Char()
    owner = fields.Many2one('res.users', string='Owner')
    user_ids = fields.One2many('res.users', 'business_id', string='Users')
    journal_ids = fields.One2many('account.journal', 'business_id', string='Journal')
