from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Tarefa

app = Flask(__name__)
app.config.from_object(Config)  # Carrega as configurações do config.py

db.init_app(app)  # Inicializa o SQLAlchemy com o aplicativo Flask

with app.app_context():
    db.create_all()  # Cria as tabelas no banco de dados, se elas não existirem

# --- Rotas da Aplicaão ---


@app.route('/')
def index():
    tarefas = Tarefa.query.order_by(
        Tarefa.concluida.asc(), Tarefa.data_criacao.desc()).all()
    return render_template('index.html', tarefas=tarefas)


@app.route('/add', methods=['POST'])
def add_tarefa():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')

    if titulo:  # Garante que o título não esteja vazio
        nova_tarefa = Tarefa(titulo=titulo, descricao=descricao)
        # Adiciona a nova tarefa à sessão do banco de dados
        db.session.add(nova_tarefa)
        db.session.commit()  # Salva a tarefa no banco de dados
    # Redireciona de volta para a página principal
    return redirect(url_for('index'))


@app.route('/toggle/<int:tarefa_id>')
def toggle_concluida(tarefa_id):
    # Busca a tarefa pelo ID, ou retorna 404
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    tarefa.concluida = not tarefa.concluida  # Inverte o status de concluída
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:tarefa_id>', methods=['GET', 'POST'])
def edit_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    if request.method == 'POST':
        tarefa.titulo = request.form.get('titulo')
        tarefa.descricao = request.form.get('descricao')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', tarefa=tarefa)


@app.route('/delete/<int:tarefa_id>')
def delete_tarefa(tarefa_id):
    tarefa = Tarefa.query.get_or_404(tarefa_id)
    db.session.delete(tarefa)  # Deleta a tarefa da sessão
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
