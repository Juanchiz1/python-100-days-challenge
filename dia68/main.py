from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
login_manager = LoginManager()
login_manager.init_app(app)

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB



with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        
        # Comprobar si el usuario ya existe en la base de datos
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        
        if user:
            # El usuario ya existe
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
            
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        
        new_user = User(
            email=email,
            name=request.form.get('name'),
            password=hash_and_salted_password
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        
        return redirect(url_for("secrets"))
        
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        
        # 1. El correo no existe
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
            
        # 2. La contraseña es incorrecta
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
            
        # 3. Todo es correcto
        else:
            login_user(user)
            return redirect(url_for('secrets'))
            
    return render_template("login.html")

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

# Añadir UserMixin a la clase User
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

if __name__ == "__main__":
    app.run(debug=True)
