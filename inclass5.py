import pprint

strang = input('Please enter a string: ')

print('Characters that occur in the string: ')

count = {}
for i in strang :
      count.setdefault(i, 0)
      count[i] += 1

pprint.pprint(count)
      
