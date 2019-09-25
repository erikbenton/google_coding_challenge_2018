# PROBLEM
# Supervin has a unique calculator. This calculator only has a display, a plus button, and a minus button.
# Currently, the integer N is displayed on the calculator display.
# Pressing the plus button increases the current number displayed on the calculator display by 1.
# Similarly, pressing the minus button decreases the current number displayed on the calculator display by 1.
# The calculator does not display any leading zeros.
# IE, if 100 is displayed on the calculator display, pressing the minus button once causes the calculator to display 99.
# Supervin does not like odd digits, because he thinks they are "odd".
# Therefore, he wants to display an integer with only even digits in its decimal representation,
# using only the calculator buttons. Since the calculator is a bit old and the buttons are hard to press,
# he wants to use a minimal number of button presses.
# Please help Supervin to determine the minimum number of button presses to make the calculator
# display an integer with no odd digits.

# INPUT
# The first line of the input gives the number of test cases, T. T test cases follow.
# Each begins with one line containing an integer N: the integer initially displayed on Supervin's calculator.


def quick_check(test_num, is_it_negative, number_digits):
    # Quick check for already all non-odd numbers
    quick_check = True
    # Start index
    start = 0
    if is_it_negative:
        start = 1
    for j in range(start, start + number_digits):
        if int(str_displayed[j]) % 2 == 1:
            quick_check = False
            break
    if quick_check:
        print("Case #{0}: {1}".format(test_num + 1, "0"))
    return


# Number of test cases
num_cases = int(input())

# Go through each test case...
for i in range(num_cases):
    # Get the number displayed on the calc
    num_displayed = int(input())
    # Turn it into a string
    str_displayed = str(num_displayed)
    # Get the number of digits
    num_digits = len(str_displayed)
    # Check for negative entries
    is_negative = False
    if str_displayed[0] == '-':
        num_digits -= 1
        is_negative = True
    # Quick check for already all non-odd numbers
    quick_check(i, is_negative, num_digits)
