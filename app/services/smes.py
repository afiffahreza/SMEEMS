from . import smes_ref

# CRUD for smes
# smes attributes: id, name, email, password

def create_sme(sme_data):
    # Create a new sme
    sme_ref = smes_ref.document(sme_data['id'])
    sme_ref.set(sme_data)
    return sme_data

def get_sme(sme_id):
    # Get a sme
    sme_ref = smes_ref.document(sme_id)
    sme = sme_ref.get()
    if sme.exists:
        return sme.to_dict()
    else:
        return None

def update_sme(sme_id, sme_data):
    # Update a sme
    sme_ref = smes_ref.document(sme_id)
    sme_ref.update(sme_data)
    return sme_data

def delete_sme(sme_id):
    # Delete a sme
    sme_ref = smes_ref.document(sme_id)
    sme_ref.delete()