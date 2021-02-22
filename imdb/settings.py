from sanic_envconfig import EnvConfig

class Settings(EnvConfig):
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 8000
    DB_URL = ''
