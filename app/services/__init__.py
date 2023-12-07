import boto3
import os
from dotenv import load_dotenv, find_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(find_dotenv())

# Obtém as credenciais da AWS do ambiente
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

# Configuração das credenciais
boto3.setup_default_session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)
