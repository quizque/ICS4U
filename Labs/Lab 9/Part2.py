#********************************************************************************
#** Nick Coombe 2020/03/14 ***
#** Lab 9 Part 2 ***
#** ***
#** Part 2 of Lab 9 ***
#** Create a function that prints a box ***
#** ***
#********************************************************************************

# Prints a box of given width and height
# INPUTS
#   - height (int)
#   - width (int)
# OUTPUT
#   - a box (print)
#   - NO RETURN
def box(height, width):
    for x in range(height):
        for y in range(width):
            print("*", end="")
        print("")

box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across