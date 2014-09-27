# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from produto_app import facade
from routes.produtos import admin
from permission_app.model import ADMIN


@permissions(ADMIN)
@no_csrf
def index():
    cmd = facade.list_produtos_cmd()
    produtos = cmd()
    public_form = facade.produto_public_form()
    produto_public_dcts = [public_form.fill_with_model(produto) for produto in produtos]
    context = {'produtos': produto_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)