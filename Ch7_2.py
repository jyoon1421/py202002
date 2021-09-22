a,b = input().split()
a = int(a)
b = int(b)

x = [2**i for i in range(a, b+1)]
x.pop(1)
x.pop(-2)
print(x)
