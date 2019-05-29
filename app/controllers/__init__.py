#importando uma a classe Flask da biblioteca flask
from flask import Flask
#app é um instancia da classe flask
#variavel name é um variavel especial que especifica qual o arquivo que estamos executando
app = Flask(__name__)

from app.controllers import default
