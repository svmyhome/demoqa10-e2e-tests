import datetime
from pathlib import Path

def path(file_name):
    return str(Path(__file__).parent.parent.joinpath(f'resources/{file_name}'))


def generate_date_of_birth(year, month, day):
    date_time = datetime.datetime(1980, 1, 10)

    # Преобразуем дату и время в нужный формат
    return date_time.strftime("%d %B,%Y")
