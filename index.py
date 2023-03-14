from flask import Flask, request, jsonify
from controllers.controller_usuario import ControllerUsuario
from controllers.controller_permissao import ControllerPermissao
app = Flask(__name__)

base_url = '/baseconhecimento/v1/'

@app.route(f'{base_url}/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        controller = ControllerUsuario()
        
        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))  
    else:
        pass

@app.route(f'{base_url}/permissao', methods=['GET', 'POST'])
def permissao():
    if request.method == 'POST':
        controller = ControllerPermissao()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))
    else:
        pass

if __name__ == '__main__':
    app.run(debug=True)