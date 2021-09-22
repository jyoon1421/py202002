key = input().split()
val = map(int, input().split())
dic = dict(zip(key,val))

del dic['delta']
dic = {key:value for key,value in dic.items() if value!=30}

print(dic)
