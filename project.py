from typing import Literal

from pydantic_settings import BaseSettings

import config


class Settings(BaseSettings):
    platform_name: Literal['android', 'ios', 'local'] = 'android'
    app_path: str = config.app_path
    base_url: str = config.base_url
    time_out: float = 10.0
    # android
    platform_version: str = "9.0"
    android_project_name: str = "Android test"
    # ios
    ios_project_name: str = "ios test"


config = Settings()
