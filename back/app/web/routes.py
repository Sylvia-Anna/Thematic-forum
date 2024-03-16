# Определение всех routes

from aiohttp.web_app import Application

def setup_routes(app: Application):
    from app.admin.routes import setup_routes as admin_setup_routes
    from app.client.routes import setup_routes as client_setup_routes

    admin_setup_routes(app)
    client_setup_routes(app)


    