import os

import dotenv
import pytest


@pytest.fixture(scope='session')
def base_url():
    dotenv.load_dotenv()
    return os.getenv("BASE_URL")
