from flask import render_template, request, Blueprint, current_app
from ..helpers.processing_helper import select_random_news, string_to_dict


bp = Blueprint('classification', __name__, )

@bp.route('/', methods=['GET'])
def sentiment():  # put application's code here
    selected_news = {"content": "char_len_less_than_25"}
    db_manager = current_app.config["DATABASE_MANAGER"]
    total_number_news = db_manager.get_total_news()
    while len(selected_news["content"]) < 25:
        selected_news = string_to_dict(str(db_manager.filter_by_id(select_random_news(total_number_news))))
    return render_template("index.html", news_id=selected_news["id"], news_content=selected_news["content"])


