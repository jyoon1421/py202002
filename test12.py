name = "이정 2018112197"
student_ID = 20201110111
department = "건설환경공학과"

print("*"*50)
print("2020년 2학기 파이썬프로그래밍 기말고사 답안지")
print("*"*50,"\n")

print("*"*30)
print("{:<7}:  {:<6}".format("이름",name))
print("{:<7}:  {:<6}".format("학번(ID)",student_ID))
print("{:<7}:  {:<6}".format("학과",department))
print("*"*30)

"""
"""

#2
num = [ int(i) for i in input("정수를 여러 개 입력하시오 :").split() ]

def mean_of_n(num):
    sum = 0
    for i in num:
        sum += i
    return sum / len(num)

def max_of_n(num):
    max = num[0]
    for i in num:
        if i>max:
            max = i
    return max

def min_of_n(num):
    min = num[0]
    for i in num:
        if i<min:
            min = i
    return min

print("평균값은", mean_of_n(num))
print("최대값은", max_of_n(num))
print("최소값은", min_of_n(num))



#3

import csv
with open("usa_alcohol_comsumption_data.csv") as file:
    reader = csv.reader(file)
    r = list(reader)

state_name = ['Utah', 'Delaware', 'New Jersey', 'Arkansas', 'Illinois', 'Indiana', 'Arizona', 'District of Columbia', 'Montana', 'Minnesota', 'Maine', 'Virginia', 'West Virginia', 'Iowa', 'Hawaii', 'South Carolina', 'Tennessee', 'Georgia', 'Texas','Wyoming', 'Kentucky', 'South Dakota', 'Mississippi', 'Ohio', 'Florida', 'Idaho', 'Michigan', 'Colorado', 'Wisconsin', 'Connecticut', 'Kansas', 'Oklahoma', 'Pennsylvania', 'Washington', 'Massachusetts', 'North Carolina', 'Missouri', 'New York', 'Louisiana', 'New Hampshire', 'Maryland', 'New Mexico', 'North Dakota', 'Alaska', 'Rhode Island', 'Vermont', 'Oregon', 'Nevada', 'California', 'Alabama', 'Nebraska']

sum = []

for i in state_name:
    beer = 0
    wine = 0
    spirits = 0
    no = 0
    for j in r:
        if j[0] == i and int(j[1]) >= 2000:
            beer += float( j[2] )
            wine += float( j[3] )
            spirits += float( j[4] )
            no = no + 1
    if no != 0:
        beer = beer / no
        wine = wine / no
        spirits = spirits / no
    sum.append( [j, beer, wine, spirits] )

sum_wine = sorted(sum, key=lambda x:x[2], reverse=True)
print(sum_wine)

print("sorting by wine >>")
print(f'{"No.":^5}{"State":^20}{"beer":>15}{"wine":>15}{"spirits":>15}')
print("="*70)
num = 1
for i in sum_wine:
    print("{:>3} {:^20} {:^15} {:^15} {:^15}".format(num, i[0], i[1], i[2], i[3]))
    num +=1
