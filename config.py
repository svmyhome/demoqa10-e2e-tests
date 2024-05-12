import os

import dotenv

from demoqa10_e2e_tests.utils import resource

# Read login and password
dotenv.load_dotenv()
user_name = os.getenv('userName')
access_key = os.getenv('accessKey')

# Read basic configuration
context = os.getenv('context', 'local_real')
appWaitActivity = os.getenv("appium:appWaitActivity", "org.wikipedia.*")

if context == 'local_real':
    dotenv.load_dotenv(resource.relative_from_root('.env.local_real'))
    udid = os.getenv('udid')
    platform_name = os.getenv('platform_name')
    android_device_name = os.getenv('android_device_name')
    android_platform_version = os.getenv('android_platform_version')
    app_path = os.getenv('appPath')
    base_url = os.getenv('baseUrl')
    time_out = os.getenv('time_out')

if context == 'local_emulator':
    dotenv.load_dotenv(resource.relative_from_root('.env.local_emulator'))
    udid = os.getenv('udid')
    platform_name = os.getenv('platform_name')
    android_device_name = os.getenv('android_device_name')
    android_platform_version = os.getenv('android_platform_version')
    app_path = os.getenv('appPath')
    base_url = os.getenv('baseUrl')
    time_out = os.getenv('time_out')

if context == 'bstack':
    dotenv.load_dotenv(resource.relative_from_root('.env.bstack'))
    udid = os.getenv('udid')
    platform_name = os.getenv('platform_name')
    android_device_name = os.getenv('android_device_name')
    android_platform_version = os.getenv('android_platform_version')
    app_path = os.getenv('appPath')
    base_url = os.getenv('baseUrl')
    time_out = os.getenv('time_out')




