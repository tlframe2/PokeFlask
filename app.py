from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/pokedex', methods=['POST'])
def pokedex():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(incoming_msg)
    msg.media('https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png')

    return str(resp)

if __name__ == "__main__":
    app.run()