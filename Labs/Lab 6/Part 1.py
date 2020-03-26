#********************************************************************************
#** Nick Coombe - March 09, 2020 ***
#** Lab 6 Back to Looping ***
#** ***
#** Prints a triangle in assending values ***
#** ***
#********************************************************************************

i = 10
# Count up to 10
for x in range(10):
    # Count from 0 -> x
    for y in range(x):
        print(str(i) + " ", end="")
        i += 1
    print()
