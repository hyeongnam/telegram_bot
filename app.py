## flask 기본 형식
# from flask import Flask
# app = Flask(__name__)
# http://127.0.01/
# @app.route("/")
# def hello():
#     return "Hello World!"
# 실행시키는 코딩
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request
import pprint
from telegram import send_message
import requests
from decouple import config
app = Flask(__name__)
# http://127.0.01/
# @app.route('/')
# def root():
#     print('LOL') # 콘솔에 응답받는 파트
#     return 'Happy Hacking' # 웹상 응답받는 파트


# @app.route('/telegram')
# def telegram():
#     send_message('lofi hiphop')
#     return '연결되었습니다!'

token = config('TOKEN')
api_url = f'https://api.telegram.org/bot{token}'

@app.route(f'/{token}',methods=['POST'])
def telegram():
    # 파일 상단에서 import pprint
    message = request.get_json().get('message')
    # 메세지가 없을때 에러방지
    if message is not None:
        chat_id = message.get('from').get('id')
        text = message.get('text')
        if text == '점심메뉴':
            # 점심메뉴를 확인하는 코드
            text = '굶어'
        elif text == '로또':
            # 로또를 확인하는 코드
            text = '특정 로또번호'
        # 받은 메세지 다시 보내기
        requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')

    return '', 200


if __name__ == '__main__':
    app.run(debug=True)
