# -- coding: utf-8 --

from odoo import models, fields


class LibraryBook(models.Model):
    _inherit = "product.template"



    salooon = fields.Char(string="salon")

