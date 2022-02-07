import os
from PyPDF2 import PdfFileMerger as PfM


def pdf_merger(dir):
    pdfs = [f'{dir}/1.pdf', f'{dir}/2.pdf']
    merger = PfM()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(f"{dir}.pdf")
    merger.close


if __name__ == '__main__':
    listed_directories = os.walk('.', False)
    dirs = [x[0] for x in listed_directories]
    for directory in dirs:
        if directory == ".":
            continue
        pdf_merger(f'{directory}')
