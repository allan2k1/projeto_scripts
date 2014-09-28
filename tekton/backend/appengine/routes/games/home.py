from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index(_resp):
    _resp.write("bosta")

@login_not_required
@no_csrf
def form(_resp):
    _resp.write("ex")