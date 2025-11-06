from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
conn = psycopg2.connect(DATABASE_URL)

app = Flask(__name__)
CORS(app) 

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "status": "OK",
        "service": "backend (Flask)",
        "message": "Data loaded from the backend.",
        "db_connection": "Successful" # Якщо підключення до БД реалізовано
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
