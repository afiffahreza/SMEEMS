from app.services import promo, smes
from flask import Blueprint, request
import uuid

promos_bp = Blueprint('promos', __name__)

# CRUD for promo
# promo attributes: id, sme_id, brochure_link, description
# id is auto generated

@promos_bp.route('/promos/<id>', methods=['GET'])
def get_promo(id):
    return promo.get_promo(id)

@promos_bp.route('/promos/smes/<id>', methods=['GET'])
def get_promos(id):
    return promo.get_promos(id)

@promos_bp.route('/promos/<id>', methods=['PUT'])
def update_promo(id):
    """
    request body:
    {
        "brochure_link": "new brochure link",
        "description": "new description"
    }
    """
    promo_data = request.get_json()
    # inject id and sme_id
    promo_data['id'] = id
    promo_data['sme_id'] = promo.get_promo(id)['sme_id']
    return promo.update_promo(id, promo_data)

@promos_bp.route('/promos/<id>', methods=['DELETE'])
def delete_promo(id):
    message = promo.delete_promo(id)
    return {'message': message}, 200

# Create a new promo
@promos_bp.route('/promos', methods=['POST'])
def create_promo():
    """
    request body:
    {
        "sme_id": "sme id",
        "brochure_link": "brochure link",
        "description": "description"
    }
    """
    # make sure the sme exists
    sme_id = request.get_json()['sme_id']
    sme = smes.get_sme(sme_id)
    if sme is None:
        return 'SME does not exist', 404
    promo_data = request.get_json()
    # inject randomly generated id
    promo_data['id'] = str(uuid.uuid4())
    return promo.create_promo(promo_data)
