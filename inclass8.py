import PyPDF2

file = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(file)

print(str(pdfReader.numPages))

page = pdfReader.getPage(4)
print(page.extractText())

file = PyPDF2.PdfFileReader(open('encrypted.pdf','rb'))
pdfReader.isEncrypted
pdfReader.decrypt('rosebud')
page = pdfReader.getPage(4)
