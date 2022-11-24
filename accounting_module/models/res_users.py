# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    business_id = fields.Many2one('business', string='Business', required=True)
