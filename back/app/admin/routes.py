import typing

if typing.TYPE_CHECKING:
    from app.web.app import Application

from app.admin.views import AdminCurrentView, AdminLoginView, AdminAuthView

def setup_routes(app: 'Application'):
    app.router.add_view('/admin.login', AdminLoginView)
    app.router.add_view('/admin.current', AdminCurrentView)
    app.router.add_view('/admin.auth', AdminAuthView)