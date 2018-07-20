# -*- coding: utf-8 -*-
from odoo import models, api


class StockPackOperationLot(models.Model):
    _inherit = 'stock.pack.operation.lot'
    
    @api.model
    def create(self, vals):
        res = super(StockPackOperationLot, self).create(vals)
        if vals.get('lot_name'):
            self.env['maintenance.equipment'].create({'name': vals.get('lot_name')})
        return res
    
    @api.multi
    def write(self, vals):
        if vals.get('lot_name'):
            lot_name = self.lot_name
            equipment_id = self.env['maintenance.equipment'].search([('name', '=', lot_name)])
            res = super(StockPackOperationLot, self).write(vals)
            equipment_id.name = vals.get('lot_name')
            return res
        else:
            return super(StockPackOperationLot, self).write(vals)
       
        