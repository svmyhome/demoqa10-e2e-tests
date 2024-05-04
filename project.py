from typing import Literal

from pydantic_settings import BaseSettings

import config


class Settings(BaseSettings):
    platform_name: Literal['android', 'ios', 'local'] = 'android'
    app_path: str = config.app_path
    base_url: str = config.base_url
    time_out: float = config.time_out
    # android
    android_project_name: str = "Android wikipedia test"
    android_device_name: str = config.android_device_name
    android_platform_version: str = config.android_platform_version
    # ios
    ios_project_name: str = "IOS wikipedia test"
    ios_device_name: str = config.ios_device_name
    ios_platform_version: str = config.ios_platform_version


settings = Settings()
