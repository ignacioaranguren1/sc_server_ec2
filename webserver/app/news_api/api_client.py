import requests


class NewsAPIException(Exception):
    """
    Based on https://github.com/mattlisiv/newsapi-python
    """

    def __init__(self, exception):
        self.exception = exception

    def get_exception(self):
        return self.exception

    def get_status(self):
        if self.exception["status"]:
            return self.exception["status"]

    def get_code(self):
        if self.exception["code"]:
            return self.exception["code"]

    def get_message(self):
        if self.exception["message"]:
            return self.exception["message"]


class NewsApiClient(object):
    """
    Based on https://github.com/mattlisiv/newsapi-python
    """
    def __init__(self, url, token):
        self.request_method = requests
        self.target_url = url
        self.payload = dict(apiKey=token, language='en', category="Business", page=2, size=100)

    def get_everything(self):
        r = self.request_method.get(self.target_url, params=self.payload)
        # Check Status of Request
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())
        return r.json()



