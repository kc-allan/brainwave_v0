from flask import make_response, jsonify, request, abort

from api.v1.views import api_views
from models import storage
from models.user import User

TO_BE_IGNORED = ['__class__', 'created_at', 'updated_at', 'id']

@api_views.route('/users')
def all_users():
    users = storage.all(User)
    return make_response(jsonify([user.to_dict() for user in users]))

@api_views.route('/users/<user_id>/')
def get_user(user_id):
    user = storage.get("User", user_id)
    print(user)
    if user is not None:
        return make_response(jsonify(user.to_dict()))
    return make_response(jsonify(None))

@api_views.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if data is None:
        abort(400, "Empty request")
    if not type(data) == dict:
        abort(400, "Not a JSON")
    user = User(**data)
    return make_response(jsonify(user.to_dict()))

@api_views.route('/users/<user_id>', methods=['PUT'])
def edit_user(user_id):
    data = request.get_json()
    if data is None:
        abort(400, "Empty request")
    if not type(data) == dict:
        abort(400, "Not a JSON")
    user = storage.get(User, user_id)
    if user is not None:
        for key, val in data.items():
            if key not in TO_BE_IGNORED:
                setattr(user, key, val)
        user.save()
    return make_response(jsonify(user.to_dict()))

@api_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = storage.get(User, user_id)
    if user is not None:
        user.delete()
        return make_response(200)
    return make_response(jsonify(None))