#********************************************************************************
#** Nick Coombe 2020/03/14 ***
#** Lab 9 Part 4 ***
#** ***
#** Part 4 of Lab 9 ***
#** Create a large random list and proform functions on it ***
#** ***
#********************************************************************************

import random

# Functions -------------------------------------------------------#

# Returns a random array (values 1-6) of given length
# INPUTS
#   - length (int)
# OUTPUT
#   - random array (list)
def create_list(length):
    tmp = []
    for x in range(length):
        tmp.append(random.randint(1,6))
    return tmp

my_list = create_list(5)
print(my_list)

# Finds the amount of times the key in the list
# INPUTS
#   - list (array)
#   - key (int)
# OUTPUT
#   - # of times key is found (int)
def count_list(list, key):
    tmp = 0
    for i in range(len(list)):
        if list[i] == key:
            tmp += 1
    return tmp

count = count_list([1,2,3,3,3,4,2,1],3)
print(count)

# Returns the average of the passed list
# INPUTS
#   - list (list)
# OUTPUT
#   - average (int)
def average_list(list):
    tmp = 0
    for x in list:
        tmp += x
    return tmp / len(list)

avg = average_list([1,2,2,3])
print(avg)

# Main Program ----------------------------------------------------#

# Print formatting
print("\n###############\n")

# Create a list of 10000 random numbers valued (1->6)
large_list = create_list(10000)

# Print the totals of each number
print("1 is found " + str(count_list(large_list, 1)) + " times.")
print("2 is found " + str(count_list(large_list, 2)) + " times.")
print("3 is found " + str(count_list(large_list, 3)) + " times.")
print("4 is found " + str(count_list(large_list, 4)) + " times.")
print("5 is found " + str(count_list(large_list, 5)) + " times.")
print("6 is found " + str(count_list(large_list, 6)) + " times.")

# Print the average
print("The average of the list is " + str(average_list(large_list)) + ".")