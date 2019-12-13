from odoo import models, fields, api

class Emprunt(models.Model):
    dateRetour = fields.Date("Date Retour")
    dateEmprunt=fields.Date("date Emprunt")