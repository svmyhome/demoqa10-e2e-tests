from dataclasses import dataclass
import datetime

from demoqa10_e2e_tests.resource import Hobbies

YEAR = 2019
MONTH = 8
DAY = 1


@dataclass
class AdvancedUser:
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


worker = AdvancedUser(
    first_name='Ivan',
    last_name='Petrov',
    email='qaz@mail.ru',
    gender='Male',
    mobile='0123456789',
    date_of_birth_year='1980',
    date_of_birth_month='January',
    date_of_birth_day='10',
    subjects='Physics',
    hobbies=[Hobbies.sport.value, Hobbies.reading.value, Hobbies.music.value],
    picture='robo.png',
    current_address='SPB, lenina 10',
    state='Uttar Pradesh',
    city='Lucknow',
)


@dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


simple_user = SimpleUser('Ivan', 'Ivan@mail.ru', 'SPB, Nevsky 10', 'SPB, Nevsky 10')
