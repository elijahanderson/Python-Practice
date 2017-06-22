# No. 14: Removing duplicates in a list:

def removeDuplicates1(oList) :

      nList = []
      
      for i in range(len(oList)) :

            if oList[i] not in nList :
                  nList.append(oList[i])
                
      return str(nList)

def removeDuplicates2(oList) :

      nSet = set(oList)
      return nSet

x = [1,1,2,2,3,3,4,4,1]
print(removeDuplicates2(x))
print(removeDuplicates1(x))
