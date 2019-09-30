import sys
import numpy as np
import random as rand
# PROBLEM
# You are participating in the Grand Kickstart Lucky Dip with many fantastic
# and amazing prizes (and some not so good ones)!
#
# In this Lucky Dip, there is a bag with N items. The i-th item in the bag has value Vi.
# You will put your hand into the bag and draw one item at random;
# all items in the bag have an equal probability of being chosen.
# The organizers want contestants to feel that they have some element of choice,
# so after you draw an item, you can either keep it, or "redip" by returning it to the bag and drawing again.
# (Note that the returned item is now just as likely to be chosen as any of the other items in the bag.)
# You may only redip a maximum of K times. If you use K redips,
# you must keep the item that you draw on your (K + 1)-th draw.
#
# If you play optimally to maximize the value of the item you will end the game with,
# what is the expected value of that item?


def find_expected_value(values, dips_remaining):
    expected_value = 0
    for l in range(len(values)):
        expected_value += values[l]
    expected_value /= len(values)
    # expected_value = float(np.mean(values))
    if dips_remaining <= 0:
        return expected_value
    for l in range(len(values)):
        if values[l] < expected_value:
            values[l] = expected_value
    expected_value = find_expected_value(values, dips_remaining-1)
    return expected_value


# Starts with the major inputs and
# sets up for recursive calculations
def main():
    num_tests = int(input())

    for i in range(num_tests):
        num_balls, num_dips = [int(j) for j in input().split()]
        ball_bag = [int(j) for j in input().split()]
        expected = find_expected_value(ball_bag, num_dips)
        print("Case #{0}: {1}".format(i + 1, expected))
    return


def tester():
    tests = 1000
    vi = []
    for i in range(2*10**4):
        vi.append(rand.randint(0, 10**9))

    k = rand.randint(0, 5*10**4)
    expected = find_expected_value(vi, k)
    print("Case #{0}: {1}".format(i + 1, expected))

# main()
tester()