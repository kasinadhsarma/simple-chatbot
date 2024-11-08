from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()

    # Simple response logic
    if 'hi' in user_message or 'hello' in user_message:
        response = "Hello! How can I help you today?"
    elif 'how are you' in user_message:
        response = "I'm doing great, thank you for asking! How about you?"
    elif 'bye' in user_message:
        response = "Goodbye! Have a great day!"
    else:
        response = "I'm here to chat and help! Feel free to ask me anything."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
