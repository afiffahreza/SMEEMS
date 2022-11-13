from app.config.db import db

if __name__ == "__main__":
    user_ref = db.collection('users')
    request = {
        'id': '1',
        'name': 'test2',
    }
    user_ref.document('1').set(request)