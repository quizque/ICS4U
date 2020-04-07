#********************************************************************************
#** Nick Coombe 2020/03/14 ***
#** Lab 9 Part 1 ***
#** ***
#** Part 1 of Lab 9 ***
#** Create a function that returns the lowest value ***
#** ***
#********************************************************************************

# Calculate the minimum of three inputs
# INPUTS
#   - Number a (int)
#   - Number b (int)
#   - Number c (int)
# OUTPUT
#   - Minimum Number (int)
def min3(a, b ,c):
    tmp = c
    if tmp > b:
        tmp = b
    if tmp > a:
        tmp = a
    return tmp

print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))

# ASCII works due to it processing it as an int insted of a string
print(min3("Z", "B", "A"))