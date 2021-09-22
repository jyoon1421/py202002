f = open("Ch6_Hey_Jude.txt",'r')
HeyJude_lyric = f.readlines()
f.close()

contents = ""
for line in HeyJude_lyric:
    contents = contents + line.strip() + "\n"

n_of_Jude = contents.upper().count("JUDE")
print("Jude word count is ", n_of_Jude)

n_of_Na = contents.upper().count("NA")
print("Na/na word count is ", n_of_Na)

first = ""
first = HeyJude_lyric[0]
first_fix = first.replace('Jude', 'JeongYoon')
print(first_fix)
