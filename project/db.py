from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from project import app

db = SQLAlchemy(app)

migrate = Migrate(app, db)