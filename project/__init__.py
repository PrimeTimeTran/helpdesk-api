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

@app.route("/tickets/<id>", methods=['PATCH'])
def update_ticket(id):
  t = Ticket.query.get(id)
  data = request.get_json()
  t.name = data['name']
  t.email = data['email']
  t.status = data['status']
  t.description = data['description']
  db.session.commit()
  return jsonify(t.toDict())

@app.route("/ticket", methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        data = request.get_json()
        ticket = Ticket(name=data['name'], email=data['email'], description=data['description'])
        db.session.add(ticket)
        db.session.commit()
        return jsonify(ticket.toDict())