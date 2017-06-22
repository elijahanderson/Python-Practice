import sys

print('Enter an integer:')
num = int(input())

sum = 0
if num < 1:
      print(0)
else :
      for i in range(1,num+1) :
            sum = sum + i

print(sum)

sys.exit()
      
