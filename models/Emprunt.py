from odoo import models, fields, api

class Emprunt(models.Model):
    _name = "bibliotheque.emprunt"
    dateRetour = fields.Date("Date Retour")
    dateEmprunt=fields.Date("date Emprunt")