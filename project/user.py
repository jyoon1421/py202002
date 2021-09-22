
from member_class import Member
from timeline_class import Timeline
from random import *
import time

#  회원가입 함수
def signup():
    name = input("\n이름:")

    nickname = input("닉네임(최대 8자):")
    if len(nickname)>8:
        print("최대 8자까지 가능합니다. 다시 입력하세요")
        nickname = input("닉네임(최대 8자):")

    pw = input("비밀번호(숫자4자리):")

    member = Member.create_member(name, nickname, pw)

    if member == '0':
        print("이미 가입된 닉네임입니다. 다른 닉네임을 입력하세요.")
        nickname = input("닉네임(최대 8자):")
        member = Member.create_member(name, nickname, pw)

    print("%s님, 가입이 완료되었습니다. 2초 후 메인화면으로 이동합니다.\n" %member.nick)
    time.sleep(2)


#  로그인 함수
def login():
    nick_enter = input("\n닉네임:")
    pw_enter = input("비밀번호:")

    member = Member.member_login(nick_enter, pw_enter)

    if member == 0:
        print("잘못 입력하셨습니다.")
        return None
    else:
        print("\n", member.nick,"님, 환영합니다. ")
        return member


#  타임라인 보기 함수
def see_timeline():
    type = input("1. 게시일자 순 (최신순) \n2. 별점 높은 순 \n원하는 정렬 순서를 선택하세요: ")
    if type == "1":
        Timeline.show_timeline(1)
    elif type == "2":
        Timeline.show_timeline(2)


# 본인 글 보기 함수
def see_mytimeline(member):
    Timeline.print_yourreview(member)


#  글 입력하기 함수
def write_review(member):
    book_name = input("리뷰를 남길 책 제목을 입력하세요:")
    star_num = input("별점을 입력하세요(1,2,3,4,5 중 택):")
    review = input("리뷰를 입력하세요:")
    Timeline.input_timeline(member, book_name, star_num, review)
    print("글이 작성되었습니다. 2초 후 메뉴화면으로 이동합니다.")
    time.sleep(2)


#  댓글 쓰기 함수
def write_comment(member):
    comment_num = int(input("댓글을 작성할 글 번호를 입력하세요:"))
    while comment_num > len(Timeline.timelinelist):
        comment_num = int( input("1 ~ %d 사이의 숫자를 입력하세요:" %len(Timeline.timelinelist)) )
    comment = input("댓글을 입력하세요:")
    comment_review = Timeline.timelinelist[comment_num-1]
    comment_review.input_comment(member, comment, comment_num)
    print("댓글이 작성되었습니다. 2초 후 메뉴화면으로 이동합니다.")
    time.sleep(2)


#  공감 누르기 함수
def push_good(member):
    good_num = int( input("공감을 누를 글 번호를 입력하세요:") )
    if good_num > len(Timeline.timelinelist):
        good_num = int( input("1 ~ %d 사이의 숫자를 입력하세요:" %len(Timeline.timelinelist)) )
    else :
        good = Timeline.timelinelist[good_num-1]
        good.add_good(member, good_num)
        print("공감되었습니다.")


#  비공감 누르기 함수
def push_bad(member):
    bad_num = int( input("비공감을 누를 글 번호를 입력하세요:") )
    if bad_num > len(Timeline.timelinelist):
        bad_num = int( input("1 ~ %d 사이의 숫자를 입력하세요:" %len(Timeline.timelinelist)) )
    else :
        bad = Timeline.timelinelist[bad_num-1]
        bad.add_bad(member, bad_num)
        print("비공감되었습니다.")


#  책 추천 함수
import csv
with open("추천도서리스트.csv") as file:
    reader = csv.reader(file)
    booklist = list(reader)

def recommend_book():
    print("3초 뒤 책을 추천해드립니다.\n")
    time.sleep(1)
    print("당신에게 추천해드릴 도서는")
    time.sleep(1)
    print("바로")
    time.sleep(1)
    i = randint(1, 216)
    print("<",booklist[i][0],">","  입니다!")
    print("2초 뒤 메뉴 화면으로 이동합니다.")
    time.sleep(2)


#회원정보보기
def see_info(member):
    print(member.nick,"님의 회원정보입니다.")
    Member.show_info(member)
    print("2초 뒤 메뉴 화면으로 이동합니다.")
    time.sleep(2)


#  회원 탈퇴 함수
def signout(member):
    remove_nick = input("탈퇴를 원하는 회원의 닉네임을 입력하세요:")
    remove_pw = input("비밀번호를 입력하세요:")
    member = Member.remove_member(remove_nick,remove_pw)
    print("탈퇴되었습니다.")
    return 0
