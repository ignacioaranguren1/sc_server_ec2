from flask import render_template, request, Blueprint, current_app
from ..helpers.processing_helper import select_random_news, string_to_dict


bp = Blueprint('classification', __name__, )


@bp.route('/', methods=['GET'])
def sentiment():
    # Retrieve db objet from configuration
    db_manager = current_app.config["DATABASE_MANAGER"]
    selected_news = db_manager.get_random_news()

    return render_template("index.html", news_id=selected_news["id"], news_content=selected_news["content"])


