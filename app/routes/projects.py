from flask import Blueprint, render_template
from app.models.project import Project

projects_bp = Blueprint("projects", __name__, url_prefix="/projects")


@projects_bp.route("/")
def index():
    projects = Project.query.filter_by(is_published=True).all()
    return render_template("public/projects.html", projects=projects)
