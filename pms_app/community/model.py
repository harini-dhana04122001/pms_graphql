from pms_app.app import db


class Community(db.Model):
    __tablename__ = 'community'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, nullable=False)
    agent_name = db.Column(db.String(), nullable=False)
    agent_contact = db.Column(db.BigInteger, nullable=False)
    # buildings = db.relationship('Building', backref='community', lazy=True)

    def __init__(self, name, agent_name, agent_contact):
        self.name = name
        self.agent_name = agent_name
        self.agent_contact = agent_contact
