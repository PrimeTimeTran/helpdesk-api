from flask import Flask
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_object('config')

from project.models import Ticket
from project.db import db

@app.route("/tickets", methods=['GET'])
def tickets():
  tickets = Ticket.query.all()
  result_dict = [u.toDict() for u in tickets]
  return jsonify(result_dict)

@app.route("/ticket", methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        data = request.get_json()
        ticket = Ticket(name=data['name'], email=data['email'], description=data['description'])
        db.session.add(ticket)
        db.session.commit()
        return jsonify(ticket.toDict())