n = int ( input() )

for i in range (1, n+1):
    for j in range (n-i):
        print(" ", end="")
    for h in range(i):
        print("*", end="")
    print()
