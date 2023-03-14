from ..database.tables import Anexo
from ..database.connection import Connection

class Controller(Anexo, Connection):
    def __init__(self):
        super().__init__()
    
    def insert_or_update(self):
        pass
