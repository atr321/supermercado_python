#importar bibliotecas
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

#instanciar a app
supermercado = Flask(__name__)

#configurar db
supermercado.config['MYSQL_DATABASE_USER'] = 'root'
supermercado.config['MYSQL_DATABASE_PASSWORD'] = 'root'
supermercado.config['MYSQL_DATABASE_DB'] = 'supermercado'

#instanciar db
mysql = MySQL()
mysql.init_app(supermercado)

#rota para /
@supermercado.route('/')
#metodo
def index():
    return render_template('form_login.html')


@supermercado.route('/listar_Produtos')
def listar_Produtos():

    # criar uma conexao com o db
    cursor = mysql.connect().cursor()
    # submeter o comando SQL
    cursor.execute(f"SELECT * FROM produto")
    # recuperar dados
    produtos = cursor.fetchall()
    mysql.connect().close()

    # imprimir nome
    return render_template('listar_Produtos.html', produto=produtos)

#rota para /login
@supermercado.route('/login')
#metodo que responde /login
def login():
    nome_usuario = request.args.get('nome_usuario')
    senha_usuario = request.args.get('senha_usuario')

    #criar uma conexao com o db
    cursor = mysql.connect().cursor()
    #submeter o comando SQL
    cursor.execute(f"SELECT nomeusuario FROM usuario where nomeusuario = '{nome_usuario}' and senhausuario = '{senha_usuario}'")
    #recuperar dados
    dados = cursor.fetchone()
    mysql.connect().close()

    #imprimir nome
    return render_template('logado.html',nome_usuario=str(dados[0]))


    #executar
supermercado.run()