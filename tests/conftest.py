import sanic
import asyncio
import pytest
from sanic.app import Sanic
from sanic.websocket import WebSocketProtocol
from sanic import response


data = {
    "popularity": 84,
    "director": "Victor Tyson",
    "genre": [
        "Adventure",
        " Family",
        " Fantasy",
        " Musical"
    ],
    "imdb_score": 8.0,
    "name": "The Wizard of Iceland"
}

@pytest.fixture
def app():
    app = Sanic("test_sanic_app")
    
    @app.get("/")
    async def test_home(request):
        return response.json({'message': 'Welcome to IMDB data explorer'})

    @app.get("/movies")
    async def test_movie_list(request):
        return response.json(data)

    @app.listener('before_server_start')
    async def mock_init_db(app, loop):
        await asyncio.sleep(0.01)

    yield app

    
@pytest.fixture
def sanic_server(loop, app, test_server):
    return loop.run_until_complete(test_server(app))


@pytest.fixture
def test_cli(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app, protocol=WebSocketProtocol))
