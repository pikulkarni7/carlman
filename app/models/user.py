import datetime
import bcrypt
import app
import jwt

from app.extensions import db
from config import Config as config


class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        bytes = password.encode("utf-8")

        # generating the salt
        salt = bcrypt.gensalt()

        self.password = bcrypt.hashpw(bytes, salt).decode()
        self.date_added = datetime.datetime.now()
        self.admin = admin

    def __repr__(self):
        return f"(id={self.id!r}, email={self.email!r}, is_admin={self.is_admin})"

    def encode_auth_token(self, user_id):
        """
        Generates JWT
        :return: string
        """

        try:
            payload = {
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
                "iat": datetime.datetime.utcnow(),
                "sub": user_id,
            }

            return jwt.encode(payload, app.config.Config.SECRET_KEY, algorithm="HS256")

        except Exception as e:
            return e
