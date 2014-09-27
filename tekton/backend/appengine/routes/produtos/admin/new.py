# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaeforms.ndb.form import ModelForm
from tekton import router
from gaecookie.decorator import no_csrf
from produto_app import facade
from routes.produtos import admin
from tekton.backend.apps.produto_app.model import ProdForm


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'produtos/admin/form.html')

def save(_logged_user,**produto_properties):
    prod_form = ProdForm(**produto_properties)




    cmd = facade.save_produto_cmd(**produto_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'produto': cmd.form}

        return TemplateResponse(context, 'produtos/admin/form.html')
    _handler.redirect(router.to_path(admin))
