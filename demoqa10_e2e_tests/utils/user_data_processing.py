from datetime import datetime

from demoqa10_e2e_tests.test_data.users import User


def generate_date_of_birth(year, month, day):
    date_time = datetime.datetime(1980, 1, 10)
    # Преобразуем дату и время в нужный формат
    return date_time.strftime("%d %B,%Y")

def get_hobbies(user: User):
    hobbies_list = []
    for hobby in user.hobbies:
        hobbies_list.append(hobby.value)
    return ', '.join(hobbies_list)
