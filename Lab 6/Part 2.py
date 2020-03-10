n = int(input("n: "))

for x in range(n*2):
    print("o", end="")
print()

for x in range(n-2):
    print("o", end="")
    for y in range(n*2-2):
        print(" ", end="")
    print("o")

for x in range(n*2):
    print("o", end="")
print()