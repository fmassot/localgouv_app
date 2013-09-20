# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, current_app, request

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return render_template('index.html')
