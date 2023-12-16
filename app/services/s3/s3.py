import boto3
import os
from dotenv import load_dotenv, find_dotenv
import base64
from io import BytesIO
from datetime import datetime

load_dotenv(find_dotenv())

class S3:
    bucket_name = None
    base_path = None
    s3 = None

    def __init__(self) -> None:
        self.bucket_name = os.getenv("BUCKET_NAME")
        self.base_path = os.getenv("BASE_PATH")
        self.s3 = boto3.client('s3')

    def upload(self, file, file_name, file_type) -> None:

        if file_type == 'local':
            self.s3.upload_file(file, self.bucket_name, f"{self.base_path}/{file_name}")
        elif file_type == 'base64':
            file_data = base64.b64decode(file)
            file_stream = BytesIO(file_data)
            self.s3.upload_fileobj(file_stream, self.bucket_name, f"{self.base_path}/{file_name}")

    def download(self, file) -> None:
        current_data = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.s3.download_file(self.bucket_name, file, f'/img/file_{current_data}.{file.split(".")[-1]}')
