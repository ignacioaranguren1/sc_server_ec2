from flask_sqlalchemy import SQLAlchemy

#################################
# SQLALCHEMY CONNECTION MANAGER #
#################################

db_conn = SQLAlchemy()

def init_db(app):
    """ Clear existing data and create new tables. """
    with app.app_context():
        db_conn.drop_all()
        db_conn.create_all()