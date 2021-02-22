#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='imdb_repo', url='postgresql://admin:admin@localhost/sanic', debug='False')
