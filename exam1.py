# exam.py - A program to test your programming for exam #1.
# This program is basically a set of functions that do various
# separate things, not one big program.

# The comments with TODO in them below are problems you need to
# finish.

# You might want to go to the bottom to look at the program code
# to see what the program expects the functions to do.



# isEven( n )
# Returns True if n is even, and False if n is odd.
def isEven (n) :

      if n % 2 == 0 :
            return True
      return False

# sumUpEvens( n )
# Returns the sum of all even numbers between 1 and n inclusive.
def sumUpEvens(n) :

      sum = 0
      
      for i in range(1,n+1) :

            if isEven(i) :
                  sum += i

      return sum

# makeList( s, n )
# Returns a list consisting of n copies of s, where s is converted
# to all capital letters.
def makeList(s, n) :

      s = s.upper()
      theList = [s]
      theList *= n
      return theList
      
      



# fillDictionary( dict )
# Prompts the user to enter a name of a person, then the name of
# one of that person's pets. Then, add that pair to the dictionary
# (the name is the key and the pet name is the value). Repeat so
# that five name-pet pairs are added to the dictionary.
def fillDictionary(dict) :

      for i in range(5) :
            person = input('Enter the name of a person: ')
            pet = input('Enter the name of that person\'s pet (note: a person cannot have more than one pet): ')
            dict.setdefault(person, pet)



# Beginning of main program

print( 'Enter a positive integer:' )
number = int( input( ) )

if number < 0 :
      print('That number is negative. The absolute value of it will be entered instead.')
      number *= -1


if ( isEven( number ) ) :
    print( str( number ) + ' is an even number.' )
else :
    print( str( number ) + ' is an odd number.' )

print( 'The sum of all even numbers from 1 to ' + str( number ) + ':' )
print( sumUpEvens( number ) )

print( 'Please enter your name:' )
name = input( )

nameList = makeList( name, number )

print( 'Here is your name in all capitals a number of times:' )
print( nameList )

namesAndPets = { }

fillDictionary( namesAndPets )

print( 'Here is the information about names and pets.' )
print( namesAndPets )
