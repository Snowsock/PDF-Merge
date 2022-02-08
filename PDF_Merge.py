import os.path
from PyPDF2 import PdfFileMerger as PfM


def pdf_merger(dir):
    pdfs = check_for_file(dir)
    print(pdfs)
    merger = PfM()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(f"{dir}.pdf")
    merger.close


def check_for_file(directory_of_pdf):
    file_list = []
    i = 0
    run = True
    while run == True:
        i = i +1
        print(i)
        if os.path.isfile(f'{directory_of_pdf}/{i}.pdf'):
            print(f'{directory_of_pdf}/{i}.pdf')
            file_list.append(f'{directory_of_pdf}/{i}.pdf')
        else:
            run = False
            return file_list


if __name__ == '__main__':
    listed_directories = os.walk('.', False)
    dirs = [x[0] for x in listed_directories]
    for directory in dirs:
        if directory == ".":
            continue
        pdf_merger(f'{directory}')
