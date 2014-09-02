# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from cadastro_app import facade
from routes.cadastros import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'cadastros/admin/form.html')


def save(_handler, cadastro_id=None, **cadastro_properties):
    cmd = facade.save_cadastro_cmd(**cadastro_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'cadastro': cmd.form}

        return TemplateResponse(context, 'cadastros/admin/form.html')
    _handler.redirect(router.to_path(admin))

