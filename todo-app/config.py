import os


class Config:
    # A SECRET_KEY é usada para segurança em sessões, CSRF, etc.
    # É importante para aplicações em produção.
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'uma_chave_muito_secreta_e_complexa_que_voce_deve_mudar'

    # String de conexão com o PostgreSQL
    # postgresql://usuario:senha@host:porta/nome_do_banco
    SQLALCHEMY_DATABASE_URI = 'postgresql://todo_user:sua_senha_segura@localhost:5432/todo_db'
    # Desativa o rastreamento de modificações do SQLAlchemy (consome menos memória)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
