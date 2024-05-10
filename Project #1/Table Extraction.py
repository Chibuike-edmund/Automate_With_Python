from PyPDF2 import PdfReader
import camelot

pdf = PdfReader('/workspaces/Automate_With_Python/Project #1/foo.pdf')

tables = camelot.read_pdf('/workspaces/Automate_With_Python/Project #1/foo.pdf', pages='1')

print(tables)


tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')