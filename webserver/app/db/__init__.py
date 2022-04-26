from .definitions import db_conn as db, init_db

from .manager import db_manager

def init_app(app, *args, **kwargs):
    """Initializes the app context for the database operation."""
    # Initialize the database connection instance
    db.init_app(app, *args, **kwargs)
    db.engine.pool._use_threadlocal = True
    # Initialize the database manager instance
    db_manager.init_app(app)