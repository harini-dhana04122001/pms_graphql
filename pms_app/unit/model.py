from pms_app.app import db


class Unit(db.Model):
    __tablename__ = 'unit'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, index=True, nullable=False)
    type_name = db.Column(db.String, index=True, nullable=False)
    floor_id = db.Column(db.Integer, db.ForeignKey('floor.id'), nullable=False)
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)

    def __init__(self, number, type_name, floor_id, model_id):
        self.number = number
        self.type_name = type_name
        self.floor_id = floor_id
        self.model_id = model_id


