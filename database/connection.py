from sqlalchemy import create_engine, inspect
from sqlalchemy_utils import database_exists
from sqlalchemy import MetaData
from sqlalchemy.orm import Session, registry
from .tables import *

class Connection():
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:postgres@localhost/baseconhecimento')
        self.inspect = inspect(self.engine)

        self.metadata = MetaData()
        
        self.mapper_registry = registry()

        self.mapper_registry.configure()

    def create_db(self):
        if database_exists(self.engine.url):
            self.create_tables()

    def add_user(self):
        session = Session(bind=self.engine)

        usuario_list = session.query(Usuario).filter_by(username='admin').all()

        usuario = Usuario(username='admin', senha='1234', ativo=True)
        if not usuario_list:
            session.add(usuario)
            session.commit()

        session.close()

    def create_tables(self):

        Usuario.__table__.create(bind=self.engine, checkfirst=True)
        Pessoa.__table__.create(bind=self.engine, checkfirst=True)
        Permissao.__table__.create(bind=self.engine, checkfirst=True)
        Conhecimento.__table__.create(bind=self.engine, checkfirst=True)
        Anexo.__table__.create(bind=self.engine, checkfirst=True)
        Relacionados.__table__.create(bind=self.engine, checkfirst=True)

        self.add_user()