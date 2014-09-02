# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from cadastro_app.commands import ListCadastroCommand, SaveCadastroCommand, UpdateCadastroCommand, \
    CadastroPublicForm, CadastroDetailForm, CadastroShortForm


def save_cadastro_cmd(**cadastro_properties):
    """
    Command to save Cadastro entity
    :param cadastro_properties: a dict of properties to save on model
    :return: a Command that save Cadastro, validating and localizing properties received as strings
    """
    return SaveCadastroCommand(**cadastro_properties)


def update_cadastro_cmd(cadastro_id, **cadastro_properties):
    """
    Command to update Cadastro entity with id equals 'cadastro_id'
    :param cadastro_properties: a dict of properties to update model
    :return: a Command that update Cadastro, validating and localizing properties received as strings
    """
    return UpdateCadastroCommand(cadastro_id, **cadastro_properties)


def list_cadastros_cmd():
    """
    Command to list Cadastro entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListCadastroCommand()


def cadastro_detail_form(**kwargs):
    """
    Function to get Cadastro's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return CadastroDetailForm(**kwargs)


def cadastro_short_form(**kwargs):
    """
    Function to get Cadastro's short form. just a subset of cadastro's properties
    :param kwargs: form properties
    :return: Form
    """
    return CadastroShortForm(**kwargs)

def cadastro_public_form(**kwargs):
    """
    Function to get Cadastro'spublic form. just a subset of cadastro's properties
    :param kwargs: form properties
    :return: Form
    """
    return CadastroPublicForm(**kwargs)


def get_cadastro_cmd(cadastro_id):
    """
    Find cadastro by her id
    :param cadastro_id: the cadastro id
    :return: Command
    """
    return NodeSearch(cadastro_id)


def delete_cadastro_cmd(cadastro_id):
    """
    Construct a command to delete a Cadastro
    :param cadastro_id: cadastro's id
    :return: Command
    """
    return DeleteNode(cadastro_id)

