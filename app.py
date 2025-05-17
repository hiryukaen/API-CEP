from flask import Flask, jsonify
import requests


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Olá, mundo!"), 200

@app.route('/senai', methods=['GET'])
def senai():
    return jsonify(message="Olá, turma python com framework!",
    message2="Olá, dnovo!"), 200


#endpoint pesquisar endereço através do cep, retorna em formato json
@app.route('/pesquisacep/<cep>', methods=['GET'])
def pesquisacep(cep):
    url = f'http://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(url)
    return resposta.json()

@app.route('/pesquisaclima/sp', methods=['GET'])
def pesquisaclima(sp):
    cidade = "Presidente Prudente"
    key = "6530d4c9075dd9776ada9025b05803dc"
    url = f'https://api.weatherapi.com/v1/current.json?key={key}&q{cidade}&lang=pt'
    resposta = requests.get(url)
    return resposta.json()


if __name__ == '__main__':
    app.run(debug=True)

