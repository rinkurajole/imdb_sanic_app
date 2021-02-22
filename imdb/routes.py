from sanic import response
from sanic.exceptions import InvalidUsage

from .models import IMDB, User
from .utils import generate_hash
from .decorators import is_user_admin


def setup_routes(app):


    @app.get("/")
    async def home(request):
        return response.html('<h1>Welcome to IMDB data explorer</h1>')


    @app.get("/movies")
    async def movie_list(request):
        query = IMDB.select()
        rows = await request.app.db.fetch_all(query)
        if rows:
            return response.json({
                'data': [dict(row) for row in rows]
            })
        return response.json({
            'message': 'No Data'
        })


    @app.get("/movies/<movie_id>")
    async def get_movie(request, movie_id):
        query = IMDB.select(IMDB.c.id==int(movie_id))
        row = await app.db.fetch_one(query)
        if row:
            return response.json({
                'data': [dict(row)]
            })
        return response.json({
            'message': 'No Movie found with id %s' % movie_id
        })


    @app.get("/search_movies")
    async def search_movies(request):
        args =  request.args
        query = ''
        if args:
            query = IMDB.select()
        if args.get('name'):
            query = query.where(IMDB.c.name.ilike('%%%s%%'%args.get('name')))
        if args.get('popularity'):
            query = query.where(IMDB.c.popularity==float(args.get('popularity')))
        elif args.get('popularity_gt'):
            query = query.where(IMDB.c.popularity > float(args.get('popularity_gt')))
        elif args.get('popularity_lt'):
            query = query.where(IMDB.c.popularity < float(args.get('popularity_lt')))
        if args.get('director'):
            query = query.where(IMDB.c.director.ilike('%%%s%%'%args.get('director')))
        if args.get('genre'):
            query = query.where(IMDB.c.genre.contains(args.get('genre').split(',')))
        if args.get('imdb_score'):
            query = query.where(IMDB.c.imdb_score==float(args.get('imdb_score')))
        elif args.get('imdb_score_gt'):
            query = query.where(IMDB.c.imdb_score > float(args.get('imdb_score_gt')))
        elif args.get('imdb_score_lt'):
            query = query.where(IMDB.c.imdb_score < float(args.get('imdb_score_lt')))
            
        rows = await app.db.fetch_all(query)
        if rows:
            return response.json({
                'data': [dict(row) for row in rows]
            })
        return response.json({
            'message': 'No data found for provided query'
        })
        
    @app.post("/movies")
    @is_user_admin
    async def create_movie(request):
        query = IMDB.insert()
        try:
            row = await app.db.execute(query, request.json)
            return response.json({'id': row, 'message': 'Movie added successfully'})
        except InvalidUsage as e:
            return response.json({'error': str(e)}, status=e.status_code)


    @app.post("/create_user")
    @is_user_admin
    async def create_user(request):
        query = User.insert()
        try:
            value = {'username': request.json.get('username'),
                     'password': generate_hash(request.json.get('password').encode('utf-8')),
                     'is_admin': bool(request.json.get('is_admin', False))}
            user_id = await app.db.execute(query, value)
            return response.json({'id': user_id, 'message': 'User added successfully'})
        except InvalidUsage as e:
            return response.json({'error': str(e)}, status=e.status_code)


    @app.get("/users")
    @is_user_admin
    async def users_list(request):
        query = User.select()
        rows = await request.app.db.fetch_all(query)
        if rows:
            return response.json({
                'data': [dict(row) for row in rows]
            })
        return response.json({
            'message': 'No Users Data'
        })
