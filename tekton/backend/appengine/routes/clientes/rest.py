# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from cliente_app import facade

@login_not_required
@no_csrf
def index():
    cmd = facade.list_clientes_cmd()
    cliente_list = cmd()
    short_form=facade.cliente_short_form()
    cliente_short = [short_form.fill_with_model(m) for m in cliente_list]
    return JsonResponse(cliente_short)

@login_not_required
@no_csrf
def save(_resp, **cliente_properties):
    cmd = facade.save_cliente_cmd(**cliente_properties)
    return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def update(_resp, id, **cliente_properties):
    cmd = facade.update_cliente_cmd(id, **cliente_properties)
    return _save_or_update_json_response(_resp, cmd)

@login_not_required
@no_csrf
def delete(id):
    facade.delete_cliente_cmd(id)()


def _save_or_update_json_response(_resp, cmd):
    try:
        cliente = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonUnsecureResponse(cmd.errors)
    short_form=facade.cliente_short_form()
    return JsonResponse(short_form.fill_with_model(cliente))