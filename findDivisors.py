print('Please enter a number: ', end ='')
n = int(input())

for i in range(1,n+1) :
      if (n % i == 0) & (i != n) :
            print(str(i) + ', ', end='')
            
      elif i == n :
            print(str(i))
                  
