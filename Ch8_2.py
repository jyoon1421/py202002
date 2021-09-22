#수강생 이름 리스트 생성
f = open("파이썬2_수강생_이름.txt",'r')
student_name = f.readlines()
f.close()
name = ""
for line in student_name:
    name = name + line.strip() +" "
name = name.split()

#학번 리스트 생성
f = open("파이썬2_수강생_학번.txt",'r')
student_number = f.readlines()
f.close()
number = ""
for line in student_number:
    number = number + line.strip() +"\n"
number = number.split()

#학과 리스트 생성
f = open("파이썬2_수강생_학과.txt",'r')
student_major = f.readlines()
f.close()
major = ""
for line in student_major:
    major = major + line.strip() +"\n"
major = major.split()

#1)
total_list = list(zip(name, number, major))
print('1) total_list = ', total_list )

#2)
num_maj = [ [i,j] for i,j in zip(number, major)]
total_dic = { i:j for i,j in zip( name, num_maj )}
print('2) total_dic = ', total_dic)

#3)
sort_dic = sorted(total_dic.items(), key = lambda x: x[0])
print('3) sort_dic = ', sort_dic)


#4)
name_maj = [ [i,j] for i,j in zip(name, major) ]
sort_num = { i:j for i,j in zip( number, name_maj) }
sort_num = sorted(sort_num.items(), key = lambda x: x[0])

sort_num = dict(sort_num)
a = list( sort_num.keys() )
b = list( sort_num.values() )
b = sum(b, [])
c = []
d = []
for i in range (len(b)):
    if i%2 == 0:
        c.append( b[i] )
    else:
        d.append( b[i] )

print('4)')
print('NO.   학번     이름     학과')
for i, (j,k,l) in enumerate(zip(a,c,d)):
    print(i+1,' ', j, k, ' ', l)
