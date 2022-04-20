import random
import ast
from nltk.tokenize import sent_tokenize


def select_random_news(total_number):
    return random.randrange(1, total_number + 1)


def string_to_dict(news_string: str):
    return ast.literal_eval(news_string)


def process_content(data):
    content = []
    for d in data:
        for k, v in d.items():
            if k == 'content':
                content = content + sent_tokenize(v)
    return dict.fromkeys("content", content)

