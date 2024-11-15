from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from g4f.client import Client

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json  # Get JSON data from the request
    user_input = data.get('input')  # Extract the input field
    client = Client()
    # print(str(user_input))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"{str(user_input)}"}],
    )
    response_data = {
        "answer": f'{response.choices[0].message.content}'  # Create a response based on user input
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run()  # Use port 5000 for PythonAnywhere
