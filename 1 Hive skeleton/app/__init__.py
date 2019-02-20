import logging
from flask import Flask, redirect
from flask_appbuilder import AppBuilder, IndexView, SQLA
from flask_appbuilder.baseviews import expose

"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
#appbuilder = AppBuilder(app, db.session) #See MODIFICATIONS


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

#MODIFICAIONS

#Own index page
class MyIndexView(IndexView):
    index_template = 'welcome.html'

appbuilder = AppBuilder(
    app,
    db.session,
    indexview=MyIndexView,
)


#IMPORT ADDDITIONAL MODELS HERE!#
#from app.models import models


#IMPORT ADDDITIONAL VIEWS HERE!#
#from app.views import views


#IMPORT ADDITIONAL MODULES HERE!#
from app import upload
#from app import merge