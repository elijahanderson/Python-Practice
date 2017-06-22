print('Please enter your name:')
name = input()
print('Please enter your age:')
age = int(input())

if name == 'Alice' :
      print('Hi, Alice.')
elif age < 12:
      print('You are not Alice.')
elif age > 2000:
      print('Unlike you, Alice is not a vampire.')
elif age > 100:
      print('Too old to be Alice...')
else:
      print('Where is Alice?')
