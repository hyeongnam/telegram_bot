token = '859091473:AAGhVK4ACKnPhuFWwfFo0_EgFtOC7pn16v8'
api_url = f'https://api.telegram.org/bot{token}'
webhook_url = input()

print(f'{api_url}/setwebhook?url={webhook_url}')