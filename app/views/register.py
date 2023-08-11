from flask.views import MethodView
from flask import Response
import json

from models import User
from app import db


class RegisterAPI(MethodView):
    """
    User Registration Resource
    """

    def post(self, request):
        post_data = request.get_json()
        user = User.query.filter_by(email=post_data.get("email").first())
        if not user:
            try:
                user = User(
                    email=post_data.get("email"), password=post_data.get("password")
                )

                db.session.add(user)
                db.session.commit()

                auth_token = user.encode_auth_token(user_id=user.id)

                responseObject = {
                    "status": "Success",
                    "message": "User registered succesfully",
                    "auth_token": auth_token.decode(),
                }

                return Response(
                    response=json.dumps(responseObject),
                    status=201,
                    mimetype="application/json",
                )
            except Exception:
                responseObject = {
                    "status": "Error",
                    "message": "An error occured while processing register request",
                }
                return Response(
                    response=json.dumps(responseObject),
                    status=500,
                    mimetype="application/json",
                )
        else:
            responseObject = {
                "status": "Error",
                "message": "User already exists. Please log in.",
            }
            return Response(
                response=json.dumps(responseObject),
                status=400,  # HTTP status code for "Bad Request"
                mimetype="application/json",
            )
