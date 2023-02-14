from pms_app.app import db


class Models(db.Model):
    __tablename__ = 'model'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, nullable=False)
    buildings = db.relationship('Unit', foreign_keys='Unit.model_id', backref='unit', lazy=True)

    def __init__(self, name):
        self.name = name
