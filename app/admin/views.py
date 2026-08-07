from flask import abort, flash, redirect, request, url_for
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_admin.form import FileUploadField
from wtforms import HiddenField, PasswordField
from wtforms.validators import DataRequired

from app import db
from app.models.contact import Contact
from app.models.investment import Investment
from app.models.news import News
from app.models.project import Project
from app.models.publication import Publication
from app.models.service import Service
from app.models.stand import Stand
from app.models.user import User
from app.models.vacancy import Vacancy
from app.models.page_section import PageSection
from app.models.council_member import CouncilMember
from app.models.award import Award


class SecureAdminMixin:
    """Require an active administrator for every Flask-Admin view."""

    def is_accessible(self):
        return (
            current_user.is_authenticated
            and current_user.is_active
            and current_user.role in {"admin", "superadmin"}
        )

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            abort(403)
        return redirect(url_for("admin_auth.login", next=request.url))


class SecureAdminIndexView(SecureAdminMixin, AdminIndexView):
    @expose("/")
    def index(self):
        counts = {
            "News": News.query.count(),
            "Projects": Project.query.count(),
            "Publications": Publication.query.count(),
            "Vacancies": Vacancy.query.count(),
            "Enquiries": Contact.query.filter_by(is_resolved=False).count(),
        }
        return self.render("admin/dashboard.html", counts=counts)


class ContentModelView(SecureAdminMixin, ModelView):
    can_view_details = True
    page_size = 25
    can_export = True


class WebsiteContentView(ContentModelView):
    """Friendly field names matching the cards and sections on the public site."""

    column_labels = {
        "name": "Title / name",
        "description": "Card description",
        "summary": "Card summary",
        "content": "Full article content",
        "image_url": "Image upload",
        "icon": "Image upload",
        "document_url": "Document download URL",
        "is_published": "Visible on website",
    }


class ImageUploadContentView(WebsiteContentView):
    """Uses the local uploads folder instead of asking editors for image URLs."""

    form_overrides = {"image_url": FileUploadField}
    form_extra_fields = {"delete_image": HiddenField()}
    extra_js = ("/static/js/admin-image-delete.js",)

    def on_model_change(self, form, model, is_created):
        if form.delete_image.data == "1":
            model.image_url = None


class ServiceAdminView(WebsiteContentView):
    form_overrides = {"icon": FileUploadField}
    form_extra_fields = {"delete_image": HiddenField()}
    extra_js = ("/static/js/admin-image-delete.js",)

    def on_model_change(self, form, model, is_created):
        if form.delete_image.data == "1":
            model.icon = None


class ContactInformationView(WebsiteContentView):
    """A direct admin menu item for the details displayed on Contact Us."""

    can_create = False
    can_delete = False
    can_export = False
    form_columns = ("title", "content", "is_published")
    column_list = ("title", "content", "is_published")
    column_labels = {
        **WebsiteContentView.column_labels,
        "content": "Address, phone, email and hours (separate each item with a blank line)",
    }

    def get_query(self):
        return super().get_query().filter(PageSection.page == "contact")

    def get_count_query(self):
        return super().get_count_query().filter(PageSection.page == "contact")


class PaymentDetailsView(ContactInformationView):
    """Payment methods shown on the public payment page."""

    def get_query(self):
        return ContentModelView.get_query(self).filter(PageSection.page == "payment")

    def get_count_query(self):
        return ContentModelView.get_count_query(self).filter(PageSection.page == "payment")


class GovernanceSectionsView(ImageUploadContentView):
    """Editable governance page blocks without exposing internal page keys."""

    form_excluded_columns = ("page",)
    column_list = ("section_key", "title", "subtitle", "display_order", "is_published")

    def get_query(self):
        return ContentModelView.get_query(self).filter(PageSection.page == "governance")

    def get_count_query(self):
        return ContentModelView.get_count_query(self).filter(PageSection.page == "governance")

    def on_model_change(self, form, model, is_created):
        model.page = "governance"
        super().on_model_change(form, model, is_created)


class AwardAdminView(WebsiteContentView):
    """Awards and recognition shown on the public awards page."""

    column_list = ("title", "icon", "display_order", "is_published")
    form_columns = ("title", "description", "icon", "display_order", "is_published")
    column_labels = {
        **WebsiteContentView.column_labels,
        "title": "Award title",
        "icon": "Font Awesome icon name (e.g. fa-trophy)",
    }


