from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.debug = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/helpdesk'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from project.models import User


@app.route("/")
def hello_world():
    return "<p>Hello, Flask World!</p>"


@app.route("/ticket", methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        u = User(body="shshsh", username="ssss")
        db.session.add(u)
        db.session.commit()
        return jsonify(
            username="hello",
            email="loi@gmail.ccom",
            id=1
        )
