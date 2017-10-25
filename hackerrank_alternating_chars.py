"""
ALTERNATING CHARACTERS

You are given a string containing characters  and  only, your task is to change it into a string such that every two consecutive characters are different. To do this, you are allowed to delete one or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, string  should be changed to  by deleting one character .

Input Format

The first line contains an integer , i.e. the number of test cases.
The next  lines contain a string .

Constraints

Output Format

For each test case, print the minimum number of deletions required in a new line.

Sample Input

5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Sample Output

3
4
0
0
4

"""

def alternatingCharacters(s):
    compare_char = s[0]
    deletions = 0
    for char in s[1:] :
        if char == compare_char :
            deletions += 1
        compare_char = char
    return deletions

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)