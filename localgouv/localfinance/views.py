# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

localfinance = Blueprint('localfinance', __name__,
                         template_folder='templates')

@localfinance.route('/', defaults={'page': 'index'})
@localfinance.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
