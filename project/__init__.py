from flask import Flask
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_object('config')

from project.models import User
from project.db import db

@app.route("/")
def hello_world():
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
