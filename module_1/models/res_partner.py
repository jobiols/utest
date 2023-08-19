# For copyright and license notices, see __manifest__.py file in module root

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    corporate_data = fields.Html(
        string="Información corporativa",
        help="Esta información aparecerá en las facturas",
    )
