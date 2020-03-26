#********************************************************************************
#** Nick Coombe - March 09, 2020 ***
#** Lab 6 Back to Looping ***
#** ***
#** Prints a box at requested size ***
#** ***
#********************************************************************************

# Ask for box size
n = int(input("n: "))

# Print top
for x in range(n*2):
    print("o", end="")
print()

# Print walls
for x in range(n-2):
    print("o", end="")
    for y in range(n*2-2):
        print(" ", end="")
    print("o")

# Print bottom 
for x in range(n*2):
    print("o", end="")
print()
