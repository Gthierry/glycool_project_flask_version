from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask("app")
CORS(app)
db = SQLAlchemy()
migrate = Migrate()
