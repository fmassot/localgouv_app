import sys
from unipath import Path
from json import load

sys.path.append(Path(__name__).ancestor(4))

from localgouv.localfinance.models import LocalFinance
from localgouv.app import create_app
app = create_app()
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

filepath = sys.argv[1]
data = load(open(filepath))

for item in data:
    # convert all data into string
    item = dict([(k, unicode(v)) for k, v in item.items()])
    lf = LocalFinance(data=item)
    db.session.add(lf)
db.session.commit()


