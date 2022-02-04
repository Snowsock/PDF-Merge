from PyPDF2 import PdfFileMerger
import tkinter


def pdf_merger():
    pdfs = ['pdf1.pdf', 'pdf2.pdf']
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("result.pdf")
    merger.close


def start_gui():
    main_window = tkinter.Tk()
    main_window.title("PDF Merger")


if __name__ == "__main__":
    start_gui()