import sys
from flask import Flask
import boto3
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

boto3.setup_default_session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

sys.path.append('../config')

api = Flask(__name__)
api.config.from_object('config.app.ConfigApp')
