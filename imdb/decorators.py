"""
User access checker decorator
"""
import base64
from sanic import response

from .models import User
from .utils import match_password


def is_user_admin(f):
    """ Give access to user to specific function if user is admin"""
    async def wrapper(request):
        if request.headers.get('authorization'):
            token = request.headers.get('authorization')
            plain = base64.b64decode(token.split(" ")[1]).split(b':')
            user = plain[0].decode("utf-8")
            query = "SELECT password, is_admin FROM \"user\" WHERE username = :username"
            res = await request.app.db.fetch_one(query, values={'username': user})
            if not res or not match_password(plain[1], res.get('password')):
                return response.json(
                    {'message': 'Username or Password is incorrect.'},
                    status=401
                )
            if res.get('is_admin', False):
                return await f(request)
            else:
                return response.json(
                    {'message': 'Admin access required to perform this operation.'},
                    status=403
                )
        return response.json(
            {'message': 'Please provide username and pasword.'},
            status=401
        ) 
    return wrapper    
