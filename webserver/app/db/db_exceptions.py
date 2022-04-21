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
