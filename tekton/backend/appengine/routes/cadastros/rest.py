# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from cadastro_app import facade


def index():
    cmd = facade.list_cadastros_cmd()
    cadastro_list = cmd()
    short_form=facade.cadastro_short_form()
    cadastro_short = [short_form.fill_with_model(m) for m in cadastro_list]
    return JsonResponse(cadastro_short)


def save(**cadastro_properties):
    cmd = facade.save_cadastro_cmd(**cadastro_properties)
    return _save_or_update_json_response(cmd)


def update(cadastro_id, **cadastro_properties):
    cmd = facade.update_cadastro_cmd(cadastro_id, **cadastro_properties)
    return _save_or_update_json_response(cmd)


def delete(cadastro_id):
    facade.delete_cadastro_cmd(cadastro_id)()


def _save_or_update_json_response(cmd):
    try:
        cadastro = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.cadastro_short_form()
    return JsonResponse(short_form.fill_with_model(cadastro))

