#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = (0, 0)
    if not my_list:
        return (0)
    else:
        for i in my_list:
            sum = (sum[0] + (i[0] * i[1]), sum[1] + i[1])
    weighted_average = sum[0] / sum[1]
    return weighted_average
