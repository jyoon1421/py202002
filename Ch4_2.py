year = int (input("연도를 입력하세요: ") )

if year % 400 == 0:
    leap_year = 1
else:
    if ( (year % 4 == 0) and (year % 100 != 0) ):
        leap_year = 1
    else:
        leap_year = 0

print (leap_year)
