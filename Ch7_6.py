f = open("대한민국헌법_1장.txt",'r')
law = f.readlines()
f.close()
contents = ""
for line in law:
    contents = contents + line.strip() + "\n"

for i in contents:
    if i.isalnum() == False:
        contents = contents.replace(i, " ")
    elif (i=='①' or i=='②' or i=='③' or i=='④' or i=='⑤' or i=='⑥' or i=='⑦'):
        contents = contents.replace(i, " ")

from collections import Counter
c = Counter(contents.split())

def sort_by_key(t):
    return t[1]

from collections import OrderedDict
c = OrderedDict(c)
result = []
for i,v in OrderedDict( sorted(c.items(), key=sort_by_key) ).items():
    result += (i,v)

for i,v in range(-1:-10)
    print (result.items)
