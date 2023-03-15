from database.tables import Conhecimento
from database.connection import Connection
from sqlalchemy.orm import Session


class ControllerConhecimento(Conhecimento):
    def __init__(self):
        super().__init__()
        self.connection = Connection()

        self.sessao = Session(bind=self.connection.engine)

    def insert_or_update(self, dados_list):
        try:
            for dados_dict in dados_list:
                if dados_dict.get('id_conhecimento'):
                    conhecimento = self.sessao.query(Conhecimento).filter_by(id_conhecimento=dados_dict['id_conhecimento']).first()
                    if conhecimento:
                        conhecimento.titulo = dados_dict['titulo']
                        conhecimento.texto_ajuda = dados_dict['texto_ajuda']
                else:
                    conhecimento_insert = Conhecimento(
                        titulo=dados_dict['titulo'], texto_ajuda=dados_dict['texto_ajuda'])
                    self.sessao.add(conhecimento_insert)

                self.sessao.commit()
            return {'sucesso': 'conhecimento inserido ou alterado com sucesso'}, 200

        except Exception as e:
            return {'error': e}, 400
