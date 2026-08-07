from flask import Blueprint, render_template
from app.models.publication import Publication

publications_bp = Blueprint(
    "publications",
    __name__,
    url_prefix="/publications"
)


@publications_bp.route("/")
def index():
    publications = Publication.query.filter_by(is_published=True).all()
    return render_template("public/publications.html", publications=publications)
