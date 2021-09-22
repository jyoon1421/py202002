# import csv
# import time
# from random import *
#
# with open("추천도서리스트.csv") as file:
#     reader = csv.reader(file)
#     booklist = list(reader)
#
# def recomment_book():
#     print("3초 뒤 책을 추천해드립니다.\n")
#     time.sleep(1)
#     print("당신에게 추천해드릴 도서는")
#     time.sleep(1)
#     print("바로")
#     time.sleep(1)
#     i = randint(1, 216)
#     print("<",booklist[i][0],">","  입니다!")
#
# recomment_book()

print('{:<3} {:ㅤ<4} {:ㅤ<6} {:ㅤ<13} {:ㅤ<3} {:ㅤ<5}'.format('No','이름','학번','학과','총점','평균'))
