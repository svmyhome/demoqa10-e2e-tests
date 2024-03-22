from pathlib import Path


# def path(file_name):
#     return str(Path(__file__).parent.parent.parent.joinpath(f'{file_name}'))
#
# print(path('list_users.json'))

def relative_from_root(path: str):
    import demoqa10_e2e_tests
    from pathlib import Path

    return (
        Path(demoqa10_e2e_tests.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
print(relative_from_root('list_users.json'))