from flask import Flask
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_object('config')

from project.models import User
from project.db import db

@app.route("/ticket", methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        data = request.get_json()

        u = User(body=data['text'], username=data['bar'])
        db.session.add(u)
        db.session.commit()
        return jsonify(
            u.toDict()
        )