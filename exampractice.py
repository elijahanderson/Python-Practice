import os, sys

theFile = open('D:\\Programming In Python WT\\output.txt', 'w')

while True :
      strang = '\n' + input('Enter a string: ')
      
      if strang == '\n' :
            break
      
      else :
            print(strang)
            theFile.write(strang)
            
print('Done!')
theFile.close()
