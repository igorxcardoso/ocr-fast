import boto3
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class S3:
    bucket_name = None
    base_path = None
    s3 = None

    def __init__(self) -> None:
        self.bucket_name = os.getenv("BUCKET_NAME")
        self.base_path = os.getenv("BASE_PATH")
        self.s3 = boto3.client('s3')

    def upload(self, file, file_name) -> None:
        self.s3.upload_file(file, self.bucket_name, f"{self.base_path}/{file_name}")

    def download(self, file) -> None:
        pass
