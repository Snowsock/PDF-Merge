import os.path
from PyPDF2 import PdfFileMerger as PfM


def pdf_merger(dir):
    pdfs = check_for_file(dir)
    merger = PfM()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(f"{dir}.pdf")
    merger.close


def check_for_file(directory_of_pdf):
    file_list = []
    i = 0
    while True:
        i = i +1
        if os.path.isfile(f'{directory_of_pdf}/{i}.pdf'):
            file_list.append(f'{directory_of_pdf}/{i}.pdf')
        else:
            return file_list


def main():
    listed_directories = os.walk('.', False)
    dirs = [x[0] for x in listed_directories]
    for directory in dirs:
        if directory == ".":
            continue
        pdf_merger(f'{directory}')


if __name__ == '__main__':
    main()
