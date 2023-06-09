from src.db import db
from typing import Dict, List, Union
from datetime import datetime

BlocklistJSON = Dict[str, str]


class BlocklistModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jwt_id = db.Column(db.String, nullable=False, unique=True)
    ttype = db.Column(db.String(16), nullable=False)
    revoked_at = db.Column(db.DateTime, default=datetime.utcnow)
    reason = db.Column(db.String, nullable=False)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)

    def __init__(self, jwt_id, reason, user_id, ttype) -> None:
        self.jwt_id = jwt_id
        self.user_id = user_id
        self.reason = reason
        self.ttype = ttype

    def json(self) -> BlocklistJSON:
        return {'id': self.id,
                'jwt_id': self.jwt_id,
                'user_id': self.user_id,
                'ttype': self.ttype,
                'revoked time': f'{self.revoked_at}',
                'reason': self.reason}

    @classmethod
    def find_by_jwtID(cls, _jwt_id) -> "BlocklistModel":
        return cls.query.filter_by(jwt_id=_jwt_id).first()

    @classmethod
    def find_by_id(cls, _id) -> "BlocklistModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_user_id(cls, user_id) -> "BlocklistModel":
        return cls.query.filter_by(user_id=user_id).first()

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
