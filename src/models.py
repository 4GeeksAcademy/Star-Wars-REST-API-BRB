from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

[
  {
    "email": "email",
    "id": 1
  },
  {
    "email": "gmail",
    "id": 6
  },
  {
    "email": "gcmail",
    "id": 9
  },
  {
    "email": "gcmddail",
    "id": 10
  },
  {
    "email": "dfsfsf@example.com",
    "id": 11
  }
]


class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Character (db.Model):

    __tablename__ = "character"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    age: Mapped[str] = mapped_column(String(5), nullable=True)
    hair_color: Mapped[str] = mapped_column(String(20), nullable=False)
    eye_color: Mapped[int] = mapped_column(String(20), nullable=False)
    height: Mapped[int] = mapped_column(String(20), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "height": self.height

            # do not serialize the password, its a security breach
        }
    

class Planet (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    population: Mapped[int] = mapped_column(nullable=True)
    is_habitable: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    weather: Mapped[str] = mapped_column(String(100), nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)
    size: Mapped[int] = mapped_column(nullable=False)


def serialize(self):
    return {
        "id": self.id,
        "name": self.name,
        "population": self.population,
        "is_habitable": self.is_habitable,
        "weather": self.weather,
        "age": self.age,
        "size": self.size
    
        # do not serialize the password, its a security breach
    }


class Fav_char(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    character_id: Mapped[str] = mapped_column(ForeignKey("character.id"))
    user: Mapped["User"] = relationship("User")
    character: Mapped["Character"] = relationship("Character")
  

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.email,
            "character": self.character.eye_color

            # do not serialize the password, its a security breach
        }
