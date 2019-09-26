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


def quick_check(number_in, test_num, is_it_negative, number_digits):
    # Quick check for already all non-odd numbers
    quick_check = True
    # Start index
    start = 0
    if is_it_negative:
        start = 1
    for j in range(start, start + number_digits):
        if int(str(number_in)[j]) % 2 == 1:
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


def check_number_beauty(number_in):
    str_in = str(number_in)
    for i in range(len(str_in)):
        if str_in[i] == '-':
            continue
        if is_odd(int(str_in[i])):
            return False
    return True


def is_odd(number_in):
    return number_in % 2 != 0


def determine_direction(number_in):
    return


def brute_force(number_in, test_num, clicks_in=0):
    up_number = number_in
    down_number = number_in
    clicks = clicks_in
    beautiful_up = check_number_beauty(up_number)
    beautiful_down = check_number_beauty(down_number)
    while not beautiful_up and not beautiful_down:
        up_number += 1
        down_number -= 1
        clicks += 1
        beautiful_up = check_number_beauty(up_number)
        beautiful_down = check_number_beauty(down_number)
    print("Case #{0}: {1}".format(test_num + 1, clicks))
    return


def gentle_force():
    # Number of test cases
    num_cases = int(input())

    # Go through each test case...
    for i in range(num_cases):
        # Get the number displayed on the calc
        num_displayed = int(input())
        # Turn it into a string
        str_displayed = str(num_displayed)
        # Get the number of digits
        initial_num_digits = len(str_displayed)
        num_digits = initial_num_digits
        # Check for negative entries
        is_negative = False if num_displayed >= 0 else True
        # Quick check for already all non-odd numbers
        if quick_check(num_displayed, i, is_negative, num_digits):
            continue
        # Number of clicks needed
        num_clicks = 0
        # Start index
        index = 1 if is_negative else 0
        # Go through each digit and check if non-odd
        while index < num_digits:
            current_digit = int(str_displayed[index])
            # See if current digit is odd
            if is_odd(current_digit):
                # Get the "magnitude" and trailing number
                num_trailing_digits = len(str_displayed[index+1:])
                if num_trailing_digits > 0:
                    magnitude = 10 ** num_trailing_digits
                    trailing_num = int(str_displayed[index + 1:])
                else:
                    num_clicks += 1
                    print("Case #{0}: {1}".format(i + 1, num_clicks))
                    j += 1
                    continue
                    # magnitude = 10
                    # trailing_num = current_digit
                difference = magnitude - trailing_num
                which_direction = 1 if num_displayed > 0 else -1
                if difference > (which_direction * trailing_num):
                    if current_digit == 1:
                        offset = 12
                    else:
                        offset = 1
                    # Click down (trailing_num + 1) times: 123 -> 123 - (23 + 1) = 99
                    num_clicks += (trailing_num + offset)
                    prev_str = str_displayed
                    num_displayed, str_displayed, num_digits = update_test_number(num_displayed,
                                                                                  -which_direction * (trailing_num + offset))
                    index += len(str_displayed) - len(prev_str)
                else:
                    # Click up difference times
                    num_clicks += difference
                    num_displayed, str_displayed, num_digits = update_test_number(num_displayed,
                                                                                  which_direction * difference)
            # Update index
            index += 1
        print("Case #{0}: {1}".format(i + 1, num_clicks))
    return


def main():
    # Number of test cases
    num_cases = int(input())

    # Go through each test case...
    for i in range(num_cases):
        # Get the number displayed on the calc
        num_displayed = int(input())
        brute_force(num_displayed, i, 0)
    return


main()

