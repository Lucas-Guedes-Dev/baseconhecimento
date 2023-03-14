from flask import Flask, request, jsonify
from controllers.controller_usuario import ControllerUsuario
app = Flask(__name__)

@app.route('/baseconhecimento/v1/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        controller = ControllerUsuario()

        dados_list = request.get_json()

        return jsonify(controller.insert_or_update(dados_list))  
    else:
        pass

if __name__ == '__main__':
    app.run(debug=True)