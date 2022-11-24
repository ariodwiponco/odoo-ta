# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ChartAccount(models.Model):
    _name = 'chart.account'
    _description = 'Chart of Account Model'

    name = fields.Char(string='Chart Name', required=True, copy=False)
    account_type = fields.Selection([('payable', 'Account Payable'), ('receivable', 'Account Receivable')],
                                    string='Account Type', required=True)
    journal_id = fields.Many2one('account.journal', string='Journal', required=True)
