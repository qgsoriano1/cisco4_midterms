from flask import Flask, request, jsonify
import json

app = Flask(__name__)

heart_data = [
    {"heart_id": 1, "date": "2023-01-20", "heart_rate": 50},
    {"heart_id": 2, "date": "2023-01-22", "heart_rate": 75},
]

@app.route('/heart_rate', methods=['GET'])
def get_heart_rate():
    return jsonify(heart_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
