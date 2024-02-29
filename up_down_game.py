import random

first_place = None


def record(score):
    global first_place
    if first_place == None:
        first_place = score

    else:
        if first_place > score:
            first_place = score


# 게임 반복 진행
while True:
    # 랜덤 번호 생성
    computer_num = random.randint(1, 100)
    if first_place == None:
        print("처음 오신 여러분 반갑습니다. 즐거운 ⬇️  업 ⬆️  다운 게임 즐기고 가세요 ^^7")
    else:
        print(f"다시오신걸 환영 합니다. 현재까지 가장 적은 횟수로 맞춘 게임횟수는 {first_place}회 입니다.")

    # 문제 정답 횟수 카운드
    count = 0

    while True:

        # 사용자 번호 입력
        print("당신이 생각하는 번호를 입력해 주세요 :", end=" ")

        # 숫자데이터 검사
        try:
            user_num = int(input())

        except ValueError as user_num:
            print("숫자가 아닌 다른 값이 입력되었습니다. 다시 입력해주세요.")
            continue

        # 1부터 100까지 숫자가 입력 되었을 때 조건 판단 및 카운트 덧셈
        if user_num >= 1 and user_num <= 100:

            if user_num == computer_num:
                count += 1
                break

            elif user_num < computer_num:
                print(f"---------정답은 {user_num}보다 큽니다.---------")
                count += 1

            else:
                print(f"---------정답은 {user_num}보다 작습니다.---------")
                count += 1

        else:
            print("1부터 100사이의 값을 입력해 주시기 바랍니다.")

    print(""" 
 ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗██╗   ██╗██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                                                                                             
""")
    print(f"\t\t\t\t  정답은 {computer_num}였으며 시도한 횟수는 {count}회 입니다.\n")

    # 재시도 물음
    while True:

        print("다시 시도 하시겠습니까? [y/n]", end=" ")
        regame = input()

        if regame == "y":
            print("게임을 다시 시작합니다.")
            record(count)
            break

        elif regame == "n":
            print("게임을 종료합니다.")
            record(count)
            exit(0)

        else:
            print("잘못된 값이 입력되었습니다.")
