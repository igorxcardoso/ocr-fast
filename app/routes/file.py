from app import api
from flask import jsonify, request
from app.services.s3.s3 import S3
import boto3

@api.route('/upload', methods=['POST'])
def upload():
    body = request.get_json(force=True)
    s3 = S3()
    file = body.get('file')
    file_type = body.get('type')
    file_name = body.get('name')
    s3.upload(file, file_name)

    return jsonify({'upload': 'upload'})