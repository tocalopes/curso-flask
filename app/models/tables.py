from app import db


class User(db.Model): #uma classe que monta uma tabela, filha da classe db
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True) #cria uma coluna do tipo inteiro, sendo ela uma primary_key
    username = db.Column(db.String(20), unique = True)
    password = db.Column(db.String)
    email = db.Column(db.String, unique = True)

    def __init__(self, username, password, name, email): #construtor da classe
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self): #função que apresenta a pesquisa no banco de dados bonitinha
        return "<User %r"> % self.username


class Pos



