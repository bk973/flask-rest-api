from flask import jsonify, request, url_for
from . import auth_blueprint
from ..Models import db, User

@auth_blueprint.route('/')
def auth_index_route():
    return jsonify('this is it')


@auth_blueprint.route('/users')
def get_all_users():

    users=User.query.all()

    from ..Models import users_schema
    data = users_schema.dump(users)

    return jsonify({'users': data})

@auth_blueprint.post('new')
def new_user():
    pass
