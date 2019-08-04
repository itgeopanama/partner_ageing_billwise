# -*- coding: utf-8 -*-

from odoo import fields, models


class AgedTrialBalanceBillwise(models.TransientModel):
    _inherit = 'account.aged.trial.balance'
    _description = 'Account Aged Trial balance Report Bill-wise'

    report_type = fields.Selection([('bill', 'Detallado'), ('customer', 'Por Cliente')], default='customer',
                                   string="Tipo de Reporte")

    def _print_report(self, data):
        data['form']['report_type'] = self.report_type
        return super(AgedTrialBalanceBillwise, self)._print_report(data)
