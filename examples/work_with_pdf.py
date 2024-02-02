import os.path

import PyPDF2

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(PROJECT_ROOT_PATH, "resources/english_grammar_book_for_students.pdf"), 'rb') as pdf:
    reader = PyPDF2.PdfReader(pdf)

    print(reader.pdf_header)
    print(reader.pages)
    print(reader.pages[5].extract_text())
    assert 'SERIES CONSULTANT' in reader.pages[2].extract_text()
    print(reader.metadata)
    print(reader.page_mode)
    print(reader.page_layout)
    print(os.path.join(PROJECT_ROOT_PATH, "resources/english_grammar_book_for_students.pdf"))