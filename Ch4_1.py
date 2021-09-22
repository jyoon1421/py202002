print("태어난 연도를 입력하세요")
year = int( input() )
animal = year % 12

if animal == 4:
    print("쥐 띠입니다.")
elif animal == 5:
    print("소 띠입니다.")
elif animal == 6:
    print("범 띠입니다.")
elif animal == 7:
    print("토끼 띠입니다.")
elif animal == 8:
    print("용 띠입니다.")
elif animal == 9:
    print("뱀 띠입니다.")
elif animal == 10:
    print("말 띠입니다.")
elif animal == 11:
    print("양 띠입니다.")
elif animal == 12:
    print("원숭이 띠입니다.")
elif animal == 1:
    print("닭 띠입니다.")
elif animal == 2:
    print("개 띠입니다.")
else:
    print("돼지 띠입니다.")
