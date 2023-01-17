from project import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    username = db.Column(db.Text)


# db.create_all()
