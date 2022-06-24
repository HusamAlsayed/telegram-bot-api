import requests


class Telegram:
    """
    this class helps using telegram bot token in ease.

    currently we support sending messages, documents and photos,
    and we also support fetching files from the telegram bot.

    I am planning to modify it to support as use cases as I could.

    Warning:
    if you don't have the id of the person you want to deal with.
        he must send any message to your chat, and then you could get his id from the "get Message" function.
    """
    def __init__(self, bot_token):
        """

        :param bot_token: the bot token of the channel.
        """
        self.end_point = 'https://api.telegram.org/bot'
        self.token = bot_token
        self.full_endpoint = self.end_point + self.token + '/'

    def __repr__(self):
        return 'your token is {}'.format(self.full_endpoint)

    def send_message(self, chat_id, message):
        """
        this method support sending message to a person specified with "chat id"

        :param chat_id: chat id you want to send message to
        :param message: the message you want to send
        :return: the response and it's status code.
        """
        send_text = self.full_endpoint + 'sendMessage'
        data = {'chat_id': chat_id, 'text': message}
        response = requests.get(send_text, data=data)
        return response

    def send_photo(self, chat_id, photo):
        """
        this method support sending photos to a person specified with "chat id"

        :param chat_id: chat id you want to send message to.
        :param photo: the photo you want to send.
        :return: the response and it's status code.
        """
        url = self.full_endpoint + 'sendPhoto'
        data = {'chat_id': chat_id}
        files = {'photo': open(photo, 'rb')}
        response = requests.post(url, data=data, files=files)
        return response

    def send_document(self, chat_id, file):
        """
        this method support sending files to a person specified with "chat id"
        :param chat_id: chat id you want to send message to.
        :param file: the file you want to send.
        :return: the response and it's status code.
        """
        url = self.full_endpoint + 'sendDocument'
        data = {'chat_id': chat_id}
        files = {'document': open(file, 'rb')}
        response = requests.post(url, data=data, files=files)
        return response

    def get_updates(self):
        """

        :return: all the update in the last 24 hours, including persons who react with the bot. and the data was send
        """
        url = self.full_endpoint + 'getUpdates'
        response = requests.get(url)
        return response

    def get_file_information(self, file_id):
        """

        :param file_id: the id you want to take
        :return: the information of the file (only text work on this days).
        """
        url = f'{self.end_point}/{self.token}/getFile'
        response = requests.post(url, data={"file_id": file_id})
        if response.status_code != 200:
            return {"ok": "False"}
        json_response = response.json()
        if not json_response['ok']:
            return {"ok": "False"}
        file_path = json_response['result']['file_path']
        file_information = requests.get(f'https://api.telegram.org/file/bot{self.token}/{file_path}')
        return file_information.text
