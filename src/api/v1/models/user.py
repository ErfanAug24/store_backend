from src.db import db
from datetime import datetime
from typing import Dict, List

UserJSON = Dict[int, str]


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.String(100), default="USER")
    is_activated = db.Column(db.Boolean, default=False)
    is_banned = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = password

    def json(self) -> UserJSON:
        return {'id': self.id,
                'username': self.username,
                'email': self.email,
                'role': self.role,
                'is_activated': self.is_activated,
                'is_banned': self.is_banned,
                'created_at': self.created_at}

    @classmethod
    def find_by_username(cls, username) -> "UserModel":
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id) -> "UserModel":
        return cls.query.filter_by(id=_id).first()

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
