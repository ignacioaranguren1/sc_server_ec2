from flask_restful import Resource, Api
from flask import current_app, request, jsonify

from ..helpers.processing_helper import select_random_news, string_to_dict
from marshmallow import ValidationError
from .news_schema import NewsSchema
from ..db import db_manager


class MainApi(Resource):
    """
        Restful API for sentiment registration and asynchronous requests
    """

    def __init__(self):
        self.schema = NewsSchema()

    def get(self):
        """
            Get random news from DB
        """
        total_number_news = db_manager.get_total_news()
        if total_number_news == 0:
            return {"id": 1, "content": "DB empty is empty"}
        return jsonify(string_to_dict(str(db_manager.filter_by_id(select_random_news(total_number_news)))))

    def post(self):
        """
            Post news with associated sentiment
        """
        # Retrieve payload from origin request
        json_data = request.get_json(force=True)
        try:
            # Use marshmallow schema to check data integrity
            news_schema = NewsSchema().load(json_data)
            # Check if requested id exist in db
            if db_manager.filter_by_id(news_schema['id']) is not None:
                db_manager.register_sentiment(news_schema['id'], news_schema['sentiment'])
                return "NEWS ID: {} UPDATED TO SENTIMENT {}".format(str(news_schema['id']), news_schema['sentiment'])
            else:
                return "REQUESTED ID: {} NEWS NOT FOUND IN DATABASE".format(str(news_schema['id'])), 232
        except ValidationError as err:
            return err.messages, 232
