from odoo import models, fields

class Livre (models.Model):
    _name = 'bibliotheque.livre'
    ISBN = fields.Char('ISBN')
    titre = fields.Char('Titre')
    numLivres = fields.Integer(string="nombre des livres")
    numLivresDisponibles = fields.Integer(string="nombre des livres disponibles")