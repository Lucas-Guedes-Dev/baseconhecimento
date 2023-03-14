from ..database.tables import Pessoa
from ..database.connection import Connection

class Controller(Pessoa, Connection):
    def __init__(self):
        super().__init__()
    
    def insert_or_update(self):
        pass
