import os
from flask import Flask
from config import Config
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# TODO: register api routes

if __name__ == "__main__":
    app.config.from_object(Config)
    app.run(host="0.0.0.0")
