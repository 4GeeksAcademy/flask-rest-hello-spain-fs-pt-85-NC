from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Boolean


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    nombre_usuario = mapped_column(String(50), nullable=False, unique=True)
    nombre_completo = mapped_column(String(80), nullable=False)
    email = mapped_column(String(120), nullable=False, unique=True)
    contraseña = mapped_column(String(80))
    is_active = mapped_column(Boolean)

    def __repr__(self):
        return '<user %r>' % self.nombre_usuario

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planetas(db.Model):
    __tablename__ = 'planetas'
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(100), nullable=False)
    diametro = mapped_column(String(100), nullable=False)
    tiempo_rotacion = mapped_column(String(100), nullable=False)
    tiempo_orbitacion = mapped_column(String(100), nullable=False)
    gravedad = mapped_column(String(100), nullable=False)
    poblacion = mapped_column(String(100), nullable=False)
    clima = mapped_column(String(100), nullable=False)
    terreno = mapped_column(String(100), nullable=False)
    superficie_acuosa = mapped_column(String(100), nullable=False)

class Vehiculos(db.Model):
    __tablename__ = 'vehiculos'
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(100), nullable=False)
    modelo = mapped_column(String(100), nullable=False)
    clase_vehiculo = mapped_column(String(100), nullable=False)
    fabricante = mapped_column(String(100), nullable=False)
    longitud = mapped_column(String(100), nullable=False)
    precio = mapped_column(String(100), nullable=False)
    tripulacion = mapped_column(String(100), nullable=False)
    velocidad_max = mapped_column(String(100), nullable=False)
    capacidad_carga = mapped_column(String(100), nullable=False)
    consumibles = mapped_column(String(100), nullable=False)
    url = mapped_column(String(200), nullable=False)

class Personajes(db.Model):
    __tablename__ = 'personajes'
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(100), nullable=False)
    fecha_nacimiento = mapped_column(String(100), nullable=False)
    color_ojos = mapped_column(String(100), nullable=False)
    genero = mapped_column(String(100), nullable=False)
    color_pelo = mapped_column(String(100), nullable=False)
    estatura = mapped_column(String(20), nullable=False)
    peso = mapped_column(String(40), nullable=False)
    color_piel = mapped_column(String(20), nullable=False)
    hogar = mapped_column(String(40), nullable=False)
    url = mapped_column(String(100), nullable=False)