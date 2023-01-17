from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)

app.debug = True
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/helpdesk'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from project.models import User
logging.getLogger('flask_cors').level = logging.DEBUG


@app.route("/")
def hello_world():
    print('h')
    return "<p>Hello, Flask World!</p>"

@app.route("/ticket", methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        print('Create Ticket')
        data = request.get_json()
        print(data)

        u = User(body=data['text'], username=data['bar'])
        db.session.add(u)
        db.session.commit()
        return jsonify(
            u.toDict()
        )
