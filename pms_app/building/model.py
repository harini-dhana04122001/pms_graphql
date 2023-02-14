from pms_app.app import db


class Building(db.Model):
    __tablename__ = 'building'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, nullable=False)
    community_id = db.Column(db.Integer(), db.ForeignKey('community.id'), nullable=False)
    # community = db.relationship('Community', backref='community')
    # floor = db.relationship('Floor', foreign_keys='Floor.building_id', backref='floor', lazy=True)

    def __init__(self, name, community_id):
        self.name = name
        self.community_id = community_id
