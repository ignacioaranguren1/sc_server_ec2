class QueryError(Exception):
    """
        Parent exceptions raised if error in query
    """


class NewsNotFoundExceptions(QueryError):
    """
        Exceptions is raised if searched news is not in DB
    """
    pass


class IdNotFoundException(QueryError):
    """
        Exception is raised if news with requested id is not found
    """
    pass


class DBManagerError(Exception):
    """
    DB Manager Exception upper class.
    """
    pass


class DBInternalError(DBManagerError):
    """
    This exception will be raised when we are unable to write or read from the database
    """
    pass

