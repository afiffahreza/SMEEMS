from app.services import subscriptions
from flask import Blueprint, request
import uuid

subs_bp = Blueprint('subs', __name__)

# Get Subscriber for a plan
@subs_bp.route('/subs/<plan_id>', methods=['GET'])
def get_subscriber(plan_id):
    subscribers = subscriptions.get_subscribers(plan_id)
    return subscribers