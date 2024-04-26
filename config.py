import os

import dotenv

dotenv.load_dotenv()
user_name = os.getenv('userName')
access_key = os.getenv('accessKey')
app_path = os.getenv('appPath')
base_url = os.getenv('baseUrl')