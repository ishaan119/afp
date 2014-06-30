from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
applicant = Table('applicant', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('applicant_name', String(length=200)),
    Column('position', String(length=120)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
    Column('appraisal_of_self', Integer),
    Column('interest_in_field', Integer),
    Column('carrer_goals', Integer),
    Column('skills', Integer),
    Column('accomplishment', Integer),
    Column('relevant_experience', Integer),
    Column('potential', Integer),
    Column('creativity', Integer),
    Column('logic', Integer),
    Column('comments', String(length=500)),
    Column('recommendation', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['applicant'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['applicant'].drop()
