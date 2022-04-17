import os
import csv
import nltk

nltk.download('punkt')

from .api_client import NewsApiClient
from flask import current_app
from nltk.tokenize import sent_tokenize

class APIManager:

    def __init__(self, app):
        self.app = app

    def get_content(self):
        # Retrieve configuration variables
        dirname = os.path.dirname(__file__)
        rel_file_name = self.app.config['API_NEWS_FILE_NAME']
        rel_file_path = "../db/" + rel_file_name
        file_path = os.path.join(dirname, rel_file_path)
        # If file is not empty write content
        if os.stat(file_path).st_size == 0:
            # get content from news API
            newsapi = NewsApiClient(url="https://api.goperigon.com/v1/all",
                                    token="089af873-e459-4dc3-a38c-7a2d027bc362")
            processed_response = self.process_content(newsapi.get_everything()['articles'])
            print(processed_response)
            with open(file_path, 'a') as file:
                writer = csv.DictWriter(file, fieldnames=['content'])
                writer.writeheader()
                writer.writerows(processed_response)

    def process_content(self, data):
        data = [{k: v for k, v in d.items() if k == 'content'} for d in data]
        result = []
        for d in data:
            result = result + sent_tokenize(d['content'])
        return dict.fromkeys("content", result)








