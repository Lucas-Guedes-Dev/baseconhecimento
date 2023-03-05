from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return 'ola mundo'

if __name__ == '__main__':
    app.run(debug=True)