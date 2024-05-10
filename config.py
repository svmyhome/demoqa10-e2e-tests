import os

import dotenv

from demoqa10_e2e_tests.utils import resource

# Read login and password
dotenv.load_dotenv()
user_name = os.getenv('userName')
access_key = os.getenv('accessKey')

# Read basic configuration
dotenv.load_dotenv(resource.relative_from_root('.env.config'))
platform_name = os.getenv('platform_name')
app_path = os.getenv('appPath')
base_url = os.getenv('baseUrl')
time_out = os.getenv('time_out')
appWaitActivity = os.getenv("appium:appWaitActivity", "org.wikipedia.*")


# The choice of test environment
runs_on_bstack = app_path.startswith("bs://")
if runs_on_bstack:
    base_url = "http://hub.browserstack.com/wd/hub"

# Read android configuration
dotenv.load_dotenv(resource.relative_from_root('.env.android'))
android_device_name = os.getenv('android_device_name')
android_platform_version = os.getenv('android_platform_version')
udid = os.getenv('udid')



