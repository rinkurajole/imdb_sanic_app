from imdb.models import IMDB, meta


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    IMDB.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    IMDB.drop()
