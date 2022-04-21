from .models import News, SentimentNews
from .db_exceptions import IdNotFoundException, NewsNotFoundExceptions
from ..helpers.processing_helper import string_to_dict, select_random_news


class DbManager:
    """
        DbManager class.
        It is in charge of handling request from the application context to the DB manager.
    """

    def __init__(self, db):
        self.db = db

    def create_from_api(self, news_content):
        """
            Insert into the DB models data from the news API
        """
        try:
            # Check if DB empty. It is assumed that if DB is not empty, DB has been previously initialized.
            if not self.query_all():
                # Add row to DB sentence by sentence.
                for row in news_content:
                    # If sentence's length is less than 25, skip it.
                    row.decode('utf-8')
                    if len(row) > 25:
                        self.db.session.add(News(row))
                # Commit the result
                self.db.session.commit()
        except ValueError as error:
            raise ValueError('Could not convert item: {}'.format(error))
        except UnicodeDecodeError as error:
            print('There\'s been a problem with data: {}'.format(error))

    def register_sentiment(self, query_id, sentiment):
        """
            Register sentiment for some content
        """
        try:
            news = self.filter_by_id(query_id)
            # Check that request the news exists
            if not news:
                raise NewsNotFoundExceptions
            # Add new row
            self.db.session.add(SentimentNews(sentiment, news.content, news.id))
            self.db.session.commit()
        except NewsNotFoundExceptions as err:
            print(err)

    def get_random_news(self):
        total_number_news = self.get_total_news()
        # Check DB is not empty
        if total_number_news == 0:
            return {"id": 1, "content": "DB empty is empty"}
        else:
            return string_to_dict(str(self.filter_by_id(select_random_news(total_number_news))))

    def query_all(self):
        return News.query.all()

    def get_total_news(self):
        return len(News.query.all())

    def filter_by_id(self, param):
        try:
            news = News.query.filter_by(id=param).first()
            if not news:
                raise IdNotFoundException("No entry for ID: {}".format(param))
            return news
        except IdNotFoundException as err:
            print(err)
            return None

    def filter_by_sentiment(self, param):
        return News.query.filter_by(sentiment=param).first()
