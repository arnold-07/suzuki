# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryAuthor(models.Model):
    _name = "library.author"

    name = fields.Char(string="Nombre")
    image = fields.Binary(string="Imagen")
    date = fields.Date(string="Fecha nacimiento")
    country_id = fields.Many2one("res.country", string="Pais nacimiento")