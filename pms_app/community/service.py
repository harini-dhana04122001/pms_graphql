from pms_app.app import db


def create_community_details(community):
    db.session.add(community)
    db.session.commit()
