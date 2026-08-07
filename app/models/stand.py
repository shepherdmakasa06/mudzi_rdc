from app import db


class Stand(db.Model):
    __tablename__ = "stands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    stand_type = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    size = db.Column(db.String(100))
    price = db.Column(db.Numeric(12, 2))
    status = db.Column(db.String(50), default="Available", nullable=False)
    is_published = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<Stand {self.name}>"
