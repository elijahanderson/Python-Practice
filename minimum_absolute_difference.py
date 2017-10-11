"""Consider an array of integers, . We define the absolute difference between two elements,
and  (where ), to be the absolute value of .

Given an array of  integers, find and print the minimum absolute difference between any two
elements in the array.

Input Format

The first line contains a single integer denoting  (the number of integers).
The second line contains  space-separated integers describing the respective values of .

Constraints

Output Format

Print the minimum absolute difference between any two elements in the array.

Sample Input 0

3
3 -7 0
Sample Output 0

3
Explanation 0

With  integers in our array, we have three possible pairs: , , and . The absolute values
of the differences between these pairs are as follows:

Notice that if we were to switch the order of the numbers in these pairs, the resulting
absolute values would still be the same. The smallest of these possible absolute differences is ,
 so we print  as our answer."""

import sys

def minimumAbsoluteDifference(n, arr):
    pairs = {}
    count = 0
    for i in range(n) :
        for j in range(n) :
            if arr[i] != arr[j] :
                val = abs(arr[i] - arr[j])
                if val not in list(pairs.values()) :
                    pairs[count] = val
            count += 1
    min = pairs.get(1)
    for key in pairs :
        if pairs.get(key) < min :
            min = pairs.get(key)
    return min

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    if n == len(arr) :
        result = minimumAbsoluteDifference(n, arr)
        print(result)
    else :
        sys.exit()
