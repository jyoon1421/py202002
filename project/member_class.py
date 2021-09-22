
#멤버 클래스
class Member:
    memberlist = []

    def __init__(self, name, nick, pw):
        self.name = name
        self.nick = nick
        self.pw = pw
        self.review = {}


    # 회원가입 메서드
    def create_member(name, nick, pw):
        for i in Member.memberlist:
            if i.nick == nick:
                return 0
        member = Member(name, nick, pw)
        Member.memberlist.append(member)
        return member


    # 로그인 메서드
    def member_login(nick, pw):
        for i in Member.memberlist:
            if i.nick == nick and i.pw == pw:
                return i
        else:
            return 0


    #  회원 탈퇴 메서드
    def remove_member(nick,pw):
        for i,j in enumerate(Member.memberlist):
            if j.nick == nick and j.pw == pw:
                del Member.memberlist[i]


    #  회원정보 보기 메서드
    def show_info(self):
        print("이름:",self.name, "\n닉네임:",self.nick, "\n비밀번호:",self.pw, "\n")
