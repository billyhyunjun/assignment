import random
from flask import Flask, render_template, request
import os
import sqlite3

# 데이터 베이스 생성
conn = sqlite3.connect('database.db')
print('create & connect database')
# 테이블 생성
try:
    conn.execute(
        '''
    create table users (user_id text, playtime INTEGER, draw INTEGER, win INTEGER, lose INTEGER)
    '''
    )
    print('create table')

    conn.close()
except sqlite3.OperationalError:
    pass

# 문자 값 숫자로 변경


def change_value(value):
    if value == "가위":
        value = 1
    elif value == "바위":
        value = 0
    else:
        value = -1
    return (value)

# 회원가입 중복 방지


def register_user(user_id):
    # 데이터베이스 연결
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()

        # user_id가 이미 존재하는지 확인
        cur.execute("SELECT user_id FROM users WHERE user_id=?", (user_id,))
        existing_user = cur.fetchone()

        # 이미 존재하는 경우
        if existing_user:
            print("이미 등록된 사용자입니다.")
            con = sqlite3.connect("database.db")  # "database.db" 파일에 접속합니다.

            cur = con.cursor()  # 커서를 생성합니다.
            # 데이터베이스에서 모든 사용자를 선택합니다.
            cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
            rows = cur.fetchone()  # 결과의 첫 번째 행을 가져옴
            con.close()
            return (rows)
        else:
            # 등록되지 않은 경우, INSERT 문 실행
            playtime = 0
            draw = 0
            win = 0
            lose = 0
            cur.execute("INSERT INTO users (user_id, playtime, draw, win, lose) VALUES (?, ?, ?, ?, ?)",
                        (user_id, playtime, draw, win, lose))
            print("사용자 등록이 완료되었습니다.")
    return (user_id, playtime, draw, win, lose)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("main.html")


@app.route('/account', methods=['POST'])
def account():
    user_id = request.form['user_id']

    data_list = register_user(user_id)
    print(data_list)
    data_return = {
        "user_id": user_id,
        "playtime": data_list[1],
        "draw": data_list[2],
        "win": data_list[3],
        "lose": data_list[4]
    }

    return render_template("game.html", data=data_return)


@app.route('/record')
def record():

    con = sqlite3.connect("database.db")  # "database.db" 파일에 접속합니다.

    cur = con.cursor()  # 커서를 생성합니다.
    # 데이터베이스에서 모든 사용자를 선택합니다.
    cur.execute(f"select * from users")
    rows = cur.fetchall()  # 전체 결과의 행을 가져옴
    rows_as_lists = [list(row) for row in rows]
    con.close()

    print(rows_as_lists)

    for i in rows_as_lists:
        win_per = round(i[3] / (i[1] - i[2]) * 100,2)
        i.append(win_per)

    print(rows_as_lists)

    sorted_data = sorted(rows_as_lists, key=lambda x: x[5], reverse=True)

    print(sorted_data)
    return render_template("record.html", data = sorted_data)


@app.route('/game', methods=['POST', 'GET'])
def game():
    print("여기까지")
    # html에서 내가 적은 값 가져오기;
    my_num = change_value(request.form['user'])
    print(f'내가 입력한 값은?{my_num}')
    user_id = request.form['user_id']
    print(f'내가 입력한 아이디는??{user_id}')

    # 데이터 베이스에서 내 기록 가져오기
    con = sqlite3.connect("database.db")  # "database.db" 파일에 접속합니다.

    cur = con.cursor()  # 커서를 생성합니다.
    # 데이터베이스에서 모든 사용자를 선택합니다.
    cur.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    rows = cur.fetchone()  # 결과의 첫 번째 행을 가져옴
    con.close()

    print(f'db 값은? {rows}')

    computer_num = random.randint(-1, 1)
    # 컴퓨터의 값을 나의 값과 빼준다 이때 합이 0이 나오면 무승부, -1이나 2가 나오면 이기게 된다 그이외에는 패배
    score = my_num - computer_num
    print(score)
    # 승패무결과및 플레이 횟수를 기록해서 저장
    playtime = rows[1]
    draw = rows[2]
    win = rows[3]
    lose = rows[4]

    print(f'각자의 값은? {playtime} {draw} {win} {lose}')
    playtime += 1

    if (score == 0):
        draw += 1
    elif score == -1 or score == 2:
        win += 1
    else:
        lose += 1

    with sqlite3.connect("database.db") as con:
        cur = con.cursor()

        # 사용자 정보를 데이터베이스에 저장
        cur.execute("UPDATE users SET playtime=?, draw=?, win=?, lose=? WHERE user_id=?",
                    (playtime, draw, win, lose, user_id))

    con.close()

    print(playtime, draw, win, lose)

    data_return = {
        "user_id": user_id,
        "my_num": my_num,
        "computer_num": computer_num,
        "playtime": playtime,
        "draw": draw,
        "win": win,
        "lose": lose
    }

    print(data_return)

    return render_template("game.html", data=data_return)


if __name__ == '__main__':
    app.run(debug=True)
