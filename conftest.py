import os

import dotenv
import pytest

from demoqa10_e2e_tests.utils.resource import relative_from_root


@pytest.fixture(scope='session')
def base_url():
    dotenv.load_dotenv()
    return os.getenv("BASE_URL")


@pytest.fixture(scope='session', autouse=True)
def api_setting():
    dotenv.load_dotenv(relative_from_root('.env.local'))