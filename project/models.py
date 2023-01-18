import enum
from project.db import db
from dataclasses import dataclass
from sqlalchemy import inspect
class Status(str, enum.Enum):
    new = 'new'
    progress = 'progress'
    resolved = 'resolved'
    def _get_value(self, **kwargs) -> str:
        return self.value

@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    username = db.Column(db.Text)

    def toDict(self):
      return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

@dataclass
class Ticket(db.Model):
    status_enum: Status
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    description = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum(Status), nullable=False, server_default="new")

    def toDict(self):
      return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
