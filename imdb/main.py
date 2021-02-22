from sanic import Sanic, response
from environs import Env

from .db import setup_database
from .settings import Settings
from .routes import setup_routes
from .middlewares import setup_middlewares


app = Sanic(__name__)


def init():
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

    
    
