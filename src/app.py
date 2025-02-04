"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Vehiculos, Planetas, Personajes
from sqlalchemy import select
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

###todos los registros de una tabla User
@app.route('/user', methods=['GET'])
def handle_hello():

    #consulta de todos los valores de una tabla
    data = db.session.scalars(select(User)).all()
    results = list(map(lambda item: item.serialize(),data))

    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results":results
    }

    return jsonify(response_body), 200


#consulta de un solo registro
@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = db.session.execute(select(User).filter_by(id=id)).scalar_one()

        response_body = {
            "msg": "Hello, this is your GET /user response ",
            "result":user.serialize()
        }

        return jsonify(response_body), 200
    except:
        return jsonify({"msg":"user not exist"}), 404


##### POST ENDPOINT
@app.route('/user', methods=['POST'])
def crear_user():
    request_data = request.json
    print(request_data)

    user = User(
        username=request_data["username"],
        email=request_data["email"],
        password=request_data["password"]
    )

    db.session.add(user)
    db.session.commit()

    response_body = {
        "msg": "User creado"
    }

    return jsonify(response_body), 200

##### DELETE ENDPOINT
@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):

    user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
    db.session.delete(user)
    db.session.commit()

    response_body = {
        "msg":"user deleted"
    }

    return jsonify(response_body), 200

# GET vehiculos endpoint
@app.route('/vehiculos', methods=['GET'])
def get_vehiculos():
    data = db.session.scalars(select(Vehiculos)).all()
    results = list(map(lambda item: item.serialize(), data))

    response_body = {
        "msg":"Lista de todos los vehiculos",
        "results":results

    }

    return jsonify(response_body), 200

# consulta de un solo registro vehiculo
@app.route('/vehiculos/<int:id>', methods=['GET'])
def vehiculo(id):
    try:
        user = db.session.execute(select(Vehiculos).filter_by(id=id)).scalar_one()

        response_body = {
            "msg": "Hello, this is your GET /user response ",
            "result":vehiculo.serialize()
        }

        return jsonify(response_body), 200
    except:
        return jsonify({"msg":"vehiculo not found"}), 404
    
# POST vehiculos
@app.route('/vehiculos', methods=['POST'])
def crear_vehiculo():
    request_data = request.json
    print(request_data)

    vehiculo = Vehiculos(
        nombre=request_data["nombre"],
        modelo=request_data["modelo"],
        clase_vehiculo=request_data["clase_vehiculo"],
        fabricante=request_data["fabricante"],
        longitud=request_data["longitud"],
        precio=request_data["precio"],
        tripulacion=request_data["tripulacion"],
        velocidad_max=request_data["velocidad_max"],
        capacidad_carga=request_data["capacidad_carga"],
        consumibles=request_data["consumibles"],
        url=request_data["url"]
    )

    db.session.add(vehiculo)
    db.session.commit()

    response_body = {
        "msg": "Vehiculo creado"
    }

    return jsonify(response_body), 200

#DELETE vehiculos
@app.route('/vehiculos/<int:id>', methods=['DELETE'])
def delete_vehiculo(id):
    vehiculo = db.session.execute(select(Vehiculos).filter_by(id=id)).scalar_one_or_none()

    if vehiculo is None:
        return jsonify({"msg": "Vehicle not found"}), 404

    db.session.delete(vehiculo)
    db.session.commit()

    response_body = {
        "msg": "Vehicle eliminado"
    }

    return jsonify(response_body), 200

#endpoint planetas
@app.route('/planets', methods=['GET'])
def get_planets():
    data = db.session.scalars(select(Planetas)).all()
    results = list(map(lambda item: item.serialize(), data))

    response_body = {
        "msg": "List of all planets",
        "results": results
    }

    return jsonify(response_body), 200

#endpoint uno solo
@app.route('/planets/<int:id>', methods=['GET'])
def get_planet(id):
    try:
        planet = db.session.execute(select(Planetas).filter_by(id=id)).scalar_one()

        response_body = {
            "msg": "Planet details",
            "result": planet.serialize()
        }

        return jsonify(response_body), 200
    except:
        return jsonify({"msg": "Planet not found"}), 404
    
