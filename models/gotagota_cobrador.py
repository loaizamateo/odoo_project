# -*- coding: utf-8 -*-

from odoo import fields, models

class GotaGotaCobrador(models.Model):
    _name = 'gotagota.cobrador'     #nombre del modelo
    _description = 'Cobrador'
    _order = 'name asc'
    name = fields.Char(string='Nombre', required=True, size=150, index=True)
    documento = fields.Char(string='Numero de documento', required=True, size=20, index=True)
    tipodocumento = fields.Selection(
        [
            ('1', 'cedula de ciudadania'),
            ('2', 'NIT'),
            ('3', 'cedula de extrangeria'),
            ('4', 'pasaporte'),
        ], string='Tipo de documento', required=True, index=True, track_visibility='onchange', track_secuence=3, default='1'
    )

    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True)
    ciudades_ids = fields.One2many('gotagota.cobrador.ciudad', 'cobrador_id', 'Ciudades', track_visibility='onchange')
    _sql_constraints = {('cobrador_uniq', 'unique(documento)', 'El numero de documento debe ser unico')}


class GotaGotaDepartamento(models.Model):
    _name = 'gotagota.departamento'  # nombre del modelo
    _description = 'Departamento'
    _order = 'name asc'
    name = fields.Char(string='Nombre', required=True, size=50, index=True)
    codigo = fields.Char(string='Codigo del departamento', required=True, size=20, index=True)
    _sql_constraints = {('departamento_uniq', 'unique(codigo)', 'El codigo del departamento debe ser unico')}


class GotaGotaCiudad(models.Model):
    _name = 'gotagota.ciudad'  # nombre del modelo
    _description = 'Ciudad'
    _order = 'name asc'
    name = fields.Char(string='Nombre', required=True, size=50, index=True)
    codigo = fields.Char(string='Codigo de la ciudad', required=True, size=20, index=True)
    #relacion
    departamento_id = fields.Many2one('gotagota.departamento', 'Departamento', required=True)
    cobradores_ids = fields.One2many('gotagota.cobrador.ciudad', 'ciudad_id', 'Cobradores',
                                     track_visibility='onchange')
    _sql_constraints = {('ciudad_uniq', 'unique(codigo)', 'El codigo de la ciudad debe ser unico')}


class GotaGotaCobradorCiudad(models.Model):
    _name = 'gotagota.cobrador.ciudad'  # nombre del modelo
    _description = 'Relacion Cobrador Ciudad'
    cobrador_id = fields.Many2one('gotagota.cobrador', 'Cobrador', required=True, index=True)
    ciudad_id = fields.Many2one('gotagota.ciudad', 'Ciudad', required=True, index=True)
    _sql_constraints = [('cobrador_ciudad_uniq', 'unique(cobrador_id, ciudad_id)', 'Ya existe la asociacion ingresada del cobrador y la ciudad')]