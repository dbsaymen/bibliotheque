from odoo import models, fields, api

class Adherent(models.Model):
    _name = 'bibliotheque.adherent'
    nom = fields.Char("Nom")
    prenom=fields.Char("Prenom")
    numTel=fields.Char("Numero Téléphone")
    dateInscription=fields.Date("Date Inscription")
    adresse=fields.Text("Adresse")
    genre = fields.Selection([('male', 'Male'), ('female', 'Female')])