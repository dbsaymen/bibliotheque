from odoo import models, fields, api


class Adherent(models.Model):
    _name = 'bibliotheque.adherent'
    nom = fields.Char("Nom")
    prenom = fields.Char("Prenom")
    genre = fields.Selection([('male', 'Male'), ('female', 'Female')])
    numTel = fields.Char("Numero Téléphone")
    dateInscription = fields.Date("Date Inscription")
    adresse = fields.Text("Adresse")
    empruntIds = fields.One2many(comodel_name='bibliotheque.emprunt',
                                 inverse_name='adherentId')
