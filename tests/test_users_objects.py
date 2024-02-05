import csv
import pytest

from models.user import User, USER_ADULT_AGE, Status


@pytest.fixture
def users() -> list[User]:
    with open('../resources_hw8/people.csv') as csv_file:
        users = list(csv.DictReader(csv_file, delimiter=';'))
    return [
        User(
            name=user['name'],
            age=int(user['age']),
            status=Status(user['status']),
            items=user['items'],
        )
        for user in users
    ]


@pytest.fixture
def workers(users) -> list[User]:
    workers = [user for user in users if user.status == Status.worker]
    return workers


def test_workers_are_adults(workers):
    for worker in workers:
        assert worker.is_adult(), f'The worker {worker.name} less USER_ADULT_AGE year'
