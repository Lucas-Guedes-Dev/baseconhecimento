from ..database.tables import Relacionados
from ..database.connection import Connection

class Controller(Relacionados, Connection):
    def __init__(self):
        super().__init__()
    
    def insert_or_update(self):
        pass
