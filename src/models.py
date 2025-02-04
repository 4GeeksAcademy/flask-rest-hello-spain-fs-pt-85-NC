from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(120), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(80), nullable=False)

    personajes_favoritos = relationship("Personajes", secondary="personajes_favoritos", back_populates="users_favorites")
    planetas_favoritos = relationship("Planetas", secondary="planetas_favoritos", back_populates="users_favorites")
    vehiculos_favoritos = relationship("Vehiculos", secondary="vehiculos_favoritos", back_populates="users_favorites")

    def __repr__(self):
        return f'<User {self.username}>'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
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

    users_favorites = relationship("User", secondary="planetas_favoritos", back_populates="planetas_favoritos")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "diametro": self.diametro,
            "tiempo_rotacion": self.tiempo_rotacion,
            "tiempo_orbitacion": self.tiempo_orbitacion,
            "gravedad": self.gravedad,
            "poblacion": self.poblacion,
            "clima": self.clima,
            "terreno": self.terreno,
            "superficie_acuosa": self.superficie_acuosa
        }

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

    users_favorites = relationship("User", secondary="vehiculos_favoritos", back_populates="vehiculos_favoritos")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "modelo": self.modelo,
            "clase_vehiculo": self.clase_vehiculo,
            "fabricante": self.fabricante,
            "longitud": self.longitud,
            "precio": self.precio,
            "tripulacion": self.tripulacion,
            "velocidad_max": self.velocidad_max,
            "capacidad_carga": self.capacidad_carga,
            "consumibles": self.consumibles,
            "url": self.url
        }

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

    users_favorites = relationship("User", secondary="personajes_favoritos", back_populates="personajes_favoritos")

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha_nacimiento": self.fecha_nacimiento,
            "color_ojos": self.color_ojos,
            "genero": self.genero,
            "color_pelo": self.color_pelo,
            "estatura": self.estatura,
            "peso": self.peso,
            "color_piel": self.color_piel,
            "hogar": self.hogar,
            "url": self.url
        }

# FAVS
class PersonajesFavoritos(db.Model):
    __tablename__ = 'personajes_favoritos'
    user_id = mapped_column(Integer, db.ForeignKey('user.id'), primary_key=True)
    personaje_id = mapped_column(Integer, db.ForeignKey('personajes.id'), primary_key=True)

class PanetasFavoritos(db.Model):
    __tablename__ = 'planetas_favoritos'
    user_id = mapped_column(Integer, db.ForeignKey('user.id'), primary_key=True)
    planeta_id = mapped_column(Integer, db.ForeignKey('planetas.id'), primary_key=True)

class VehiculosFavoritos(db.Model):
    __tablename__ = 'vehiculos_favoritos'
    user_id = mapped_column(Integer, db.ForeignKey('user.id'), primary_key=True)
    vehiculo_id = mapped_column(Integer, db.ForeignKey('vehiculos.id'), primary_key=True)