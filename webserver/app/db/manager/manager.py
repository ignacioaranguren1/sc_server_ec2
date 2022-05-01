from ..models.models import News, SentimentNews
from pymysql.err import DataError
from .exceptions import IdNotFoundException, NewsNotFoundExceptions, DBInternalError
from ...helpers.processing_helper import string_to_dict, select_random_news
from ..definitions import db_conn as db
from sqlalchemy import exc


class DbManager(object):
    """
        DbManager class.
        It is in charge of handling request from the application context to the DB manager.
    """

    def commit_changes(self):
        """
            Commit the changes made to the SQLAlchemy model objects to the database.
        """
        try:
            db.session.commit()
            db.session.flush()
        except exc.IntegrityError as e:
            db.session.rollback()
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            raise DBInternalError("Can't update the database")


    def create_from_api(self, news_content):
        """
            Insert into the DB models data from the news API
        """
        try:
            # Check if DB empty. It is assumed that if DB is not empty, DB has been previously initialized.
            if not self.query_all():
                # Add row to DB sentence by sentence.
                for index, row in enumerate(news_content):
                    # If sentence's length is less than 25, skip it.
                    if len(row) > 25 and index < 500:
                        db.session.add(News(row))
                # Commit the result
                self.commit_changes()
        except ValueError as error:
            raise ValueError('Could not convert item: {}'.format(error))
        except DataError as error:
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
            db.session.add(SentimentNews(sentiment, news.content, news.id))
            self.commit_changes()
        except NewsNotFoundExceptions as err:
            print(err)

    def get_random_news(self):
        """
            Get random news from all the news form db
        """
        total_number_news = self.get_total_news()
        # Check DB is not empty
        if total_number_news == 0:
            return {"id": 1, "content": "DB empty is empty"}
        else:
            return string_to_dict(str(self.filter_by_id(select_random_news(total_number_news))))

    def query_all(self):
        """
            Retrieve all news from db
        """
        return News.query.all()

    def get_total_news(self):
        """
            Get total number of news
        """
        return len(self.query_all())

    def filter_by_id(self, param):
        """
            Get news filtered by id
        """
        try:
            news = News.query.filter_by(id=param).first()
            if not news:
                raise IdNotFoundException("No entry for ID: {}".format(param))
            return news
        except IdNotFoundException as err:
            print(err)
            return None

    def filter_by_sentiment(self, param):
        """
            Get news filtered by sentiment
        """
        return News.query.filter_by(sentiment=param).first()
