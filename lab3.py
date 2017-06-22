import sys, numpy as np, matplotlib.pyplot as plt

def getNumbers(i) :
      
      NUMBER = i+1
      theList = []
      print('Please enter ' + str(i) + ' numbers.')
      
      while i > 0 :
            num = int(input('Number ' + str(NUMBER-i) + ': '))
            theList.append(num)
            i -= 1
      
      print('Here are the values you entered: ' + str(theList))

      arr = np.array([theList[i] for i in range(len(theList))])
      smallCount = 0
      largeCount = 0
      smallest = np.amin(arr)
      largest = np.amax(arr)
      
      for i in range(len(arr)) :
            if arr[i] == smallest :
                  smallCount += 1

      for i in range(len(arr)) :
            if arr[i] == largest :
                  largeCount += 1
      
      print('The smallest item in the list is ' + str(smallest) + ', and it occurs ' + str(smallCount) + ' times.')
      print('The largest item in the list is ' + str(largest) + ', and it occurs ' + str(largeCount) + ' times.')
      print('The mean of the items in the list is ' + str(np.mean(arr)) + '.')
      print('The median of the items in the list is ' + str(np.median(arr)) + '.')
      print('The range of the items in the list is ' + str(np.amax(arr)-np.amin(arr)) + '.')

      plt.plot(arr)
      plt.show()

#-------Main-------

print('How many numbers would you like to enter?')
i = int(input())
getNumbers(i)
      
