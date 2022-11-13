from . import plans_ref

# CRUD for plans
# plans attributes: id, sme_id, name, price, description

def create_plan(plan_data):
    # Create a new plan
    plan_ref = plans_ref.document(plan_data['id'])
    plan_ref.set(plan_data)
    return plan_data

def get_plan(plan_id):
    # Get a plan
    plan_ref = plans_ref.document(plan_id)
    plan = plan_ref.get()
    if plan.exists:
        return plan.to_dict()
    else:
        return None

def get_plans(sme_id):
    # Get all plans of an sme
    plans = plans_ref.where('sme_id', '==', sme_id).stream()
    return [plan.to_dict() for plan in plans]

def update_plan(plan_id, plan_data):
    # Update a plan
    plan_ref = plans_ref.document(plan_id)
    plan_ref.update(plan_data)
    return plan_data

def delete_plan(plan_id):
    # Delete a plan
    plan_ref = plans_ref.document(plan_id)
    plan_ref.delete()
