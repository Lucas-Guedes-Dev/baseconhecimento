from database.tables import Permissao
from database.connection import Connection
from sqlalchemy.orm import Session

class ControllerPermissao(Permissao):
    def __init__(self):
        super().__init__()
        self.connection = Connection()

        self.sessao = Session(bind=self.connection.engine)
    
    def insert_or_update(self, dados_list):
        try:
            for dados_dict in dados_list:
                if dados_dict.get('id_permissao'):
                    permissao = self.sessao.query(Permissao).filter_by(id_permissao=dados_dict['id_permissao']).first()
                    if permissao:
                        permissao.nivel_permissao = dados_dict['nivel_permissao']
                        permissao.id_usuario = dados_dict['id_usuario']
                    
                else:
                    permissao_insert = Permissao(nivel_permissao=dados_dict['nivel_permissao'], id_usuario=dados_dict['id_usuario'])
                    self.sessao.add(permissao_insert)

                self.sessao.commit()

            return {'sucesso': 'permissao inserida ou alterada com sucesso'}, 200


        except Exception as e:
            return {'error': e}, 400
