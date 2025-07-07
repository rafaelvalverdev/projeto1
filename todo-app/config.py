import os


class Config:

    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '99334411'

    # postgresql://usuario:senha@host:porta/nome_do_banco
    SQLALCHEMY_DATABASE_URI = 'postgresql://todo_user:99334411@localhost:5432/todo_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
