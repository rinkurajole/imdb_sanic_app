from sanic_envconfig import EnvConfig

class Settings(EnvConfig):
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 8080
    DB_URL = ''
    POSTGRES_USER=''
    POSTGRES_PASSWORD=''
    POSTGRES_DB=''
