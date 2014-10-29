# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from cliente_app import facade
from routes.clientes import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_clientes_cmd()
    clientes = cmd()
    public_form = facade.cliente_public_form()
    cliente_public_dcts = [public_form.fill_with_model(cliente) for cliente in clientes]
    context = {'clientes': cliente_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

