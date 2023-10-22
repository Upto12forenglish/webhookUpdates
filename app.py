from flask import Flask, request

##########################
import requests

# Replace 'YOUR_BOT_API_TOKEN' with your Telegram Bot API token
bot_token = '6092786649:AAGsiM_0resGLglZTtRc-9iJtod2TagIhNE'

# Replace '801280384' with the chat ID of the recipient
chat_id = '801280384'

# URL for sending a message using the Telegram Bot API
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

# Message content
message_text = 'Hello, this is a message from your bot!'

# Parameters for the POST request
params = {
    'chat_id': chat_id,
    'text': message_text,
}
##########################

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_updates():
    data = request.get_json()
    print("Received Update:")
    print(data)
    try:
        response = requests.post(url, data=params)
        data = response.json()
        if data['ok']:
            print(f'Message sent to {chat_id}: {message_text}')
        else:
            print(f'Failed to send the message. Telegram API response: {data}')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')
    return '', 200

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8501)
