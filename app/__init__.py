#importando uma a classe Flask da biblioteca flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#app é um instancia da classe flask
#variavel name é um variavel especial que especifica qual o arquivo que estamos executando
app = Flask(__name__)
app.config('SQLALCHEMY_DATABASE_URI') = 'mysql://root:@localhost/storage.db' #faz a conexão com o banco de dados
db = SQLAlchemy(app)



#decorator -> @  -> aplica um finção a outra
@app.route("/") #metodo rooute defini uma rota para um pagina, no caso, a função index
def index():
    return "hello word"

#testa se estamos executando o arquivo principal do nosso app
if __name__  == "__main__":
    app.run()

