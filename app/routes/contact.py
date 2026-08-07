from flask import Blueprint, flash, redirect, render_template, request, url_for
from app import db
from app.models.contact import Contact
from app.models.page_section import PageSection

contact_bp = Blueprint(
    "contact",
    __name__,
    url_prefix="/contact"
)


@contact_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        values = {field: request.form.get(field, "").strip() for field in ("name", "email", "phone", "subject", "message")}
        if not all(values[field] for field in ("name", "email", "subject", "message")):
            flash("Please complete your name, email, subject, and message.", "error")
        else:
            db.session.add(Contact(**values))
            db.session.commit()
            flash("Message sent successfully. We will get back to you soon.", "success")
            return redirect(url_for("contact.index"))

    contact_details = PageSection.query.filter_by(page="contact", section_key="contact-details", is_published=True).first()
    return render_template("public/contact.html", contact_details=contact_details)
