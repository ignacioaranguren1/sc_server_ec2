from flask_restful import Resource, Api
from flask import current_app, request, jsonify

from ..helpers.news_manager import select_random_news, string_to_dict
from marshmallow import Schema, fields, ValidationError


class NewsSchema(Schema):
    id = fields.Int(required=True)
    sentiment = fields.Str(required=True)


class IdNotFoundException(Exception):
    pass


class MainApi(Resource):

    def __init__(self):
        self.db_manager = current_app.config["DATABASE_MANAGER"]
        self.schema = NewsSchema()

    def get(self):
        total_number_news = self.db_manager.get_total_news()
        return jsonify(string_to_dict(str(self.db_manager.filter_by_id(select_random_news(total_number_news)))))

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        try:
            news_schema = NewsSchema().load(json_data)
            if not self.db_manager.filter_by_id(news_schema['id']):
                raise IdNotFoundException("No entry for {}".format(news_schema['id']))
            self.db_manager.register_sentiment(news_schema['id'], news_schema['sentiment'])
            return "NEWS ID: " + str(news_schema['id']) + " UPDATED TO SENTIMENT " + news_schema['sentiment']
        except IdNotFoundException as err:
            print(err)
        except ValidationError as err:
            print(err.messages)
