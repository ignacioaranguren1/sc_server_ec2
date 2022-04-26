from flask import render_template, request, Blueprint, current_app


bp = Blueprint('classification', __name__, )


@bp.route('/', methods=['GET'])
def sentiment():
    from ..db import db_manager
    # select random news
    selected_news = db_manager.get_random_news()
    print(selected_news)
    return render_template("index.html", news_id=selected_news["id"], news_content=selected_news["content"])


