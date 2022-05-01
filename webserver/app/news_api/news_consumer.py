import os

from .api_client import NewsApiClient
from ..helpers.processing_helper import process_content
from ..db import db_manager


class APIManager:

    def __init__(self, app):
        self.app = app

    def get_content(self):
        # If db is not empty write content
        if not db_manager.query_all():
            # get content from news API
            news_api = NewsApiClient(url="https://api.goperigon.com/v1/all",
                                     token="0e97de0f-d215-403e-8e89-16351deaa204")
            processed_response = process_content(news_api.get_everything()['articles'])['c']
            db_manager.create_from_api(processed_response)






