# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from google.appengine.ext import ndb
from gaeforms import base
from gaeforms.base import Form
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node, Arc, destinations_cache_key
from tekton import router
from gaecookie.decorator import no_csrf
import routes.produtos
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    query = Produto.query().order(Produto.price)
    produto_lista = query.fetch()
    editar_form_path = router.to_path(editar_form)
    for produto in produto_lista:
        produto['edit_path'] = '%s/%s'%(editar_form_path, produto['id'])
    contexto = {'produto_lista': produto_lista}
    return TemplateResponse(contexto)

@no_csrf
def form():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)

class Produto(Node):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty()
    release = ndb.DateProperty()

class AutorArco(Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Produto, required=True)
    
class ProdutoForm(Form):
    title = base.StringField(required=True)
    price = base.FloatField()
    release = base.DateField()

def salvar(_logged_user, **propriedades):
    produto = Produto(title=propriedades['title'], price=float(propriedades['price']))
    chave_do_livro = produto.put()
    chave_de_usuario=_logged_user.key
    autorArco=AutorArco(origin=chave_de_usuario, destination = chave_do_livro)
    autorArco.put()
    return RedirectResponse(router.to_path(index))

def editar_form(produto_id):
    contexto = {'salvar_path': router.to_path(editar)}
    return TemplateResponse(contexto, 'produto/form.html')

def editar(_resp, **propriedades):
    produto = Produto(title=propriedades['title'], price=float(propriedades['price']))
    produto.put()
    return RedirectResponse(router.to_path(index))