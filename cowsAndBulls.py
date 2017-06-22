import random, re

#Convert int to list to for subscriptal comparison later on
def intToList(x) :
      
      num = [int(digit) for digit in str(x)]

      return num

r = random.randint(1111,9999)
num = intToList(r)

#Every number in a correct place is a cow. In the wrong place is a bull
cows = bulls = 0

while cows != 4 :
      
      guess = intToList(input('Input a 4-digit number: '))
      cows = bulls = 0
      
      for i in range(4) :

            if guess[i] == num[i] : 
                  cows += 1
            else : 
                  bulls += 1

      print(str(cows) + ' cows, ' + str(bulls) +' bulls')
      

