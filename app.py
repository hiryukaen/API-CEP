from flask import Flask, jsonify, render_template
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
    key = "c4380707dde242f4b78202712252204"
    url = f'https://api.weatherapi.com/v1/current.json?key={key}&q={cidade}&lang=pt'
    resposta = requests.get(url)
    result = resposta.json()

    temperatura = result['current']['temp_c']
    umidade = result['current']['humidity']
    localtime = result['location']['localtime']
    region = result['location']['region']
    vis_km = result['current']['vis_km']
    pressure_mb = result['current']['pressure_mb']


    return render_template('tempo.html' , temp=temperatura, umid=umidade, loc=localtime, reg=region, vis=vis_km, press=pressure_mb)
    #return resposta.json()

if __name__ == '__main__':
    app.run(debug=True)

