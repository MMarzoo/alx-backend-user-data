#!/usr/bin/env python3
""" Module of Session authentication views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Login endpoint
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    valid_user = User.search({'email': email})
    if not valid_user:
        return jsonify({"error": "no user found for this email"}), 404

    valid_user = valid_user[0]
    if not valid_user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(valid_user)
    cookie = getenv('SESSION_NAME')
    user_dict = jsonify(valid_user.to_json())
    user_dict.set_cookie(cookie, session_id)
    return user_dict
