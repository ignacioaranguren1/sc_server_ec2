from ..definitions import db_conn as db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(11000))
    sentiment_news = db.relationship('SentimentNews', backref='news', lazy=True)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return "{'id': %r" % str(self.id) + ",'content': %r" % self.content + "}"


class SentimentNews(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sentiment = db.Column(db.Integer)
    content = db.Column(db.String(1000))
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), nullable=False)

    def __init__(self, sentiment, content, news_id):
        self.sentiment = sentiment
        self.content = content
        self.news_id = news_id

    def __repr__(self):
        return "{'id': %r" % str(self.id) + ",'sentiment': %r" % self.sentiment + ",'content': %r" % self.content + "}"

