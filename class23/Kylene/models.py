from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import (check_password_hash, generate_password_hash)

db = SQLAlchemy()

class Member(UserMixin, db.Model):
    __tablename__ = "member"

    id = db.Column(db.Integer,
        primary_key=True)
    username = db.Column(db.String(50),
        nullable=False,
        unique=True)
    email = db.Column(db.String(255),
        nullable=False)
    password_hash = db.Column(db.String(255),
        nullable=False)

    # methods
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return (f"<Member {self.id}: {self.username}")