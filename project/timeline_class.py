
import datetime as dt
import time


#  타임라인 클래스
class Timeline:
    timelinelist = []

    def __init__(self, member, writetime, booktitle, star, review, absnum):
        self.member = member.nick
        self.writetime = writetime
        self.booktitle = booktitle
        self.star = star
        self.review = review
        self.comment = list()
        self.good = list()
        self.bad = list()
        self.absnum = absnum


#  타임라인글 입력
    def input_timeline(member, booktitle, star, review):
        writetime = dt.datetime.now()
        absnum = len(Timeline.timelinelist)+1
        review = Timeline(member, writetime, booktitle, star, review, absnum)
        Timeline.timelinelist.append(review)
        Timeline.print_info(review)
        return review

#  댓글 작성
    def input_comment(self, member, comment, absnum):
        self.comment.append( (absnum, member.nick, comment) )

#  공감 누르기
    def add_good(self,member, absnum):
        self.good.append((absnum, member))

#  비공감 누르기
    def add_bad(self, member, absnum):
        self.bad.append((absnum, member))

#  본인 글 보여주기
    def print_yourreview(member):
        print("\n본인 작성글 입니다.")
        for i in Timeline.timelinelist:
                if i.member == member.nick:
                    Timeline.print_info(i)
                else: pass

#  타임라인 보여주기
    def show_timeline(type):
        if len(Timeline.timelinelist) == 0:
            print("작성된 리뷰가 없습니다.")
        if type == 1:
            print("----------시간순 보기----------")
            for i in reversed(Timeline.timelinelist):
                Timeline.print_info(i)
        elif type == 2:
            print("----------별점순 보기----------")
            for i in reversed( sorted(Timeline.timelinelist, key=lambda x:x.star) ):
                Timeline.print_info(i)

#  타임라인 보여주기 틀
    def print_info(self):
        print("글 번호:", self.absnum)
        print("작성자:", self.member, '{:>20}'.format('작성일자:'),self.writetime )
        sstar = "★" * int(self.star) + "☆" * ( 5-int(self.star) )
        print("책:",self.booktitle, '{:>25}'.format('별점:'), sstar)
        print("리뷰:", self.review)

        good_cnt = 0
        bad_cnt = 0
        for i in self.good:
            if i[0] == self.absnum:
                good_cnt +=1
        for i in self.bad:
            if i[0] == self.absnum:
                bad_cnt +=1

        print("댓글", len(self.comment), '{:>20}'.format('공감:'), good_cnt, "/ 비공감",bad_cnt )
        if len(self.comment) != 0:
            for i in self.comment:
                if i[0] == self.absnum:
                    print(i[1], ":", i[2])
        print("----------------------------------------------------------------")
