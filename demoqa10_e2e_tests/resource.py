from pathlib import Path


def path(file_name):
    return str(Path(__file__).parent.parent.joinpath(f'resources/{file_name}'))
