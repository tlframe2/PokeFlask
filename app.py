from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
# from flask_pymongo import PyMongo
from pymongo import MongoClient
import os

app = Flask(__name__)
# app.config["MONGO_URI"] = os.environ["MONGO_URI"]

# mongo = PyMongo(app)

client = MongoClient(os.environ["MONGO_URI"])

db = client.pokeflask

pokemon = db.pokemon

@app.route('/pokedex', methods=['POST'])
def pokedex():
    name = request.values.get('Body', '').lower().strip()
    print(name)
    pokemon_result = pokemon.find_one({ "name":  name })
    print(pokemon_result)
    body = f"{pokemon_result['name']}\nTypes: {pokemon_result['types']}\n{pokemon_result['description']}"
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(body)
    msg.media(pokemon_result['image_url'])

    # msg.body(pokemon_result['description'])
    # msg.media(pokemon_result['image_url'])

    return str(resp)

@app.route('/test/<name>', methods=['GET'])
def test(name):
    # pokemon_result = mongo.db.pokemon.find_one_or_404({"name": name})
    # print(pokemon_result['name'])
    # return { "name": pokemon_result['name'], "types": pokemon_result['types'] }

    pokemon_result = pokemon.find_one({"name": name})
    return { "name": pokemon_result['name'], "description": pokemon_result['description'] }

@app.route('/test2', methods=['GET'])
def test2():
    print(collection.find_one())
    return { "msg": "success" }

if __name__ == "__main__":
    app.run()