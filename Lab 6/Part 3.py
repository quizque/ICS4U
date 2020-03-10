n = int(input("n: "))

for i in range(n):
    for x in range(n-i):
        print(1 + i*2 + 2*x,"", end="")
    for x in range(i*2):
        print("  ", end="")
    for x in range(0,n-i):
        print((n*2-1)-x*2,"", end="")
    print()

for i in range(n-1,-1,-1):
    for x in range(n-i):
        print(1 + i*2 + 2*x,"", end="")
    for x in range(i*2):
        print("  ", end="")
    for x in range(0,n-i):
        print((n*2-1)-x*2,"", end="")
    print()