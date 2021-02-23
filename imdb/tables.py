"""
Module for exporting json file data into database
Use: Run/Export this module from python shell
"""
import json

from databases import Database
from environs import Env

from .models import IMDB
from .settings import Settings


env = Env()
env.read_env()
database = Database(Settings.DB_URL)

    
async def insert_records(): 
    """ Insert records into IMDB table """
    try:
        await database.connect()
        print("Connected to Database")
        
        print("loading data into tables")
        f = open('imdb.json', 'r')
        imdb_data = f.read()
        
        # Executing many
        query = IMDB.insert()
        values = json.loads(imdb_data.replace('\n', ''))
    
        await database.execute_many(query, values)
        print("IMDB data loaded successfully")

        await database.disconnect()
        print('Disconnecting from Database')
    except Exception as e:
        print('Connection to Database Failed', e)


# Uncomment below 3 lines if you want to load fresh copy of imdb data into database
# After work done comment otherwise this will call on every server start and stop event

import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(insert_records())
loop.close()
