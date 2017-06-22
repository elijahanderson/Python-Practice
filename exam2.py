# exam2.py - Once completed, the program should do the following:
#   1. Prompt the user to enter the name of a PDF file
#   2. Prompt the user to enter a term to search for
#   3. Go through the pages of the PDF file the user entered
#   4. Write out a new PDF document that contains only the pages
#      from the original file that contain the search term the
#      user specified. The new file should be named 'output.pdf'.
#
#  For example, if the user enters 'meetingminutes.pdf' as the file,
#    and 'Schools' as the search term, the file 'output.pdf' should
#    contain all the pages from 'meetingminutes.pdf' that have the
#    word 'Schools' on it. (In this case, there should be 6 pages).
#
#  Fill in the code that you need to complete this program.
#

import PyPDF2, re, os, sys

print('Enter the name of a file (make sure to end it with \'.pdf\'): ')
file = open(input(), 'rb')
pdf = PyPDF2.PdfFileReader(file)

if pdf.isEncrypted :
      print('This PDF is encrypted; error.')
      sys.exit()

output = open('output.pdf', 'wb')
pdfOut = PyPDF2.PdfFileWriter()

#strang = input('Enter the search term: ')
#reg_formatted = '^' + strang + '$'

print('Enter the search term: ', end='')
reg_formatted = input()
msg = re.compile(reg_formatted)

for i in range(pdf.numPages) :
      print('\nSearching page ' + str(i) + '...',end='')
      currPage = pdf.getPage(i)
      text = currPage.extractText()
      
      match = msg.search(text)

      if match is not None:
            pdfOut.addPage(currPage)
            print('Found a match!')

pdfOut.write(output)

file.close()
output.close
