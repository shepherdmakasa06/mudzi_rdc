from datetime import datetime

from app import db


class Vacancy(db.Model):
    __tablename__ = "vacancies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    department = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    employment_type = db.Column(db.String(80), default="Full-time", nullable=False)
    closing_date = db.Column(db.Date)
    overview = db.Column(db.Text, nullable=False)
    duties = db.Column(db.Text)
    qualifications = db.Column(db.Text)
    application_instructions = db.Column(db.Text)
    status = db.Column(db.String(30), default="Open", nullable=False)
    is_published = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Vacancy {self.title}>"
