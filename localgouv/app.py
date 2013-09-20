# -*- coding: utf-8 -*-

import os

from flask import Flask
from .config import DefaultConfig
from .database import db

from .localfinance import localfinance
from .geoadmin import geoadmin
from .api import api
from front import front

__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (
    localfinance,
    geoadmin,
    api,
    front,
)

def create_app():
    app_name = DefaultConfig.PROJECT
    app = Flask(app_name, instance_path='/tmp/instance', instance_relative_config=True)
    app.config.from_object(DefaultConfig)
    for blueprint in DEFAULT_BLUEPRINTS:
        app.register_blueprint(blueprint)
    db.init_app(app)
    return app
