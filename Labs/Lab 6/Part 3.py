# Ask for size
n = int(input("n: "))

# Top half
for i in range(n):
    # Count up
    for x in range(n-i):
        print(1 + i*2 + 2*x,"", end="")
    #Spacing
    for x in range(i*2):
        print("  ", end="")
    #Count down
    for x in range(0,n-i):
        print((n*2-1)-x*2,"", end="")
    print()

# Bottom half
for i in range(n-1,-1,-1):
    # Count up
    for x in range(n-i):
        print(1 + i*2 + 2*x,"", end="")
    # Spacing
    for x in range(i*2):
        print("  ", end="")
    # Count down
    for x in range(0,n-i):
        print((n*2-1)-x*2,"", end="")
    print()
