from flask import Flask, request, jsonify
import requests
from datetime import datetime, timezone


app = Flask(__name__)

# CORS (IMPORTANT)
@app.after_request
def apply_cors(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/classify', methods=['GET'])
def classify_name():
    name = request.args.get('name')

    # 400: Mising or empty name
    if name is None or name.strip() == '':
        return jsonify({
            'status': 'error',
            'message': 'Missing or empty name parameter'
        }), 400
        
    if not name.isalpha():
        return jsonify({
            'status': 'error',
            'message': 'Name is not a string'
        }), 422
        
    try:
        # Call the Genderize API to classify the name
        url = 'https://api.genderize.io'
        response = requests.get(url, params={'name': name}, timeout=5)
        
        if response.status_code != 200:
            return jsonify({
                'status': 'error',
                'message': 'Upstream or server failure'
            }), 502

        data = response.json()
        probability = data.get('probability')
        count = data.get('count')
        gender = data.get('gender')
        
            
        if gender is None or count == 0:
            return jsonify({
                'status': 'error',
                'message': 'No Prediction available for the provided name'
            }), 422
        
        # Confidence logic
        is_confident = probability >= 0.7 and count >= 100
        
        # Processes time (UTC ISO 8601 format)
        processed_time = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        
        return jsonify({
            "status": "success",
            "data": {
                'name': data.get('name'),
                'gender': data.get('gender'),
                'probability': data.get('probability'),
                'sample_size': data.get('count'),
                'is_confident': is_confident,
                'processed_time': processed_time
            }
        }), 200
    except Exception:
        return jsonify({
            'status': 'error',
            'message': 'Upstream or server failure'
        }), 502
    
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
        
    
    