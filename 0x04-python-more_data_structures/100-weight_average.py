#!/usr/bin/python3

# This function returns the weighted average of all
# integers tuple (<score>, <weight>)

def weight_average(my_list=[]):
    if my_list:
        total_score, weight, average = 0, 0, 0

        for i in my_list:
            total_score += i[0] * i[1]
            weight += i[1]

        average = total_score / weight
        return average
    else:
        return 0
