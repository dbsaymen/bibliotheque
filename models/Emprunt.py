from odoo import models, fields, api

class Emprunt(models.Model):
    _name = "bibliotheque.emprunt"
    dateEmprunt=fields.Datetime("Date", default=fields.datetime.now())
    type_empr = fields.Selection([('retour', 'Retour'), ('emprunt', 'Emprunt')])
    adherentId = fields.Many2one(comodel_name='bibliotheque.adherent', string="Adherent", required=True)
    livreId = fields.Many2one(comodel_name='bibliotheque.livre', string="livre", required=True)
    def name_get(self):
        result=[]
        for Emprunt in self:
            name="["+str(Emprunt.dateEmprunt)+"]"+Emprunt.livreId.titre+"--"+Emprunt.adherentId.nom+" "+Emprunt.adherentId.prenom
            result.append((Emprunt.id,name))
        return result