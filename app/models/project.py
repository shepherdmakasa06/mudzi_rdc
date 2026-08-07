from app import db


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(80))
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(150))
    status = db.Column(db.String(50), default="Planned", nullable=False)
    image_url = db.Column(db.String(500))
    is_published = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<Project {self.name}>"
