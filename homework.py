import os
import zipfile
from zipfile import ZipFile


def create_zip(file_archive):
    path = os.path.join(os.getcwd(), 'resources')
    list_dir = os.listdir(path)
    with ZipFile(file_archive, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file_name in list_dir:
            add_file = os.path.join(path, file_name)
            zf.write(add_file, os.path.basename(add_file))


def add_file_to_zip(name_archive, name_file):
    path = os.getcwd()
    with ZipFile(name_archive, 'a', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(name_file)


def list_files_to_zip(name_archive):
    with ZipFile(name_archive, 'a') as zf:
        print(zf.namelist())


def extract_all_files(name_archive):
    extract_dir = 'extract_dir'
    with ZipFile(name_archive) as zf:
        zf.extractall(extract_dir)


def extract_file(name_archive, name_file):
    extract_dir = 'extract_dir_one'
    with ZipFile(name_archive) as zf:
        zf.extract(name_file, extract_dir)


create_zip('test1.zip')
add_file_to_zip('test1.zip', 'README.md')
list_files_to_zip('test1.zip')
extract_all_files('test1.zip')
extract_file('test1.zip', 'README.rst')
