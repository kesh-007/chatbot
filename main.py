from flask import Flask, request, jsonify
from chat import ChatPDFClient
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

chatbot_client = ChatPDFClient()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = chatbot_client.get_response(message)
        
    if response[0] == 'Result:':
        return jsonify({'response': response[1]})
    else:
        return jsonify({'error': response[2]}), response[1]

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
