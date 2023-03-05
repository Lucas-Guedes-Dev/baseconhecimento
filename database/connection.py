from sqlalchemy import create_engine, inspect
from sqlalchemy_utils import database_exists
from sqlalchemy import Column, Integer, String, MetaData, Table, Boolean

class Connection():
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:postgres@localhost/baseconhecimento')
        self.inspect = inspect(self.engine)

        self.metadata = MetaData()

    def create_db(self):
        if database_exists(self.engine.url):
            self.create_tables()

    def create_tables(self):
        try:
            if not self.inspect.has_table('usuarios'):
                Table('usuarios', self.metadata,
                    Column('id', Integer, primary_key=True),
                    Column('username', String),
                    Column('senha', String),
                    Column('ativo', Boolean, default=True)
                )
                
            self.metadata.create_all(self.engine)   

            return True
        
        except Exception as e:
            print(e)
            return False