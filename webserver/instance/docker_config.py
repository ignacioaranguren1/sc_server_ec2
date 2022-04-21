DB_USERNAME = "sin_chan"
DB_PASSWORD = "_sinosuke_noara"
DB_NAME = "sentiment"
MYSQL_DATABASE_CHARSET = 'utf8mb4'
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + DB_USERNAME + ":" + DB_PASSWORD + "@mysql:3306/" + DB_NAME
SQLALCHEMY_TRACK_MODIFICATIONS = True
