# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from cliente_app.model import Cliente

class ClientePublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Cliente
    _include = [Cliente.email,
                Cliente.cpf, 
                Cliente.nome]


class ClienteForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Cliente
    _include = [Cliente.email,
                Cliente.cpf, 
                Cliente.nome]


class ClienteDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Cliente
    _include = [Cliente.creation,
                Cliente.email, 
                Cliente.cpf, 
                Cliente.nome]


class ClienteShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Cliente
    _include = [Cliente.creation,
                Cliente.email, 
                Cliente.cpf, 
                Cliente.nome]


class SaveClienteCommand(SaveCommand):
    _model_form_class = ClienteForm


class UpdateClienteCommand(UpdateNode):
    _model_form_class = ClienteForm


class ListClienteCommand(ModelSearchCommand):
    def __init__(self):
        super(ListClienteCommand, self).__init__(Cliente.query_by_creation())

