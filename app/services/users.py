from . import users_ref

# CRUD for users
# users attributes: id, name, email, line_uid

def create_user(user_data):
    # Create a new user
    user_ref = users_ref.document(user_data['id'])
    user_ref.set(user_data)
    return user_data

def get_user(user_id):
    # Get a user
    user_ref = users_ref.document(user_id)
    user = user_ref.get()
    if user.exists:
        return user.to_dict()
    else:
        return None

def update_user(user_id, user_data):
    # Update a user
    user_ref = users_ref.document(user_id)
    user_ref.update(user_data)
    return user_data

def delete_user(user_id):
    # Delete a user
    user_ref = users_ref.document(user_id)
    user_ref.delete()
