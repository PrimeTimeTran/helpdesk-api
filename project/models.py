from project.db import db
from dataclasses import dataclass
from sqlalchemy import inspect

@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    username = db.Column(db.Text)

    def toDict(self):
      return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

@dataclass
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    email = db.Column(db.Text)

    def toDict(self):
      return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}