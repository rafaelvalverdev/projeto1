from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Inicializamos o SQLAlchemy, mas não conectamos ainda (isso será feito em app.py)
db = SQLAlchemy()


class Tarefa(db.Model):
    __tablename__ = 'tarefas'  # Nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)  # Não pode ser nulo
    descricao = db.Column(db.Text, nullable=True)  # Pode ser nulo
    # Data e hora que a tarefa foi criada
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    concluida = db.Column(db.Boolean, default=False)  # Status da tarefa

    def __repr__(self):
        return f'<Tarefa {self.id}: {self.titulo}>'
