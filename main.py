import requests
import time
authToken = "6955282368:AAG8m7VanYaN-VRi6HmtqvYOgRKOT8ahJ88"
chat_id = "6460367199"
print("Success")
def sendMessage(token, id):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=Hello Cute'
    status = requests.get(url)
    time.sleep(2)
    print("Success")

while True:
    sendMessage(authToken, chat_id)
    time.sleep(1)
