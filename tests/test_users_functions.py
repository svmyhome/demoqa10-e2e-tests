import csv
import pytest
import os


@pytest.fixture
def users():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(test_dir, '..', 'resources_hw8', 'people.csv')) as csv_file:
        users = list(csv.DictReader(csv_file, delimiter=';'))
    return users


@pytest.fixture
def workers(users):
    workers = [user for user in users if user['status'] == 'worker']
    return workers


def test_workers_are_adults(workers):
    for worker in workers:
        assert user_is_adults(
            worker
        ), f'The worker {worker["name"]} have {worker["age"]} year'


def user_is_adults(worker):
    return int(worker['age']) >= 18
