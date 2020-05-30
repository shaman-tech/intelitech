import os
from os.path import join, dirname
from dotenv import load_dotenv
import array

ngenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=ngenv_path)

INTELITECH_API_KEY= os.getenv('INTELITECH_API_KEY')
INTELITECH_API_SECRET= os.getenv('INTELITECH_API_SECRET') 
INTELITECH_HOST_ID = os.getenv('INTELITECH_HOST_ID')

LOG_FILENAME = os.getenv('LOG_FILENAME')