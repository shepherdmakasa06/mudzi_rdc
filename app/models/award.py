from app import db


class Award(db.Model):
    """Recognition and accolades won by the Council, shown on the public awards page."""

    __tablename__ = "awards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(500))
    display_order = db.Column(db.Integer, default=0, nullable=False)
    is_published = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<Award {self.title}>"
