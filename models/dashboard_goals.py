from odoo import models, fields

class dashboard_goals(models.Model):
    _name = 'dashboard_goals'
    _description = 'Metas de Facturación'

    start_date = fields.Date(string='Fecha Inicio')
    end_date = fields.Date(string='Fecha Fin')
    user_id = fields.Many2one('res.users', string='Vendedor')
    quotation_goal = fields.Monetary(string='Meta Cotización')
    order_goal = fields.Monetary(string='Meta Orden Venta')
    invoice_goal = fields.Monetary(string='Meta de Facturación')
    team_id = fields.Many2one('crm.team', string='Equipo')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.ref('base.COP'))