#POST planetas
@app.route('/planets', methods=['POST'])
def create_planet():
    request_data = request.json
    print(request_data)

    planet = Planetas(
        nombre=request_data["nombre"],
        diametro=request_data["diametro"],
        tiempo_rotacion=request_data["tiempo_rotacion"],
        tiempo_orbitacion=request_data["tiempo_orbitacion"],
        gravedad=request_data["gravedad"],
        poblacion=request_data["poblacion"],
        clima=request_data["clima"],
        terreno=request_data["terreno"],
        superficie_acuosa=request_data["superficie_acuosa"]
    )

    db.session.add(planet)
    db.session.commit()

    response_body = {
        "msg": "Planet created"
    }

    return jsonify(response_body), 200

#DELETE planetas
@app.route('/planets/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = db.session.execute(select(Planetas).filter_by(id=id)).scalar_one_or_none()

    if planet is None:
        return jsonify({"msg": "Planet not found"}), 404

    db.session.delete(planet)
    db.session.commit()

    response_body = {
        "msg": "Planet deleted"
    }

    return jsonify(response_body), 200

#endpoint personajes
@app.route('/people', methods=['GET'])
def get_people():
    data = db.session.scalars(select(Personajes)).all()
    results = list(map(lambda item: item.serialize(), data))

    response_body = {
        "msg": "List of all characters",
        "results": results
    }

    return jsonify(response_body), 200

#uno solo
@app.route('/people/<int:id>', methods=['GET'])
def get_character(id):
    try:
        character = db.session.execute(select(Personajes).filter_by(id=id)).scalar_one()

        response_body = {
            "msg": "Character details",
            "result": character.serialize()
        }

        return jsonify(response_body), 200
    except:
        return jsonify({"msg": "Character not found"}), 404
    
#POST personajes
@app.route('/people', methods=['POST'])
def create_person():
    request_data = request.json
    print(request_data)

    person = Personajes(
        nombre=request_data["nombre"],
        fecha_nacimiento=request_data["fecha_nacimiento"],
        color_ojos=request_data["color_ojos"],
        genero=request_data["genero"],
        color_pelo=request_data["color_pelo"],
        estatura=request_data["estatura"],
        peso=request_data["peso"],
        color_piel=request_data["color_piel"],
        hogar=request_data["hogar"],
        url=request_data["url"]
    )

    db.session.add(person)
    db.session.commit()

    response_body = {
        "msg": "Character created"
    }

    return jsonify(response_body), 200

#DELETE personajes
@app.route('/people/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = db.session.execute(select(Personajes).filter_by(id=id)).scalar_one_or_none()

    if person is None:
        return jsonify({"msg": "Character not found"}), 404

    db.session.delete(person)
    db.session.commit()

    response_body = {
        "msg": "Character deleted"
    }

    return jsonify(response_body), 200

#Parte de los favoritos
# Endpoint obtener favoritos de un usuario
@app.route('/usuarios/favoritos', methods=['GET'])
def obtener_favoritos_usuario():
    try:
        user_id = 1  
        user = db.session.execute(select(User).filter_by(id=user_id)).scalar_one()
        favoritos = {
            "personajes": [favorite.serialize() for favorite in user.personajes_favoritos],
            "planetas": [favorite.serialize() for favorite in user.planetas_favoritos],
            "vehiculos": [favorite.serialize() for favorite in user.vehiculos_favoritos]
        }

        return jsonify({"msg": "Favoritos del usuario", "favoritos": favoritos}), 200
    except Exception as e:
        return jsonify({"msg": f"Error: {str(e)}"}), 400


# Añadir un personaje a favoritos
@app.route('/favorito/personaje/<int:personaje_id>', methods=['POST'])
def añadir_favorito_personaje(personaje_id):
    try:
        user_id = 1  
        user = db.session.execute(select(User).filter_by(id=user_id)).scalar_one()
        personaje = db.session.execute(select(Personajes).filter_by(id=personaje_id)).scalar_one()

        user.personajes_favoritos.append(personaje)
        db.session.commit()

        return jsonify({"msg": f"Personaje {personaje.nombre} añadido a favoritos"}), 200
    except Exception as e:
        return jsonify({"msg": f"Error: {str(e)}"}), 400


# Añadir un planeta a favoritos
@app.route('/favorito/planeta/<int:planeta_id>', methods=['POST'])
def añadir_favorito_planeta(planeta_id):
    try:
        user_id = 1  
        user = db.session.execute(select(User).filter_by(id=user_id)).scalar_one()
        planeta = db.session.execute(select(Planetas).filter_by(id=planeta_id)).scalar_one()

        user.planetas_favoritos.append(planeta)
        db.session.commit()

        return jsonify({"msg": f"Planeta {planeta.nombre} añadido a favoritos"}), 200
    except Exception as e:
        return jsonify({"msg": f"Error: {str(e)}"}), 400


# Eliminar un personaje de favoritos
@app.route('/favorito/personaje/<int:personaje_id>', methods=['DELETE'])
def eliminar_favorito_personaje(personaje_id):
    try:
        user_id = 1  
        user = db.session.execute(select(User).filter_by(id=user_id)).scalar_one()
        personaje = db.session.execute(select(Personajes).filter_by(id=personaje_id)).scalar_one()

        user.personajes_favoritos.remove(personaje)
        db.session.commit()

        return jsonify({"msg": f"Personaje {personaje.nombre} eliminado de favoritos"}), 200
    except Exception as e:
        return jsonify({"msg": f"Error: {str(e)}"}), 400


# Eliminar un planeta de favoritos
@app.route('/favorito/planeta/<int:planeta_id>', methods=['DELETE'])
def eliminar_favorito_planeta(planeta_id):
    try:
        user_id = 1  
        user = db.session.execute(select(User).filter_by(id=user_id)).scalar_one()
        planeta = db.session.execute(select(Planetas).filter_by(id=planeta_id)).scalar_one()

        user.planetas_favoritos.remove(planeta)
        db.session.commit()

        return jsonify({"msg": f"Planeta {planeta.nombre} eliminado de favoritos"}), 200
    except Exception as e:
        return jsonify({"msg": f"Error: {str(e)}"}), 400
    
# Añadir un vehículo a favoritos
@app.route('/favorito/vehiculo/<int:vehiculo_id>', methods=['POST'])
def añadir_favorito_vehiculo(vehiculo_id):
    try:
        user_id = 1  # Puedes obtenerlo de la sesión o pasarlo como parámetro
        user = db.session.execute(select(User).filter_by(id=user_id)).scalar_one()
        vehiculo = db.session.execute(select(Vehiculos).filter_by(id=vehiculo_id)).scalar_one()

        user.vehiculos_favoritos.append(vehiculo)
        db.session.commit()

        return jsonify({"msg": f"Vehículo {vehiculo.nombre} añadido a favoritos"}), 200
    except Exception as e:
        return jsonify({"msg": f"Error: {str(e)}"}), 400
    
# Eliminar un vehículo de favoritos
@app.route('/favorito/vehiculo/<int:vehiculo_id>', methods=['DELETE'])
def eliminar_favorito_vehiculo(vehiculo_id):
    try:
        user_id = 1  # Puedes obtenerlo de la sesión o pasarlo como parámetro
        user = db.session.execute(select(User).filter_by(id=user_id)).scalar_one()
        vehiculo = db.session.execute(select(Vehiculos).filter_by(id=vehiculo_id)).scalar_one()

        user.vehiculos_favoritos.remove(vehiculo)
        db.session.commit()

        return jsonify({"msg": f"Vehículo {vehiculo.nombre} eliminado de favoritos"}), 200
    except Exception as e:
        return jsonify({"msg": f"Error: {str(e)}"}), 400



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)