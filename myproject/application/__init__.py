from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:root@104.197.74.221/sqldb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# (change to remote db)
db = SQLAlchemy(app)

from application import routes