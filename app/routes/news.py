from flask import Blueprint, render_template
from app.models.news import News
from app.models.vacancy import Vacancy

news_bp = Blueprint("news", __name__, url_prefix="/news")


@news_bp.route("/")
def index():
    news_items = News.query.filter_by(is_published=True).order_by(News.published_at.desc()).all()
    vacancies = Vacancy.query.filter_by(is_published=True).order_by(Vacancy.closing_date.asc()).all()
    return render_template("public/news.html", news_items=news_items, vacancies=vacancies)
