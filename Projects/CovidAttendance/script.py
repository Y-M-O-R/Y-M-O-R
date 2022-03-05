import csv
import random




def binary_search(sequence_list, item):
    start = 0
    end = len(sequence_list) - 1

    while start <= end:
        midpoint = start + (end - start) // 2
        midpoint_value = sequence_list[midpoint]

        print(sequence_list[midpoint-1])
        #print(sequence_list[midpoint])
        print(sequence_list[midpoint+1])

        if midpoint_value == item:
            return midpoint

        elif midpoint_value > item:
            end = midpoint - 1

        else:
            start = midpoint + 1

    return None
a=[1,2,4,5,6,43,232,1311]
binary_search(a,1)