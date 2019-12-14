from odoo import models, fields

class Livre (models.Model):
    _name = 'bibliotheque.livre'
    ISBN = fields.Char('ISBN')
    titre = fields.Char('Titre')
    auteurId= fields.Many2one(comodel_name="bibliotheque.auteur",string="Auteur")
    numLivres = fields.Integer(string="nombre des livres")
    numLivresDisponibles = fields.Integer(string="nombre des livres disponibles", compute="comp_livre_dispo")
    empruntIds = fields.One2many(comodel_name='bibliotheque.emprunt',
                                 inverse_name='livreId',string="Emprint")
    def name_get(self):
        result=[]
        for livre in self:
            name=livre.titre
            result.append((livre.id,name))
        return result

    def comp_livre_dispo(self):
        self.numLivresDisponibles = self.numLivres-len(self.empruntIds)
