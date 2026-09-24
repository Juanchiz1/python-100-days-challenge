import os
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

ckeditor = CKEditor(app)

# Capturamos la ruta absoluta del directorio donde se encuentra main.py (dia67)
basedir = os.path.abspath(os.path.dirname(__file__))

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

# Forzamos la ruta apuntando a la carpeta 'instance' exacta dentro de 'dia67'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'posts.db')
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")    


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # Consulta a la base de datos para extraer todos los registros
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Recupera un BlogPost específico basado en su ID; si no existe, devuelve error 404
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    # Instanciamos el formulario que creaste arriba
    form = CreatePostForm()
    
    if form.validate_on_submit():
        current_date = date.today().strftime("%B %d, %Y")
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=current_date
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
        
    # CRÍTICO: Asegúrate de enviar la variable 'form' a render_template
    return render_template("make-post.html", form=form, is_edit=False)

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    # Recuperar el post de la base de datos
    post = db.get_or_404(BlogPost, post_id)
    
    # Rellenar el formulario con los datos actuales del post
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    
    # Si el usuario envía las ediciones y pasa la validación
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        
        # Redirigir a la vista del post recién editado
        return redirect(url_for("show_post", post_id=post.id))
        
    # Enviar la variable is_edit=True para que el HTML sepa que estamos editando
    return render_template("make-post.html", form=edit_form, is_edit=True)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    # Buscar el post por su ID
    post_to_delete = db.get_or_404(BlogPost, post_id)
    
    # Eliminarlo de la base de datos y guardar los cambios
    db.session.delete(post_to_delete)
    db.session.commit()
    
    # Redirigir de vuelta a la página principal
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True, port=5003)
