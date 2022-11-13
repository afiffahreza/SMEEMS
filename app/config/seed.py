from . import SEED

# If SEED is set to True, then run the seed script
def seed():
    if SEED=='1':

        print('Seeding database...')

        # seed users
        from app.services.users import create_user
        user_data = {
            'id': '1',
            'name': 'John Doe',
            'email': 'john@gmail.com',
            'line_uid': 'U1234567890'
        }
        create_user(user_data)

        # seed smes
        from app.services.smes import create_sme
        sme_data = {
            'id': '1',
            'name': 'McDonalds',
            'email': 'mcd@mcd.id',
            'password': 'mcd123'
        }
        create_sme(sme_data)

        # seed plans
        from app.services.plans import create_plan
        plan_data = {
            'id': '1',
            'sme_id': '1',
            'name': 'McSpicy',
            'price': 10000,
            'description': 'Spicy chicken burger'
        }
        create_plan(plan_data)

        print('Database seeded.')
