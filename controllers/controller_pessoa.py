from database.tables import Pessoa
from database.connection import Connection
from sqlalchemy.orm import Session


class ControllerPessoa(Pessoa):
    def __init__(self):
        super().__init__()
        self.connection = Connection()

        self.sessao = Session(bind=self.connection.engine)

    def insert_or_update(self, dados_list):
        try:
            for dados_dict in dados_list:
                if dados_dict.get('id_pessoa'):
                    pessoa = self.sessao.query(Pessoa).filter_by(
                        id_pessoa=dados_dict['id_pessoa']).first()
                    if pessoa:
                        pessoa.nome = dados_dict['nome']
                        pessoa.documento = dados_dict['documento']
                        pessoa.tipo_documento = dados_dict['tipo_documento']
                        pessoa.ativo = dados_dict['ativo']
                else:
                    pessoa_insert = Pessoa(
                        nome=dados_dict['nome'], documento=dados_dict['documento'], tipo_documento=dados_dict['tipo_documento'], ativo=dados_dict['ativo'])
                    self.sessao.add(pessoa_insert)

                self.sessao.commit()

            return {'sucesso': 'pessoa inserida ou alterada com sucesso'}, 200

        except Exception as e:
            return {'error': e}, 400
