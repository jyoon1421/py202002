f = open("Ch6_Hey_Jude.txt",'r')
HeyJude_lyric = f.readlines()
f.close()

contents = ""
for line in HeyJude_lyric:
    contents = contents + line.strip() + "\n"

contents = contents.replace('-', '')
contents = contents.replace(',', '')
contents = contents.replace('(', '')
contents = contents.replace(')', '')

word = ""
word = contents.split()
print(len(word))
