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

@app.route('/tempo', methods=['GET'])
def tempo():
    cidade = "Presidente Prudente"
    key = "158e461d420bb8b31a1288bbe9dee7ee"
    url = f'https://api.weatherapi.com/v1/current.json?key={key}&q{cidade}&lang=pt'
    resposta = requests.get(url)
    return resposta.json()

    temperatura = result['curent']['temp_c']
    umidade = result['current']['humidity']

    return render_template('tempo.html' , temp=temperatura, umid=umidade)
    #return resposta.json()

if __name__ == '__main__':
    app.run(debug=True)

