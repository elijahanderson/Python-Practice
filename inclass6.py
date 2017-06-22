import re

message = input('Write a sentence that contains a phone number: ')
phone = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = phone.search(message)

if match == None :
      print('No phone number found')

else :
      print('Phone number: ' + match.group())
      
