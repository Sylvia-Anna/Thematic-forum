import typing

from app.client.views import UserAuthView, UserCurrentView, UserLoginView

if typing.TYPE_CHECKING:
    from app.web.app import Application

def setup_routes(app: "Application"):
    app.router.add_route('/user.login', UserLoginView)
    app.router.add_route('/user.auth', UserAuthView)
    app.router.add_route('/user.current', UserCurrentView)
