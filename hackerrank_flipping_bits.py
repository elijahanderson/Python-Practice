"""You will be given a list of 32 bits unsigned integers. You are required to output the list of the
 unsigned integers you get by flipping bits in its binary representation (i.e. unset bits must be set, and set bits must be unset).

Input Format

The first line of the input contains the list size , which is followed by  lines, each line having an
 integer from the list.

Constraints



Output Format

Output one line per element from the list with the requested result.

Sample Input

3
2147483647
1
0
Sample Output

2147483648
4294967294
4294967295
Explanation

Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001 and doing the flipping we get
11111111111111111111111111111110 which in turn is 4294967294."""

def to_bits(nums):
    bits = list()
    for i in range(len(nums)):
        num = int(nums[i])
        if num == 0:
            bits.append('00000000000000000000000000000000')
            break
        bit_string = ''
        while num != 0:
            remainder = int(num % 2)
            bit_string = bit_string + str(remainder)
            num = int(num / 2)
        if len(bit_string) != 32:
            count = 32 - len(bit_string)
            while count != 0:
                bit_string = '0' + bit_string
                count -= 1
        bits.append(bit_string)
    return bits


def reverse_bits(bits):
    reversed_bits = []
    for bit in bits:

        bit = list(bit)
        new_bit = []
        for ele in bit:
            if ele == '1':
                new_bit.append('0')
            elif ele == '0':
                new_bit.append('1')
        new_bit = ''.join(new_bit)
        reversed_bits.append(new_bit)
    return reversed_bits


def to_deci(reversed_bits):
    decimals = []
    for bit in reversed_bits:
        decimal = 0
        for i in range(len(bit)):
            if bit[i] == '1':
                decimal += 2 ** ((len(bit) - 1) - i)
        decimals.append(decimal)
    return decimals


list_size = int(input())
nums = []
if list_size >= 1 and list_size <= 100:
    for i in range(list_size):
        num = input()
        if int(num) >= 0 and int(num) <= 2 ** 32:
            nums.append(num)
        else:
            print('Number entered is too small or large')
    bits = to_bits(nums)
    reversed_bits = reverse_bits(bits)
    flipped_deci = to_deci(reversed_bits)
    for deci in flipped_deci:
        print(int(deci))
else:
    print('List size too small or large')