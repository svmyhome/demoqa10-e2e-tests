import datetime

from demoqa10_e2e_tests.test_data.users import User


def generate_hobbies(user: User):
    hobbies_list = []
    for hobby in user.hobbies:
        hobbies_list.append(hobby.value)
    return ', '.join(hobbies_list)
