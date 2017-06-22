import random

r = random.randint(1,100)
guessCount = 0

print('The computer has picked a number from 1 to 100./nYou have 9 guesses.')

while True :
      
      if guessCount == 9 :
            print('You ran out of guesses!')
            break

      guess = input('Guess the number: ')

      if guess == 'exit' :
            break
      
      elif int(guess) == r :
            guessCount += 1
            print("That's correct!")
            break
      
      elif int(guess) > r :
            guessCount += 1
            print("Too high...")
      else :
            guessCount += 1
            print("Too low...")

print('No. of attempts: ' + str(guessCount))
