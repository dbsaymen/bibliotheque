
from odoo import models, fields

class Auteur (models.Model):
    _name = "bibliotheque.auteur"
    f_name = fields.Char('Nom')
    f_prenom = fields.Char('Prénom')
    livreId = fields.One2many(comodel_name='bibliotheque.livre',
                              inverse_name="auteurId",string = "Livre")
    def name_get(self):
        result=[]
        for Auteur in self:
            name=Auteur.f_name+" "+Auteur.f_prenom
            result.append((Auteur.id,name))
        return result