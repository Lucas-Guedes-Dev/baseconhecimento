from database.tables import Anexo
from database.connection import Connection
from sqlalchemy.orm import Session


class ControllerAnexo(Anexo):
    def __init__(self):
        super().__init__()
        self.connection = Connection()

        self.sessao = Session(blind=self.connection.engine)

    def insert_or_update(self, dados_list):
        try:
            for daddos_dict in dados_list:
                if daddos_dict.get('id_anexo'):
                    anexo = self.sessao.query(Anexo).filter_by(
                        id_anexo=daddos_dict['id_anexo']).first()
                    if anexo:
                        anexo.anexo = daddos_dict['anexo']
                        anexo.id_conhecimento = daddos_dict['id_conhecimento']

                else:
                    anexo_insert = Anexo(
                        anexo=daddos_dict['anexo'], id_conhecimento=daddos_dict['id_conhecimento'])
                    self.sessao.add(anexo_insert)

                self.sessao.commit()

            return {'sucesso': 'anexo inserido ou alterado com sucesso'}, 200

        except Exception as e:
            return {'error': e}, 400
