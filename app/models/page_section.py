from app import db


class PageSection(db.Model):
    """Editable text/image block used by the public informational pages."""

    __tablename__ = "page_sections"

    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(80), nullable=False, index=True)
    section_key = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    subtitle = db.Column(db.Text)
    content = db.Column(db.Text)
    image_url = db.Column(db.String(500))
    display_order = db.Column(db.Integer, default=0, nullable=False)
    is_published = db.Column(db.Boolean, default=True, nullable=False)

    __table_args__ = (db.UniqueConstraint("page", "section_key", name="uq_page_section_key"),)

    def __repr__(self):
        return f"<PageSection {self.page}:{self.section_key}>"
