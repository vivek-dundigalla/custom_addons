from odoo import models, fields, api
# from datetime import date, datetime
# from odoo.osv import expression
# import base64

class busniessmanagement(models.Model):
    _name = "business.management"
    _rec_name = "customer_id"
    _inherit = ["mail.thread","mail.activity.mixin"]

    customer_id = fields.Many2one(comodel_name="res.partner", string="Customer Name", tracking=True, required=True)
    customer_number = fields.Char(string="Mobile Number",tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender" , tracking=True,)
    age = fields.Integer(string="Age",tracking=True)
    email = fields.Char(string="email",tracking=True)

    customer_imeage = fields.Binary(string="Upload Imeage")


