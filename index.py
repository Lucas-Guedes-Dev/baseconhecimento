from flask import Flask, request, jsonify

from controllers.controller_usuario import ControllerUsuario
from controllers.controller_permissao import ControllerPermissao
from controllers.controller_anexo import ControllerAnexo
from controllers.controller_conhecimento import ControllerConhecimento
from controllers.controller_pessoa import ControllerPessoa
from controllers.controller_relacionados import ControllerRelacionados
from controllers.controller_busca import ControllerBusca

app = Flask(__name__)

base_url = '/baseconhecimento/v1/'

@app.route(f'{base_url}/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        controller = ControllerUsuario()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    
    elif request.method == 'GET':

        paramatros_url = request.args

        controller = ControllerUsuario

        return_list = ControllerBusca(controller).select(paramatros_url)

        return jsonify(return_list)
    
    
@app.route(f'{base_url}/permissao', methods=['GET', 'POST'])
def permissao():
    if request.method == 'POST':
        controller = ControllerPermissao()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    
    elif request.method == 'GET':

        paramatros_url = request.args

        controller = ControllerPermissao

        return_list = ControllerBusca(controller).select(paramatros_url)

        return jsonify(return_list)

@app.route(f'{base_url}/anexo', methods=['GET', 'POST'])
def anexo():
    if request.method == 'POST':
        controller = ControllerAnexo()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    else:
        paramatros_url = request.args

        controller = ControllerAnexo

        return_list = ControllerBusca(controller).select(paramatros_url)

        return jsonify(return_list)


@app.route(f'{base_url}/conhecimento', methods=['GET', 'POST'])
def conhecimento():
    if request.method == 'POST':
        controller = ControllerConhecimento()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    else:
        paramatros_url = request.args
        
        controller = ControllerConhecimento

        return_list = ControllerBusca(controller).select(paramatros_url)

        return jsonify(return_list)


@app.route(f'{base_url}/pessoa', methods=['GET', 'POST'])
def pessoa():
    if request.method == 'POST':
        controller = ControllerPessoa()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    else:
        pass


@app.route(f'{base_url}/relacionados', methods=['GET', 'POST'])
def relacionados():
    if request.method == 'POST':
        controller = ControllerRelacionados()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    else:
        pass


if __name__ == '__main__':
    app.run(debug=True)
