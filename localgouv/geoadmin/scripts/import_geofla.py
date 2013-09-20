import sys
from unipath import Path

sys.path.append(Path(__name__).ancestor(4))

from localgouv.geoadmin.models import AdminZone, SRID
from localgouv.app import create_app
app = create_app()
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# awesome lib to manipulate data very fast
import pandas as pd
from shapely.geometry import asShape
from shapely.geometry import MultiPolygon
from geoalchemy2.elements import WKTElement

# Fiona is a very good lib to process shapefile
from fiona import collection

# Import GEOFLA data
geofla_filepath = './data/COMMUNES/COMMUNE_4326.SHP'

# Set a simple function to extract only useful data
def extract_data(com):
    properties = com['properties']
    return {
        'id': com['id'],
        'insee_code': properties['INSEE_COM'],
        'name': properties['NOM_COMM'],
        'population': properties['POPULATION'] * 1000,
        'POPULATION': properties['POPULATION'],
        'department': properties['NOM_DEPT'],
        'code_dep': properties['CODE_DEPT'],
    }
with collection(geofla_filepath) as communes:
    for com in communes:
        data = extract_data(com)
        if com['geometry']['type'] == 'Polygon':
            multipoly = MultiPolygon([asShape(com['geometry'])])
        else:
            multipoly = asShape(com['geometry'])

        az = AdminZone(is_country=False,
                    is_region=False,
                    is_department=False,
                    is_city=True,
                    is_city_arr=False,
                    name=data['name'],
                    slug_name=data['name'].lower(),
                    code_department=data['code_dep'],
                    code_city=data['insee_code'][-3:],
                    geometry=WKTElement(multipoly.wkt, srid=SRID))
        db.session.add(az)
    db.session.commit()

