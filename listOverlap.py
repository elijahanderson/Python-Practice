import random

list1 = []
list2 = []

for i in range(0,random.randint(1,20)) :
      list1.append(random.randint(0,100))

for i in range(0,random.randint(1,20)) :
      list2.append(random.randint(0,100))

list1.sort()
list2.sort()
print(str(list1))
print(str(list2))
greater = list1
lesser = list2

if len(list2) > len(list1) :
      greater = list2
      lesser = list1

finalList = []

for i in range(len(lesser)) :
      n = lesser[i]

      for j in range(len(greater)) :
            if n == greater[j] :
                  finalList.append(n)
                  break

print(str(finalList))


      
