import numpy as np
# Problem
# No Nine is a counting game that you can try when you are bored.
# In this game, you are only allowed to say numbers that are legal.
# A number is legal if and only if all of the following are true:
#
# * it is a natural number (i.e. in the set {1, 2, 3...})
# * it does not contain the digit 9 anywhere in its base 10 representation
# * it is not divisible by 9
# For example, the numbers 16 and 17 are legal. The numbers 18, 19, 17.2, and -17 are not legal.
#
# On the first turn of the game, you choose and say a legal number F.
# On each subsequent turn, you say the next legal number.
# For example, if you played a game with F = 16, you would say 16, 17, 20, 21, and so on.
#
# Alice is very good at this game and never makes mistakes.
# She remembers that she played a game in which the first number was F and the last number was L
# (when she got tired of the game and stopped), and she wonders how many turns were in the game in total
# (that is, how many numbers she said).


def check_legality(num):
    # Results array for which cases fail
    results = []
    # Check for natural
    if num <= 0 or not isinstance(num, int):
        results.append(1)
    # Check for 9 in base 10
    num_str = str(num)
    digits = []
    for j in range(len(num_str)):
        if num_str[j] == '9':
            digits.append(j)
    if len(digits) > 1:
        results.append(digits)
    # Check for divisible by 9
    if num % 9 == 0:
        results.append(1)
    return results


def escape_9_digit(num):
    # Find the first 9 in the number
    # EG - 59291 -> the 9 in 59 is the first 9
    num_str = str(num)
    for j in range(len(num_str)):
        if num_str[j] == '9':
            first_nine = j
            if first_nine > 0:
                new_num = list(str(num))
                new_num[j-1] = str(int(new_num[j-1]) + 1)
                for k in range(j, len(new_num)):
                    new_num[k] = "0"
                new_num = convert_list_int(new_num)
                return new_num - num, new_num
            else:
                return 10**len(num_str) - num, 10**len(num_str)
    return 0, num


def convert_list_int(list_in):
    result_list = list(map(int, list_in))
    result = 0
    for j in range(len(result_list)):
        result += result_list[j] * 10 ** (len(result_list) - j - 1)
    return result


def main():
    num_tests = int(input())
    for test in range(num_tests):
        first, last = [int(num) for num in input().split()]
        current = first
        how_many = 0
        while current <= last:
            legality = check_legality(current)
            if len(legality) == 0:
                how_many += 1
            current += 1
        print("Case #{0}: {1}".format(test + 1, how_many))
    return

print(str(escape_9_digit(9291)))
# main()
