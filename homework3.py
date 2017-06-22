import os
import sys
import re

print('Enter a file name: ', end='')
msg = input()

if not os.path.isfile(msg) :
      print('This file does not exist.')
      sys.exit()

theFile = open(msg)
strang = input('Enter a string: ')
reg_formatted = "^" + strang + "$"
regEx = re.compile(reg_formatted)
lines = theFile.readlines()
matchCount = 0

for i in range(len(lines)) :
      words = lines[i].split(' ')
      
      for j in range(len(words)) :
            match = regEx.search(words[j])

            if match is not None :
                  matchCount += 1
            
print('Number of times \"' + strang + '\" occurs: ' + str(matchCount))
            
