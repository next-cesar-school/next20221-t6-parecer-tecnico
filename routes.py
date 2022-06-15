from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

@app.route('/listar-parecer', methods=["GET"])
def listParecer():
    return "Listagem de pareceres"

@app.route('/cadastro-parecer', methods=["POST"])
def cadParecer():
    return "Adicionar parecer"

@app.route('/remover-parecer', methods = ["DELETE"])
def deleteParecer():
    return "Parecer deletado!"

@app.route('/baixar-arquivo')
def baixarArq():
    return "Arquivo baixado!"


if __name__== '__main__':
    app.run(debug=True)

