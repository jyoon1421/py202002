from member_class import Member
from user import *

# 제일 처음 보이는 화면 -> 로그인 후 보이는 화면
def mainscreen():
    while 1:
        print("----------------------------------------------------------------")
        print(" {0:>30s}". format("*동국 도서관*\n") )
        print("1. 로그인 \n2. 회원가입\n")
        print("원하는 메뉴 번호를 입력하세요:")
        choice = int(input("->"))

        if choice == 2: signup()
        else:
            member = login()

            if member != None:
                while 1:
                    print("\n1. 리뷰타임라인 보기 \n2. 리뷰 작성하기 \n3. 댓글 작성하기 \n4. 공감하기 \n5. 비공감하기")
                    print("6. 오늘의 추천 책 \n7. 회원정보보기 \n8.내 글 보기 \n9. 로그아웃 \n10. 회원탈퇴\n")
                    print("원하는 메뉴 번호를 입력하세요:")
                    memberchoice = int( input("->"))
                    if memberchoice == 1:
                        see_timeline()
                    elif memberchoice == 2:
                        write_review(member)
                    elif memberchoice == 3:
                        write_comment(member)
                    elif memberchoice == 4:
                        push_good(member)
                    elif memberchoice == 5:
                        push_bad(member)
                    elif memberchoice == 6:
                        recommend_book()
                    elif memberchoice == 7:
                        see_info(member)
                    elif memberchoice == 8:
                        see_mytimeline(member)
                    elif memberchoice == 9:
                        break
                    elif memberchoice == 10:
                        signout(member)
                        break
            else:
                print("메인 화면으로 돌아가려면 1, 종료하려면 2를 입력하세요.")
                num = int(input("->"))
                if num == 1:
                    mainscreen()
                else:
                    False
#  ------------------------------------------------------------------------------
mainscreen()
