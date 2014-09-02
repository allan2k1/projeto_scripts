# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from cadastro_app import facade
from routes.cadastros import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_cadastros_cmd()
    cadastros = cmd()
    public_form = facade.cadastro_public_form()
    cadastro_public_dcts = [public_form.fill_with_model(cadastro) for cadastro in cadastros]
    context = {'cadastros': cadastro_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

