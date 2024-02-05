import csv
import pytest

from models.provider import UserProvider, CSVUserProvider
from models.user import User, USER_ADULT_AGE, Status
from models.user_over_head import Worker

@pytest.fixture
def user_provider() -> UserProvider:
    return CSVUserProvider()
@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()


@pytest.fixture
def workers(users) -> list[Worker]:
    workers = [
        Worker(
            name=user.name,
            age=user.age,
            items=user.items,
        )
        for user in users
        if user.status == Status.worker
    ]
    return workers


def test_workers_are_adults(workers):
    for worker in workers:
        assert worker.is_adult(), f'The worker {worker.name} less USER_ADULT_AGE year'
