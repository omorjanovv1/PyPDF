"""
PDF ЭКСТРАКТЕР ДАННЫХ

"""

import PyPDF2 as p2

PDFfile = open("Паспорт.pdf", "rb")
pdfread = p2.PdfFileReader(PDFfile)

"""Извлечь весь PDF-файл"""
# x = pdfread.getPage(1)
# print(x.extractText())
# print(pdfread.getIsEncrypted())
# print(pdfread.getDocumentInfo())
# print(pdfread.getNumPages())


"""Extract Entire PDF"""
i = 0
while i<pdfread.getNumPages():
    pageinfo = pdfread.getPage(i)
    print(pageinfo.extractText())
    i = i + 1