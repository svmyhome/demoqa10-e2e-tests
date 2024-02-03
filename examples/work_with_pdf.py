import os.path
import pypdf

os.chdir('../resources')
path = os.getcwd()
with open(os.path.join(path, "english_grammar_book_for_students.pdf"), 'rb') as pdf:
    reader = pypdf.PdfReader(pdf)

    print(reader.pdf_header)
    print(reader.pages)
    print(reader.pages[5].extract_text())
    assert 'SERIES CONSULTANT' in reader.pages[2].extract_text()
    print(reader.metadata)
    print(reader.page_mode)
    print(reader.page_layout)
    print(os.path.join(path, "resources/english_grammar_book_for_students.pdf"))
