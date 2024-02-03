import os
import shutil
import zipfile
from zipfile import ZipFile

import pytest


@pytest.fixture(scope='module')
def create_zip():
    print(
        'This is Create ZIP', os.path.join(os.path.dirname(os.path.abspath(__file__)))
    )
    file_archive = 'test1.zip'
    files_source = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../tmp')
    files_for_zip = os.listdir(files_source)
    # print(files_source)
    # print(files_for_zip)
    # print('Befor change', os.getcwd())
    # os.chdir('..')
    # print('After change', os.getcwd())
    # print('After change2 ', os.path.join(os.path.dirname(os.path.abspath(__file__))))
    path_resources = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'resources'
    )
    # source_path = os.path.join(os.getcwd(), 'tmp')
    os.mkdir('resources')
    # path = os.path.join(os.getcwd(), 'resources')
    # print()
    # files_for_zip = os.listdir(path)
    destination = os.path.join(path_resources, file_archive)
    # if file_archive in files_for_zip:
    #     os.remove(destination)
    with ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file_name in files_for_zip:
            add_file = os.path.join(files_source, file_name)
            zf.write(add_file, os.path.basename(add_file))


@pytest.fixture(scope='module')
def extract_delete_zip(create_zip):
    print(
        'This is EXTRACT ZIP', os.path.join(os.path.dirname(os.path.abspath(__file__)))
    )
    # print(os.listdir())
    extract_all_files()
    yield

    print(
        'This is DELETE FOLDER',
        os.path.join(os.path.dirname(os.path.abspath(__file__))),
    )
    delete_folder()


# def add_file_to_zip(name_archive, name_file):
#     destination = os.path.join(os.getcwd(), 'resources', name_archive)
#     with ZipFile(destination, 'a', compression=zipfile.ZIP_DEFLATED) as zf:
#         zf.write(name_file)
#
#
# def list_files_to_zip(name_archive):
#     destination = os.path.join(os.getcwd(), 'resources', name_archive)
#     with ZipFile(destination, 'a') as zf:
#         print(zf.namelist())
#
#
def extract_all_files():
    name_archive = 'test1.zip'
    print(os.getcwd())
    extract_dir = os.path.join(os.getcwd(), 'resources')
    destination = os.path.join(os.getcwd(), 'resources', name_archive)
    with ZipFile(destination) as zf:
        zf.extractall(extract_dir)


#
#
# def extract_file(name_archive, name_file):
#     extract_dir = '../extract_dir_one'
#     destination = os.path.join(os.getcwd(), 'resources', name_archive)
#     with ZipFile(destination) as zf:
#         zf.extract(name_file, extract_dir)
def delete_folder():
    shutil.rmtree(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '../resources')
    )


#
# @pytest.fixture(scope='module', autouse=True)
# def work_with_zip(create_zip):
#     create_zip()
#     yield
#     delete_folder()
