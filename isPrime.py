#Determines whether or not n is prime
def isPrime(n) :

      for i in range(2,n) :

            if n % i == 0 :
                  return False

      return True



n = int(input('Enter a number: '))

if isPrime(n) :
      print(str(n) + ' is prime.')
else :
      print (str(n) + ' is not prime.')
