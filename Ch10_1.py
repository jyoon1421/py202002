
import csv
with open('파이썬프로그래밍02반_CSV.csv') as file:
    reader = csv.reader(file)
    Student_list = list(reader)
del Student_list[0]


class Student():
    def __init__(self, name, number, department, math, english, korean):
        self.name = name
        self.number = number
        self.department = department
        self.math = math
        self.english = english
        self.korean = korean

    def show_info(self):
        print(name, ' ', number, ' ', department)

    def calc_sum(self):
        return float(self.math) + float(self.english) + float(self.korean)

    def calc_aver(self):
        return round( (float(self.math) + float(self.english) + float(self.korean))/3 ,1)

    def calc_grade_math(self, math):
        mathlist.sort()
        mathlist.reverse()
        acut = float( mathlist[int(len(mathlist)*0.3)] )
        bcut = float( mathlist[int(len(mathlist)*0.7)] )
        if float(self.math) >= acut:
            return 'A'
        elif float(self.math) < bcut:
            return 'C'
        else: return'B'

    def calc_grade_english(self, english):
        englishlist.sort()
        englishlist.reverse()
        acut = float( englishlist[int(len(englishlist)*0.3)] )
        bcut = float( englishlist[int(len(englishlist)*0.7)] )
        if float(self.english) >= acut:
            return 'A'
        elif float(self.english) < bcut:
            return 'C'
        else: return'B'

    def calc_grade_korean(self, korean):
        koreanlist.sort()
        koreanlist.reverse()
        acut = float( koreanlist[int(len(koreanlist)*0.3)] )
        bcut = float( koreanlist[int(len(koreanlist)*0.7)] )
        if float(self.korean) >= acut:
            return 'A'
        elif float(self.korean) < bcut:
            return 'C'
        else: return'B'

point =[]
gradelist=[]
mathlist=[]
englishlist=[]
koreanlist=[]
for i in range(len(Student_list)):
    mathlist.append(Student_list[i][3])
    englishlist.append(Student_list[i][4])
    koreanlist.append(Student_list[i][5])
i=0
for j in Student_list:
    studenti = j
    studenti = Student(studenti[0],studenti[1],studenti[2],studenti[3],studenti[4],studenti[5])

    sum = studenti.calc_sum()
    aver = studenti.calc_aver()
    point.append( [ j[0], j[1], j[2], sum, aver ] )

    mgrade = studenti.calc_grade_math(j[3])
    egrade = studenti.calc_grade_english(j[4])
    kgrade = studenti.calc_grade_korean(j[5])
    gradelist.append( [j[0], j[1], mgrade, egrade, kgrade] )
    i+=1


point.sort(key = lambda x:x[3])
point.reverse()

print("2)")
print("No.  이름    학번     학과     총점   평균")
for i in range(len(point)):
    print(f"{i+1}  {point[i][0]} {point[i][1]} {point[i][2]} {point[i][3]}   {point[i][4]}" )



gradelist.sort(key = lambda x:x[0])

print("\n3)")
print("No. 이름     학번    수학 영어 국어")
for i in range( len(gradelist) ):
    print(f"{i+1}  {gradelist[i][0]} {gradelist[i][1]}   {gradelist[i][2]}   {gradelist[i][3]}   {gradelist[i][4]}")
