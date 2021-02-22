from .conftest import data

    
async def test_movies(test_cli):
    resp = await test_cli.get('/movies')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == data
