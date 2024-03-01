from typing import Literal

from pydantic_settings import BaseSettings

from demoqa10_e2e_tests.utils import resource


class Settings(BaseSettings):
    context: Literal['local', 'test', 'stage', 'prod'] = 'local'
    base_url: str = 'https://demoqa.com'
    driver_name: str = 'chrome'
    hold_driver_at_exit: bool = False
    window_width: int = 1800
    window_height: int = 2000
    timeout: float = 4.0


config = Settings(_env_file=resource.relative_from_root(f'.env.{Settings().context}'))
