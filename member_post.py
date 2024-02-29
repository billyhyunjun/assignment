import bcrypt


# 멤버 클래스 생성
class Member():
    # 고객정보 인스턴스화
    def __init__(self, name="None", username="None", password="None"):
        self.name = name
        self.username = username

        # 비밀번호 해시 값으로 저장
        pw = password.encode()
        h_pw = bcrypt.hashpw(password=pw, salt=bcrypt.gensalt())
        self.password = h_pw

    # 고객 정보 출력
    def display(self):
        print("\n\n고객님의 회원정보 알려드리겠습니다.")
        print(f"고객님의 이름은 {self.name}입니다.")
        print(f"고객님의 아이디는 {self.username}입니다.\n\n")

    # 비밀번호 확인!
    def password_check(self, username):
        print(f"{username}님의 패스워드를 입력해 주시기 바랍니다 :", end=" ")
        pw_input = input().encode()
        ok_pw = bcrypt.checkpw(pw_input, self.password)
        return (ok_pw)


# 포스트 클래스 생성 및 멤버 클래스 상속받기
class Post():
    # 글정보 인스턴스화
    def __init__(self, title="None", content="None", author="None"):
        self.title = title
        self.content = content
        self.author = author

    # 게시글 내용 출력
    def show(self):
        print(f"\n\n{self.author}님의 게시글을 알려드리겠습니다.")
        print(f"{self.author}님의 게시글 제목은 {self.title}입니다.")
        print(f"{self.author}님의 게시글 내용은 {self.content}입니다.\n\n")


# 빈껍데기 멤버주소 등록해주세요 ㅠㅠ
members = []
posts = []


# 주민등록 ㅎㅎ
def make_member():
    print("\n당신의 이름을 적어주세요 :", end=" ")
    name = input()
    print("\n당신의 아이디을 적어주세요 :", end=" ")
    username = input()
    print("\n당신의 비밀번호를 적어주세요 :", end=" ")
    password = input()

    # 중복 검사
    found = False
    for member in members:
        if member.username == username:
            print("\n\n\n----회원님의 아이디로 이미 정보가 기록되었습니다.----\n\n\n")
            found = True
            return
    if not found:
        # 인스턴스 생성
        member = Member(name=name, username=username, password=password)

        # 멤버들 리스트에 저장
        members.append(member)
        print("\n\n\n----회원님의 정보가 정상적으로 기록되었습니다.----\n\n\n")


# 사람찾기
def find_member():
    found = False
    print("\n당신이 찾으시는 분의 아이디을 적어주세요 :", end=" ")
    username = input()
    for member in members:
        if member.username == username:
            if member.password_check(username) == True:
                member.display()
                found = True
                break
    if not found:
        print("\n잘못입력하셨습니다. 처음부터 다시 입력해 주시기 바랍니다.\n")


# 게시글 만들기
def make_post():

    print("\n게시글의 제목을 적어주세요 :", end=" ")
    title = input()
    print("\n게시글 내용을 적어주세요 :", end=" ")
    content = input()
    print("\n작성자의 이름를 적어주세요 :", end=" ")
    author = input()
    found = False

    for member in members:
        if member.name == author:
            # 인스턴스 생성
            post = Post(title=title, content=content, author=author)
            # 게시글 리스트에 저장
            posts.append(post)
            print("\n\n\n----회원님의 게시글이 정상적으로 기록되었습니다.----\n\n\n")
            found = True
            break
    if not found:
        print("\n잘못입력하셨거나 리스트에 없는 이름입니다.")


# 게시글 찾기
def find_post():
    print("\n어떤 방식으로 찾고 싶으십니까? \n 1: 포함된 제목으로 찾기 \n 2: 게시글 내용으로 찾기 \n 3: 글쓴이 이름으로 찾기")
    print("입력해 주세요 :", end=" ")

    # 문자입력방지
    try:
        select_type = int(input())
        if select_type == 1:
            print("\n당신이 찾으시는 게시글의 제목을 적어주세요 :", end=" ")
            text = input()
            found = False
            for post in posts:
                if text in post.title:
                    post.show()
                    found = True
            if not found:
                print("\n잘못입력하셨거나 리스트에 없는 내용입니다 처음부터 다시 입력해 주시기 바랍니다.")

        elif select_type == 2:
            print("\n당신이 찾으시는 게시글의 내용을 적어주세요 :", end=" ")
            text = input()
            found = False
            for post in posts:
                if text in post.content:
                    post.show()
                    found = True
            if not found:
                print("\n잘못입력하셨거나 리스트에 없는 내용입니다.")
        elif select_type == 3:
            print("\n당신이 찾으시는 게시자의 이름을 적어주세요 :", end=" ")
            text = input()
            found = False
            for post in posts:
                if text in post.author:
                    post.show()
                    found = True
            if not found:
                print("\n잘못입력하셨거나 리스트에 없는 이름입니다 처음부터 다시 입력해 주시기 바랍니다.")
        else:
            print("\n잘못입력하셨습니다.")
    except ValueError:
        print("\n잘못입력하셨습니다 처음부터 다시 입력해 주시기 바랍니다.\n")


# 메뉴시작
while True:
    print("안녕하세요 반갑습니다.")
    print("\n어떤 작업을 원하시나요? \n 1 : 등록하기\n 2 : 등록확인하기\n 3 : 게시글 등록하기\n 4 : 게시글 확인하기")
    print("입력해 주세요 :", end=" ")
    # 문자입력방지
    try:
        select = int(input())
        if select == 1:
            # 주민등록받아오기
            make_member()
        elif select == 2:
            # 보여주자
            find_member()
        elif select == 3:
            # 게시글 등록하기
            make_post()
        elif select == 4:
            # 게시글보여주자
            find_post()
        else:
            print("\n잘못입력하셨습니다 처음부터 다시 입력해 주시기 바랍니다.")
    except ValueError:
        print("\n잘못입력하셨습니다 처음부터 다시 입력해 주시기 바랍니다.\n")
