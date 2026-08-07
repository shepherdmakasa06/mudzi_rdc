from app import db


class Investment(db.Model):
    __tablename__ = "investments"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    sector = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500))
    is_published = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<Investment {self.title}>"
