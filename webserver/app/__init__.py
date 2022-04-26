__author__ = "Ignacio Aranguren"
__credits__ = ["Ignacio Aranguren"]
__version__ = "0.1.0"
__maintainer__ = "Ignacio Aranguren"
__email__ = "ignacio.aranguren98@gmail.com"

enabled_modules = {
    "db_manager",
    "news_api",
    "rest_api",
    "app_database",
    "news_blueprint"
}

# Create instance
from flask import Flask, current_app

app = Flask(__name__, instance_relative_config=True)

# Load config from file
# app.config.from_object('../config')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')

with app.app_context():
    # Init the database and db_manager modules
    if "app_database" in enabled_modules:
        from .db import db

        # Database linkage with app and context setting
        db.init_app(app)
        from .db import db_manager

    if "news_api" in enabled_modules:
        from .news_api.news_consumer import APIManager

        # Init news api
        news_manager = APIManager(app)
        news_manager.get_content()

    if "rest_api" in enabled_modules:
        from flask_restful import Api
        from .api_rest.main_services import MainApi

        # Register rest services
        api = Api(app)
        api.add_resource(MainApi, '/update_news')

if "news_blueprint" in enabled_modules:
    from .blueprints import classification

    # Register blueprints
    app.register_blueprint(classification.bp)
