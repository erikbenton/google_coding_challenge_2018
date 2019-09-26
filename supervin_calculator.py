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
        return True
    return False


def update_test_number(test_number, change):
    test_number += change
    new_str = str(test_number)
    new_num_digits = len(new_str)
    return test_number, new_str, new_num_digits


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
    if quick_check(i, is_negative, num_digits):
        continue
    # Number of clicks needed
    num_clicks = 0
    # Start index
    start = 0
    if is_negative:
        start = 1
    # Go through each digit and check if non-odd
    # for j in range(start, num_digits + start):
    j = start
    while j < num_digits + start:
        current_digit = int(str_displayed[j])
        # See if current digit is odd
        if current_digit % 2 != 0:
            # Get the "magnitude" and trailing number
            num_trailing_digits = len(str_displayed[j+1:])
            magnitude = 10**num_trailing_digits
            trailing_num = int(str_displayed[j+1:])
            difference = magnitude - trailing_num
            if difference > trailing_num:
                # Click down (trailing_num + 1) times: 123 -> 123 - (23 + 1) = 99
                num_clicks += (trailing_num + 1)
                prev_str = str_displayed
                num_displayed, str_displayed, num_digits = update_test_number(num_displayed, -(trailing_num + 1))
                j += len(str_displayed) - len(prev_str)
            else:
                # Click up difference times
                num_clicks += difference
                num_displayed, str_displayed, num_digits = update_test_number(num_displayed, difference)
        # Update j
        j += 1
    print("Case #{0}: {1}".format(i + 1, num_clicks))

