from app.config.db import db

users_ref = db.collection('users')
smes_ref = db.collection('smes')
plans_ref = db.collection('plans')
subscriptions_ref = db.collection('subscriptions')
promos_ref = db.collection('promos')