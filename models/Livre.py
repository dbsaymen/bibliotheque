from odoo import models, fields

class Livre (models.Model):
    _name = 'bibliotheque.livre'
    ISBN = fields.Char('ISBN')
    titre = fields.Char('Titre')
    auteurId= fields.Many2one(comodel_name="bibliotheque.auteur",string="Auteur")
    numLivres = fields.Integer(string="nombre des livres")
    numLivresDisponibles = fields.Integer(string="nombre des livres disponibles")
    empruntIds = fields.One2many(comodel_name='bibliotheque.emprunt',
                                 inverse_name='livreId',string="Emprint")
    def name_get(self):
        result=[]
        for Livre in self:
            name="["+Livre.auteurId.f_name+"]"+Livre.titre
            result.append((Livre.id,name))
        return result
