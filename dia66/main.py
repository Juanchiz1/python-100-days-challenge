from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
import os
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
# 1. Obtiene la ruta absoluta exacta de la carpeta dia66
basedir = os.path.abspath(os.path.dirname(__file__))

# 2. Conecta específicamente con el archivo cafes.db dentro de dia66/instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'cafes.db')

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    
    # Validar que la lista no esté vacía antes de elegir
    if not all_cafes:
        return jsonify(error={"Not Found": "Sorry, we don't have any cafes in the database."}), 404
    
    random_cafe = random.choice(all_cafes)
    
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price,
    })


@app.route("/all")
def get_all_cafes():
    # 1. Consultar todos los cafés en la base de datos (puedes ordenarlos alfabéticamente si lo deseas)
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    
    # 2. Convertir la lista de objetos SQLAlchemy a una lista de diccionarios
    # Utilizamos una "list comprehension" de Python para crear la lista rápidamente
    cafes_list = [
        {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        } for cafe in all_cafes
    ]
    
    # 3. Retornar los datos serializados en JSON bajo la clave "cafes"
    return jsonify(cafes=cafes_list)

# HTTP GET - Read Record
@app.route("/search")
def search_cafe():
    # 1. Obtener el parámetro 'loc' de la URL (ej. /search?loc=Peckham)
    query_location = request.args.get("loc")
    
    # 2. Consultar la base de datos filtrando por la ubicación exacta
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    cafes_at_location = result.scalars().all()
    
    # 3. Comprobar si se encontraron resultados
    if cafes_at_location:
        # Convertir a lista de diccionarios
        cafes_list = [
            {
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price,
            } for cafe in cafes_at_location
        ]
        return jsonify(cafes=cafes_list)
    else:
        # 4. Retornar mensaje de error 404 si la lista está vacía
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    # 1. Crear un nuevo objeto Cafe con los datos provenientes de la petición (simulando un formulario)
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        # Los booleanos desde un formulario suelen llegar como strings, los convertimos a bool
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    
    # 2. Guardar el nuevo registro en la base de datos
    db.session.add(new_cafe)
    db.session.commit()
    
    # 3. Retornar un mensaje JSON de éxito
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    # 1. Capturar el nuevo precio desde los parámetros de la URL (?new_price=...)
    new_price = request.args.get("new_price")
    
    # 2. Buscar el café específico por su ID en la base de datos
    cafe = db.session.get(Cafe, cafe_id)
    
    # 3. Intentar actualizar si el café existe
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        # Retornamos el JSON de éxito junto con el código 200 (OK)
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        # Si db.session.get() retorna None, el café no existe. Retornamos el error y el código 404.
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    # 1. Extraer la API Key de los parámetros de la petición
    api_key = request.args.get("api-key")
    
    # 2. Validar credenciales de seguridad
    if api_key == "TopSecretAPIKey":
        # 3. Buscar el recurso en la base de datos
        cafe = db.session.get(Cafe, cafe_id)
        
        if cafe:
            # 4. Eliminar el registro y guardar los cambios
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            # Error 404: La clave es correcta, pero el café no existe
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        # Error 403: El usuario no tiene permisos (clave incorrecta o ausente)
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
