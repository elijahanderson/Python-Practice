print('Enter a number of strings, and an empty one to quit.')

theFile = open('D:\\output.txt', 'w')

while True :
      line = input()
      

      if line == '' :
            break
      theFile.write(line)

theFile.close()
