from flask import Blueprint, render_template

stands_bp = Blueprint(
    "stands",
    __name__,
    url_prefix="/stands"
)


@stands_bp.route("/")
def index():
    return render_template("public/stands.html")