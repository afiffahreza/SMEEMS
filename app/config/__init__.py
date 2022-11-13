import os
from dotenv import load_dotenv

#  Import Environment Variables
print('Loading environment variables...')
load_dotenv()
CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')
CHANNEL_SECRET = os.getenv('CHANNEL_SECRET')
FIRESTORE_CREDENTIALS = os.getenv('FIRESTORE_CREDENTIALS')
SEED= os.getenv('SEED')