class EnquiryAdminView(ContentModelView):
    """Public submissions can be reviewed and resolved; admins do not create them."""

    can_create = False
    can_delete = False
    can_edit = False
    details_template = "admin/enquiry_details.html"
    column_list = ("created_at", "name", "email", "phone", "subject", "is_resolved")
    column_searchable_list = ("name", "email", "subject", "message")
    column_filters = ("is_resolved", "created_at")
    column_labels = {"is_resolved": "Resolved"}

    @expose("/resolve/<int:id>", methods=("POST",))
    def resolve_view(self, id):
        enquiry = db.session.get(Contact, id)
        if enquiry is None:
            abort(404)
        enquiry.is_resolved = True
        db.session.commit()
        flash("Enquiry marked as resolved.", "success")
        return redirect(self.get_url(".details_view", id=id, url=request.args.get("url")))


class VacancyAdminView(WebsiteContentView):
    column_list = ("title", "department", "location", "employment_type", "closing_date", "status", "is_published")
    column_searchable_list = ("title", "department", "location")
    column_filters = ("department", "status", "is_published")
    form_columns = (
        "title", "department", "location", "employment_type", "closing_date",
        "status", "overview", "duties", "qualifications",
        "application_instructions", "is_published",
    )
    form_choices = {
        "status": [("Open", "Open"), ("Closed", "Closed")],
        "employment_type": [("Full-time", "Full-time"), ("Part-time", "Part-time"), ("Contract", "Contract")],
    }
    column_labels = {
        **WebsiteContentView.column_labels,
        "title": "Job title",
        "department": "Department",
        "location": "Work location",
        "employment_type": "Employment type",
        "closing_date": "Closing date",
        "overview": "Job overview",
        "duties": "Key duties (one per line)",
        "qualifications": "Qualifications and experience (one per line)",
        "application_instructions": "How to apply",
    }


class UserAdminView(ContentModelView):
    column_list = ("username", "email", "role", "is_active")
    column_searchable_list = ("username", "email")
    column_editable_list = ("role", "is_active")
    form_excluded_columns = ("password_hash",)
    form_extra_fields = {
        "password": PasswordField("Password", validators=[DataRequired()]),
    }

    def on_model_change(self, form, model, is_created):
        password = form.password.data
        if password:
            model.set_password(password)
        elif is_created:
            raise ValueError("A password is required for new users.")

    def edit_form(self, obj=None):
        form = super().edit_form(obj)
        form.password.validators = []
        return form


def register_admin_views(admin):
    """Attach content management screens once for application factories/tests."""
    if getattr(admin, "_mudzi_views_registered", False):
        return

    admin.add_view(UserAdminView(User, db.session, endpoint="admin_users", category="Administration"))
    upload_args = {"base_path": admin.app.static_folder, "relative_path": "uploads/"}
    ImageUploadContentView.form_args = {"image_url": upload_args}
    ServiceAdminView.form_args = {"icon": upload_args}

    admin.add_view(ImageUploadContentView(News, db.session, endpoint="admin_news", category="Website content"))
    admin.add_view(ImageUploadContentView(Project, db.session, endpoint="admin_projects", category="Website content"))
    admin.add_view(WebsiteContentView(Publication, db.session, endpoint="admin_publications", category="Website content"))
    admin.add_view(ImageUploadContentView(Investment, db.session, endpoint="admin_investments", category="Website content"))
    admin.add_view(WebsiteContentView(Stand, db.session, endpoint="admin_stands", category="Website content"))
    admin.add_view(ServiceAdminView(Service, db.session, endpoint="admin_services", category="Website content"))
    admin.add_view(VacancyAdminView(Vacancy, db.session, endpoint="admin_vacancies", category="Website content"))
    admin.add_view(ImageUploadContentView(PageSection, db.session, endpoint="admin_page_sections", name="Page sections", category="Website content"))
    admin.add_view(GovernanceSectionsView(PageSection, db.session, endpoint="admin_governance", name="Governance sections", category="Governance"))
    admin.add_view(ImageUploadContentView(CouncilMember, db.session, endpoint="admin_council_members", name="Councillors & management", category="Governance"))
    admin.add_view(AwardAdminView(Award, db.session, endpoint="admin_awards", name="Awards & recognition", category="Governance"))
    admin.add_view(ContactInformationView(PageSection, db.session, endpoint="admin_contact_information", name="Contact information", category="Contact us"))
    admin.add_view(PaymentDetailsView(PageSection, db.session, endpoint="admin_payment_details", name="Payment details", category="Payments"))
    admin.add_view(EnquiryAdminView(Contact, db.session, endpoint="admin_contacts", name="Submitted messages", category="Enquiries"))
    admin._mudzi_views_registered = True
