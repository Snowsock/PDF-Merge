import os
import sys
from PyPDF2 import PdfFileMerger as PfM


def pdf_merger():
    pdfs = ['pdf1.pdf', 'pdf2.pdf']
    merger = PfM()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("result.pdf")
    merger.close


if __name__ == '__main__':
    listed_directories = os.walk('.', False)
    print([x[0] for x in listed_directories])
