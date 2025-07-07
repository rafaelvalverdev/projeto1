from flask_sqlalchemy import SQLAlchemy  # type: ignore
from datetime import datetime

db = SQLAlchemy()


class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    # Data e hora que a tarefa foi criada
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    concluida = db.Column(db.Boolean, default=False)  # Status da tarefa

    def __repr__(self):
        return f'<Tarefa {self.id}: {self.titulo}>'
