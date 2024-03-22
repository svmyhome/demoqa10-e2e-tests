import demoqa10_e2e_tests
from pathlib import Path


def relative_from_root(path: str):
    return (
        Path(demoqa10_e2e_tests.__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )