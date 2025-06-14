from flask import Flask, render_template, request, jsonify #type:ignore
from chatbot import generate_response #type:ignore
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'response': "Please enter a valid message."})

    bot_response = generate_response(user_input)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
