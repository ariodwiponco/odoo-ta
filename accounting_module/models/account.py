# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountPayable(models.Model):
    _name = 'account.payable'
    _description = 'Account Payable Model'

    name = fields.Char()
    amount = fields.Float(string='Amount')
    journal_id = fields.Many2one('account.journal', string='Journal')


class AccountReceivable(models.Model):
    _name = 'account.receivable'
    _description = 'Account Receivable Model'

    name = fields.Char()
    amount = fields.Float(string='Amount')
    journal_id = fields.Many2one('account.journal', string='Journal')
