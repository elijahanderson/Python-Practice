import sys

list = []

print('Please enter a squence of integers. Enter 0 to finish.')

while True:
      num = int(input())

      if num != 0 :
            list.append(num)
            
      else :
            list.append(0)
            break
      
list.remove(0)      
print('The numbers you entered are:')
print(str(list))

sum = 0;

for i in range(len(list)) :
      sum += list[i]

print('The sum of the numbers you entered is ' + str(sum))
      

