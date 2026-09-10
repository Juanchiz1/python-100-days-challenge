from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

TMDB_API_KEY = "TU_API_KEY_DE_TMDB"
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_INFO_URL = "https://api.themoviedb.org/3/movie"
TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

# Formulario para buscar la película por título
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
    
# CREAR BD
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREAR TABLA
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()
    
with app.app_context():
    db.create_all()

    # --- PEGA ESTO TEMPORALMENTE PARA LLENAR LA BD ---
    if not db.session.execute(db.select(Movie).where(Movie.title == "Phone Booth")).scalar():
        new_movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()
    # --------------------------------------------------    

# FORMULARIO WTFORMS
class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

# RUTA INICIO
@app.route("/")
def home():
    # 1. Obtener todas las películas ordenadas por rating (de menor a mayor)
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all() # Convertir el resultado en una lista de Python
    
    # 2. Asignar el ranking dinámicamente: 
    # El de menor rating recibe el número mayor (ej. 10) y el de mayor rating recibe el 1.
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    
    # 3. Consultar las películas ordenadas por su nuevo ranking para mostrarlas correctamente
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars().all()
    
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        # Hacer petición a la API de TMDB para buscar coincidencias
        response = requests.get(TMDB_SEARCH_URL, params={"api_key": TMDB_API_KEY, "query": movie_title})
        data = response.json().get("results")
        # Renderizar la página de selección con los resultados encontrados
        return render_template("select.html", options=data)
        
    return render_template("add.html", form=form)

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_info_url = f"{TMDB_INFO_URL}/{movie_api_id}"
        # Petición para obtener todos los detalles de la película seleccionada
        response = requests.get(movie_info_url, params={"api_key": TMDB_API_KEY})
        data = response.json()
        
        # Crear un nuevo objeto Movie con los datos de la API
        new_movie = Movie(
            title=data.get("title"),
            # Extraer solo el año de la fecha de lanzamiento (ej. "2022-12-14" -> 2022)
            year=data.get("release_date").split("-")[0] if data.get("release_date") else 0,
            description=data.get("overview"),
            img_url=f"{TMDB_IMAGE_URL}{data.get('poster_path')}" if data.get("poster_path") else "",
            rating=0.0,
            ranking=0,
            review=""
        )
        db.session.add(new_movie)
        db.session.commit()
        
        # Redirigir a la ruta de edición pasando el ID de la nueva película recién creada
        return redirect(url_for("rate_movie", id=new_movie.id))

@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

# RUTA ACTUALIZAR
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
        
    return render_template("edit.html", movie=movie, form=form)

if __name__ == '__main__':
    app.run(debug=True)