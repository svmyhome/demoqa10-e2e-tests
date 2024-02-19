from dataclasses import dataclass
import datetime


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
