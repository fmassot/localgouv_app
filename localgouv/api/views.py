# -*- coding: utf-8 -*-

from flask import Blueprint, current_app, request, jsonify

from ..database import db
from ..localfinance.models import LocalFinance


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/finance/<code>')
def adminzone_finance(code):
    finances = db.session.query(LocalFinance).filter(LocalFinance.data['insee_code']==code).all()
    if finances:
        return jsonify(dict([(finance.data['year'], finance.data) for finance in finances]))
    else:
        return jsonify(flag='fail', msg='Sorry, No admin zone has been found')

