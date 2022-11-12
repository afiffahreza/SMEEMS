import os
from dotenv import load_dotenv

#  Import Environment Variables
load_dotenv()
CHANNEL_ACCESS_TOKEN = os.getenv('CHANNEL_ACCESS_TOKEN')
CHANNEL_SECRET = os.getenv('CHANNEL_SECRET')