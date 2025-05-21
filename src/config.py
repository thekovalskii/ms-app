import os

from dotenv import load_dotenv


load_dotenv(override=True)

REDIS_HOST = os.getenv('redis_host')
REDIS_PORT = int(os.getenv('redis_port'))
REDIS_PASSWORD = os.getenv('redis_password')
