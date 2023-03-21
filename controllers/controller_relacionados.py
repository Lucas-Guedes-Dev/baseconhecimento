from database.tables import Relacionados
from database.connection import Connection
from sqlalchemy.orm import Session


class ControllerRelacionados(Relacionados):
    def __init__(self):
        super().__init__()
        self.connection = Connection()

        self.sessao = Session(bind=self.connection.engine)

    def insert_or_update(self, dados_list):
        try:
            for dados_dict in dados_list:
                if dados_dict.get('id_relacao'):
                    relacionado = self.sessao.query(Relacionados).filter_by(
                        id_relacionado=dados_dict['id_relacao']).first()
                    if relacionado:
                        relacionado.id_conhecimento_base = dados_dict['id_conhecimento_base']
                        relacionado.id_conhecimento_relacionado = dados_dict[
                            'id_conhecimento_relacionado']
                else:
                    relacionado_insert = Relacionados(
                        id_conhecimento_base=dados_dict['id_conhecimento_base'], id_conhecimento_relacionado=dados_dict['id_conhecimento_relacionado'])
                    self.sessao.add(relacionado_insert)

                self.sessao.commit()

            return {'sucesso': 'relacionado inserido ou alterado com sucesso'}, 200

        except Exception as e:
            return {'error': e}, 400
