DB_USERNAME = "sin_chan"
DB_PASSWORD = "_sinosuke_noara"
DB_NAME = "sentiment"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + DB_USERNAME + ":" + DB_PASSWORD + "@localhost/" + DB_NAME + "?charset=utf8mb4"
SQLALCHEMY_TRACK_MODIFICATIONS = True
