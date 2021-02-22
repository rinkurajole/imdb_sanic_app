# from sanic_envconfig import EnvConfig

# class Settings(EnvConfig):
#     DEBUG = True
#     HOST = '127.0.0.1'
#     PORT = 8000
#     DB_URL = ''

class Settings:
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8080
    DB_URL = 'postgresql://admin:admin@db/imdb'
