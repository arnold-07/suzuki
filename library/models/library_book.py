# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields


class LibraryBook(models.Model):
    _name = "library.book"
    _description = 'Library Book'

    name = fields.Char(string="Nombre")
    isbn = fields.Char(string="ISBN", size=9, required=True)
    image = fields.Binary(string="Imagen")
    date = fields.Date(string="Fecha Pubilicacion")

