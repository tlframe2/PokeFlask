from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
import os

app = Flask(__name__)

pokemon = MongoClient(os.environ["MONGO_URI"]).pokeflask.pokemon

@app.route('/pokedex', methods=['POST'])
def pokedex():
    name = request.values.get('Body', '').lower().strip()
    pokemon_result = pokemon.find_one({ "name":  name })
    body = f"Name: {pokemon_result['name'].capitalize()}\nTypes: {pokemon_result['types']}\nBio: {pokemon_result['description']}"

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(body)
    msg.media(pokemon_result['image_url'])

    return str(resp)

@app.route('/test/<name>', methods=['GET'])
def test(name):
    pokemon_result = pokemon.find_one({"name": name})
    return { "name": pokemon_result['name'], "description": pokemon_result['description'] }

if __name__ == "__main__":
    app.run()