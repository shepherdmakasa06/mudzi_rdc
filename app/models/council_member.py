from app import db


class CouncilMember(db.Model):
    __tablename__ = "council_members"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    position = db.Column(db.String(150), nullable=False)
    group = db.Column(db.String(30), default="Council", nullable=False)
    ward_or_role = db.Column(db.String(150))
    image_url = db.Column(db.String(500))
    display_order = db.Column(db.Integer, default=0, nullable=False)
    is_published = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"<CouncilMember {self.name}>"
