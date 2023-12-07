from app import api
from flask import jsonify

@api.route('/extract', methods=['GET'])
def extract():
    return jsonify({'extract': 'extract'})
