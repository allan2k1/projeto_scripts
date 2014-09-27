# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.ndb.form import ModelForm
from gaegraph.model import Node, Arc
from gaeforms.ndb import property


class Produto(Node):
    nome = ndb.StringProperty(required=True)
    preco = ndb.StringProperty(required=True)

class AutorArco(Arc):
    origin = ndb.KeyProperty(required=True)
    destination = ndb.KeyProperty(Produto, required=True)