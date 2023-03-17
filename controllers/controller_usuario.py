from database.tables import Usuario
from database.connection import Connection
from sqlalchemy.orm import Session


class ControllerUsuario(Usuario):
    def __init__(self):
        super().__init__()
        self.connection = Connection()

        self.sessao = Session(bind=self.connection.engine)

    def insert_or_update(self, dados_list):
        try:
            for dados_dict in dados_list:
                if dados_dict.get('id_usuario'):
                    usuario = self.sessao.query(Usuario).filter_by(
                        id_usuario=dados_dict['id_usuario']).first()
                    if usuario:
                        usuario.ativo = dados_dict['ativo']
                        usuario.username = dados_dict['username']
                        usuario.senha = dados_dict['senha']
                else:
                    usuario_insert = Usuario(
                        username=dados_dict['username'], senha=dados_dict['senha'], ativo=dados_dict['ativo'])
                    self.sessao.add(usuario_insert)

                self.sessao.commit()

            return {'sucesso': 'usuario inserido ou alterado com sucesso'}, 200

        except Exception as e:
            return {'error': e}, 400
