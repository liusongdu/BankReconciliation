# -*- coding: utf-8 -*-
# pip install pdfminer

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

# Open a PDF file.
fp = open('e.pdf', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser)
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# Create a PDF device object.
device = PDFDevice(rsrcmgr)
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)


def readPDF(pdfFile):
    parser = PDFParser(pdfFile)
    document = PDFDocument(parser)
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()  #
    laparams = LAParams()  #
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    # process_pdf(rsrcmgr, device, pdfFile)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = open('e.pdf', 'rb')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()