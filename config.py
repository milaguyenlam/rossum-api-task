import os
from dotenv import load_dotenv

load_dotenv()

rossum_username = os.environ["ROSSUM_API_USERNAME"]
rossum_password = os.environ["ROSSUM_API_PASSWORD"]

default_username = os.environ["DEFAULT_USERNAME"]
default_password = os.environ["DEFAULT_PASSWORD"]


class Config:
    DEBUG = True
