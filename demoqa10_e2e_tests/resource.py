import datetime
from enum import Enum
from pathlib import Path
from demoqa10_e2e_tests.data.users import User


class Hobbies(Enum):
    sport = 'Sports'
    reading = 'Reading'
    music = 'Music'


def path(file_name):
    return str(Path(__file__).parent.parent.joinpath(f'resources/{file_name}'))


def generate_date_of_birth(year, month, day):
    date_time = datetime.datetime(1980, 1, 10)
    # Преобразуем дату и время в нужный формат
    return date_time.strftime("%d %B,%Y")


def generate_hobbies(user: User):
    hobbies_list = []
    for hobby in user.hobbies:
        hobbies_list.append(hobby)
    return ', '.join(hobbies_list)