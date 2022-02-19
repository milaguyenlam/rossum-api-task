from flask import Flask
from config import Config
from api.annotation import annotation_route

# TODO: implement https communication


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(annotation_route)
    return app


app = create_app()

if __name__ == "__main__":
    app.run()
