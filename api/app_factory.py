from flask import Flask
import inspect
import logging
import sys

from configs import app_config


def initialize_extensions(app):
    from extensions import ext_db
    ext_db.init_db(app)


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(app_config.model_dump())
    initialize_extensions(app)
    return app
