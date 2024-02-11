import csv

from models.user import User, Status


class UserProvider:
    def get_users(self) -> list[User]:
        raise NotImplementedError


class CSVUserProvider(UserProvider):
    def get_users(self) -> list[User]:
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


class DBUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        raise NotImplementedError


class APIUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        raise NotImplementedError