
from odoo import models, fields

class Auteur (models.Model):
    _name = "bibliotheque.Auteur"
    f_name = fields.Char('Nom')
    f_prenom = fields.Char('Prénom')