from flask import Flask, request, jsonify
import json

app = Flask(__name__)

heart_data = [
    {"heart_id": 1, "date": "2023-01-20", "heart_rate": 50},
    {"heart_id": 2, "date": "2023-01-22", "heart_rate": 75},
]

@app.route('/heart_rate/<int:heart_id>', methods=['DELETE'])
def delete_heart_rate(heart_id):
    global heart_data

    for index, heart in enumerate(heart_data):
        if heart['heart_id'] == heart_id:
            del heart_data[index]
            return jsonify({"message": f"Heart rate record for heart_id {heart_id} deleted successfully"})

    return jsonify({"error": f"Heart rate record for heart_id {heart_id} not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
