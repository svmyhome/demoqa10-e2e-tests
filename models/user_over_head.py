from dataclasses import dataclass
from enum import Enum

USER_ADULT_AGE = 18


class Status(Enum):
    status = 'student'
    worker = 'worker'


@dataclass
class User:
    name: str
    age: int
    status: Status
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE


class Worker(User):
    status = Status.worker

    def __init__(self, name, age, items):
        self.name = name
        self.age = age
        self.items = items

    def do_work(self):
        ...


if __name__ == '__main__':
    user3 = User('Vladimir', 23, Status('student'), ['book', 'pen'])
    user4 = User('Vladimir', 23, Status('student'), ['book', 'pen'])
    worker1 = Worker('Vladimir', 23, ['book', 'pen'])

    print(user3)
    print(user4)
    print(worker1)
