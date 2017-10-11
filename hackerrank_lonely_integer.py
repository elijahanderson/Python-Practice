"""Consider an array of  integers, , where all but one of the integers occur in pairs.
In other words, every element in  occurs exactly twice except for one unique element.

Given , find and print the unique element.

Input Format

The first line contains a single integer, , denoting the number of integers in the array.
The second line contains  space-separated integers describing the respective values in .

Constraints

It is guaranteed that  is an odd number.
, where .
Output Format

Print the unique number that occurs only once in  on a new line.

Sample Input 0

1
1
Sample Output 0

1
Explanation 0
The array only contains a single , so we print  as our answer.

Sample Input 1

3
1 1 2
Sample Output 1

2
Explanation 1
We have two 's and one . We print , because that's the only unique element in the array.

Sample Input 2

5
0 0 1 2 1
Sample Output 2

2
Explanation 2
We have two 's, two 's, and one . We print , because that's the only unique element
in the array."""
import sys

def lonelyinteger(a):
    pairs = {}
    for i in range(len(a)):
        val1 = a[i]
        if a[i] not in pairs.keys():
            pairs[a[i]] = 0
        for j in range(len(a)):
            val2 = a[j]
            if val1 == val2:
                pairs[a[i]] += 1
    for key, value in pairs.items():
        if value == 1:
            return key


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
if n == len(a):
    result = lonelyinteger(a)
    print(result)
else:
    sys.exit()
