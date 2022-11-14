from app.services import promo
from flask import Blueprint, request
import uuid

promo_bp = Blueprint('smes', __name__)

# CRUD for promo
# promo attributes: id, sme_id, brochure_link, description
# id is auto generated

@promo_bp.route('/promos/<id>', methods=['GET'])
def get_promo(id):
    return promo.get_promo(id)

@promo_bp.route('/promos/smes/<id>', methods=['GET'])
def get_promos(id):
    return promo.get_promos(id)

@promo_bp.route('/promos/<id>', methods=['PUT'])
def update_promo(id):
    """
    request body:
    {
        "brochure_link": "new brochure link",
        "description": "new description"
    }
    """
    promo_data = request.get_json()
    return promo.update_promo(id, promo_data)

@promo_bp.route('/promos/<id>', methods=['DELETE'])
def delete_promo(id):
    return promo.delete_promo(id)

# Create a new promo
@promo_bp.route('/promos', methods=['POST'])
def create_promo():
    """
    request body:
    {
        "sme_id": "sme id",
        "brochure_link": "brochure link",
        "description": "description"
    }
    """
    promo_data = request.get_json()
    # inject randomly generated id
    promo_data['id'] = str(uuid.uuid4())
    return promo.create_promo(promo_data)
