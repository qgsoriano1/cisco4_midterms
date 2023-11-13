from flask import Flask, request, jsonify
import json

app = Flask(__name__)

heart_data = [
    {"heart_id": 1, "date": "2023-01-20", "heart_rate": 50},
    {"heart_id": 2, "date": "2023-01-22", "heart_rate": 75},
]

@app.route('/heart_rate/<int:heart_id>', methods=['GET'])
def get_heart_rate_by_id(heart_id):
    result = next((heart for heart in heart_data if heart['heart_id'] == heart_id), None)

    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "heart_id not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
