from app import app
from flask import jsonify

@app.route('/user/hello', methods=['GET'])
def user_hello():
    return "Hello"