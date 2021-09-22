
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

n = int(input())
result = list(str(factorial(n)))
five = str()

while len(five) < 5 :
    if result[-1] == '0':
        del result[-1]
    else:
        for i in range(5):
            five += result[-1]
            del result[-1]

print(five[::-1])
