import os
import zipfile
from zipfile import ZipFile


def create_zip(file_archive):
    path = os.path.join(os.getcwd(), 'resources')
    list_dir = os.listdir(path)
    print(list_dir)
    with ZipFile(file_archive, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file_name in list_dir:
            add_file = os.path.join(path, file_name)
            zf.write(add_file, os.path.basename(add_file))


def add_file_to_zip(name_archive, name_file):
    path = os.getcwd()
    with ZipFile(name_archive, 'a', compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(name_file)


create_zip('test1.zip')
add_file_to_zip('test1.zip', 'README.md')
