import os

import dotenv

from demoqa10_e2e_tests.utils import resource

dotenv.load_dotenv()
user_name = os.getenv('userName')
access_key = os.getenv('accessKey')


dotenv.load_dotenv(resource.relative_from_root('.env.remote'))
platform_name = os.getenv('platform_name')
app_path = os.getenv('appPath')
base_url = os.getenv('baseUrl')
time_out = os.getenv('time_out')
udid = os.getenv('udid')


runs_on_bstack = (app_path.startswith("bs://") or platform_name.startswith("ios"))
if runs_on_bstack:
    base_url = "http://hub.browserstack.com/wd/hub"
if platform_name.startswith("ios"):
    app_path = "bs://sample.app"
android_device_name = os.getenv('android_device_name')
android_platform_version = os.getenv('android_platform_version')

ios_device_name = os.getenv('ios_device_name')
ios_platform_version = os.getenv('ios_platform_version')


appWaitActivity = os.getenv("appium:appWaitActivity", "org.wikipedia.*")
