f = open("Ch6_Hey_Jude.txt", 'r')
jude_lyric = f.readlines()
f.close()
contents = ""
for line in jude_lyric:
     contents = contents + line.strip() + "\n"

for i in contents:
   if (i.isalnum() or i == "'") == False:
        contents = contents.replace(i, " ")
print(contents.split())
print(len(contents.split()))  #564
