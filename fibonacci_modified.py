"""
    Given terms ti and ti+1, ti+2 is computed using the following relation:
        ti+2 = ti + (ti+1)^2

    Given three integers, , , and , compute and print term  of a modified Fibonacci sequence.

Note: The value of  may far exceed the range of a -bit integer. Many submission languages have libraries that can handle such large results but, for those that don't (e.g., C++), you will need to be more creative in your solution to compensate for the limitations of your chosen submission language.

Input Format

A single line of three space-separated integers describing the respective values of , , and .

Constraints

 may far exceed the range of a -bit integer.
Output Format

Print a single integer denoting the value of term  in the modified Fibonacci sequence where the first two terms are  and .

Sample Input

0 1 5
Sample Output

5
"""

def fibonacciModified(t1, t2, n):
    fib_arr = [t1, t2]
    for i in range(n - 2):
        fib_arr.append(fib_arr[i] + pow(fib_arr[i + 1], 2))
    return fib_arr[len(fib_arr) - 1]

if __name__ == "__main__":
    t1, t2, n = input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print(result)
