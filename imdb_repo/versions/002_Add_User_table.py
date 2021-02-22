from imdb.models import User, meta


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    User.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    User.drop()
