from . import subscriptions_ref

# CRUD for subscriptions
# subscriptions attributes: id, plan_id, user_id, start_date, end_date, status

def create_subscription(subscription_data):
    # Create a new subscription
    subscription_ref = subscriptions_ref.document(subscription_data['id'])
    subscription_ref.set(subscription_data)
    return subscription_data

def get_subscription(subscription_id):
    # Get a subscription
    subscription_ref = subscriptions_ref.document(subscription_id)
    subscription = subscription_ref.get()
    if subscription.exists:
        return subscription.to_dict()
    else:
        return None

def get_subscriptions(user_id):
    # Get all subscriptions of a user
    subscriptions = subscriptions_ref.where('user_id', '==', user_id).stream()
    return [subscription.to_dict() for subscription in subscriptions]

def get_subscribers(plan_id):
    # Get all subscriber of a plan
    subscriptions = subscriptions_ref.where('plan_id', '==', plan_id).stream()
    return [subscription.to_dict() for subscription in subscriptions]

def update_subscription(subscription_id, subscription_data):
    # Update a subscription
    subscription_ref = subscriptions_ref.document(subscription_id)
    subscription_ref.update(subscription_data)
    return subscription_data

def delete_subscription(subscription_id):
    # Delete a subscription
    subscription_ref = subscriptions_ref.document(subscription_id)
    subscription_ref.delete()
    return "subscription_id: " + subscription_id + " deleted"