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
    date_of_birth_year: str
    date_of_birth_month: str
    date_of_birth_day: str
    subjects: str
    hobbies: list
    picture: str
    current_address: str
    state: str
    city: str


@dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str