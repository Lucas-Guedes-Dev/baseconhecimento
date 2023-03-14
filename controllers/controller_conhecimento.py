from ..database.tables import Conhecimento
from ..database.connection import Connection

class Controller(Conhecimento, Connection):
    def __init__(self):
        super().__init__()
    
    def insert_or_update(self):
        pass
