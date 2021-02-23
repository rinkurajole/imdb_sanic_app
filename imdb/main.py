"""
Main module
Operations: Export environment vars, Setup database, Setup and Export routes, 
            Add respose security headers using middlewares, Start Server
"""
from sanic import Sanic, response
from environs import Env

from .db import setup_database
from .settings import Settings
from .routes import setup_routes
from .middlewares import setup_middlewares


app = Sanic(__name__)


def init():
    """ Invoking app run to start server"""
    env = Env()
    env.read_env()
    app.config.from_object(Settings)
    setup_database(app)
    setup_routes(app)
    setup_middlewares(app)
    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        auto_reload=app.config.DEBUG,
    )

    
    
