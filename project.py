from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    platform_name: Literal['android', 'ios', 'local'] = 'android'
    app_path: str = "bs://sample.app"
    base_url: str = "http://hub.browserstack.com/wd/hub"
    time_out: float = 10.0
    # android
    platform_version: str = "9.0"
    android_project_name: str = "Android test"
    # ios
    ios_project_name: str = "ios test"


config = Settings()
