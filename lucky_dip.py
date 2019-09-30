import sys
import numpy as np
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


def expected_value(values):
    result = 0.0
    for k in range(len(values)):
        result += values[k]
    return result/len(values)


num_tests = int(input())

for i in range(num_tests):
    num_balls, num_dips = [int(j) for j in input().split()]
    ball_bag = [int(j) for j in input().split()]
    print("Case #{0}: {1}".format(i + 1, 1))
