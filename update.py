from flask import Flask, request, jsonify
import json

app = Flask(__name__)

heart_data = [
    {"heart_id": 1, "date": "2023-01-20", "heart_rate": 50},
    {"heart_id": 2, "date": "2023-01-22", "heart_rate": 75},
]

@app.route('/heart_rate/<int:heart_id>', methods=['PUT'])
def update_heart_rate(heart_id):
    data = request.get_json()

    if not data or not all(k in data for k in ('date', 'heart_rate')):
        return jsonify({"error": "bad request, 'date' and 'heart_rate' are required"}), 400

    for heart in heart_data:
        if heart['heart_id'] == heart_id:
            heart['date'] = data['date']
            heart['heart_rate'] = data['heart_rate']
            return jsonify({"message": f"Heart rate record for heart_id {heart_id} updated successfully"})

    return jsonify({"error": f"Heart rate record for heart_id {heart_id} not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
