## 모듈로딩
from myweb import db

class FoodWaste(db.Model) :
    d = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Trashlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20),nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)

class recycleTrash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)