from zipfile import ZipFile
import os

os.chdir('../resources')
path = os.getcwd()
with ZipFile(os.path.join(path, "test1.zip"), ) as zip_file:
    print(zip_file.namelist())
    text = zip_file.read('README.rst').decode()
    print(text)
    zip_file.extract('pytest_logo_curves.svg', os.path.join(path, "temp_arch"))
