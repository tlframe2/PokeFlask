from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["MONGO_URI"]

mongo = PyMongo(app)

@app.route('/pokedex', methods=['POST'])
def pokedex():
    # submitted_name = request.values.get('Body', '').lower()
    # pokemon_result = mongo.db.pokemon.find_one_or_404({"name": submitted_name})
    # body = f"{pokemon_result['name']}\n{pokemon_result['description']}"
    # resp = MessagingResponse()
    # msg = resp.message()
    # msg.body(body)
    # msg.media(pokemon_result['image_url'])

    body = request.values.get('Body', '').lower()
    pokemon_result = mongo.db.pokemon.find_one({"name": body})
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(f"body is {body}")

    return str(resp)

if __name__ == "__main__":
    app.run()