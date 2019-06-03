import requests

def send_message(text):
    token = '859091473:AAGhVK4ACKnPhuFWwfFo0_EgFtOC7pn16v8'
    api_url = f'https://api.telegram.org/bot{token}'

    response = requests.get(api_url + '/getUpdates').json() # json 형식으로 출력
    chat_id = response['result'][0]['message']['from']['id']

    requests.get(f'{api_url}/sendMessage?chat_id={chat_id}&text={text}')