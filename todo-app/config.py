import os


class Config:
    # A SECRET_KEY é usada para segurança em sessões, CSRF, etc.
    # É importante para aplicações em produção.
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '99334411'

    # String de conexão com o PostgreSQL
    # postgresql://usuario:senha@host:porta/nome_do_banco
    SQLALCHEMY_DATABASE_URI = 'postgresql://todo_user:99334411@localhost:5432/todo_db'
    # Desativa o rastreamento de modificações do SQLAlchemy (consome menos memória)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
