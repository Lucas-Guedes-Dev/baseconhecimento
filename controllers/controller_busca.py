from database.connection import Connection
from sqlalchemy.orm import Session

class ControllerBusca():
    def __init__(self, parent):
        super().__init__()
        self.connection = Connection()  

        self.parent = parent

        self.session = Session(bind=self.connection.engine)

    def select(self, url_parametros):
        try:
            where_dict = {}
            for chave, valor in url_parametros.items():
                where_dict[chave] = valor

            return_list = self.session.query(self.parent).filter_by(**where_dict).all()
            
            result_list = []

            for obj in return_list:
                object_dict = vars(obj)
                del object_dict['_sa_instance_state']

                result_list.append(object_dict)

            return {'lista': result_list}, 200
        
        except Exception as e:

            return {'error': str(e)}, 400
         