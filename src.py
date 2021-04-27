import requests


class Telegram:

    def __init__(self, bot_token):
        self.end_point = 'https://api.telegram.org/bot'
        self.token = bot_token
        self.full_endpoint = self.end_point + self.token + '/'

    def __repr__(self):
        return 'your token is {}'.format(self.full_endpoint)

    def send_message(self, chat_id, message):
        send_text = self.full_endpoint + 'sendMessage'
        data = {'chat_id': chat_id, 'text': message}
        response = requests.get(send_text, data=data)
        return response

    def send_photo(self, chat_id, photo):
        url = self.full_endpoint + 'sendPhoto'
        data = {'chat_id': chat_id}
        files = {'photo': open(photo, 'rb')}
        response = requests.post(url, data=data, files=files)
        return response

    def get_updates(self):
        url = self.full_endpoint + 'getUpdates'
        response = requests.get(url)
        return response



