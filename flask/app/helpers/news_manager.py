import random
import ast

def select_random_news(total_number):
    return random.randrange(1, total_number + 1)

def string_to_dict(news_string: str):
    return ast.literal_eval(news_string)
