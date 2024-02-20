from dataclasses import dataclass
import datetime


YEAR = 2019
MONTH = 8
DAY = 1


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: datetime.date
    subjects: tuple
    hobbies: list
    picture: str
    address: str
    state: str
    city: str


@dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str