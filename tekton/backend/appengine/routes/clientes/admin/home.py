# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaepermission.decorator import permissions
from permission_app.model import ADMIN
from tekton import router
from gaecookie.decorator import no_csrf
from cliente_app import facade
from routes.clientes.admin import new, edit

@permissions(ADMIN)
def delete(_handler, cliente_id):
    facade.delete_cliente_cmd(cliente_id)()
    _handler.redirect(router.to_path(index))

@permissions(ADMIN)
@no_csrf
def index():
    context = {'new_path': router.to_path(new)}
    return TemplateResponse(context)