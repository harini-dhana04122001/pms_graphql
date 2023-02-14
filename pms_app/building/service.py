from pms_app.app import db


def create_building_details(building):
    db.session.add(building)
    db.session.commit()
