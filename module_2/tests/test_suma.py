from odoo.tests.common import TransactionCase


class DocumentTestSumaCase(TransactionCase):
    def test_01_suma(self):
        partner_obj = self.env["res.partner"]
        self.assertEqual(partner_obj._suma(4, 2), 4 + 2)
