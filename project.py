from typing import Literal

from pydantic_settings import BaseSettings

import config
from demoqa10_e2e_tests.utils import resource


class Settings(BaseSettings):
    platform_name: Literal['android', 'ios'] = config.platform_name
    context: Literal['local_emulator', 'local_real', 'bstack'] = config.context
    app_path: str = config.app_path
    base_url: str = config.base_url
    time_out: float = config.time_out
    # android
    udid: str = config.udid
    android_project_name: str = "Android wikipedia test"
    android_device_name: str = config.android_device_name
    android_platform_version: str = config.android_platform_version

    appWaitActivity: str = config.appWaitActivity


settings = Settings(_env_file=resource.relative_from_root(f'.env.{Settings().platform_name}'))
