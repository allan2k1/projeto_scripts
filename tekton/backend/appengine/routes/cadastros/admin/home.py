# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from cadastro_app import facade
from routes.cadastros.admin import new, edit


def delete(_handler, cadastro_id):
    facade.delete_cadastro_cmd(cadastro_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_cadastros_cmd()
    cadastros = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.cadastro_short_form()

    def short_cadastro_dict(cadastro):
        cadastro_dct = short_form.fill_with_model(cadastro)
        cadastro_dct['edit_path'] = router.to_path(edit_path, cadastro_dct['id'])
        cadastro_dct['delete_path'] = router.to_path(delete_path, cadastro_dct['id'])
        return cadastro_dct

    short_cadastros = [short_cadastro_dict(cadastro) for cadastro in cadastros]
    context = {'cadastros': short_cadastros,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

