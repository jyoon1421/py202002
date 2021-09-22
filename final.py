
name = "이정윤"
student_ID = 2018112197
department = "건설환경공학과"

print("*"*50)
print("2020년 2학기 파이썬프로그래밍 기말고사 답안지")
print("*"*50,"\n")

print("*"*30)
print("{:<7}:  {:<6}".format("이름",name))
print("{:<7}:  {:<6}".format("학번(ID)",student_ID))
print("{:<7}:  {:<6}".format("학과",department))
print("*"*30)


#2

tu = (1, 2, 5, 4, 3, 2, 9, 4, 7, 8, 9, 9, 3, 7, 3)
notuple = tuple( set(tu) )

cnt = Counter(tu)
order = cnt.most_common()
max = order[0][1]

modes = []
for i in order:
    if i[1] == max:
        modes.append(i[0])

temp=0
for i in modes:
    if temp ==0 or i>temp:
        temp = i

print("입력 : 주어진 튜플 : ", tu)
print("출력 : 중복 제거 튜플 : ", notuple)
print("{:>20}".format("가장 많은 중복 요소 :"),temp)



import csv
with open('korea_floating_population_data.csv') as file:
    reader = csv.reader(file)
    population = list(reader)
print(population)

print("*"*55)
print("{:<6} {: <6} {: <7} {: <7} {: <6} {: <7}".format("조사지역", "전체수", "20대", "20대비율", "50대", "50대비율"))
print("{:<10} {:<9} {:<9} {: <10} {: <8} {: <7}".format("Area", "total", "No.", "Rate%", "No.", "Rate%"))
print("*"*55)
print("종로구")
print("도봉구")
print("-"*55)
