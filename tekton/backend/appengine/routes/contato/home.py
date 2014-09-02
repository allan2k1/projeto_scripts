# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router


@login_not_required
@no_csrf
def index(_handler):
    path = router.to_path(funcao)
    _handler.redirect(path)


@login_not_required
@no_csrf
def funcao(_resp, req,nome):
    nome = req.get('nome')
    _resp.write('%s'%(nome))