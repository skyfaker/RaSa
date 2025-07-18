from flask import Flask
import inspect
import sys

from configs import app_config


def initialize_extensions(app):
    from extensions import __all__
    for init_func in __all__:
        init_func(app)


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(app_config.model_dump())
    initialize_extensions(app)
    return app
