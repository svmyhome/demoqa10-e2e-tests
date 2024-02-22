from dataclasses import dataclass


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
