# -*- coding: utf-8 -*-

from sqlalchemy import Column, types, Integer
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.dialects.postgresql import HSTORE

from ..database import db

class LocalFinance(db.Model):
    """Financial data by zone (city, dep, region) and by year"""
    __tablename__ = 'localfinance'

    #def __repr__(self):
    #    return '<Zone %r>' % (self.name)
    #
    id = Column(Integer, primary_key=True)
    data = Column(MutableDict.as_mutable(HSTORE))

