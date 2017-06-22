# No. 16: Password Generator
import random

def generateWeak() :
      
      result = ''
      
      for i in range(0,9,1) :
            result += random.choice('abcdefghijklmnopqrstuvwxysABCDEFGHIJKLMNOPQRSTUVWXYZ')

      return result
      
def generateStrong() :

      result = ''
      
      for i in range(0,29,1) :
            result += random.choice('abcdefghijklmnopqrstuvwxysABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*<>?')

      return result

howStrong = input('Would you like your password to be strong or weak? ')

if howStrong == 'strong' or howStrong == 'Strong':
      print(str(generateStrong()))
else : print(str(generateWeak()))
