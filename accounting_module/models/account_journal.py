# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountJournal(models.Model):
    _name = 'account.journal'
    _description = 'Account Journal Model'

    name = fields.Char()
    business_id = fields.Many2one('business', string='Business')
