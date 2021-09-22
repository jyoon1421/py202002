
a = 777
b = 777
print(a == b, a is b)
#Result : true, true
a = 3.5
b = int(3.5)
print(a**((a//b)*2))
#Result : 12.25

print(((a - b) * a) // b)
#Result : 0

b = (((a - b) * a) % b)
print(b)
#Result : 1.75

print((a * 4) % (b * 4))
#Result : 0
