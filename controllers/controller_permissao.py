from ..database.tables import Permissao
from ..database.connection import Connection

class Controller(Permissao, Connection):
    def __init__(self):
        super().__init__()
    
    def insert_or_update(self):
        pass
