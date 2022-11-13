from . import promo_ref

# CRUD for promo
# promo attributes: id, sme_id, brochure_link, description

def create_promo(promo_data):
    # Create a new promo
    promo_ref = promo_ref.document(promo_data['id'])
    promo_ref.set(promo_data)
    return promo_data

def get_promo(promo_id):
    # Get a promo
    promo_ref = promo_ref.document(promo_id)
    promo = promo_ref.get()
    if promo.exists:
        return promo.to_dict()
    else:
        return None

def get_promos(sme_id):
    # Get all promos of an sme
    promos = promo_ref.where('sme_id', '==', sme_id).stream()
    return [promo.to_dict() for promo in promos]

def update_promo(promo_id, promo_data):
    # Update a promo
    promo_ref = promo_ref.document(promo_id)
    promo_ref.update(promo_data)
    return promo_data

def delete_promo(promo_id):
    # Delete a promo
    promo_ref = promo_ref.document(promo_id)
    promo_ref.delete()
