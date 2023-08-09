from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from .models.user import User

# Create the Flask app instance
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object("app.config.Config")

# Initialize database
database = SQLAlchemy(app)


# Initialize migration
migrate = Migrate(app, database)

# # Import your routes
# from app.routes import authentication
# # Import other routes as needed

# # This import should be at the end to avoid circular dependencies
# from app import routes
