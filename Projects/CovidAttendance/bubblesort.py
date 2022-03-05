import csv
import os
from time import time
# with open('Attendance Record.csv','r') as file:
#     csv_reader = csv.reader(file)
#     names_list = []
#     for line in csv_reader:
#         # gets one large list of names
#         names_list.append(line[0].strip('[]\''))

# quick bubble sort implementation


def bubble_sort(list_sort):
    for value in range(len(list_sort)):
        for item in range(len(list_sort)-1):
            #print(list_sort)
            if list_sort[item] > list_sort[item+1]:
                list_sort[item], list_sort[item+1] = list_sort[item+1] ,list_sort[item]

    return list_sort
# sorted = bubble_sort(names_list)

# t0 = time()

# Sorts file using bubble search algrothim
#with open('Attendance Record.csv','r') as file:
#    csv_reader = csv.DictReader(file)
#    Attendance = ['Name', 'Day\'s']
#    # goes through sorted list
#    for index, item in enumerate(sorted):
#        # creates a key selecting a item from  list
#        located = f'[\'{sorted[index]}\']'
#        # finds corresponding file value
#        for line in csv_reader:
#            if line['Name'] == located:
#                print('winner winner chicken dinner', line)
#                # oragines file use a a secondary file

#                with open('Organise Attendance Record.csv', 'a', newline='') as second_file:
#                    csv_writer = csv.DictWriter(second_file, fieldnames=Attendance)
#                    fileEmpty = os.stat('Attendance Record.csv').st_size == 0  # if file is empty write header

#                    if fileEmpty:
#                        dict_writer.writeheader()
#                    else:
#                        csv_writer.writerow(line)
#                break

#            else:
#                print('non non', line['Name'], located)


#        file.seek(0)


#t1 = time()
#print(f'time taken for execution {t1-t0}')

# rewrites orignal file
# with open('Organise Attendance Record.csv', 'r') as file:
#     csv_reader = csv.DictReader(file)
#     Attendance = ['Name', 'Day\'s']

#     with open('Attendance Record.csv', 'w', newline='') as second_file:
#         csv_writer = csv.DictWriter(second_file, Attendance)
#         csv_writer.writeheader()
#         for line in csv_reader:
#             csv_writer.writerow(line)
