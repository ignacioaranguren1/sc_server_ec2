from flask import Flask, current_app
from .blueprints import classification
from .db.db_manager import DbManager
from .db.models import db
from flask_restful import Api
from .api_rest.main_services import MainApi
from .news_api.news_consumer import APIManager


# Create instance
app = Flask(__name__)
app = Flask(__name__, instance_relative_config=True)
# Load config from file
app.config.from_object('config')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')
# Register blueprints
app.register_blueprint(classification.bp)
# Register rest services
api = Api(app)
api.add_resource(MainApi, '/update_news')
# Database linkage with app and context setting
db.init_app(app)
app.app_context().push()
db.create_all()
# Create database manager
db_manager = DbManager(db)
# Init news api
api_manager = APIManager(app, db_manager)
api_manager.get_content()
# Load manager to env
current_app.config["DATABASE_MANAGER"] = db_manager
