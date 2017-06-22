#Combines all PDF files in the working directory into a single file
#
#
import PyPDF2, os

print('Searching current directory for PDF files...')

allFiles = os.listdir()
pdfFiles = []

for file in allFiles :

      if file.endswith('.pdf') :
            pdfFiles.append(file)

print('Found these pdf files: ', end='')
print(pdfFiles)

output = open('output.pdf', 'wb')
pdfOut = PyPDF2.PdfFileWriter()

for file in pdfFiles :
      print('Working with file: ' + file)
      infile = open(file, 'rb')
      inPDF = PyPDF2.PdfFileReader(infile)

      if not inPDF.isEncrypted :
            
            for i in range( inPDF.numPages) :
                  page = inPDF.getPage(i)
                  pdfOut.addPage( page )

      else :
            print(file + ' is encrypted.')

pdfOut.write(output)

output.close()
infile.close()
