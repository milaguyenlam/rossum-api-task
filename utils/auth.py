from functools import wraps
import os
from flask import request
import config


def dummy_authenticate():
    auth = request.authorization
    return auth.username == config.default_username and auth.password == config.default_password


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if dummy_authenticate():
            return f(*args, **kwargs)
        else:
            return "Access not granted, please submit correct credentials!", 401

    return wrapper
