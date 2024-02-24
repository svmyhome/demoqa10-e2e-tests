from dataclasses import dataclass
from enum import Enum


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
    hobbies: list[Enum]
    picture: str
    current_address: str
    state: str
    city: str


class Hobbies(Enum):
    Sport = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


advanced_user = User(
    first_name='Ivan',
    last_name='Petrov',
    email='qaz@mail.ru',
    gender='Male',
    mobile='0123456789',
    date_of_birth_year='1980',
    date_of_birth_month='January',
    date_of_birth_day='10',
    subjects='Physics',
    hobbies=[Hobbies.Sport, Hobbies.Music],
    picture='robo.png',
    current_address='SPB, lenina 10',
    state='Uttar Pradesh',
    city='Lucknow',
)
