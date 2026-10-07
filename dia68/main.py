from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email
from forms import RegisterForm, LoginForm
from functools import wraps
from flask import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# 1. INICIALIZAR FLASK-LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
Bootstrap5(app)

# 2. DEFINIR LA CLASE BASE PRIMERO
class Base(DeclarativeBase):
    pass    

# 3. CONFIGURAR E INICIALIZAR LA BASE DE DATOS (db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# 4. DEFINIR EL FORMULARIO
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")
    
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")    
    
# 5. DEFINIR EL MODELO DE USUARIO
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))    

# 6. CREAR LAS TABLAS (AHORA db y User YA EXISTEN)
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Si el usuario no ha iniciado sesión o su id no es 1, lanzar error 403
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        # De lo contrario, continuar con la función de la ruta
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        
        # 3. Comprobar si el email ya existe en la base de datos
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
            
        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=hash_and_salted_password
        )
        db.session.add(new_user)
        db.session.commit()
        
        # 2. Iniciar sesión al usuario recién registrado y redirigir
        login_user(new_user)
        return redirect(url_for("home")) # Cambia "home" por "get_all_posts" si ese es el nombre de tu ruta principal
        
    return render_template("register.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        # 1. Buscar al usuario usando where()
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        
        # 4. Mensajes flash para email incorrecto o contraseña incorrecta
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))
            
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/secrets')
@login_required
def secrets():
    # Usar current_user para obtener el nombre del usuario activo
    return render_template("secrets.html", name=current_user.name)

@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf')


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    # Tu código para crear posts...
    pass

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    # Tu código para editar posts...
    pass

@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    # Tu código para borrar posts...
    pass


if __name__ == "__main__":
    app.run(debug=True)