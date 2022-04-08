from flask import render_template, request, Blueprint, current_app
from ..helpers.news_manager import select_random_news, string_to_dict


bp = Blueprint('classification', __name__, )


@bp.route('/', methods=['GET'])
def sentiment():  # put application's code here
    db_manager = current_app.config["DATABASE_MANAGER"]
    total_number_news = db_manager.get_total_news()
    selected_news = string_to_dict(str(db_manager.filter_by_id(select_random_news(total_number_news))))
    return render_template("index.html", news_id=selected_news["id"], news_content=selected_news["content"])


