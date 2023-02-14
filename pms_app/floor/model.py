from pms_app.app import db


class Floor(db.Model):
    __tablename__ = 'floor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, nullable=False)
    building_id = db.Column(db.Integer(), db.ForeignKey('building.id'), nullable=False)
    units = db.relationship('Unit', foreign_keys='Unit.floor_id', backref='units', lazy=True)

    def __init__(self, name, building_id):
        self.name = name
        self.building_id = building_id
