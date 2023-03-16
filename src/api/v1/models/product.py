from src.db import db
from datetime import datetime
from typing import Dict, List


ProductJSON = Dict[int,str]


class ProductModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Coulmn(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.Integer(500), nullable=False)
    number_of = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.String(50), nullable=False, default="default.jpeg")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, price, description, number_of, picture) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.number_of = number_of
        self.picture = picture

    def json(self) -> ProductJSON:
        return {'id': self.id,
                'name': self.name,
                'number': self.number_of,
                'created_datetime': f'{self.created_at}'}

    @classmethod
    def find_by_name(cls, name) -> "ProductModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id) -> "ProductModel":
        return cls.query.filter_by(id=_id).first()

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.deleet(self)
        db.session.commit()
