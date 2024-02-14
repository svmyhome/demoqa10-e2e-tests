import csv
import os

from models.user import User, Status


class UserProvider:
    def get_users(self) -> list[User]:
        raise NotImplementedError


class CSVUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        test_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(test_dir, '..', 'resources_hw8', 'people.csv')) as csv_file:
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


class DBUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        raise NotImplementedError


class APIUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        raise NotImplementedError