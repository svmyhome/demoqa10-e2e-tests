import os
import pypdf
from openpyxl import load_workbook
from xlrd import open_workbook
import csv


def test_pdf(extract_delete_zip):
    pdf_file = 'english_grammar_book_for_students.pdf'
    os.chdir(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources')
    )
    destination = os.getcwd()
    with open(os.path.join(destination, pdf_file), 'rb') as pdf:
        reader = pypdf.PdfReader(pdf)
        text = reader.pages[2].extract_text()
        assert 'SERIES CONSULTANT' in text


def test_xlsx(extract_delete_zip):
    xlsx_file = 'calendare.xlsx'
    os.chdir(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources')
    )
    destination = os.getcwd()
    workbook = load_workbook(os.path.join(destination, xlsx_file))
    sheet = workbook.active
    value = sheet['C3'].value
    assert 'Введение в компьютерные приложения' in value


def test_xls(extract_delete_zip):
    xls_file = 'template.xls'
    os.chdir(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources')
    )
    destination = os.getcwd()
    reader = open_workbook(os.path.join(destination, xls_file))
    value = reader.sheet_by_index(0).cell_value(4, 1)
    assert 'Verify the is correct' in value


def test_csv(extract_delete_zip):
    csv_file = 'csv_test.csv'
    os.chdir(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources')
    )
    destination = os.getcwd()
    with open(os.path.join(destination, csv_file)) as f:
        reader = csv.reader(f)
        value = reader.__next__()
    assert 'Value 1' in value


def test_txt(extract_delete_zip):
    txt_file = 'README.rst'
    os.chdir(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'resources')
    )
    destination = os.getcwd()
    with open(os.path.join(destination, txt_file)) as txt:
        reader = txt.read()
        text = reader
    assert 'align: center' in text
