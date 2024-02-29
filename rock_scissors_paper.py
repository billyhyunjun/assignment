import random
from time import sleep

# 승점
score_win = 0
score_lose = 0
score_draw = 0

# 카운트 다운 3초


def wait():
    print("\n\n\t\t?!?!?!?!?!자 과연 결과는?!?!?!?!?!?")
    sleep(1)
    print("\n\t\t\t\t3")
    sleep(1)
    print("\n\t\t\t\t2")
    sleep(1)
    print("\n\t\t\t\t1")

# 유저 손


def draw_user(user):

    user_hand = []

    if user == 1:
        user_hand.append("    _______       ")
        user_hand.append("---'   ____)____  ")
        user_hand.append("          ______) ")
        user_hand.append("       __________)")
        user_hand.append("      (____)      ")
        user_hand.append("---.__(___)       ")

    elif user == 2:
        user_hand.append("    _______       ")
        user_hand.append("---'   ____)      ")
        user_hand.append("       (_____)    ")
        user_hand.append("       (_____)    ")
        user_hand.append("       (____)     ")
        user_hand.append(" ---.__(___)      ")

    elif user == 3:
        user_hand.append("     _______      ")
        user_hand.append("---'    ____)____ ")
        user_hand.append("           ______)")
        user_hand.append("          _______)")
        user_hand.append("         _______) ")
        user_hand.append("---.__________)   ")

    return (user_hand)

# 컴퓨터 손


def draw_com(user):

    user_hand = []

    if user == 1:
        user_hand.append("       _______    ")
        user_hand.append("  ____(____   '---")
        user_hand.append(" (______          ")
        user_hand.append("(__________       ")
        user_hand.append("       (____)     ")
        user_hand.append("       (___)__.---")

    elif user == 2:
        user_hand.append("  _______         ")
        user_hand.append(" (____   '---     ")
        user_hand.append("(_____)           ")
        user_hand.append("(_____)           ")
        user_hand.append(" (____)           ")
        user_hand.append("  (___)__.---     ")

    elif user == 3:
        user_hand.append("      _______     ")
        user_hand.append(" ____(____   '----")
        user_hand.append("(______           ")
        user_hand.append("(_______          ")
        user_hand.append(" (_______         ")
        user_hand.append("    (_________.---")

    return (user_hand)

# 승부 판별


def versus(user, com):
    result = None
    if user == com:
        result = "draw"
    elif user == 1 and com == 2:
        result = "lose"
    elif user == 1 and com == 3:
        result = "win"
    elif user == 2 and com == 3:
        result = "lose"
    elif user == 2 and com == 1:
        result = "win"
    elif user == 3 and com == 1:
        result = "lose"
    elif user == 3 and com == 1:
        result = "win"
    return (result)


# 전체 구문 반복 실행
while True:

    # 환영 문구
    print(""" 
                                            .''.       
            .''.      .        *''*    :_\/_:     . 
            :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
        .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
        :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
        : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
        '..'  ':::'     * /\ *     .'/.\'.   '
            *            *..*         :
                *
                *
    !!!!반갑습니다 가위 바위 보 리그에 오신 것을 환영합니다!!!!\n\n""")

    # 컴퓨터 입력 받기
    com_select = random.randint(1, 3)

    while True:
        # 유저 입력 받기 (대문자는 소문자로 변환)
        print(
            "\t\t원하시는 선택지를 골라주세요. \n[바위(묵), 가위(찌), 보(빠)] 또는 [rock, scissors, paper] :", end=" ")
        user_select = input().lower()
        set_select = 0

        # 입력 값 가위바위보 변환하기
        if user_select == "가위" or user_select == "찌" or user_select == "scissors":
            set_select = 1
            break
        elif user_select == "바위" or user_select == "묵" or user_select == "rock":
            set_select = 2
            break
        elif user_select == "보" or user_select == "빠" or user_select == "paper":
            set_select = 3
            break
        else:
            print("""
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            잘못 입력된 값 입니다 다시 입력해 주시기 바랍니다.
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                  """)

    # 승부 결과 전송
    result = versus(set_select, com_select)

    # 승부 판독
    wait()
    user_hand = draw_user(set_select)
    com_hand = draw_com(com_select)
    print(f"\t{user_hand[0]}\t\t{com_hand[0]}")
    print(f"\t{user_hand[1]}\t\t{com_hand[1]}")
    print(f"\t{user_hand[2]}\t\t{com_hand[2]}")
    print(f"\t{user_hand[3]}\t\t{com_hand[3]}")
    print(f"\t{user_hand[4]}\t\t{com_hand[4]}")
    print(f"\t{user_hand[5]}\t\t{com_hand[5]}")
    print("\t당신\t\t\t\t\t\t컴퓨터")

    if result == "win":
        print("\t\t축하합니다!!!! 짝짝짝 이겼습니다!")
        score_win += 1
    elif result == "lose":
        print("\t\t아~~~ 아쉽게도 졌습니다 다음기회에")
        score_lose += 1
    elif result == "draw":
        print("\t\t    비겼네요 다시 한번 더!")
        score_draw += 1
        sleep(2)
        continue

    # 재시도 물음
    while True:

        print("\n\t\t    다시 시도하시겠습니까? \n\t\t  [y/n] or [네/아니오] :", end=" ")
        regame = input()

        if regame == "y" or regame == "네":
            print("\n\t\t게임을 다시 시작합니다.")
            break

        elif regame == "n" or regame == "아니오":
            print("\n\t\t\t게임을 종료합니다.")
            print("\t\t수고하셨습니다^^ 당신의 전적은?")
            print(f"\t\t\t[{score_win}승 {score_lose}패 {score_draw}무]")
            exit(0)

        else:
            print("""
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            잘못 입력된 값 입니다 다시 입력해 주시기 바랍니다.
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                  """)
