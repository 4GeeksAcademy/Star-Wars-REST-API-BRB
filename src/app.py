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
from models import db, User, Character, Planet, Fav_char
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

@app.route('/user', methods=['GET'])
def get_users():
    allUsers = User.query.all()
    user_list = [user.serialize() for user in allUsers]
    
    return jsonify(user_list), 200


@app.route('/character', methods=['GET'])
def get_characters():
    allCharacters = Character.query.all()
    character_list = [character.serialize() for character in allCharacters]
    
    return jsonify(character_list), 200


@app.route('/planet', methods=['GET'])
def get_plnets():
    allPlanets = Planet.query.all()
    planet_list = [planet.serialize() for planet in allPlanets]
    
    return jsonify(planet_list), 200



@app.route('/user', methods=['POST'])
def post_user():
    data = request.json
    newUser = User(
        # id = data["id"],
        email = data["email"],
        password = data["password"],
        is_active = data.get("is_active")
    )

    db.session.add(newUser)
    db.session.commit()

    return jsonify(newUser.serialize()), 200




@app.route('/character', methods=['POST'])
def post_character():
    data = request.json
    new_character = Character(
        # id= data["id"],
        name= data['name'],
        age = data['age'],
        hair_color = data['hair_color'],
        eye_color = data['eye_color'],
        height =  data['height']
    
    )

    db.session.add(new_character)
    db.session.commit()

    return jsonify(new_character.serialize()), 200




@app.route('/fav_char', methods=['POST'])
def post_favchar():
    data = request.json
    new_favchar = Fav_char(
        # id = data["id"],
        user_id = data["user_id"],
        character_id = data["character_id"]
        
    )

    db.session.add(new_favchar)
    db.session.commit()

    return jsonify(new_favchar.serialize()), 200




@app.route('/fav_char', methods=['GET'])
def get_favchar():
   
    allFavs = Fav_char.query.all()
    fav_list = [Fav_char.serialize() for Fav_char in allFavs]


    return jsonify(fav_list), 200





# @app.route('/character', methods=['POST'])
# def post_character():


# return jsonify(response_body), 200
    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
