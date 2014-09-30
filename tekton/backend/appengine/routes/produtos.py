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
def index(_logged_user):
    chave_do_usuario = _logged_user.key
    query = AutorArco.query(AutorArco.origin==chave_do_usuario)
    autor_arcos = query.fetch()
    chaves_de_produtos = [arco.destination for arco in autor_arcos]
    produto_lista = ndb.get_multi(chaves_de_produtos)
    produto_form = ProdutoFormTable()
    produto_lista = [produto_form.fill_with_model(produto) for produto in produto_lista]
    editar_form_path = router.to_path(editar_form)
    delete_path = router.to_path(delete)
    for produto in produto_lista:
        produto['edit_path'] = '%s/%s' % (editar_form_path, produto['id'])
        produto['delete_path'] = '%s/%s' % (delete_path, produto['id'])
    contexto = {'produto_lista': produto_lista, 'form_path':router.to_path(form)}
    return TemplateResponse(contexto)

def delete(produto_id):
    chave = ndb.Key(Produto, int(produto_id))
    chave.delete()
    return RedirectResponse(router.to_path(index))

@no_csrf
def form():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)

class Produto(Node):
    title = ndb.StringProperty(required=True)
    price = ndb.FloatProperty(required=True)
    release = ndb.DateProperty()

class AutorArco(Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Produto, required=True)
    
class ProdutoForm(ModelForm):
    _model_class = Produto
    _include = [Produto.title, Produto.release, Produto.price]

class ProdutoFormTable(ModelForm):
    _model_class = Produto
    _include = [Produto.title, Produto.creation, Produto.price]

def salvar(_logged_user, **propriedades):
    produto_form = ProdutoForm(**propriedades)
    erros = produto_form.validate()

    if erros:
        contexto = {'salvar_path': router.to_path(salvar), 'erros':erros, 'produto':produto_form}
        return TemplateResponse(contexto, 'produtos/form.html')
    else:
        produto = produto_form.fill_model()
        chave_do_livro = produto.put()
        chave_de_usuario=_logged_user.key
        autorArco=AutorArco(origin=chave_de_usuario, destination = chave_do_livro)
        autorArco.put()
        return RedirectResponse(router.to_path(index))

@no_csrf
def editar_form(produto_id):
    produto_id = int(produto_id)
    produto = Produto.get_by_id(produto_id)
    produto_form = ProdutoForm()
    produto_form.fill_with_model(produto)
    contexto = {'salvar_path': router.to_path(editar, produto_id), 'produto':produto_form}
    return TemplateResponse(contexto, 'produtos/form.html')

def editar(produto_id, **propriedades):
    produto_id = int(produto_id)
    produto = Produto._get_by_id(produto_id)
    produto_form = ProdutoForm(**propriedades)
    erros = produto_form.validate()

    if erros:
        contexto = {'salvar_path': router.to_path(salvar), 'erros':erros, 'produto':produto_form}
        return TemplateResponse(contexto, 'produtos/form.html')
    else:
        produto = produto_form.fill_model(produto)
        produto.put()
        return RedirectResponse(router.to_path(index))
