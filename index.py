from flask import Flask
from database.connection import Connection 
app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return 'ola mundo'

@app.route('/create-db')
def create_db():
    connection = Connection()

    connection.create_db()

    return 'feito' 

if __name__ == '__main__':
    app.run(debug=True)