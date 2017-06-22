#Printing the Fibonacci Sequence
#Eli Anderson

def loop(numTimes) :

      curr = 1
      prev1 = 0
      prev2 = 0
              
      for i in range(int(numTimes)) :
            print(str(curr))
            prev2 = prev1
            prev1 = curr
            curr = prev1 + prev2

print('How many Fibonacci numbers would you like to generate?')
i = input()
loop(i)
