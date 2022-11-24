# -*- coding: utf-8 -*-
# from odoo import http


# class SalesModule(http.Controller):
#     @http.route('/sales_module/sales_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_module/sales_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_module.listing', {
#             'root': '/sales_module/sales_module',
#             'objects': http.request.env['sales_module.sales_module'].search([]),
#         })

#     @http.route('/sales_module/sales_module/objects/<model("sales_module.sales_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_module.object', {
#             'object': obj
#         })
