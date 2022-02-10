from functools import wraps
import secrets
import decimal
import json

from flask import request, jsonify

from drone_inventory.models import Drone, User

# Token required decorator for protected API Routes
def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(' ')[1]
        if not token:
            return jsonify({'message':'Token is missing!'}), 401

        try:
            current_user_token = User.query.filter_by(token = token).first()

            if current_user_token.token == token:
                print(current_user_token.token, 'current token')
                print(token)
        except:
            owner = User.query.filter_by(token=token).first()

            if token != owner.token and secrets.compare_digest(token, owner.token):
                return jsonify({'message':'Token is invalid'})

        return our_flask_function(current_user_token, *args,**kwargs)
    return decorated

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)