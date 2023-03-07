from sqlalchemy import create_engine, inspect
from sqlalchemy_utils import database_exists
from sqlalchemy import MetaData
from sqlalchemy.orm import relationship
from .tables import *

class Connection():
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:postgres@localhost/baseconhecimento')
        self.inspect = inspect(self.engine)

        self.metadata = MetaData()

    def create_db(self):
        if database_exists(self.engine.url):
            self.create_tables()

    def create_tables(self):
        Usuario.__table__.create(bind=self.engine, checkfirst=True)
        Pessoa.__table__.create(bind=self.engine, checkfirst=True)
        Permissao.__table__.create(bind=self.engine, checkfirst=True)
        Conhecimento.__table__.create(bind=self.engine, checkfirst=True)
        Anexo.__table__.create(bind=self.engine, checkfirst=True)
        Relacionados.__table__.create(bind=self.engine, checkfirst=True)