from wedding import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"


class Invitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    party_size = db.Column(db.Integer, nullable=False, default=0)
    attending_to_ceremony = db.Column(db.Boolean, nullable=False, default=False)
    attending_to_reception = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"Invitation('{self.name}', '{self.party_size}')"