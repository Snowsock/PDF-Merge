from PyPDF2 import PdfFileMerger

def pdf_merger():
    pdfs = ['pdf1.pdf', 'pdf2.pdf']
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("result.pdf")
    merger.close


