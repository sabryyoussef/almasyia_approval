# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('wait', 'Waiting engineering'), ('engineering', 'Engineering'), ('sent',)])
    confirmed_user_id = fields.Many2one('res.users', string='Confirmed User')

    def action_confirm(self):
        super(SaleOrder, self).action_confirm()
        self.confirmed_user_id = self.env.user.id

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['confirmed_user_id'] = self.confirmed_user_id.id
        return invoice_vals

    def send_to_engineering(self):
        self.state = 'wait'

    def action_done(self):
            self.state = 'sent'
