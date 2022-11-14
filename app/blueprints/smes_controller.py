from app.services import smes
from flask import Blueprint, request

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
        "password": "new password"
    }
    """
    sme_data = request.get_json()
    return smes.update_sme(id, sme_data)

@smes_bp.route('/smes/<id>', methods=['DELETE'])
def delete_sme(id):
    return smes.delete_sme(id)

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
@smes_bp.route('/register', methods=['PUT'])
def register_sme():
    sme_data = request.get_json()
    sme = smes.get_sme(sme_data['email'])
    if sme is not None:
        return {'message': 'SME already exists'}, 400
    sme_data['id'] = sme_data['email']
    return smes.create_sme(sme_data)