from flask import Flask, render_template, request, redirect, url_for, flash
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms import FileField
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'csv'}  # Adapte conforme necessário
app.config['SECRET_KEY'] = 'sua_chave_secreta_aleatoria'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, username, password):
        self.id = username
        self.password = password

users = {'user': User('user', 'password')}  # Substitua isso por um sistema de armazenamento mais seguro

class UploadForm(FlaskForm):
    file = FileField()

@app.route('/')
@login_required
def index():
    form = UploadForm()
    return render_template('index.html', form=form)

@app.route('/upload', methods=['POST'])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Implemente a lógica de treinamento do modelo aqui
            flash("Modelo treinado com sucesso!", 'success')
            return redirect(url_for('index'))
    flash("Falha no treinamento do modelo.", 'danger')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user.password == password:
            login_user(user)
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciais inválidas.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout bem-sucedido!', 'success')
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(username):
    return users.get(username)

if __name__ == '__main__':
    app.run(debug=True)
