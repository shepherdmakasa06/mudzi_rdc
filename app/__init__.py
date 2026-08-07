import click
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin

from config import Config


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

from app.admin.views import SecureAdminIndexView


admin = Admin(
    name="Mudzi RDC Administration",
    index_view=SecureAdminIndexView(url="/admin"),
)


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User

    return db.session.get(User, int(user_id))


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    admin.init_app(app)

    # Login configuration
    login_manager.login_view = "admin_auth.login"
    login_manager.login_message_category = "warning"

    from app.admin import admin_bp
    from app.admin.views import register_admin_views

    app.register_blueprint(admin_bp)
    register_admin_views(admin)

    # Import routes
    from app.routes.main import main_bp
    from app.routes.news import news_bp
    from app.routes.projects import projects_bp
    from app.routes.publications import publications_bp
    from app.routes.investments import investments_bp
    from app.routes.stands import stands_bp
    from app.routes.contact import contact_bp

    # Register routes
    app.register_blueprint(main_bp)
    app.register_blueprint(news_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(publications_bp)
    app.register_blueprint(investments_bp)
    app.register_blueprint(stands_bp)
    app.register_blueprint(contact_bp)

    # The default SQLite setup should work immediately for a fresh checkout.
    # Production deployments can continue to manage schema changes with
    # Flask-Migrate.
    with app.app_context():
        db.create_all()
        from app.content_seed import seed_initial_content
        seed_initial_content()

    @app.template_filter("content_image")
    def content_image(path):
        """Resolve uploaded images while preserving existing external seed images."""
        if not path:
            return ""
        if path.startswith(("http://", "https://", "/")):
            return path
        from flask import url_for
        return url_for("static", filename=path)

    @app.cli.command("create-admin")
    @click.option("--username", prompt=True)
    @click.option("--email", prompt=True)
    @click.password_option()
    def create_admin(username, email, password):
        """Create an administrator account for /admin."""
        from app.models.user import User

        if User.query.filter(
            (User.username == username) | (User.email == email)
        ).first():
            raise click.ClickException("That username or email is already in use.")

        user = User(username=username, email=email, role="admin")
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        click.echo(f"Administrator '{username}' created.")

    return app
