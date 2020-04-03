# -*- coding: utf-8 -*-
# from odoo import http


# class Coopplanning(http.Controller):
#     @http.route('/coopplanning/coopplanning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/coopplanning/coopplanning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('coopplanning.listing', {
#             'root': '/coopplanning/coopplanning',
#             'objects': http.request.env['coopplanning.coopplanning'].search([]),
#         })

#     @http.route('/coopplanning/coopplanning/objects/<model("coopplanning.coopplanning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('coopplanning.object', {
#             'object': obj
#         })
