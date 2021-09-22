price = list( input().split(';'))
price_int = []

for i in price:
    price_int.append(int(i))

price_int.sort(reverse = True)

for i in price_int:
    print( str( "{:9,d}".format(i) ) )
