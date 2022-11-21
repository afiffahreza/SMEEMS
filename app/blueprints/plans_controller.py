from app.services import plans, smes, steppay
from flask import Blueprint, request
import uuid

plans_bp = Blueprint('plans', __name__)

# CRUD for plans
# plans attributes: id, sme_id, name, description, price
# id is auto generated

@plans_bp.route('/plans/<id>', methods=['GET'])
def get_plan(id):
    return plans.get_plan(id)

@plans_bp.route('/plans/smes/<id>', methods=['GET'])
def get_plans(id):
    return plans.get_plans(id)

@plans_bp.route('/plans/<id>', methods=['PUT'])
def update_plan(id):
    """
    request body:
    {
        "name": "new name",
        "description": "new description",
        "price": "new price"
    }
    """
    plan_data = request.get_json()
    return plans.update_plan(id, plan_data)

@plans_bp.route('/plans/<id>', methods=['DELETE'])
def delete_plan(id):
    message = plans.delete_plan(id)
    return {"message": message}, 200

# Create a new plan
@plans_bp.route('/plans', methods=['POST'])
def create_plan():
    """
    request body:
    {
        "sme_id": "sme id",
        "name": "name",
        "description": "description",
        "price": "price"
    }
    """
    # make sure the sme exists
    sme_id = request.get_json()['sme_id']
    sme = smes.get_sme(sme_id)
    if sme is None:
        return 'SME does not exist', 404
    plan_data = request.get_json()
    # inject randomly generated id
    plan_data['id'] = str(uuid.uuid4())

    # create a new steppay plan
    steppay_plan = steppay.create_steppay_plan(plan_data['name'], plan_data['price'], plan_data['description'])
    plan_data['steppay_price_code'] = steppay_plan['code']

    return plans.create_plan(plan_data)