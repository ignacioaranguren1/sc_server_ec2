from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(80))
    sentiment_news = db.relationship('SentimentNews', backref='news', lazy=True)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return "{'id': %r" % str(self.id) + ",'content': %r" % self.content + "}"


class SentimentNews(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sentiment = db.Column(db.String(80))
    content = db.Column(db.String(80))
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), nullable=False)

    def __init__(self, sentiment, content, news_id):
        self.sentiment = sentiment
        self.content = content
        self.news_id = news_id

    def __repr__(self):
        return "{'id': %r" % str(self.id) + ",'sentiment': %r" % self.sentiment + ",'content': %r" % self.content + "}"


