from flask import Blueprint, render_template
from app.models.news import News
from app.models.page_section import PageSection
from app.models.service import Service
from app.models.council_member import CouncilMember
from app.models.award import Award

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    sections = {section.section_key: section for section in PageSection.query.filter_by(page="home", is_published=True).all()}
    services = Service.query.filter_by(is_published=True).all()
    latest_news = News.query.filter_by(is_published=True).order_by(News.published_at.desc()).limit(4).all()
    return render_template("public/index.html", sections=sections, services=services, latest_news=latest_news)


@main_bp.route("/governance")
def governance():
    sections = {section.section_key: section for section in PageSection.query.filter_by(page="governance", is_published=True).all()}
    return render_template("public/governance.html", sections=sections)


@main_bp.route("/council")
def council():
    members = CouncilMember.query.filter_by(group="Council", is_published=True).order_by(CouncilMember.display_order).all()
    return render_template("public/council.html", members=members)


@main_bp.route("/management")
def management():
    members = CouncilMember.query.filter_by(group="Management", is_published=True).order_by(CouncilMember.display_order).all()
    return render_template("public/management.html", members=members)


@main_bp.route("/awards")
def awards():
    awards_list = Award.query.filter_by(is_published=True).order_by(Award.display_order).all()
    return render_template("public/awards.html", awards=awards_list)


@main_bp.route("/payment")
def payment():
    payment_details = PageSection.query.filter_by(page="payment", is_published=True).order_by(PageSection.display_order).all()
    return render_template("public/payment.html", payment_details=payment_details)


@main_bp.route("/application")
def application():
    return render_template("public/application.html")


@main_bp.route("/login")
def login():
    return render_template("admin/login.html")
