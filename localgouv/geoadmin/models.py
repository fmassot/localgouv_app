# -*- coding: utf-8 -*-

from flask import Blueprint

from sqlalchemy import (
        Table, Column, ForeignKey,
        Boolean, Float, Integer, Unicode,
        )
from sqlalchemy.orm import aliased, relationship, backref
from geoalchemy2 import Geometry

from ..database import db

SRID = 4326

geoadmin = Blueprint('geoadmin', __name__,
                     template_folder='templates')


class AdminZone(db.Model):
    __tablename__ = 'geoadmin_adminzone'

    id = Column(Integer, primary_key=True)

    is_country      = Column(Boolean)
    is_region       = Column(Boolean)
    is_department   = Column(Boolean)
    is_city         = Column(Boolean)
    is_city_arr     = Column(Boolean)

    name        = Column(Unicode(100))
    slug_name   = Column(Unicode(100))
    code_department  = Column(Unicode(3))
    code_city  = Column(Unicode(3)) 

    geometry    = Column(Geometry('MULTIPOLYGON', srid=SRID))
