from flask import Flask, jsonify, request, session
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash
import os # Usado para a chave secreta da sessão

# --- Configuração da Aplicação Flask ---
app = Flask(__name__)
CORS(app, supports_credentials=True) # Habilita CORS e permite credenciais/cookies
# Chave secreta para gerenciar sessões de login de forma segura
# !!! ATENÇÃO: Em um projeto real, use uma chave mais complexa e segura !!!
app.secret_key = os.urandom(24) 

# --- Configurações do Banco de Dados ---
# Substitua com suas credenciais do MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '', # Sua senha real
    'database': 'hemocentro_db'
}

# --- Função para conectar ao banco de dados ---
def criar_conexao():
    try:
        return mysql.connector.connect(**db_config)
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# --- ROTAS DA API ---

# Rota para o estoque de sangue (já existente)
@app.route('/api/estoque', methods=['GET'])
def get_estoque():
    conexao = criar_conexao()
    if not conexao:
        return jsonify({"erro": "Não foi possível conectar ao banco de dados"}), 500
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT tipo_sanguineo, quantidade_bolsas FROM estoque_sanguineo")
        estoque = cursor.fetchall()
        return jsonify(estoque)
    finally:
        cursor.close()
        conexao.close()

# Rota para CADASTRO de um novo usuário
@app.route('/api/register', methods=['POST'])
def register_user():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')

    if not nome or not email or not senha:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    # Criptografa a senha antes de salvar
    senha_hash = generate_password_hash(senha)

    conexao = criar_conexao()
    if not conexao:
        return jsonify({"erro": "Erro no servidor"}), 500
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha_hash) VALUES (%s, %s, %s)", (nome, email, senha_hash))
        conexao.commit()
        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    except mysql.connector.IntegrityError:
        return jsonify({"erro": "Este e-mail já está cadastrado."}), 409
    except Error as e:
        return jsonify({"erro": f"Erro no banco de dados: {e}"}), 500
    finally:
        cursor.close()
        conexao.close()

# Rota para LOGIN do usuário
@app.route('/api/login', methods=['POST'])
def login_user():
    dados = request.get_json()
    email = dados.get('email')
    senha = dados.get('senha')

    if not email or not senha:
        return jsonify({"erro": "E-mail e senha são obrigatórios"}), 400

    conexao = criar_conexao()
    if not conexao:
        return jsonify({"erro": "Erro no servidor"}), 500
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()

        if usuario and check_password_hash(usuario['senha_hash'], senha):
            # Login bem-sucedido, armazena informações na sessão
            session['user_id'] = usuario['id']
            session['user_name'] = usuario['nome']
            return jsonify({"mensagem": f"Bem-vindo, {usuario['nome']}!", "usuario": {"nome": usuario['nome']}}), 200
        else:
            return jsonify({"erro": "E-mail ou senha inválidos"}), 401
    finally:
        cursor.close()
        conexao.close()

# Rota para LOGOUT
@app.route('/api/logout', methods=['POST'])
def logout_user():
    session.clear() # Limpa todos os dados da sessão
    return jsonify({"mensagem": "Logout realizado com sucesso."}), 200

# Rota para verificar se o usuário já está logado
@app.route('/api/check_session', methods=['GET'])
def check_session():
    if 'user_id' in session:
        return jsonify({"logado": True, "usuario": {"nome": session['user_name']}}), 200
    else:
        return jsonify({"logado": False}), 200

# Rota para BUSCAR todos os comentários
@app.route('/api/comments', methods=['GET'])
def get_comments():
    conexao = criar_conexao()
    if not conexao:
        return jsonify({"erro": "Erro no servidor"}), 500
    cursor = conexao.cursor(dictionary=True)
    try:
        # Junta as tabelas para pegar o nome do usuário junto com o comentário
        query = """
            SELECT c.id, c.comentario_texto, c.data_postagem, u.nome as nome_usuario
            FROM comentarios c
            JOIN usuarios u ON c.usuario_id = u.id
            ORDER BY c.data_postagem DESC
        """
        cursor.execute(query)
        comentarios = cursor.fetchall()
        return jsonify(comentarios)
    finally:
        cursor.close()
        conexao.close()

# Rota para PUBLICAR um novo comentário
@app.route('/api/comments', methods=['POST'])
def post_comment():
    # Verifica se o usuário está logado
    if 'user_id' not in session:
        return jsonify({"erro": "Acesso não autorizado. Faça o login para comentar."}), 401

    dados = request.get_json()
    comentario_texto = dados.get('comentario_texto')
    usuario_id = session['user_id'] # Pega o ID do usuário da sessão

    if not comentario_texto:
        return jsonify({"erro": "O comentário não pode estar vazio."}), 400

    conexao = criar_conexao()
    if not conexao:
        return jsonify({"erro": "Erro no servidor"}), 500
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO comentarios (comentario_texto, usuario_id) VALUES (%s, %s)", (comentario_texto, usuario_id))
        conexao.commit()
        return jsonify({"mensagem": "Comentário publicado com sucesso!"}), 201
    except Error as e:
        return jsonify({"erro": f"Erro no banco de dados: {e}"}), 500
    finally:
        cursor.close()
        conexao.close()

# --- Rodar a aplicação ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)