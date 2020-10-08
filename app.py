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

collection = db.pokemon

# @app.route('/pokedex', methods=['POST'])
# def pokedex():
#     # submitted_name = request.values.get('Body', '').lower()
#     # pokemon_result = mongo.db.pokemon.find_one_or_404({"name": submitted_name})
#     # body = f"{pokemon_result['name']}\n{pokemon_result['description']}"
#     # resp = MessagingResponse()
#     # msg = resp.message()
#     # msg.body(body)
#     # msg.media(pokemon_result['image_url'])

#     body = request.values.get('Body', '').lower()
#     print(body)
#     pokemon_result = mongo.db.pokemon.find_one_or_404({"name": "bulbasaur"})
#     print(pokemon_result)
#     resp = MessagingResponse()
#     msg = resp.message()
#     msg.body(f"body is {body}")

#     return str(resp)

# @app.route('/test/<name>', methods=['GET'])
# def test(name):
#     pokemon_result = mongo.db.pokemon.find_one_or_404({"name": name})
#     print(pokemon_result['name'])
#     return { "name": pokemon_result['name'], "types": pokemon_result['types'] }

@app.route('/test2', methods=['GET'])
def test2():
    print(collection.find_one())
    return { "msg": "success" }

if __name__ == "__main__":
    app.run()