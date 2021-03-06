# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from cadastro_app.model import Cadastro

class CadastroPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Cadastro
    _include = [Cadastro.nome, 
                Cadastro.sobrenome, 
                Cadastro.email]


class CadastroForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Cadastro
    _include = [Cadastro.nome, 
                Cadastro.sobrenome, 
                Cadastro.email]


class CadastroDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Cadastro
    _include = [Cadastro.sobrenome, 
                Cadastro.creation, 
                Cadastro.email, 
                Cadastro.nome]


class CadastroShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Cadastro
    _include = [Cadastro.sobrenome, 
                Cadastro.creation, 
                Cadastro.email, 
                Cadastro.nome]


class SaveCadastroCommand(SaveCommand):
    _model_form_class = CadastroForm


class UpdateCadastroCommand(UpdateNode):
    _model_form_class = CadastroForm


class ListCadastroCommand(ModelSearchCommand):
    def __init__(self):
        super(ListCadastroCommand, self).__init__(Cadastro.query_by_creation())

