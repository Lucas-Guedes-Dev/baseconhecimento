from flask import Flask, request, jsonify
from controllers.controller_usuario import ControllerUsuario
from controllers.controller_permissao import ControllerPermissao
from controllers.controller_anexo import ControllerAnexo
from controllers.controller_conhecimento import ControllerConhecimento
app = Flask(__name__)


@app.route('/baseconhecimento/v1/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        controller = ControllerUsuario()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    else:
        pass


@app.route('/baseconhecimento/v1/permissao', methods=['GET', 'POST'])
def permissao():
    if request.method == 'POST':
        controller = ControllerPermissao()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    else:
        pass


@app.route('/baseconhecimento/v1/anexo', methods=['GET', 'POST'])
def anexo():
    if request.method == 'POST':
        controller = ControllerAnexo()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    else:
        pass


@app.route('/baseconhecimento/v1/conhecimento', methods=['GET', 'POST'])
def anexo():
    if request.method == 'POST':
        controller = ControllerConhecimento()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)
