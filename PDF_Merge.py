from PyPDF2 import PdfFileMerger
import tkinter as tk


def pdf_merger():
    pdfs = ['pdf1.pdf', 'pdf2.pdf']
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("result.pdf")
    merger.close


def start_gui():
    main_window = tk.Tk()
    main_window.title("PDF Merger")
    button = tk.Button(main_window, text='Stop', width=25, command=main_window.destroy)
    button.pack()
    main_window.mainloop()


if __name__ == "__main__":
    start_gui()
