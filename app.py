from flask import Flask, render_template, request, jsonify
import requests

RASA_API_URL = 'http://localhost:5005/webhooks/rest/webhook'
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message =  request.json.get('message')
    print("\nUser:", user_message)

    # Send user message to Rasa and get bot's response
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    bot_response = rasa_response.json()
    print("\nChatbot:", bot_response)

    return jsonify(bot_response)


if __name__ == "__main__":
    app.run(debug=True, port=3000)