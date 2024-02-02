from zipfile import ZipFile
import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

with ZipFile(os.path.join(PROJECT_ROOT_PATH, "resources/lesson_7.zip")) as zip_file:
    print(zip_file.namelist())
    text = zip_file.read('README.rst').decode()
    print(text)
    zip_file.extract('pytest_logo_curves.svg', os.path.join(PROJECT_ROOT_PATH, "resources/temp_arch"))