from flask import Flask, request, jsonify
import json

app = Flask(__name__)

heart_data = [
    {"heart_id": 1, "date": "2023-01-20", "heart_rate": 50},
    {"heart_id": 2, "date": "2023-01-22", "heart_rate": 75},
]

@app.route('/heart_rate', methods=['POST'])
def add_heart_rate():
    global heart_data
    data = request.get_json()

    #if not data or not all(k in data for k in ('heart_id', 'date', 'heart_rate')):
     #   return jsonify({"error": "bad request, all keys are required"}), 400

    heart_data.append(data)

    with open('heart_data.json', 'w') as f:
        json.dump(heart_data, f)

    return jsonify({"message": "HearRate recorded successfully"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
