from flask import Blueprint, render_template
from app.models.investment import Investment

investments_bp = Blueprint(
    "investments",
    __name__,
    url_prefix="/investments"
)


@investments_bp.route("/")
def index():
    investments = Investment.query.filter_by(is_published=True).all()
    return render_template("public/investments.html", investments=investments)
