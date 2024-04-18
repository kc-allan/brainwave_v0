from api.v1.views import api_views
from models import storage
from models.group import Group
from flask import jsonify, make_response, request

TO_BE_IGNORED = []

@api_views.route('/groups', methods=['POST'])
def create_group():
    data = request.get_json()
    if not data:
        return make_response(jsonify("Empty parameters"), 400)
    if not type(data) == dict:
        return make_response(jsonify("Not a JSON"), 400)
    group = Group(**data)
    return make_response(jsonify(group.to_dict()))

@api_views.route('/groups', methods=['GET'])
def get_groups():
    groups = storage.all(Group)
    return make_response(jsonify([group.to_dict() for group in groups]))

@api_views.route('/groups/<group_id>', methods=['GET'])
def get_group_by_id(group_id):
    group = storage.get(Group, group_id)
    if group is None:
        return make_response(jsonify(None))
    return make_response(jsonify(group.to_dict()))

@api_views.route('/groups/<group_id>/users', methods=['GET'])
def get_group_users(group_id):
    group = storage.get(Group, group_id)
    if group is None:
        return make_response(jsonify("Group not found"), 400)
    members = group.members
    if not members:
        return make_response(jsonify("No members"), 400)
    return make_response(jsonify(members))

@api_views.route('/groups/<group_id>/files', methods=['GET'])
def get_group_files(group_id):
    group = storage.get(Group, group_id)
    if group is None:
        return make_response(jsonify("Group not found"), 400)
    files = group.group_files
    if not files:
        return make_response(jsonify("No files"), 400)
    return make_response(jsonify(files))

@api_views.route('/groups/<group_id>', methods=['PUT'])
def update_group(group_id):
    data = request.get_json()
    if not data:
        return make_response(jsonify("Empty parameters"), 400)
    if not type(data) == dict:
        return make_response(jsonify("Not a JSON"), 400)
    group = storage.get(Group, group_id)
    if not group:
        return make_response(jsonify("Group not found"), 400)
    for key, val in data.items():
        if key not in TO_BE_IGNORED:
            setattr(group, key, val)
    group.save()
    return make_response(jsonify(group.to_dict()))

@api_views.route('/groups/<group_id>', methods=['DELETE'])
def delete_group(group_id):
    group = storage.get(Group, group_id)
    if not group:
        return make_response(jsonify("Group not found"), 400)
    group.delete()
    return make_response(jsonify("success"), 200)