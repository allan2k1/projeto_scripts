# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from cliente_app import facade
from routes.clientes import admin


@no_csrf
def index(cliente_id):
    cliente = facade.get_cliente_cmd(cliente_id)()
    detail_form = facade.cliente_detail_form()
    context = {'save_path': router.to_path(save, cliente_id), 'cliente': detail_form.fill_with_model(cliente)}
    return TemplateResponse(context, 'clientes/admin/form.html')


def save(_handler, cliente_id, **cliente_properties):
    cmd = facade.update_cliente_cmd(cliente_id, **cliente_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'cliente': cmd.form}

        return TemplateResponse(context, 'clientes/admin/form.html')
    _handler.redirect(router.to_path(admin))

