from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ["MONGO_URI"]

mongo = PyMongo(app)

@app.route('/pokedex', methods=['POST'])
def pokedex():
    submitted_name = request.values.get('Body', '').lower()
    pokemon_result = mongo.db.pokemon.find_one_or_404({"name": name})
    #body = f"{pokemon_result['name']}\n{pokemon_result['description']}"
    resp = MessagingResponse()
    msg = resp.message()
    #msg.body(body)
    msg.body(f"body is {submitted_name}")
    #msg.media(pokemon_result['image_url'])

    return str(resp)

if __name__ == "__main__":
    app.run()