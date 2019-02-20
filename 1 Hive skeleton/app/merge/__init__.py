# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 09:38:43 2019

@author: Tanzelle.Oberholster
"""

import logging
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)


appbuilder = AppBuilder(app, db.session)

"""
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from app.merge.views import merge
from app.merge.forms import merge