#Lab 2 - 12.1.2017
import os

#prints number of words in the file
def printWords() :

      wordCount = 0
      
      for i in range(numLines) :
            words = lines[i].split()
            wordCount += len(words)
            
      print('There are ' + str(wordCount) + ' words in this file.')

#prints number of unique words in the file (repeated words not included)
def printUniqueWords() :

      wordCount = 0
      dict = {}

      for i in range(numLines) :
            words = lines[i].split()

            for j in range(len(words)) :
                  
                  if words[j] not in dict.keys() :
                        dict.setdefault(words[j] , 0)

      print('There are ' + str(len(dict)) + ' unique words in this file.')

#prints number of names in the file
def printNames() :

      nameCount = 0

      for i in range(numLines) :
            words = lines[i].split()

            for j in range(len(words)) :

                  if words[j].istitle() :
                        nameCount += 1

      print('There are ' + str(nameCount) + ' names in that file.')
      
print('Welcome to my program!')

print('Please enter a file to read: ')
fileString = input()
theFile = open(fileString)

lines = theFile.readlines()
numLines = len(lines)

print('There are ' + str(numLines) + ' lines in this file.')

printWords()
printUniqueWords()
printNames()

print('Done!')
