from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'BVXRGsFzKwtGF9fPAO61B8WZKfsc3B_CSV0Fo-PM0_o'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:harini04121@localhost/pms_db'
# db.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate()


def create_app():

    # migrate.init_app(app, db)

    from pms_app.community.view import display as community_display
    from pms_app.building.view import display as building_display
    from pms_app.floor.view import display as floor_display
    from pms_app.models.view import display as models_display
    from pms_app.unit.view import display as unit_display

    app.register_blueprint(community_display, name='community_display', url_prefix='/community')
    app.register_blueprint(building_display, name='building_display', url_prefix='/building')
    app.register_blueprint(floor_display, name='floor_display', url_prefix='/floor')
    app.register_blueprint(models_display, name='models_display', url_prefix='/models')
    app.register_blueprint(unit_display, name='unit_display', url_prefix='/unit')

    with app.app_context():
        db.create_all()
    return app
