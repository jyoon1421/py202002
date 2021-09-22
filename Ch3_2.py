
test_size = int( input() )

for i in range (test_size):
    num, text = input().split()
    num = int(num)
    text = str(text)
    for j in range (len(text)):
        print( num * text[j], end='' )
    print()
