# For copyright and license notices, see __manifest__.py file in module root

from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _suma(self, a, b):
        return a + b

    def total_partners(self):
        """calcula el total de partners"""

        total = self.search([])
        i = 0
        for a in total:
            i = i + 1
        
