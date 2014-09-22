from __future__ import absolute_import, unicode_literals
from tekton.backend.appengine.config.template_middleware import TemplateResponse
from tekton.backend.appengine.lib.gaecookie.decorator import no_csrf


@no_csrf
def form():
    return TemplateResponse()
