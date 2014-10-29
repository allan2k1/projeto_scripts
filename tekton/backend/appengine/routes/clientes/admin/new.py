# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from cliente_app import facade
from routes.clientes import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'clientes/admin/form.html')


def save(_handler, cliente_id=None, **cliente_properties):
    cmd = facade.save_cliente_cmd(**cliente_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'cliente': cmd.form}

        return TemplateResponse(context, 'clientes/admin/form.html')
    _handler.redirect(router.to_path(admin))

