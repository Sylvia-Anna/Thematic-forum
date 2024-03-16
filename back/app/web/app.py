from aiohttp.web import Application

from app.web.routes import setup_routes

app = Application()

def setup_app() -> Application: 
    setup_routes(app)
    return app