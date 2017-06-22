# No. 15: Reverse Word Order (three methods)

def reverse(oSentence) :

      words = oSentence.split()
      nSentence = []

      for i in range(len(words)-1,-1,-1) :
            nSentence.append(words[i])
            
      fSentence = ' '.join(nSentence)
      return fSentence

def oneLineReverse(oSentence) :

      return ' '.join(oSentence.split()[::-1])

def withReverseFunction(oSentence) :

      nSentence = oSentence.split()
      nSentence.reverse()
      return ' '.join(nSentence)

sentence = input('Enter a sentence: ')

print(reverse(sentence))
print(oneLineReverse(sentence))
print(withReverseFunction(sentence))
