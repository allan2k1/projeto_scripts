# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from cliente_app.model import Cliente
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import ADMIN, CORRETOR
from routes.imoveis.home import exibir
from tekton import router


@permissions(ADMIN, CORRETOR)
@no_csrf
def index():
    query = Cliente.query().order(Cliente.nome)
    clientes = query.fetch()
    contexto = {'clientes': clientes}
    return TemplateResponse(contexto)