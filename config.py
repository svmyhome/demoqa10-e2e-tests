import os

import dotenv

dotenv.load_dotenv()
user_name = os.getenv('userName')
access_key = os.getenv('accessKey')