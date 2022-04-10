import csv
import sys

from .models import News, SentimentNews


class NewsNotFoundExceptions(Exception):
    """
        Exceptions raised if searched news is not in DB
    """
    pass


class DbManager:
    def __init__(self, db):
        self.db = db
        self.create_from_csv()

    def create_from_csv(self):
        try:
            if not self.query_all():
                with open('app/db/news_dataset.txt', mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        print(row)
                        self.db.session.add(News(row['content']))
                self.db.session.commit()
        except ValueError as error:
            raise ValueError('Could not convert item: {}'.format(error))

    def register_sentiment(self, query_id, sentiment):
        try:
            news = self.filter_by_id(query_id)
            if not news:
                raise NewsNotFoundExceptions
            self.db.session.add(SentimentNews(sentiment, news.content, news.id))
            self.db.session.commit()
        except NewsNotFoundExceptions as err:
            print(err)
        except Exception as err:
            print(err)
            print("Unexpected exception happened in register_sentiment")

    def query_all(self):
        return News.query.all()

    def get_total_news(self):
        return len(News.query.all())

    def filter_by_id(self, param):
        return News.query.filter_by(id=param).first()

    def filter_by_sentiment(self, param):
        return News.query.filter_by(sentiment=param).first()
