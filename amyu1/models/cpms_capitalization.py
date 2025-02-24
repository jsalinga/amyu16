from odoo import models, fields


class CapitalizationShare(models.Model):
    _name = 'capitalization.share'
    _description = "Capitalization Shares"

    name = fields.Char(string="Class of Shares")
    par_value = fields.Char(string="Par Value per Share", default='')
    # column_3 = fields.Char(string="Authorized")
    authorized_no = fields.Integer(string=" Authorized No.")
    authorized_amount = fields.Float(string="Authorized Amount")
    # column_4 = fields.Char(string="Subscribed")
    subscribed_no = fields.Integer(string="Subscribed No.")
    subscribed_amount = fields.Float(string="Subscribed Amount")
    # column_5 = fields.Char(string="Treasury")
    treasury_no = fields.Integer(string="Treasury No.")
    treasury_amount = fields.Float(string="Treasury Amount")
    # column_6 = fields.Char(string="Paid-Up")
    paid_up_no = fields.Integer(string="Paid-Up No.")
    paid_up_amount = fields.Float(string="Paid-Up Amount")
    capitalization_id = fields.Many2one(comodel_name='client.profile', string="Class")
