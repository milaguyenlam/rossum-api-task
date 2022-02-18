from functools import wraps
import os
from flask import request

default_username = os.environ("DEFAULT_USERNAME")
default_password = os.environ("DEFAULT_PASSWORD")


def dummy_authenticate():
    auth = request.authorization
    return auth.username == default_username and auth.password == default_password


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if dummy_authenticate():
            return f(*args, **kwargs)
        else:
            return "Access not granted, please submit correct credentials!", 403

    return wrapper
