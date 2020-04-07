#********************************************************************************
#** Nick Coombe 2020/03/14 ***
#** Lab 9 Part 3 ***
#** ***
#** Part 3 of Lab 9 ***
#** Create a function that finds a value in a list ***
#** ***
#********************************************************************************

# Finds the given key in the list
# INPUTS
#   - list (array)
#   - key (int)
# OUTPUT
#   - the index values (print)
#   - NO RETURN
def find(list, key):
    for i in range(len(list)):
        if list[i] == key:
            print("Found", key, "at position", i)

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
 
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)