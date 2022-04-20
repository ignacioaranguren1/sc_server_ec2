import os

from .api_client import NewsApiClient
from ..helpers.processing_helper import process_content


class APIManager:

    def __init__(self, app, db_man):
        self.app = app
        self.db_manager = db_man

    def get_content(self):
        # Retrieve configuration variables
        dirname = os.path.dirname(__file__)
        rel_file_name = self.app.config['API_NEWS_FILE_NAME']
        rel_file_path = "../db/" + rel_file_name
        file_path = os.path.join(dirname, rel_file_path)
        # If db is not empty write content
        if not self.db_manager.query_all():
            # get content from news API
            newsapi = NewsApiClient(url="https://api.goperigon.com/v1/all",
                                    token="089af873-e459-4dc3-a38c-7a2d027bc362")
            processed_response = process_content(newsapi.get_everything()['articles'])['c']
            self.db_manager.create_from_api(processed_response)





