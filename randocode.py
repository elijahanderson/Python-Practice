def isPalindrome(strang) :

      for i in range(1,len(strang)+1) :

            if strang[i-1] != strang[-i] :
                  print('This string is not a palindrome.')
                  return False

      return True
      
##########################################
      
print('Enter a string: ', end='')
strang = input()

if isPalindrome(strang) :
      print('This string is a palindrome.')
