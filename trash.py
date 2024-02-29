# <!-- <script>
#     let play_time = 0;
#     let win_number = 0;
#     let lose_number = 0;
#     let draw_number = 0;

#     // 내가 누르는 버튼 요소 가져오기
#     document.querySelectorAll('.button_area input').forEach(function (button) {
#         button.addEventListener('click', function () { // 내가 클릭을 했을 때 작동하게
#             var value = button.value; //버튼 양식에 value=""안에 있는 값을 value에 넣어주기
#             // 딕셔너리로 필요한 것들 묶어주기
#             let data = {
#                 play_time,
#                 win_number,
#                 lose_number,
#                 draw_number,
#                 value
#             }
#             // 내가 입력한 데이터 딕셔너리를 Flask에서 받아 볼 수 있게 json코드로 변환해서 전송
#             var xhr = new XMLHttpRequest();
#             xhr.open("POST", "{{ url_for('game_result')}}", true);
#             xhr.setRequestHeader('Content-Type', 'application/json');
#             xhr.send(JSON.stringify({ data }));
#         });
#     });
# </script> -->







# @app.route('/game/result', methods=['POST'])
# def game_result():
#     # html에서 json코드로 온것을 data에 딕셔너리 형식으로 저장
#     data = request.json
#     # 나의 선택 값을 변수에 저장 "가위=1", "바위=0", "보=-1"
#     my_num = change_value(data["data"]["value"])
#     # 컴퓨터의 선택값을 랜덤으로 저장
#     computer_num = random.randint(-1, 1)
#     # 컴퓨터의 값을 나의 값과 빼준다 이때 합이 0이 나오면 무승부, -1이나 2가 나오면 이기게 된다 그이외에는 패배
#     score = my_num - computer_num
    
#     # 승패무결과및 플레이 횟수를 기록해서 저장
#     time = int(data["data"]["play_time"]) 
#     draw = int(data["data"]["draw_number"])
#     win = int(data["data"]["win_number"])
#     lose = int(data["data"]["lose_number"])
    
#     time += 1
    
#     if (score == 0):
#         draw += 1
#     elif score == -1 or score == 2:
#         win += 1 
#     else: 
#         lose += 1 
    
#     print(time, draw, win, lose)
    
#     data_return = {
#         "my_num": my_num,
#         "computer_num": computer_num,
#         "time": time,
#         "draw": draw,
#         "win": win,
#         "lose": lose
#     }

#     print(data_return)
#     return render_template("game.html", data = data_return)