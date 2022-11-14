from app.services import smes
from flask import Blueprint, request
import uuid

smes_bp = Blueprint('smes', __name__)

@smes_bp.route('/smes/<id>', methods=['GET'])
def get_sme(id):
    return smes.get_sme(id)

@smes_bp.route('/smes/<id>', methods=['PUT'])
def update_sme(id):
    """
    request body:
    {
        "name": "new name",
        "email": "new email",
        "password": "new password"
    }
    """
    sme_data = request.get_json()
    # inject id and email
    sme_data['id'] = id
    return smes.update_sme(id, sme_data)

@smes_bp.route('/smes/<id>', methods=['DELETE'])
def delete_sme(id):
    message = smes.delete_sme(id)
    return {'message': message}, 200

# SME Authentication
@smes_bp.route('/login', methods=['POST'])
def auth_sme():
    """
    request body:
    {
        "email": "email",
        "password": "password"
    }
    """
    sme_data = request.get_json()
    sme = smes.get_sme(sme_data['email'])
    if sme is None:
        return {'message': 'SME does not exist'}, 404
    if sme['password'] != sme_data['password']:
        return {'message': 'Invalid password'}, 401
    return {'message': 'SME authenticated successfully'}, 200

# SME Registration
@smes_bp.route('/register', methods=['POST'])
def register_sme():
    sme_data = request.get_json()
    sme = smes.get_sme(sme_data['email'])
    if sme is not None:
        return {'message': 'SME already exists'}, 400
    # randomly generate id
    sme_data['id'] = str(uuid.uuid4())
    return smes.create_sme(sme_data)